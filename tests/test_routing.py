"""Unit tests for Flood-Safe A* Routing and Impassable Barrier Detection."""

import pytest

from src.core.routing_engine import FloodSafeRouter


def test_dry_shortest_path(sample_streets, sample_intersections):
    """Verifies standard shortest path computation when all roads are dry."""
    router = FloodSafeRouter()
    router.build_network(sample_streets, sample_intersections)

    # Path from i1 to i3:
    # Direct bypass (s3): 850m
    # Via i2 (s1 + s2): 300m + 400m = 700m -> shorter!
    route = router.find_safe_route("i1", "i3", street_depth_map={})

    assert route.path_found
    assert route.total_distance_m == 700.0
    assert route.max_flood_depth_encountered_cm == 0.0
    assert route.overall_safety_rating == "safe"
    assert len(route.steps) == 2
    assert route.steps[0].segment_id == "s1"
    assert route.steps[1].segment_id == "s2"


def test_flood_penalty_rerouting(sample_streets, sample_intersections):
    """Verifies that moderate flooding on the primary route causes rerouting to a dry path."""
    router = FloodSafeRouter()
    router.build_network(sample_streets, sample_intersections)

    # s1 has 10cm water (caution depth), s3 is dry (850m)
    # Cost of s1 + s2 with penalty exceeds 850m -> should reroute via s3
    depth_map = {"s1": 12.0, "s2": 0.0, "s3": 0.0}
    route = router.find_safe_route("i1", "i3", street_depth_map=depth_map)

    assert route.path_found
    # Routed via Highland Bypass (s3)
    assert route.steps[0].segment_id == "s3"
    assert route.total_distance_m == 850.0
    assert route.max_flood_depth_encountered_cm == 0.0


def test_critical_depth_hard_cutoff(sample_streets, sample_intersections):
    """Verifies that streets with depth >= 15cm are strictly blocked as impassable barriers."""
    router = FloodSafeRouter()
    router.build_network(sample_streets, sample_intersections)

    # Both s1 and s3 are deeply flooded (>= 15cm)
    depth_map = {"s1": 18.0, "s3": 25.0}
    route = router.find_safe_route("i1", "i3", street_depth_map=depth_map)

    # No alternate paths exist -> should return blocked status or cached fallback
    assert route.overall_safety_rating == "impassable_blocked" or route.is_cached_fallback


def test_route_cache_fallback(sample_streets, sample_intersections):
    """Verifies fallback to cached safe route when network conditions degrade."""
    router = FloodSafeRouter()
    router.build_network(sample_streets, sample_intersections)

    # First, run a successful dry route query to populate cache
    route1 = router.find_safe_route("i1", "i3", street_depth_map={})
    assert route1.path_found

    # Now all paths are flooded to 30cm
    depth_map_flooded = {"s1": 30.0, "s2": 30.0, "s3": 30.0}
    route2 = router.find_safe_route("i1", "i3", street_depth_map=depth_map_flooded, is_degraded_nowcast=True)

    assert route2.path_found
    assert route2.is_cached_fallback
    assert "cached" in route2.warning_message.lower()
