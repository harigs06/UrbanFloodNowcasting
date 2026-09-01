"""SQLAlchemy ORM models for Drainage Network, Streets, and Nowcast Inundation states."""

from datetime import datetime
from typing import Optional
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    JSON,
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship

from src.db.session import Base


class DrainageNode(Base):
    """Represents a drainage inlet, manhole, junction, or outfall in the stormwater network."""
    __tablename__ = "drainage_nodes"

    id = Column(String(64), primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    node_type = Column(String(32), default="inlet", nullable=False)  # inlet, manhole, outfall, storage
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    invert_elevation_m = Column(Float, nullable=False, default=0.0)
    rim_elevation_m = Column(Float, nullable=False, default=2.0)
    max_depth_m = Column(Float, nullable=False, default=2.0)
    surface_area_m2 = Column(Float, nullable=False, default=250.0)  # Subcatchment surface ponding area
    is_outfall = Column(Boolean, default=False, nullable=False)
    metadata_json = Column(JSON, nullable=True)

    # Relationships
    outflow_conduits = relationship("DrainageConduit", foreign_keys="DrainageConduit.from_node_id", back_populates="from_node")
    inflow_conduits = relationship("DrainageConduit", foreign_keys="DrainageConduit.to_node_id", back_populates="to_node")

    def __repr__(self) -> str:
        return f"<DrainageNode id={self.id} type={self.node_type} lat={self.latitude:.4f} lon={self.longitude:.4f}>"


class DrainageConduit(Base):
    """Represents a stormwater underground pipe, culvert, or open drainage channel."""
    __tablename__ = "drainage_conduits"

    id = Column(String(64), primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    from_node_id = Column(String(64), ForeignKey("drainage_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    to_node_id = Column(String(64), ForeignKey("drainage_nodes.id", ondelete="CASCADE"), nullable=False, index=True)
    length_m = Column(Float, nullable=False)
    diameter_m = Column(Float, nullable=False)  # Height / Diameter
    width_m = Column(Float, nullable=True)     # For rectangular conduits
    roughness = Column(Float, nullable=False, default=0.015)  # Manning's n
    shape = Column(String(32), default="circular", nullable=False)
    slope = Column(Float, nullable=False, default=0.005)
    full_capacity_m3s = Column(Float, nullable=True)  # Precomputed Manning full-flow capacity
    metadata_json = Column(JSON, nullable=True)

    # Relationships
    from_node = relationship("DrainageNode", foreign_keys=[from_node_id], back_populates="outflow_conduits")
    to_node = relationship("DrainageNode", foreign_keys=[to_node_id], back_populates="inflow_conduits")

    def __repr__(self) -> str:
        return f"<DrainageConduit id={self.id} from={self.from_node_id} to={self.to_node_id} diam={self.diameter_m}m>"


class StreetSegment(Base):
    """Represents an urban road segment linked to the drainage graph for flood-safe routing."""
    __tablename__ = "street_segments"

    id = Column(String(64), primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    from_intersection_id = Column(String(64), nullable=False, index=True)
    to_intersection_id = Column(String(64), nullable=False, index=True)
    length_m = Column(Float, nullable=False)
    width_m = Column(Float, nullable=False, default=7.0)
    base_speed_kmh = Column(Float, nullable=False, default=40.0)
    elevation_m = Column(Float, nullable=False, default=10.0)
    nearest_node_id = Column(String(64), ForeignKey("drainage_nodes.id", ondelete="SET NULL"), nullable=True, index=True)
    coordinates_json = Column(JSON, nullable=True)  # Array of [[lon, lat], ...] for road centerline

    def __repr__(self) -> str:
        return f"<StreetSegment id={self.id} name='{self.name}' len={self.length_m}m node={self.nearest_node_id}>"


class NowcastCycle(Base):
    """Tracks each execution of the nowcasting pipeline across various forecasting horizons."""
    __tablename__ = "nowcast_cycles"

    id = Column(String(64), primary_key=True, index=True)
    cycle_timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    horizon_minutes = Column(Integer, nullable=False, default=15)
    radar_timestamp = Column(DateTime, nullable=True)
    radar_staleness_seconds = Column(Float, nullable=False, default=0.0)
    data_quality = Column(String(32), default="nominal", nullable=False)  # nominal, degraded, synthetic
    max_depth_cm = Column(Float, default=0.0, nullable=False)
    mean_depth_cm = Column(Float, default=0.0, nullable=False)
    total_flooded_nodes = Column(Integer, default=0, nullable=False)
    execution_duration_ms = Column(Float, default=0.0, nullable=False)
    status = Column(String(32), default="completed", nullable=False)  # running, completed, failed

    # Relationships
    inundation_records = relationship("InundationDepth", back_populates="cycle", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<NowcastCycle id={self.id} horizon={self.horizon_minutes}m quality={self.data_quality} max_depth={self.max_depth_cm:.1f}cm>"


class InundationDepth(Base):
    """Spatio-temporal flood depth and storage state for a node or street segment at a nowcast cycle."""
    __tablename__ = "inundation_depths"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cycle_id = Column(String(64), ForeignKey("nowcast_cycles.id", ondelete="CASCADE"), nullable=False, index=True)
    entity_type = Column(String(16), nullable=False)  # "node" or "street"
    entity_id = Column(String(64), nullable=False, index=True)
    water_depth_cm = Column(Float, nullable=False, default=0.0)
    surcharge_flow_m3s = Column(Float, nullable=False, default=0.0)
    excess_storage_m3 = Column(Float, nullable=False, default=0.0)
    risk_level = Column(String(16), nullable=False, default="safe")  # "safe" (<5cm), "caution" (5-15cm), "impassable" (>=15cm)
    recorded_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    cycle = relationship("NowcastCycle", back_populates="inundation_records")

    __table_args__ = (
        Index("ix_inundation_cycle_entity", "cycle_id", "entity_type", "entity_id"),
        Index("ix_inundation_risk", "risk_level"),
    )

    def __repr__(self) -> str:
        return f"<InundationDepth cycle={self.cycle_id} entity={self.entity_type}:{self.entity_id} depth={self.water_depth_cm:.1f}cm risk={self.risk_level}>"
