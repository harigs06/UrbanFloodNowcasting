"""Generate complete, dense, realistic city-wide street networks for all 6 cities."""

import json

# Let's define the comprehensive dataset for all 6 cities
# Every street will have:
# id, name, ward, fromIntersection, toIntersection, lengthM, waterDepthCm, riskLevel, flowVelocityMs, elevationM, drainageCapacityM3s, runoffInflowM3s, blocked, coordinates

script_content = '''import { CityConfig, StreetSegment, DrainageNode, DrainageConduit, HistoricalStormScenario, AlertNotification } from '../types';

export const CITIES: CityConfig[] = [
  {
    id: 'hyderabad',
    name: 'Hyderabad',
    state: 'Telangana',
    center: [17.425, 78.465],
    zoom: 13,
    radarStation: 'HYD (caz_hyd)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_hyd.gif',
    description: 'Hussain Sagar & Musi River Basin Urban Watershed'
  },
  {
    id: 'mumbai',
    name: 'Mumbai',
    state: 'Maharashtra',
    center: [19.015, 72.835],
    zoom: 13,
    radarStation: 'MUM (caz_mum)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_mum.gif',
    description: 'Mithi River Basin & Coastal Lowland Catchment'
  },
  {
    id: 'chennai',
    name: 'Chennai',
    state: 'Tamil Nadu',
    center: [13.045, 80.235],
    zoom: 13,
    radarStation: 'CHE (caz_chn)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_chn.gif',
    description: 'Adyar & Cooum River Urban Flood Corridor'
  },
  {
    id: 'bengaluru',
    name: 'Bengaluru',
    state: 'Karnataka',
    center: [12.965, 77.615],
    zoom: 13,
    radarStation: 'BLR (caz_blr)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_blr.gif',
    description: 'Bellandur & Varthur Interconnected Lake Catchment'
  },
  {
    id: 'delhi',
    name: 'Delhi NCR',
    state: 'Delhi',
    center: [28.625, 77.225],
    zoom: 13,
    radarStation: 'DEL (caz_dlh)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_dlh.gif',
    description: 'Yamuna Floodplain & Najafgarh Drain Corridor'
  },
  {
    id: 'kolkata',
    name: 'Kolkata',
    state: 'West Bengal',
    center: [22.565, 88.355],
    zoom: 13,
    radarStation: 'KOL (caz_kol)',
    radarEndpoint: 'https://mausam.imd.gov.in/Radar/caz_kol.gif',
    description: 'Hooghly Tidal Drainage & East Kolkata Wetlands'
  }
];
'''
print("Script template ready.")
