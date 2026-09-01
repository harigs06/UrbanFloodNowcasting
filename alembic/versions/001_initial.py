"""Initial database schema for flood engine models

Revision ID: 001_initial
Revises: 
Create Date: 2026-08-28 23:30:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Drainage Nodes
    op.create_table(
        'drainage_nodes',
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('node_type', sa.String(length=32), nullable=False, server_default='inlet'),
        sa.Column('latitude', sa.Float(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=False),
        sa.Column('invert_elevation_m', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('rim_elevation_m', sa.Float(), nullable=False, server_default='2.0'),
        sa.Column('max_depth_m', sa.Float(), nullable=False, server_default='2.0'),
        sa.Column('surface_area_m2', sa.Float(), nullable=False, server_default='250.0'),
        sa.Column('is_outfall', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('metadata_json', sa.JSON(), nullable=True),
    )

    # 2. Drainage Conduits
    op.create_table(
        'drainage_conduits',
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('from_node_id', sa.String(length=64), sa.ForeignKey('drainage_nodes.id', ondelete='CASCADE'), nullable=False),
        sa.Column('to_node_id', sa.String(length=64), sa.ForeignKey('drainage_nodes.id', ondelete='CASCADE'), nullable=False),
        sa.Column('length_m', sa.Float(), nullable=False),
        sa.Column('diameter_m', sa.Float(), nullable=False),
        sa.Column('width_m', sa.Float(), nullable=True),
        sa.Column('roughness', sa.Float(), nullable=False, server_default='0.015'),
        sa.Column('shape', sa.String(length=32), nullable=False, server_default='circular'),
        sa.Column('slope', sa.Float(), nullable=False, server_default='0.005'),
        sa.Column('full_capacity_m3s', sa.Float(), nullable=True),
        sa.Column('metadata_json', sa.JSON(), nullable=True),
    )

    # 3. Street Segments
    op.create_table(
        'street_segments',
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('from_intersection_id', sa.String(length=64), nullable=False),
        sa.Column('to_intersection_id', sa.String(length=64), nullable=False),
        sa.Column('length_m', sa.Float(), nullable=False),
        sa.Column('width_m', sa.Float(), nullable=False, server_default='7.0'),
        sa.Column('base_speed_kmh', sa.Float(), nullable=False, server_default='40.0'),
        sa.Column('elevation_m', sa.Float(), nullable=False, server_default='10.0'),
        sa.Column('nearest_node_id', sa.String(length=64), sa.ForeignKey('drainage_nodes.id', ondelete='SET NULL'), nullable=True),
        sa.Column('coordinates_json', sa.JSON(), nullable=True),
    )

    # 4. Nowcast Cycles
    op.create_table(
        'nowcast_cycles',
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('cycle_timestamp', sa.DateTime(), nullable=False),
        sa.Column('horizon_minutes', sa.Integer(), nullable=False, server_default='15'),
        sa.Column('radar_timestamp', sa.DateTime(), nullable=True),
        sa.Column('radar_staleness_seconds', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('data_quality', sa.String(length=32), nullable=False, server_default='nominal'),
        sa.Column('max_depth_cm', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('mean_depth_cm', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('total_flooded_nodes', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('execution_duration_ms', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='completed'),
    )

    # 5. Inundation Depths
    op.create_table(
        'inundation_depths',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('cycle_id', sa.String(length=64), sa.ForeignKey('nowcast_cycles.id', ondelete='CASCADE'), nullable=False),
        sa.Column('entity_type', sa.String(length=16), nullable=False),
        sa.Column('entity_id', sa.String(length=64), nullable=False),
        sa.Column('water_depth_cm', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('surcharge_flow_m3s', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('excess_storage_m3', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('risk_level', sa.String(length=16), nullable=False, server_default='safe'),
        sa.Column('recorded_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('inundation_depths')
    op.drop_table('nowcast_cycles')
    op.drop_table('street_segments')
    op.drop_table('drainage_conduits')
    op.drop_table('drainage_nodes')
