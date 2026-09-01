"""Cities API Router for Multi-City Management and Discovery."""

from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException, status

from src.api.v1.auth import verify_api_key
from src.cities import CITY_REGISTRY, CityProfile, list_registered_cities, get_city_profile

router = APIRouter(prefix="/cities", tags=["Cities & Multi-Tenancy"])


@router.get("", response_model=List[CityProfile])
async def list_cities(api_key: str = Depends(verify_api_key)) -> List[CityProfile]:
    """Lists all registered metropolitan regions available for flood nowcasting."""
    return list_registered_cities()


@router.get("/{city_id}", response_model=CityProfile)
async def get_city_details(city_id: str, api_key: str = Depends(verify_api_key)) -> CityProfile:
    """Retrieves profile, bounding box coordinates, and radar station for a specific city."""
    try:
        return get_city_profile(city_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
