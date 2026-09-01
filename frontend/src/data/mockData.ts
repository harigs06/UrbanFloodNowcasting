import { CityConfig, StreetSegment, DrainageNode, DrainageConduit, HistoricalStormScenario, AlertNotification } from '../types';

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

// Dense City-Wide Street Network for Hyderabad (45 Segments)
export const HYDERABAD_STREETS: StreetSegment[] = [
  {
    id: "hyd-st-01",
    name: "Tank Bund Road (Hussain Sagar East)",
    ward: "Secunderabad / Begumpet",
    fromIntersection: "Sailing Club Jn",
    toIntersection: "Secretariat Circle",
    lengthM: 2100,
    waterDepthCm: 22.4,
    riskLevel: "impassable",
    flowVelocityMs: 1.45,
    coordinates: [
      [17.43200, 78.47800],
      [17.42600, 78.47600],
      [17.41800, 78.47400],
      [17.41200, 78.47100]
    ],
    blocked: true,
    elevationM: 512.1,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 9.2
  },
  {
    id: "hyd-st-02",
    name: "Begumpet Airport Nallah Corridor",
    ward: "Begumpet (Ward 148)",
    fromIntersection: "Prakash Nagar Metro",
    toIntersection: "Rasoolpura Flyover",
    lengthM: 1750,
    waterDepthCm: 18.6,
    riskLevel: "impassable",
    flowVelocityMs: 1.82,
    coordinates: [
      [17.44300, 78.46800],
      [17.44100, 78.47500],
      [17.43800, 78.48300]
    ],
    blocked: true,
    elevationM: 508.3,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 8.7
  },
  {
    id: "hyd-st-03",
    name: "Khairatabad Anand Nagar Subway",
    ward: "Khairatabad (Ward 96)",
    fromIntersection: "Khairatabad Rly Bridge",
    toIntersection: "Lakdikapul Jn",
    lengthM: 980,
    waterDepthCm: 34.2,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [17.41100, 78.46200],
      [17.40800, 78.46400],
      [17.40400, 78.46600]
    ],
    blocked: true,
    elevationM: 504.6,
    drainageCapacityM3s: 3.1,
    runoffInflowM3s: 7.9
  },
  {
    id: "hyd-st-04",
    name: "Banjara Hills Road No. 12 (Elevated Ridge)",
    ward: "Banjara Hills (Ward 98)",
    fromIntersection: "Cancer Hospital Jn",
    toIntersection: "MLA Colony Gate",
    lengthM: 1600,
    waterDepthCm: 2.1,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [17.41500, 78.43500],
      [17.42000, 78.44100],
      [17.42500, 78.44800]
    ],
    blocked: false,
    elevationM: 545.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 2.4
  },
  {
    id: "hyd-st-05",
    name: "Somajiguda Raj Bhavan Road",
    ward: "Somajiguda (Ward 97)",
    fromIntersection: "Erramanzil Colony",
    toIntersection: "Raj Bhavan Quarters",
    lengthM: 1250,
    waterDepthCm: 8.4,
    riskLevel: "caution",
    flowVelocityMs: 0.75,
    coordinates: [
      [17.42100, 78.45200],
      [17.42400, 78.45600],
      [17.42600, 78.45800]
    ],
    blocked: false,
    elevationM: 516.4,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 5.1
  },
  {
    id: "hyd-st-06",
    name: "Panjagutta Main Flyover (High Clearance)",
    ward: "Panjagutta (Ward 100)",
    fromIntersection: "Nagarjuna Circle",
    toIntersection: "Ameerpet Metro",
    lengthM: 1400,
    waterDepthCm: 4.2,
    riskLevel: "safe",
    flowVelocityMs: 0.35,
    coordinates: [
      [17.42500, 78.44800],
      [17.42900, 78.45100],
      [17.43500, 78.45500]
    ],
    blocked: false,
    elevationM: 528.2,
    drainageCapacityM3s: 5.8,
    runoffInflowM3s: 3.2
  },
  {
    id: "hyd-st-07",
    name: "Necklace Road (PV Ghat Shoreline)",
    ward: "Khairatabad Basin",
    fromIntersection: "Sanjeevaiah Park Gate",
    toIntersection: "Peoples Plaza Ingress",
    lengthM: 1850,
    waterDepthCm: 28.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.65,
    coordinates: [
      [17.43500, 78.46800],
      [17.43000, 78.46500],
      [17.42500, 78.46300],
      [17.41800, 78.46500]
    ],
    blocked: true,
    elevationM: 506.0,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 8.4
  },
  {
    id: "hyd-st-08",
    name: "Lower Tank Bund Road (Kavadiguda Channel)",
    ward: "Musheerabad (Ward 87)",
    fromIntersection: "Bible House Jn",
    toIntersection: "Indira Park Gate",
    lengthM: 1650,
    waterDepthCm: 16.2,
    riskLevel: "impassable",
    flowVelocityMs: 1.3,
    coordinates: [
      [17.42500, 78.48200],
      [17.42000, 78.48100],
      [17.41500, 78.48000],
      [17.41000, 78.47900]
    ],
    blocked: true,
    elevationM: 507.5,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 7.5
  },
  {
    id: "hyd-st-09",
    name: "Basheerbagh - Liberty Circle Arterial",
    ward: "Himayatnagar (Ward 83)",
    fromIntersection: "Liberty Circle",
    toIntersection: "Basheerbagh Flyover",
    lengthM: 1100,
    waterDepthCm: 3.0,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [17.40200, 78.47500],
      [17.40500, 78.47800],
      [17.40800, 78.48200]
    ],
    blocked: false,
    elevationM: 520.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 2.1
  },
  {
    id: "hyd-st-10",
    name: "Himayatnagar Main Road",
    ward: "Himayatnagar (Ward 84)",
    fromIntersection: "Himayatnagar Y-Jn",
    toIntersection: "Narayanaguda Flyover",
    lengthM: 1300,
    waterDepthCm: 6.5,
    riskLevel: "caution",
    flowVelocityMs: 0.45,
    coordinates: [
      [17.40500, 78.48500],
      [17.40200, 78.49000],
      [17.39800, 78.49400]
    ],
    blocked: false,
    elevationM: 518.0,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 4.2
  },
  {
    id: "hyd-st-11",
    name: "RTC X Roads - Chikkadpally Corridor",
    ward: "Chikkadpally (Ward 86)",
    fromIntersection: "RTC X Roads",
    toIntersection: "Narayanaguda Jn",
    lengthM: 1450,
    waterDepthCm: 11.2,
    riskLevel: "caution",
    flowVelocityMs: 0.85,
    coordinates: [
      [17.40800, 78.49500],
      [17.40300, 78.49600],
      [17.39800, 78.49400]
    ],
    blocked: false,
    elevationM: 512.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 6.1
  },
  {
    id: "hyd-st-12",
    name: "Musheerabad - Kavadiguda Link",
    ward: "Musheerabad (Ward 88)",
    fromIntersection: "Musheerabad Jn",
    toIntersection: "Kavadiguda Cross Roads",
    lengthM: 1200,
    waterDepthCm: 13.8,
    riskLevel: "caution",
    flowVelocityMs: 0.95,
    coordinates: [
      [17.42000, 78.50000],
      [17.41600, 78.49200],
      [17.41200, 78.48500]
    ],
    blocked: false,
    elevationM: 510.5,
    drainageCapacityM3s: 3.8,
    runoffInflowM3s: 6.9
  },
  {
    id: "hyd-st-13",
    name: "MG Road Secunderabad (Central Commercial)",
    ward: "Secunderabad (Ward 147)",
    fromIntersection: "Paradise Circle",
    toIntersection: "Secunderabad Station",
    lengthM: 1600,
    waterDepthCm: 7.8,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [17.44200, 78.48700],
      [17.44000, 78.49800],
      [17.43700, 78.50400]
    ],
    blocked: false,
    elevationM: 522.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 5.0
  },
  {
    id: "hyd-st-14",
    name: "SP Road / Parade Ground Link",
    ward: "Secunderabad (Ward 146)",
    fromIntersection: "Rasoolpura Jn",
    toIntersection: "Sangeet Cinema Jn",
    lengthM: 1900,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [17.44100, 78.47500],
      [17.44000, 78.48500],
      [17.44200, 78.50200]
    ],
    blocked: false,
    elevationM: 525.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 3.8
  },
  {
    id: "hyd-st-15",
    name: "Bowenpally National Highway NH-44",
    ward: "Bowenpally (Ward 131)",
    fromIntersection: "Tadbund Cross Roads",
    toIntersection: "Bowenpally Checkpost",
    lengthM: 2200,
    waterDepthCm: 5.5,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [17.45800, 78.48800],
      [17.46500, 78.48600],
      [17.47200, 78.48400]
    ],
    blocked: false,
    elevationM: 532.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 4.5
  },
  {
    id: "hyd-st-16",
    name: "Trimulgherry - Alwal Corridor",
    ward: "Alwal (Ward 133)",
    fromIntersection: "Trimulgherry Cross Roads",
    toIntersection: "Lothkunta Jn",
    lengthM: 2400,
    waterDepthCm: 9.2,
    riskLevel: "caution",
    flowVelocityMs: 0.65,
    coordinates: [
      [17.47500, 78.51000],
      [17.48800, 78.51200],
      [17.50200, 78.51500]
    ],
    blocked: false,
    elevationM: 530.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 5.8
  },
  {
    id: "hyd-st-17",
    name: "Malkajgiri Railway Overbridge Approach",
    ward: "Malkajgiri (Ward 139)",
    fromIntersection: "Malkajgiri Jn",
    toIntersection: "Anandbagh Cross Roads",
    lengthM: 1700,
    waterDepthCm: 14.5,
    riskLevel: "caution",
    flowVelocityMs: 1.1,
    coordinates: [
      [17.44800, 78.52500],
      [17.45200, 78.53000],
      [17.45800, 78.53800]
    ],
    blocked: false,
    elevationM: 515.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 6.8
  },
  {
    id: "hyd-st-18",
    name: "Tarnaka Flyover & University Link",
    ward: "Tarnaka (Ward 142)",
    fromIntersection: "Sangeet Jn",
    toIntersection: "Tarnaka Cross Roads",
    lengthM: 2100,
    waterDepthCm: 2.5,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [17.43800, 78.51500],
      [17.43200, 78.52500],
      [17.42800, 78.53200]
    ],
    blocked: false,
    elevationM: 535.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 2.8
  },
  {
    id: "hyd-st-19",
    name: "Habsiguda - Uppal Ring Road Corridor",
    ward: "Uppal (Ward 7)",
    fromIntersection: "Tarnaka Cross Roads",
    toIntersection: "Uppal Ring Road Jn",
    lengthM: 2800,
    waterDepthCm: 8.0,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [17.42800, 78.53200],
      [17.41500, 78.54500],
      [17.40000, 78.56000]
    ],
    blocked: false,
    elevationM: 518.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 5.5
  },
  {
    id: "hyd-st-20",
    name: "Ramanthapur Lake Road Corridor",
    ward: "Amberpet (Ward 81)",
    fromIntersection: "Uppal Ring Road Jn",
    toIntersection: "Amberpet Causeway",
    lengthM: 2300,
    waterDepthCm: 26.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.7,
    coordinates: [
      [17.40000, 78.56000],
      [17.39500, 78.53500],
      [17.38800, 78.51500]
    ],
    blocked: true,
    elevationM: 502.0,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 9.5
  },
  {
    id: "hyd-st-21",
    name: "Amberpet Causeway & Nallah Crossing",
    ward: "Amberpet (Ward 82)",
    fromIntersection: "Amberpet Bridge",
    toIntersection: "Nimboliadda Jn",
    lengthM: 1500,
    waterDepthCm: 31.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.95,
    coordinates: [
      [17.38800, 78.51500],
      [17.38200, 78.50200],
      [17.37800, 78.49500]
    ],
    blocked: true,
    elevationM: 498.0,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 10.8
  },
  {
    id: "hyd-st-22",
    name: "Hitec City Cyber Towers Flyover",
    ward: "Madhapur (Ward 107)",
    fromIntersection: "Cyber Gateway",
    toIntersection: "Cyber Towers Rotary",
    lengthM: 1400,
    waterDepthCm: 3.5,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [17.45200, 78.37000],
      [17.44900, 78.37500],
      [17.44700, 78.38000]
    ],
    blocked: false,
    elevationM: 552.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 2.8
  },
  {
    id: "hyd-st-23",
    name: "Mindspace - Inorbit Mall Arterial",
    ward: "Madhapur (Ward 106)",
    fromIntersection: "Cyber Towers Rotary",
    toIntersection: "Inorbit Mall Ingress",
    lengthM: 1650,
    waterDepthCm: 7.2,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [17.44700, 78.38000],
      [17.44000, 78.38300],
      [17.43500, 78.38700]
    ],
    blocked: false,
    elevationM: 546.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 4.8
  },
  {
    id: "hyd-st-24",
    name: "Durgam Cheruvu Cable Bridge Approach",
    ward: "Jubilee Hills Link",
    fromIntersection: "Inorbit Mall Ingress",
    toIntersection: "Jubilee Hills Rd 45 Jn",
    lengthM: 1800,
    waterDepthCm: 2.0,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [17.43500, 78.38700],
      [17.43200, 78.39500],
      [17.43000, 78.40500]
    ],
    blocked: false,
    elevationM: 558.0,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 1.9
  },
  {
    id: "hyd-st-25",
    name: "Road No. 36 Jubilee Hills",
    ward: "Jubilee Hills (Ward 104)",
    fromIntersection: "Jubilee Hills Rd 45 Jn",
    toIntersection: "Jubilee Hills Checkpost",
    lengthM: 2100,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [17.43000, 78.40500],
      [17.43100, 78.41200],
      [17.43000, 78.42000]
    ],
    blocked: false,
    elevationM: 560.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 3.0
  },
  {
    id: "hyd-st-26",
    name: "Road No. 10 Banjara Hills Connector",
    ward: "Banjara Hills (Ward 99)",
    fromIntersection: "Jubilee Hills Checkpost",
    toIntersection: "Banjara Hills Rd 1 Jn",
    lengthM: 1900,
    waterDepthCm: 5.0,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [17.43000, 78.42000],
      [17.42500, 78.43500],
      [17.42200, 78.45000]
    ],
    blocked: false,
    elevationM: 548.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 3.6
  },
  {
    id: "hyd-st-27",
    name: "Gachibowli Flyover & Bio-Diversity Jn",
    ward: "Gachibowli (Ward 105)",
    fromIntersection: "Bio-Diversity Park Jn",
    toIntersection: "Gachibowli Stadium Cross",
    lengthM: 2200,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [17.44000, 78.36500],
      [17.44000, 78.35500],
      [17.44000, 78.34800]
    ],
    blocked: false,
    elevationM: 550.0,
    drainageCapacityM3s: 6.8,
    runoffInflowM3s: 4.2
  },
  {
    id: "hyd-st-28",
    name: "Financial District ISB Main Road",
    ward: "Nanakramguda (Ward 108)",
    fromIntersection: "Gachibowli Stadium Cross",
    toIntersection: "Wipro Circle Nanakramguda",
    lengthM: 2600,
    waterDepthCm: 3.2,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [17.44000, 78.34800],
      [17.42800, 78.34500],
      [17.41800, 78.34200]
    ],
    blocked: false,
    elevationM: 555.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 2.5
  },
  {
    id: "hyd-st-29",
    name: "Kondapur Main Road / Botanical Garden",
    ward: "Kondapur (Ward 109)",
    fromIntersection: "Botanical Garden Jn",
    toIntersection: "Kothaguda Cross Roads",
    lengthM: 1750,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [17.45500, 78.35800],
      [17.46000, 78.36500],
      [17.46300, 78.37200]
    ],
    blocked: false,
    elevationM: 544.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 5.2
  },
  {
    id: "hyd-st-30",
    name: "KPHB Colony Main Road Phase 1",
    ward: "Kukatpally (Ward 114)",
    fromIntersection: "JNTU Metro Station",
    toIntersection: "KPHB Phase 1 Rotary",
    lengthM: 1900,
    waterDepthCm: 13.5,
    riskLevel: "caution",
    flowVelocityMs: 0.9,
    coordinates: [
      [17.49800, 78.39000],
      [17.49300, 78.39000],
      [17.48700, 78.39200]
    ],
    blocked: false,
    elevationM: 528.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 6.5
  },
  {
    id: "hyd-st-31",
    name: "Kukatpally Y-Junction National Highway",
    ward: "Kukatpally (Ward 115)",
    fromIntersection: "KPHB Phase 1 Rotary",
    toIntersection: "Moosapet Metro Jn",
    lengthM: 2100,
    waterDepthCm: 16.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.25,
    coordinates: [
      [17.48700, 78.39200],
      [17.48000, 78.40500],
      [17.47200, 78.43200]
    ],
    blocked: true,
    elevationM: 518.0,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 7.8
  },
  {
    id: "hyd-st-32",
    name: "Balanagar Industrial Main Road",
    ward: "Balanagar (Ward 120)",
    fromIntersection: "Moosapet Metro Jn",
    toIntersection: "IDPL Colony Cross Roads",
    lengthM: 2300,
    waterDepthCm: 19.8,
    riskLevel: "impassable",
    flowVelocityMs: 1.4,
    coordinates: [
      [17.47200, 78.43200],
      [17.46800, 78.44800],
      [17.46500, 78.46200]
    ],
    blocked: true,
    elevationM: 514.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 8.5
  },
  {
    id: "hyd-st-33",
    name: "Moosarambagh Lowland Causeway",
    ward: "Malakpet (Ward 24)",
    fromIntersection: "Moosarambagh Bridge",
    toIntersection: "Amberpet Old Bridge",
    lengthM: 1100,
    waterDepthCm: 38.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.3,
    coordinates: [
      [17.37500, 78.50500],
      [17.37800, 78.50800],
      [17.38200, 78.51200]
    ],
    blocked: true,
    elevationM: 492.0,
    drainageCapacityM3s: 2.8,
    runoffInflowM3s: 13.5
  },
  {
    id: "hyd-st-34",
    name: "Chaderghat Bridge & Musi River Bank",
    ward: "Chaderghat (Ward 26)",
    fromIntersection: "Chaderghat Rotary",
    toIntersection: "Rang Mahal Jn",
    lengthM: 1350,
    waterDepthCm: 29.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.85,
    coordinates: [
      [17.37800, 78.48800],
      [17.37500, 78.48400],
      [17.37200, 78.48000]
    ],
    blocked: true,
    elevationM: 495.0,
    drainageCapacityM3s: 3.0,
    runoffInflowM3s: 11.2
  },
  {
    id: "hyd-st-35",
    name: "Malakpet Railway Underpass Corridor",
    ward: "Malakpet (Ward 25)",
    fromIntersection: "Chaderghat Rotary",
    toIntersection: "Malakpet Gunj Jn",
    lengthM: 1500,
    waterDepthCm: 33.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.05,
    coordinates: [
      [17.37800, 78.48800],
      [17.37200, 78.49200],
      [17.36800, 78.50200]
    ],
    blocked: true,
    elevationM: 494.0,
    drainageCapacityM3s: 3.1,
    runoffInflowM3s: 12.0
  },
  {
    id: "hyd-st-36",
    name: "Dilsukhnagar Main Commercial Highway",
    ward: "Dilsukhnagar (Ward 21)",
    fromIntersection: "Malakpet Gunj Jn",
    toIntersection: "Dilsukhnagar Bus Depot",
    lengthM: 2200,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [17.36800, 78.50200],
      [17.36800, 78.51500],
      [17.36800, 78.52500]
    ],
    blocked: false,
    elevationM: 510.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 5.0
  },
  {
    id: "hyd-st-37",
    name: "LB Nagar Ring Road Multi-tier Jn",
    ward: "LB Nagar (Ward 11)",
    fromIntersection: "Dilsukhnagar Bus Depot",
    toIntersection: "LB Nagar Metro Hub",
    lengthM: 2600,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [17.36800, 78.52500],
      [17.36000, 78.54000],
      [17.35000, 78.55000]
    ],
    blocked: false,
    elevationM: 520.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 3.5
  },
  {
    id: "hyd-st-38",
    name: "Nayapul / High Court Musi River Road",
    ward: "Old City (Ward 53)",
    fromIntersection: "Madina Chowk",
    toIntersection: "High Court Gate Jn",
    lengthM: 1200,
    waterDepthCm: 24.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.55,
    coordinates: [
      [17.36700, 78.47500],
      [17.36900, 78.47300],
      [17.37200, 78.47000]
    ],
    blocked: true,
    elevationM: 497.0,
    drainageCapacityM3s: 3.4,
    runoffInflowM3s: 9.8
  },
  {
    id: "hyd-st-39",
    name: "Charminar Pedestrian & Heritage Ring",
    ward: "Charminar (Ward 50)",
    fromIntersection: "Madina Chowk",
    toIntersection: "Charminar Monument Circle",
    lengthM: 1100,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [17.36500, 78.47500],
      [17.36300, 78.47400],
      [17.36100, 78.47400]
    ],
    blocked: false,
    elevationM: 510.0,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 4.0
  },
  {
    id: "hyd-st-40",
    name: "Puranapul Bridge & Riverbank Road",
    ward: "Puranapul (Ward 55)",
    fromIntersection: "City College Cross",
    toIntersection: "Puranapul Darwaza",
    lengthM: 1300,
    waterDepthCm: 27.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.75,
    coordinates: [
      [17.36600, 78.46800],
      [17.36400, 78.46400],
      [17.36400, 78.46000]
    ],
    blocked: true,
    elevationM: 496.0,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 10.5
  },
  {
    id: "hyd-st-41",
    name: "Bahadurpura Zoo Park Corridor",
    ward: "Bahadurpura (Ward 58)",
    fromIntersection: "Puranapul Darwaza",
    toIntersection: "Nehru Zoo Park Main Gate",
    lengthM: 1800,
    waterDepthCm: 11.5,
    riskLevel: "caution",
    flowVelocityMs: 0.8,
    coordinates: [
      [17.36400, 78.46000],
      [17.35800, 78.45800],
      [17.35000, 78.45500]
    ],
    blocked: false,
    elevationM: 508.0,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 6.2
  },
  {
    id: "hyd-st-42",
    name: "Falaknuma Palace Hilltop Link",
    ward: "Falaknuma (Ward 62)",
    fromIntersection: "Falaknuma Rly Station",
    toIntersection: "Palace Gate Main",
    lengthM: 1600,
    waterDepthCm: 1.5,
    riskLevel: "safe",
    flowVelocityMs: 0.1,
    coordinates: [
      [17.33800, 78.46500],
      [17.33400, 78.46700],
      [17.33000, 78.46800]
    ],
    blocked: false,
    elevationM: 548.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 1.8
  },
  {
    id: "hyd-st-43",
    name: "Chandrayangutta Flyover Jn",
    ward: "Chandrayangutta (Ward 64)",
    fromIntersection: "Falaknuma Rly Station",
    toIntersection: "Chandrayangutta Cross Roads",
    lengthM: 1900,
    waterDepthCm: 8.2,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [17.33800, 78.46500],
      [17.33000, 78.47200],
      [17.32000, 78.48000]
    ],
    blocked: false,
    elevationM: 515.0,
    drainageCapacityM3s: 5.8,
    runoffInflowM3s: 5.2
  },
  {
    id: "hyd-st-44",
    name: "Santoshnagar Main Road Corridor",
    ward: "Santoshnagar (Ward 44)",
    fromIntersection: "Chandrayangutta Cross Roads",
    toIntersection: "IS Sadan Cross Roads",
    lengthM: 2100,
    waterDepthCm: 12.0,
    riskLevel: "caution",
    flowVelocityMs: 0.85,
    coordinates: [
      [17.32000, 78.48000],
      [17.33000, 78.49500],
      [17.34000, 78.51000]
    ],
    blocked: false,
    elevationM: 518.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 6.5
  },
  {
    id: "hyd-st-45",
    name: "PVNR Elevated Expressway (Airport Bypass)",
    ward: "Mehdipatnam to Aramghar",
    fromIntersection: "Mehdipatnam Rotary",
    toIntersection: "Aramghar Jn",
    lengthM: 4500,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [17.39500, 78.44000],
      [17.38500, 78.43500],
      [17.37500, 78.43000],
      [17.36500, 78.42500],
      [17.35500, 78.42000]
    ],
    blocked: false,
    elevationM: 560.0,
    drainageCapacityM3s: 15.0,
    runoffInflowM3s: 0.5
  }
];

// Dense City-Wide Street Network for Mumbai (35 Segments)
export const MUMBAI_STREETS: StreetSegment[] = [
  {
    id: "mum-st-01",
    name: "Marine Drive Promenade Outer Lane",
    ward: "Nariman Point (Ward A)",
    fromIntersection: "NCPA Circle",
    toIntersection: "Churchgate Flyover",
    lengthM: 1900,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [18.92500, 72.82200],
      [18.93500, 72.82400],
      [18.94500, 72.82500]
    ],
    blocked: false,
    elevationM: 5.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 6.5
  },
  {
    id: "mum-st-02",
    name: "Colaba Causeway Main Commercial",
    ward: "Colaba (Ward A)",
    fromIntersection: "Regal Cinema Circle",
    toIntersection: "Colaba Post Office",
    lengthM: 1600,
    waterDepthCm: 5.2,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [18.92200, 72.83200],
      [18.91800, 72.83000],
      [18.91200, 72.82600]
    ],
    blocked: false,
    elevationM: 6.2,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 5.0
  },
  {
    id: "mum-st-03",
    name: "CST / Dr. DN Road Heritage Corridor",
    ward: "Fort (Ward A)",
    fromIntersection: "CST Station Plaza",
    toIntersection: "Flora Fountain Circle",
    lengthM: 1400,
    waterDepthCm: 9.8,
    riskLevel: "caution",
    flowVelocityMs: 0.7,
    coordinates: [
      [18.94000, 72.83500],
      [18.93600, 72.83300],
      [18.93200, 72.83100]
    ],
    blocked: false,
    elevationM: 7.5,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 6.2
  },
  {
    id: "mum-st-04",
    name: "JJ Flyover Elevated Viaduct",
    ward: "Byculla to CST",
    fromIntersection: "JJ Hospital Ingress",
    toIntersection: "CST Flyover Ramp",
    lengthM: 2400,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [18.96000, 72.83800],
      [18.95000, 72.83600],
      [18.94200, 72.83500]
    ],
    blocked: false,
    elevationM: 18.0,
    drainageCapacityM3s: 12.0,
    runoffInflowM3s: 0.8
  },
  {
    id: "mum-st-05",
    name: "Peddar Road / Cumballa Hill Ridge",
    ward: "Malabar Hill (Ward D)",
    fromIntersection: "Kemps Corner",
    toIntersection: "Haji Ali Jn",
    lengthM: 1800,
    waterDepthCm: 2.0,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [18.96500, 72.80800],
      [18.97200, 72.81000],
      [18.97800, 72.81200]
    ],
    blocked: false,
    elevationM: 32.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 2.2
  },
  {
    id: "mum-st-06",
    name: "Haji Ali Junction Coastal Lowland",
    ward: "Worli (Ward G/South)",
    fromIntersection: "Haji Ali Circle",
    toIntersection: "Lotus Cinema Jn",
    lengthM: 1300,
    waterDepthCm: 22.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.45,
    coordinates: [
      [18.97800, 72.81200],
      [18.98500, 72.81400],
      [18.99200, 72.81500]
    ],
    blocked: true,
    elevationM: 3.8,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 10.5
  },
  {
    id: "mum-st-07",
    name: "Worli Seaface Coastal Boulevard",
    ward: "Worli (Ward G/South)",
    fromIntersection: "Worli Dairy",
    toIntersection: "Bandra-Worli Sea Link Ingress",
    lengthM: 2100,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [18.99500, 72.81500],
      [19.00500, 72.81600],
      [19.01500, 72.81800]
    ],
    blocked: false,
    elevationM: 5.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 7.2
  },
  {
    id: "mum-st-08",
    name: "Senapati Bapat Marg / Lower Parel",
    ward: "Lower Parel (Ward G/South)",
    fromIntersection: "Currey Road Jn",
    toIntersection: "Kamala Mills Gate",
    lengthM: 1700,
    waterDepthCm: 14.2,
    riskLevel: "caution",
    flowVelocityMs: 0.95,
    coordinates: [
      [18.99200, 72.83000],
      [18.99800, 72.83000],
      [19.00600, 72.83200]
    ],
    blocked: false,
    elevationM: 6.5,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 7.8
  },
  {
    id: "mum-st-09",
    name: "Hindmata Cinema TT Circle Low Point",
    ward: "Parel (Ward F/South)",
    fromIntersection: "Dadar Tram Jn",
    toIntersection: "Parel TT Circle",
    lengthM: 1300,
    waterDepthCm: 38.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [19.01200, 72.84200],
      [19.01600, 72.84400],
      [19.02000, 72.84600]
    ],
    blocked: true,
    elevationM: 3.2,
    drainageCapacityM3s: 3.0,
    runoffInflowM3s: 14.5
  },
  {
    id: "mum-st-10",
    name: "Dadar TT Circle Commercial Hub",
    ward: "Dadar (Ward F/North)",
    fromIntersection: "Khodadad Circle",
    toIntersection: "Chitra Cinema Jn",
    lengthM: 1500,
    waterDepthCm: 18.2,
    riskLevel: "impassable",
    flowVelocityMs: 1.2,
    coordinates: [
      [19.01800, 72.84400],
      [19.02200, 72.84600],
      [19.02500, 72.84800]
    ],
    blocked: true,
    elevationM: 5.8,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 8.5
  },
  {
    id: "mum-st-11",
    name: "King's Circle / Gandhi Market Basin",
    ward: "Matunga (Ward F/North)",
    fromIntersection: "Maheshwari Udyan",
    toIntersection: "Sion Hospital Jn",
    lengthM: 1600,
    waterDepthCm: 42.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.3,
    coordinates: [
      [19.02800, 72.85200],
      [19.03200, 72.85500],
      [19.03600, 72.85800]
    ],
    blocked: true,
    elevationM: 2.8,
    drainageCapacityM3s: 2.8,
    runoffInflowM3s: 15.0
  },
  {
    id: "mum-st-12",
    name: "Sion Circle & Highway Junction",
    ward: "Sion (Ward F/North)",
    fromIntersection: "Sion Hospital Jn",
    toIntersection: "Sion Fort Cross",
    lengthM: 1400,
    waterDepthCm: 16.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.1,
    coordinates: [
      [19.03600, 72.85800],
      [19.04000, 72.86200],
      [19.04400, 72.86500]
    ],
    blocked: true,
    elevationM: 5.5,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 8.2
  },
  {
    id: "mum-st-13",
    name: "Dharavi 90 Feet Road Catchment",
    ward: "Dharavi (Ward G/North)",
    fromIntersection: "Kala Killa Jn",
    toIntersection: "Mahim Nature Park Gate",
    lengthM: 1900,
    waterDepthCm: 28.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.65,
    coordinates: [
      [19.04000, 72.85000],
      [19.04300, 72.85400],
      [19.04600, 72.85800]
    ],
    blocked: true,
    elevationM: 3.5,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 11.8
  },
  {
    id: "mum-st-14",
    name: "Mahim Causeway Marine Link",
    ward: "Mahim (Ward G/North)",
    fromIntersection: "Mahim Church Circle",
    toIntersection: "Bandra Reclamation Ramp",
    lengthM: 1600,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [19.03800, 72.84000],
      [19.04400, 72.83600],
      [19.04800, 72.83000]
    ],
    blocked: false,
    elevationM: 6.2,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 5.5
  },
  {
    id: "mum-st-15",
    name: "Bandra-Kurla Complex (BKC) Connector",
    ward: "Bandra East (Ward H/East)",
    fromIntersection: "Kalanagar Jn",
    toIntersection: "BKC Bharat Diamond Bourse",
    lengthM: 2100,
    waterDepthCm: 11.2,
    riskLevel: "caution",
    flowVelocityMs: 0.85,
    coordinates: [
      [19.05800, 72.85200],
      [19.06300, 72.86100],
      [19.06800, 72.86900]
    ],
    blocked: false,
    elevationM: 6.8,
    drainageCapacityM3s: 7.2,
    runoffInflowM3s: 7.9
  },
  {
    id: "mum-st-16",
    name: "BKC Central Avenue Financial Corridor",
    ward: "BKC (Ward H/East)",
    fromIntersection: "BKC Connector Jn",
    toIntersection: "MTNL Building Circle",
    lengthM: 1800,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [19.06800, 72.86900],
      [19.06500, 72.87500],
      [19.06200, 72.88000]
    ],
    blocked: false,
    elevationM: 8.2,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 4.2
  },
  {
    id: "mum-st-17",
    name: "Milan Subway Lowland Crossing",
    ward: "Santacruz (Ward H/West)",
    fromIntersection: "Santacruz West Station",
    toIntersection: "Milan Flyover Ingress",
    lengthM: 850,
    waterDepthCm: 48.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.6,
    coordinates: [
      [19.08500, 72.84200],
      [19.08300, 72.84500],
      [19.08100, 72.84800]
    ],
    blocked: true,
    elevationM: 2.1,
    drainageCapacityM3s: 2.5,
    runoffInflowM3s: 16.5
  },
  {
    id: "mum-st-18",
    name: "Khar Subway Lowland Corridor",
    ward: "Khar (Ward H/West)",
    fromIntersection: "Khar West Market",
    toIntersection: "Khar East S.V. Link",
    lengthM: 780,
    waterDepthCm: 44.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.45,
    coordinates: [
      [19.07000, 72.83600],
      [19.07000, 72.83900],
      [19.07100, 72.84200]
    ],
    blocked: true,
    elevationM: 2.3,
    drainageCapacityM3s: 2.6,
    runoffInflowM3s: 15.8
  },
  {
    id: "mum-st-19",
    name: "Andheri Subway Critical Underpass",
    ward: "Andheri (Ward K/West)",
    fromIntersection: "Andheri West Market",
    toIntersection: "Andheri East Highway Ingress",
    lengthM: 920,
    waterDepthCm: 52.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.8,
    coordinates: [
      [19.11800, 72.84200],
      [19.11800, 72.84500],
      [19.11900, 72.84800]
    ],
    blocked: true,
    elevationM: 1.8,
    drainageCapacityM3s: 2.2,
    runoffInflowM3s: 18.0
  },
  {
    id: "mum-st-20",
    name: "Western Express Highway (Bandra - Airport)",
    ward: "Santacruz East",
    fromIntersection: "Kalanagar Flyover",
    toIntersection: "Domestic Airport Flyover",
    lengthM: 3400,
    waterDepthCm: 3.5,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [19.05800, 72.85200],
      [19.07500, 72.85000],
      [19.09500, 72.85200]
    ],
    blocked: false,
    elevationM: 14.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 3.8
  },
  {
    id: "mum-st-21",
    name: "Western Express Highway (Andheri - Goregaon)",
    ward: "Goregaon (Ward P/South)",
    fromIntersection: "WEH Andheri Metro",
    toIntersection: "Goregaon Hub Mall Flyover",
    lengthM: 3800,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [19.11800, 72.85200],
      [19.13800, 72.85500],
      [19.15800, 72.85800]
    ],
    blocked: false,
    elevationM: 16.5,
    drainageCapacityM3s: 10.5,
    runoffInflowM3s: 4.5
  },
  {
    id: "mum-st-22",
    name: "Western Express Highway (Malad - Borivali)",
    ward: "Borivali (Ward R/Central)",
    fromIntersection: "Malad Inorbit Link",
    toIntersection: "Borivali National Park Jn",
    lengthM: 4200,
    waterDepthCm: 3.0,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [19.18000, 72.86000],
      [19.20500, 72.86200],
      [19.22800, 72.86500]
    ],
    blocked: false,
    elevationM: 18.0,
    drainageCapacityM3s: 11.0,
    runoffInflowM3s: 3.2
  },
  {
    id: "mum-st-23",
    name: "S.V. Road Bandra to Santacruz",
    ward: "Bandra (Ward H/West)",
    fromIntersection: "Lucky Restaurant Jn",
    toIntersection: "Santacruz Station West",
    lengthM: 2300,
    waterDepthCm: 13.5,
    riskLevel: "caution",
    flowVelocityMs: 0.9,
    coordinates: [
      [19.05500, 72.83500],
      [19.07000, 72.83500],
      [19.08500, 72.83600]
    ],
    blocked: false,
    elevationM: 6.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 7.5
  },
  {
    id: "mum-st-24",
    name: "Linking Road Shopping Corridor",
    ward: "Khar (Ward H/West)",
    fromIntersection: "Waterfield Road Jn",
    toIntersection: "Santacruz Linking Road Jn",
    lengthM: 1900,
    waterDepthCm: 8.0,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [19.06000, 72.83200],
      [19.07200, 72.83300],
      [19.08200, 72.83400]
    ],
    blocked: false,
    elevationM: 7.2,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 5.8
  },
  {
    id: "mum-st-25",
    name: "JVLR (Jogeshwari-Vikhroli Link Road)",
    ward: "Jogeshwari East",
    fromIntersection: "WEH Jogeshwari Jn",
    toIntersection: "SEEPZ Tech Corridor",
    lengthM: 3100,
    waterDepthCm: 7.0,
    riskLevel: "caution",
    flowVelocityMs: 0.45,
    coordinates: [
      [19.13500, 72.85500],
      [19.13000, 72.87000],
      [19.12500, 72.88500]
    ],
    blocked: false,
    elevationM: 15.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 6.0
  },
  {
    id: "mum-st-26",
    name: "Eastern Freeway High Viaduct",
    ward: "Chembur to South Bombay",
    fromIntersection: "Bhakti Park Ramp",
    toIntersection: "Wadala Gate",
    lengthM: 3500,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [19.03000, 72.88000],
      [19.01500, 72.87500],
      [18.99500, 72.86500]
    ],
    blocked: false,
    elevationM: 18.5,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 1.2
  },
  {
    id: "mum-st-27",
    name: "Kurla LBS Marg Mithi River Lowland",
    ward: "Kurla (Ward L)",
    fromIntersection: "Kurla Kalpana Cinema",
    toIntersection: "Kurla Bus Depot Jn",
    lengthM: 1800,
    waterDepthCm: 36.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.15,
    coordinates: [
      [19.06500, 72.87500],
      [19.06800, 72.87800],
      [19.07200, 72.88200]
    ],
    blocked: true,
    elevationM: 3.0,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 13.8
  },
  {
    id: "mum-st-28",
    name: "SCLR (Santacruz-Chembur Link Road)",
    ward: "Kurla East",
    fromIntersection: "BKC Connector East",
    toIntersection: "Amar Mahal Jn",
    lengthM: 2800,
    waterDepthCm: 6.5,
    riskLevel: "caution",
    flowVelocityMs: 0.45,
    coordinates: [
      [19.06800, 72.86900],
      [19.07200, 72.88000],
      [19.06500, 72.89500]
    ],
    blocked: false,
    elevationM: 14.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 5.5
  },
  {
    id: "mum-st-29",
    name: "Eastern Express Highway (Sion - Ghatkopar)",
    ward: "Ghatkopar (Ward N)",
    fromIntersection: "Priyadarshini Circle",
    toIntersection: "Ghatkopar Pant Nagar Jn",
    lengthM: 3600,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [19.04500, 72.87000],
      [19.06500, 72.89000],
      [19.08500, 72.91000]
    ],
    blocked: false,
    elevationM: 12.0,
    drainageCapacityM3s: 9.5,
    runoffInflowM3s: 4.5
  },
  {
    id: "mum-st-30",
    name: "Eastern Express Highway (Vikhroli - Mulund)",
    ward: "Bhandup / Mulund",
    fromIntersection: "Vikhroli Godrej Flyover",
    toIntersection: "Mulund Toll Naka",
    lengthM: 4500,
    waterDepthCm: 3.8,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [19.11000, 72.92500],
      [19.14500, 72.94000],
      [19.17500, 72.95500]
    ],
    blocked: false,
    elevationM: 14.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 4.0
  },
  {
    id: "mum-st-31",
    name: "Chembur Naka Commercial Corridor",
    ward: "Chembur (Ward M/West)",
    fromIntersection: "Diamond Garden",
    toIntersection: "Chembur Railway Station Jn",
    lengthM: 1600,
    waterDepthCm: 9.5,
    riskLevel: "caution",
    flowVelocityMs: 0.65,
    coordinates: [
      [19.05500, 72.89500],
      [19.05800, 72.90000],
      [19.06200, 72.90500]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 6.2
  },
  {
    id: "mum-st-32",
    name: "Ghatkopar Andheri Link Road (GALR)",
    ward: "Ghatkopar (Ward N)",
    fromIntersection: "Asalpha Metro Station",
    toIntersection: "Ghatkopar Station West",
    lengthM: 2200,
    waterDepthCm: 14.8,
    riskLevel: "caution",
    flowVelocityMs: 1.05,
    coordinates: [
      [19.10200, 72.89200],
      [19.09500, 72.90200],
      [19.08800, 72.91000]
    ],
    blocked: false,
    elevationM: 7.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 7.5
  },
  {
    id: "mum-st-33",
    name: "Bhandup LBS Marg Low Point",
    ward: "Bhandup (Ward S)",
    fromIntersection: "Bhandup Station West",
    toIntersection: "Kanjurmarg Nallah Crossing",
    lengthM: 1750,
    waterDepthCm: 24.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.6,
    coordinates: [
      [19.14500, 72.93000],
      [19.14800, 72.93500],
      [19.15200, 72.93800]
    ],
    blocked: true,
    elevationM: 4.5,
    drainageCapacityM3s: 3.8,
    runoffInflowM3s: 10.2
  },
  {
    id: "mum-st-34",
    name: "Chunabhatti Sion-Trombay Link",
    ward: "Chunabhatti (Ward L)",
    fromIntersection: "Chunabhatti Flyover Ramp",
    toIntersection: "Kurla Priyadarshini Link",
    lengthM: 1500,
    waterDepthCm: 21.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.4,
    coordinates: [
      [19.04800, 72.87200],
      [19.05200, 72.87600],
      [19.05600, 72.88000]
    ],
    blocked: true,
    elevationM: 4.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 9.2
  },
  {
    id: "mum-st-35",
    name: "Sion-Panvel Highway Deonar Corridor",
    ward: "Deonar (Ward M/East)",
    fromIntersection: "Mankhurd Flyover Jn",
    toIntersection: "Vashi Creek Bridge Ingress",
    lengthM: 3200,
    waterDepthCm: 5.0,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [19.04800, 72.91500],
      [19.04000, 72.93500],
      [19.03500, 72.95500]
    ],
    blocked: false,
    elevationM: 9.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 5.0
  }
];

// Dense City-Wide Street Network for Chennai (32 Segments)
export const CHENNAI_STREETS: StreetSegment[] = [
  {
    id: "chn-st-01",
    name: "Kamarajar Salai (Marina Beach Road)",
    ward: "Mylapore (Zone 9)",
    fromIntersection: "War Memorial Circle",
    toIntersection: "Light House Jn",
    lengthM: 2800,
    waterDepthCm: 5.0,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [13.07800, 80.28500],
      [13.05500, 80.28200],
      [13.03800, 80.28000]
    ],
    blocked: false,
    elevationM: 4.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 5.5
  },
  {
    id: "chn-st-02",
    name: "Santhome High Road Coastal Corridor",
    ward: "Mylapore (Zone 9)",
    fromIntersection: "Light House Jn",
    toIntersection: "Foreshore Estate Bus Stand",
    lengthM: 1900,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [13.03800, 80.28000],
      [13.02800, 80.27800],
      [13.01800, 80.27500]
    ],
    blocked: false,
    elevationM: 4.2,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 6.2
  },
  {
    id: "chn-st-03",
    name: "Anna Salai (Mount Road Central)",
    ward: "Teynampet (Zone 9)",
    fromIntersection: "Gemini Flyover",
    toIntersection: "Saidapet Bridge Ingress",
    lengthM: 3100,
    waterDepthCm: 6.2,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [13.05200, 80.25000],
      [13.03500, 80.23500],
      [13.02000, 80.22200]
    ],
    blocked: false,
    elevationM: 9.5,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 5.8
  },
  {
    id: "chn-st-04",
    name: "Gemini / Anna Flyover (High Clearance)",
    ward: "Teynampet (Zone 9)",
    fromIntersection: "Cathedral Road Jn",
    toIntersection: "Nungambakkam High Rd Link",
    lengthM: 1600,
    waterDepthCm: 1.5,
    riskLevel: "safe",
    flowVelocityMs: 0.1,
    coordinates: [
      [13.05500, 80.25200],
      [13.05200, 80.25000],
      [13.04800, 80.24800]
    ],
    blocked: false,
    elevationM: 16.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 1.8
  },
  {
    id: "chn-st-05",
    name: "T. Nagar G.N. Chetty Road Commercial",
    ward: "T. Nagar (Zone 10)",
    fromIntersection: "Panagal Park Circle",
    toIntersection: "Vani Mahal Jn",
    lengthM: 1500,
    waterDepthCm: 12.5,
    riskLevel: "caution",
    flowVelocityMs: 0.85,
    coordinates: [
      [13.04000, 80.23500],
      [13.04200, 80.24000],
      [13.04500, 80.24500]
    ],
    blocked: false,
    elevationM: 7.8,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 7.0
  },
  {
    id: "chn-st-06",
    name: "Usman Road Flyover & Lowland Approach",
    ward: "T. Nagar (Zone 10)",
    fromIntersection: "T. Nagar Bus Terminus",
    toIntersection: "Ranganathan Street Jn",
    lengthM: 1700,
    waterDepthCm: 18.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.25,
    coordinates: [
      [13.03200, 80.22800],
      [13.03800, 80.23200],
      [13.04400, 80.23500]
    ],
    blocked: true,
    elevationM: 6.5,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 8.5
  },
  {
    id: "chn-st-07",
    name: "Nungambakkam High Road Corridor",
    ward: "Nungambakkam (Zone 9)",
    fromIntersection: "Sterling Road Jn",
    toIntersection: "Gemini Flyover Link",
    lengthM: 1900,
    waterDepthCm: 8.0,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [13.06500, 80.24000],
      [13.05800, 80.24500],
      [13.05200, 80.25000]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.0
  },
  {
    id: "chn-st-08",
    name: "Chetpet / Harrington Road Subway",
    ward: "Chetpet (Zone 8)",
    fromIntersection: "Chetpet Railway Station",
    toIntersection: "Harrington Rd Cross",
    lengthM: 1100,
    waterDepthCm: 32.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.05,
    coordinates: [
      [13.07200, 80.23600],
      [13.07000, 80.23800],
      [13.06800, 80.24000]
    ],
    blocked: true,
    elevationM: 3.8,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 11.5
  },
  {
    id: "chn-st-09",
    name: "Poonamallee High Road (EVR Periyar)",
    ward: "Kilpauk (Zone 8)",
    fromIntersection: "Chennai Central Station",
    toIntersection: "Kilpauk Medical College Jn",
    lengthM: 2900,
    waterDepthCm: 11.0,
    riskLevel: "caution",
    flowVelocityMs: 0.75,
    coordinates: [
      [13.08200, 80.27500],
      [13.07800, 80.25500],
      [13.07500, 80.23500]
    ],
    blocked: false,
    elevationM: 7.5,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 7.2
  },
  {
    id: "chn-st-10",
    name: "Velachery Main Road (Lake Marsh Corridor)",
    ward: "Velachery (Zone 13)",
    fromIntersection: "Vijayanagar Bus Terminus",
    toIntersection: "Kaiveli Jn",
    lengthM: 2200,
    waterDepthCm: 38.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.3,
    coordinates: [
      [12.97800, 80.21800],
      [12.97100, 80.22200],
      [12.96500, 80.22600]
    ],
    blocked: true,
    elevationM: 4.2,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 13.5
  },
  {
    id: "chn-st-11",
    name: "Velachery Bypass Road Corridor",
    ward: "Velachery (Zone 13)",
    fromIntersection: "Guru Nanak College Jn",
    toIntersection: "Vijayanagar Bus Terminus",
    lengthM: 1850,
    waterDepthCm: 24.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.55,
    coordinates: [
      [12.98500, 80.21200],
      [12.98000, 80.21500],
      [12.97800, 80.21800]
    ],
    blocked: true,
    elevationM: 5.0,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 9.8
  },
  {
    id: "chn-st-12",
    name: "Madipakkam Lake Basin Road",
    ward: "Madipakkam (Zone 14)",
    fromIntersection: "Kaiveli Jn",
    toIntersection: "Koot Road Madipakkam",
    lengthM: 1600,
    waterDepthCm: 34.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [12.96500, 80.22600],
      [12.96200, 80.21000],
      [12.96000, 80.19800]
    ],
    blocked: true,
    elevationM: 3.8,
    drainageCapacityM3s: 3.0,
    runoffInflowM3s: 12.2
  },
  {
    id: "chn-st-13",
    name: "Adyar Thiru Vi Ka Bridge Riverbank",
    ward: "Adyar (Zone 13)",
    fromIntersection: "Malar Hospital Jn",
    toIntersection: "Adyar Signal",
    lengthM: 1500,
    waterDepthCm: 16.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.1,
    coordinates: [
      [13.01000, 80.26000],
      [13.00500, 80.25800],
      [13.00200, 80.25500]
    ],
    blocked: true,
    elevationM: 5.2,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 8.5
  },
  {
    id: "chn-st-14",
    name: "Sardar Patel Road / Guindy Highway",
    ward: "Guindy (Zone 9)",
    fromIntersection: "Adyar Signal",
    toIntersection: "Kathipara Cloverleaf",
    lengthM: 3200,
    waterDepthCm: 5.5,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [13.00200, 80.25500],
      [13.00500, 80.23000],
      [13.00800, 80.20300]
    ],
    blocked: false,
    elevationM: 12.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 5.2
  },
  {
    id: "chn-st-15",
    name: "Kathipara Multi-Level Grade Separator",
    ward: "Guindy (Zone 9)",
    fromIntersection: "Kathipara Rotary",
    toIntersection: "Airport GST Flyover Ingress",
    lengthM: 2100,
    waterDepthCm: 1.0,
    riskLevel: "safe",
    flowVelocityMs: 0.05,
    coordinates: [
      [13.00800, 80.20300],
      [13.00200, 80.19800],
      [12.99800, 80.19200]
    ],
    blocked: false,
    elevationM: 22.0,
    drainageCapacityM3s: 12.0,
    runoffInflowM3s: 1.5
  },
  {
    id: "chn-st-16",
    name: "GST Road (Guindy - Airport Link)",
    ward: "Guindy / Meenambakkam",
    fromIntersection: "Kathipara Cloverleaf",
    toIntersection: "Chennai Airport Main Gate",
    lengthM: 2800,
    waterDepthCm: 9.5,
    riskLevel: "caution",
    flowVelocityMs: 0.7,
    coordinates: [
      [13.00800, 80.20300],
      [12.99800, 80.19200],
      [12.98500, 80.18000]
    ],
    blocked: false,
    elevationM: 11.4,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 8.0
  },
  {
    id: "chn-st-17",
    name: "OMR Elevated IT Expressway (Perungudi)",
    ward: "Perungudi (Zone 14)",
    fromIntersection: "Tidel Park Jn",
    toIntersection: "Thoraipakkam Toll",
    lengthM: 3600,
    waterDepthCm: 2.2,
    riskLevel: "safe",
    flowVelocityMs: 0.1,
    coordinates: [
      [12.98800, 80.24800],
      [12.96800, 80.24400],
      [12.94800, 80.24000]
    ],
    blocked: false,
    elevationM: 14.5,
    drainageCapacityM3s: 12.0,
    runoffInflowM3s: 3.5
  },
  {
    id: "chn-st-18",
    name: "OMR Lowland Service Road (Sholinganallur)",
    ward: "Sholinganallur (Zone 15)",
    fromIntersection: "Thoraipakkam Toll",
    toIntersection: "Sholinganallur ELCOT Jn",
    lengthM: 3800,
    waterDepthCm: 21.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.4,
    coordinates: [
      [12.94800, 80.24000],
      [12.92500, 80.23500],
      [12.90000, 80.22800]
    ],
    blocked: true,
    elevationM: 4.8,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 10.2
  },
  {
    id: "chn-st-19",
    name: "ECR Coastal Highway (Thiruvanmiyur)",
    ward: "Thiruvanmiyur (Zone 13)",
    fromIntersection: "Thiruvanmiyur Signal",
    toIntersection: "Neelankarai Beach Link",
    lengthM: 3400,
    waterDepthCm: 4.8,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [12.98000, 80.26000],
      [12.96500, 80.26000],
      [12.95000, 80.26000]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 5.0
  },
  {
    id: "chn-st-20",
    name: "Pallikaranai Marshland 200 Feet Radial",
    ward: "Pallikaranai (Zone 14)",
    fromIntersection: "Thoraipakkam Radial Ingress",
    toIntersection: "Medavakkam Jn",
    lengthM: 3900,
    waterDepthCm: 29.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.8,
    coordinates: [
      [12.94000, 80.23500],
      [12.93500, 80.21500],
      [12.93000, 80.19500]
    ],
    blocked: true,
    elevationM: 3.5,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 12.5
  },
  {
    id: "chn-st-21",
    name: "Medavakkam Main Road",
    ward: "Medavakkam (Zone 14)",
    fromIntersection: "Medavakkam Jn",
    toIntersection: "Kovilambakkam Lowland",
    lengthM: 2400,
    waterDepthCm: 18.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.15,
    coordinates: [
      [12.93000, 80.19500],
      [12.94000, 80.18500],
      [12.95000, 80.17500]
    ],
    blocked: true,
    elevationM: 6.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 8.0
  },
  {
    id: "chn-st-22",
    name: "Tambaram GST Highway Corridor",
    ward: "Tambaram (Zone 15)",
    fromIntersection: "Chromepet Flyover",
    toIntersection: "Tambaram Sanatorium Bus Stand",
    lengthM: 3100,
    waterDepthCm: 7.0,
    riskLevel: "caution",
    flowVelocityMs: 0.45,
    coordinates: [
      [12.95000, 80.14500],
      [12.93800, 80.13500],
      [12.92500, 80.12500]
    ],
    blocked: false,
    elevationM: 15.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 6.2
  },
  {
    id: "chn-st-23",
    name: "Chennai Central Railway Station Approach",
    ward: "Park Town (Zone 5)",
    fromIntersection: "Central Station Plaza",
    toIntersection: "Ripon Building Gate",
    lengthM: 1200,
    waterDepthCm: 14.5,
    riskLevel: "caution",
    flowVelocityMs: 0.95,
    coordinates: [
      [13.08200, 80.27500],
      [13.08000, 80.27200],
      [13.07800, 80.27000]
    ],
    blocked: false,
    elevationM: 6.2,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 7.5
  },
  {
    id: "chn-st-24",
    name: "Rajaji Salai / Port Access Corridor",
    ward: "George Town (Zone 5)",
    fromIntersection: "Central Station Plaza",
    toIntersection: "Chennai Port Gate 1",
    lengthM: 1800,
    waterDepthCm: 8.0,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [13.08200, 80.27500],
      [13.08800, 80.28500],
      [13.09500, 80.29200]
    ],
    blocked: false,
    elevationM: 5.5,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.0
  },
  {
    id: "chn-st-25",
    name: "Vyasarpadi Jeeva Railway Subway",
    ward: "Vyasarpadi (Zone 4)",
    fromIntersection: "Vyasarpadi Station Road",
    toIntersection: "GNT Road Link",
    lengthM: 950,
    waterDepthCm: 46.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.5,
    coordinates: [
      [13.10500, 80.26000],
      [13.10700, 80.26300],
      [13.11000, 80.26500]
    ],
    blocked: true,
    elevationM: 2.2,
    drainageCapacityM3s: 2.5,
    runoffInflowM3s: 15.5
  },
  {
    id: "chn-st-26",
    name: "Perambur High Road Underpass Corridor",
    ward: "Perambur (Zone 4)",
    fromIntersection: "Perambur Loco Works",
    toIntersection: "Perambur Flyover Ramp",
    lengthM: 1750,
    waterDepthCm: 28.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.7,
    coordinates: [
      [13.11000, 80.24500],
      [13.10800, 80.24000],
      [13.10500, 80.23500]
    ],
    blocked: true,
    elevationM: 4.0,
    drainageCapacityM3s: 3.8,
    runoffInflowM3s: 11.0
  },
  {
    id: "chn-st-27",
    name: "Madhavaram GNT Highway NH-16",
    ward: "Madhavaram (Zone 3)",
    fromIntersection: "Madhavaram Roundabout",
    toIntersection: "Puzhal Lake Ingress",
    lengthM: 3300,
    waterDepthCm: 6.5,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [13.12500, 80.23000],
      [13.14000, 80.22000],
      [13.15500, 80.21000]
    ],
    blocked: false,
    elevationM: 14.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 5.8
  },
  {
    id: "chn-st-28",
    name: "100 Feet Inner Ring Road (Vadapalani)",
    ward: "Vadapalani (Zone 10)",
    fromIntersection: "Koyambedu CMBT Jn",
    toIntersection: "Vadapalani Signal",
    lengthM: 2600,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [13.07000, 80.19500],
      [13.06000, 80.20200],
      [13.05000, 80.21000]
    ],
    blocked: false,
    elevationM: 9.2,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 6.5
  },
  {
    id: "chn-st-29",
    name: "Koyambedu CMBT Bus Hub Corridor",
    ward: "Koyambedu (Zone 7)",
    fromIntersection: "Poonamallee High Rd Jn",
    toIntersection: "CMBT Bus Terminal Entrance",
    lengthM: 1900,
    waterDepthCm: 19.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.3,
    coordinates: [
      [13.07500, 80.19000],
      [13.07200, 80.19500],
      [13.06800, 80.19800]
    ],
    blocked: true,
    elevationM: 6.0,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 9.2
  },
  {
    id: "chn-st-30",
    name: "Arcot Road Kodambakkam Corridor",
    ward: "Kodambakkam (Zone 10)",
    fromIntersection: "Vadapalani Signal",
    toIntersection: "Kodambakkam Power House",
    lengthM: 2100,
    waterDepthCm: 13.5,
    riskLevel: "caution",
    flowVelocityMs: 0.9,
    coordinates: [
      [13.05000, 80.21000],
      [13.05200, 80.22000],
      [13.05500, 80.23000]
    ],
    blocked: false,
    elevationM: 7.5,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 7.2
  },
  {
    id: "chn-st-31",
    name: "Royapuram Bridge Coastal Road",
    ward: "Royapuram (Zone 5)",
    fromIntersection: "Royapuram Station",
    toIntersection: "Kasimedu Fishing Harbour",
    lengthM: 1700,
    waterDepthCm: 9.0,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [13.11000, 80.29500],
      [13.12000, 80.29800],
      [13.13000, 80.30000]
    ],
    blocked: false,
    elevationM: 5.8,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.5
  },
  {
    id: "chn-st-32",
    name: "Thirumangalam Metro - Anna Nagar West",
    ward: "Anna Nagar (Zone 8)",
    fromIntersection: "Thirumangalam Jn",
    toIntersection: "Anna Nagar Roundabout",
    lengthM: 2200,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [13.08500, 80.19000],
      [13.08500, 80.20500],
      [13.08500, 80.21500]
    ],
    blocked: false,
    elevationM: 15.5,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 4.0
  }
];

// Dense City-Wide Street Network for Delhi NCR (30 Segments)
export const DELHI_STREETS: StreetSegment[] = [
  {
    id: "del-st-01",
    name: "Minto Bridge Railway Underpass",
    ward: "Connaught Place (Ward 78)",
    fromIntersection: "Deen Dayal Upadhyaya Marg",
    toIntersection: "Connaught Circus Ramp",
    lengthM: 650,
    waterDepthCm: 56.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.5,
    coordinates: [
      [28.63400, 77.22800],
      [28.63600, 77.23000],
      [28.63800, 77.23200]
    ],
    blocked: true,
    elevationM: 208.5,
    drainageCapacityM3s: 3.0,
    runoffInflowM3s: 14.0
  },
  {
    id: "del-st-02",
    name: "Connaught Place Outer Circle",
    ward: "Connaught Place (Ward 78)",
    fromIntersection: "Barakhamba Road Radial",
    toIntersection: "Janpath Radial Cross",
    lengthM: 2200,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [28.63200, 77.21800],
      [28.63500, 77.22200],
      [28.63000, 77.22500]
    ],
    blocked: false,
    elevationM: 216.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 6.0
  },
  {
    id: "del-st-03",
    name: "Tilak Bridge Railway Underpass",
    ward: "ITO (Ward 80)",
    fromIntersection: "Bahadur Shah Zafar Marg",
    toIntersection: "Tilak Marg Cross",
    lengthM: 820,
    waterDepthCm: 42.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.2,
    coordinates: [
      [28.62600, 77.23800],
      [28.62800, 77.24000],
      [28.63000, 77.24200]
    ],
    blocked: true,
    elevationM: 209.0,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 12.5
  },
  {
    id: "del-st-04",
    name: "ITO Junction Yamuna Lowland Corridor",
    ward: "IP Estate (Ward 80)",
    fromIntersection: "Vikas Minar Jn",
    toIntersection: "Pragati Maidan Gate",
    lengthM: 1800,
    waterDepthCm: 18.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.25,
    coordinates: [
      [28.62800, 77.24200],
      [28.62500, 77.24600],
      [28.62100, 77.24900]
    ],
    blocked: true,
    elevationM: 211.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 8.8
  },
  {
    id: "del-st-05",
    name: "Pragati Maidan Integrated Tunnel",
    ward: "Central Delhi Tunnel",
    fromIntersection: "Purana Qila Ramp",
    toIntersection: "Ring Road Ingress",
    lengthM: 1600,
    waterDepthCm: 32.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.85,
    coordinates: [
      [28.62000, 77.24000],
      [28.62000, 77.24500],
      [28.62000, 77.25200]
    ],
    blocked: true,
    elevationM: 206.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 11.0
  },
  {
    id: "del-st-06",
    name: "Kartavya Path / Rajpath Boulevard",
    ward: "New Delhi (NDMC)",
    fromIntersection: "Rashtrapati Bhavan",
    toIntersection: "India Gate C-Hexagon",
    lengthM: 2600,
    waterDepthCm: 1.5,
    riskLevel: "safe",
    flowVelocityMs: 0.1,
    coordinates: [
      [28.61400, 77.19800],
      [28.61400, 77.21800],
      [28.61300, 77.22900]
    ],
    blocked: false,
    elevationM: 222.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 2.0
  },
  {
    id: "del-st-07",
    name: "India Gate C-Hexagon Arterial",
    ward: "New Delhi (NDMC)",
    fromIntersection: "Ashoka Road Ingress",
    toIntersection: "Shahjahan Road Ingress",
    lengthM: 1800,
    waterDepthCm: 3.0,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [28.61600, 77.22600],
      [28.61300, 77.22900],
      [28.60800, 77.23000]
    ],
    blocked: false,
    elevationM: 220.0,
    drainageCapacityM3s: 9.0,
    runoffInflowM3s: 3.2
  },
  {
    id: "del-st-08",
    name: "Barapullah Elevated Corridor",
    ward: "South Delhi Expressway",
    fromIntersection: "Sarai Kale Khan Ramp",
    toIntersection: "INA Market Terminus",
    lengthM: 3800,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [28.58800, 77.25500],
      [28.57900, 77.24000],
      [28.57200, 77.21800]
    ],
    blocked: false,
    elevationM: 228.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 1.0
  },
  {
    id: "del-st-09",
    name: "Ring Road Kashmere Gate ISBT Low Point",
    ward: "Kashmere Gate (Ward 72)",
    fromIntersection: "ISBT Bus Ingress",
    toIntersection: "Monastery Market Jn",
    lengthM: 1950,
    waterDepthCm: 36.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [28.66800, 77.22800],
      [28.66800, 77.23200],
      [28.67000, 77.23600]
    ],
    blocked: true,
    elevationM: 207.0,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 13.0
  },
  {
    id: "del-st-10",
    name: "Yamuna Bazar Lowland River Corridor",
    ward: "Old Delhi (Ward 74)",
    fromIntersection: "Hanuman Mandir Yamuna",
    toIntersection: "Salimgarh Fort Link",
    lengthM: 1500,
    waterDepthCm: 48.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.45,
    coordinates: [
      [28.66500, 77.23500],
      [28.66200, 77.23800],
      [28.65800, 77.24000]
    ],
    blocked: true,
    elevationM: 205.5,
    drainageCapacityM3s: 2.8,
    runoffInflowM3s: 15.2
  },
  {
    id: "del-st-11",
    name: "Vikas Marg (Laxmi Nagar - ITO Bridge)",
    ward: "East Delhi (Ward 90)",
    fromIntersection: "Laxmi Nagar Metro",
    toIntersection: "ITO Yamuna Bridge",
    lengthM: 2400,
    waterDepthCm: 14.0,
    riskLevel: "caution",
    flowVelocityMs: 0.95,
    coordinates: [
      [28.63000, 77.27500],
      [28.62900, 77.26000],
      [28.62800, 77.24800]
    ],
    blocked: false,
    elevationM: 212.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 7.5
  },
  {
    id: "del-st-12",
    name: "Akshardham NH-9 Highway Corridor",
    ward: "East Delhi (Ward 92)",
    fromIntersection: "Akshardham Temple Gate",
    toIntersection: "Mayur Vihar Flyover",
    lengthM: 3200,
    waterDepthCm: 5.0,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [28.61500, 77.28000],
      [28.60800, 77.28800],
      [28.60000, 77.29500]
    ],
    blocked: false,
    elevationM: 215.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 5.2
  },
  {
    id: "del-st-13",
    name: "DND Flyway Elevated Viaduct",
    ward: "Delhi-Noida Link",
    fromIntersection: "Maharani Bagh Ramp",
    toIntersection: "Noida Toll Plaza",
    lengthM: 4200,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [28.58000, 77.26500],
      [28.58000, 77.28500],
      [28.58000, 77.30500]
    ],
    blocked: false,
    elevationM: 225.0,
    drainageCapacityM3s: 14.0,
    runoffInflowM3s: 0.8
  },
  {
    id: "del-st-14",
    name: "Ashram Chowk Underpass & Ring Road",
    ward: "Ashram (Ward 62)",
    fromIntersection: "Mathura Road Cross",
    toIntersection: "Lajpat Nagar Ring Link",
    lengthM: 1600,
    waterDepthCm: 28.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.7,
    coordinates: [
      [28.57000, 77.25500],
      [28.57000, 77.26000],
      [28.57000, 77.26500]
    ],
    blocked: true,
    elevationM: 210.0,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 10.5
  },
  {
    id: "del-st-15",
    name: "Moolchand Underpass Ring Road",
    ward: "Lajpat Nagar (Ward 60)",
    fromIntersection: "Moolchand Hospital Jn",
    toIntersection: "Lajpat Nagar Metro Cross",
    lengthM: 980,
    waterDepthCm: 38.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.15,
    coordinates: [
      [28.56800, 77.23200],
      [28.56500, 77.23000],
      [28.56200, 77.22800]
    ],
    blocked: true,
    elevationM: 209.5,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 12.8
  },
  {
    id: "del-st-16",
    name: "AIIMS Flyover Grade Separator",
    ward: "South Delhi (Ward 58)",
    fromIntersection: "AIIMS Main Gate",
    toIntersection: "Safdarjung Hospital Jn",
    lengthM: 1900,
    waterDepthCm: 2.5,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [28.57000, 77.21500],
      [28.57000, 77.21000],
      [28.57000, 77.20500]
    ],
    blocked: false,
    elevationM: 226.0,
    drainageCapacityM3s: 9.0,
    runoffInflowM3s: 2.8
  },
  {
    id: "del-st-17",
    name: "Dhaula Kuan Multi-tier Interchange",
    ward: "South West Delhi",
    fromIntersection: "Dhaula Kuan Metro",
    toIntersection: "Sardar Patel Marg Ingress",
    lengthM: 2300,
    waterDepthCm: 3.5,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [28.59500, 77.16500],
      [28.59800, 77.17000],
      [28.60200, 77.17500]
    ],
    blocked: false,
    elevationM: 235.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 3.5
  },
  {
    id: "del-st-18",
    name: "Mehrauli-Badarpur Road (MB Road)",
    ward: "Saket (Ward 52)",
    fromIntersection: "Saket Metro Station",
    toIntersection: "Khanpur Extension Jn",
    lengthM: 2800,
    waterDepthCm: 19.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.25,
    coordinates: [
      [28.51500, 77.20500],
      [28.51200, 77.22500],
      [28.51000, 77.25000]
    ],
    blocked: true,
    elevationM: 215.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 9.0
  },
  {
    id: "del-st-19",
    name: "Outer Ring Road (Munirka - IIT Gate)",
    ward: "Hauz Khas (Ward 55)",
    fromIntersection: "Munirka Flyover",
    toIntersection: "IIT Delhi Main Gate",
    lengthM: 2400,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [28.55500, 77.17000],
      [28.55000, 77.18500],
      [28.54500, 77.19500]
    ],
    blocked: false,
    elevationM: 230.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 4.2
  },
  {
    id: "del-st-20",
    name: "Rohtak Road Punjabi Bagh Lowland",
    ward: "Punjabi Bagh (Ward 35)",
    fromIntersection: "Punjabi Bagh Club",
    toIntersection: "Zakhira Flyover Ramp",
    lengthM: 2100,
    waterDepthCm: 26.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.65,
    coordinates: [
      [28.66500, 77.12500],
      [28.66500, 77.13500],
      [28.66500, 77.14500]
    ],
    blocked: true,
    elevationM: 210.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 10.5
  },
  {
    id: "del-st-21",
    name: "Najafgarh Drain Perimeter Road",
    ward: "West Delhi (Ward 40)",
    fromIntersection: "Uttam Nagar East",
    toIntersection: "Janakpuri District Centre",
    lengthM: 2600,
    waterDepthCm: 22.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.45,
    coordinates: [
      [28.62500, 77.06500],
      [28.62800, 77.07500],
      [28.63000, 77.08500]
    ],
    blocked: true,
    elevationM: 212.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 9.5
  },
  {
    id: "del-st-22",
    name: "Noida Expressway (Sector 18 - 62)",
    ward: "Noida Expressway",
    fromIntersection: "Film City Flyover",
    toIntersection: "Sector 62 Ingress",
    lengthM: 4500,
    waterDepthCm: 2.0,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [28.57000, 77.32000],
      [28.55000, 77.34000],
      [28.53000, 77.36000]
    ],
    blocked: false,
    elevationM: 218.0,
    drainageCapacityM3s: 12.0,
    runoffInflowM3s: 2.5
  },
  {
    id: "del-st-23",
    name: "NH-48 Cyber City Highway Corridor",
    ward: "Gurugram / DLF",
    fromIntersection: "Ambience Mall Ingress",
    toIntersection: "Cyber Hub Underpass Link",
    lengthM: 2800,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [28.50500, 77.09500],
      [28.49500, 77.09000],
      [28.48500, 77.08500]
    ],
    blocked: false,
    elevationM: 225.0,
    drainageCapacityM3s: 9.0,
    runoffInflowM3s: 5.5
  },
  {
    id: "del-st-24",
    name: "Hero Honda Chowk Low Point (Gurugram)",
    ward: "Gurugram NH-48",
    fromIntersection: "Rajiv Chowk Gurugram",
    toIntersection: "Hero Honda Chowk Flyover",
    lengthM: 2900,
    waterDepthCm: 34.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [28.46000, 77.04500],
      [28.45000, 77.03000],
      [28.44000, 77.01500]
    ],
    blocked: true,
    elevationM: 214.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 13.5
  },
  {
    id: "del-st-25",
    name: "Subhash Chowk Sohna Road Corridor",
    ward: "Gurugram Central",
    fromIntersection: "Subhash Chowk",
    toIntersection: "Vatika City Jn",
    lengthM: 2600,
    waterDepthCm: 16.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.1,
    coordinates: [
      [28.43500, 77.04000],
      [28.42000, 77.04500],
      [28.40500, 77.05000]
    ],
    blocked: true,
    elevationM: 218.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 8.0
  },
  {
    id: "del-st-26",
    name: "Dwarka Expressway Link (Sector 21)",
    ward: "Dwarka (Ward 48)",
    fromIntersection: "Dwarka Sector 21 Metro",
    toIntersection: "Bijwasan Rly Bridge",
    lengthM: 3100,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [28.55000, 77.06000],
      [28.53500, 77.05500],
      [28.52000, 77.05000]
    ],
    blocked: false,
    elevationM: 222.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 4.5
  },
  {
    id: "del-st-27",
    name: "Civil Lines Boulevard (Ridge Ingress)",
    ward: "Civil Lines (Ward 70)",
    fromIntersection: "Delhi University Metro",
    toIntersection: "Tis Hazari Court Link",
    lengthM: 2300,
    waterDepthCm: 3.0,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [28.69000, 77.21500],
      [28.67500, 77.22000],
      [28.66500, 77.22000]
    ],
    blocked: false,
    elevationM: 232.0,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 3.0
  },
  {
    id: "del-st-28",
    name: "Majnu Ka Tilla Outer Ring Road",
    ward: "Civil Lines (Ward 70)",
    fromIntersection: "Wazirabad Bridge Ingress",
    toIntersection: "ISBT Kashmere Gate",
    lengthM: 2500,
    waterDepthCm: 21.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.4,
    coordinates: [
      [28.70500, 77.23000],
      [28.68500, 77.22800],
      [28.66800, 77.22800]
    ],
    blocked: true,
    elevationM: 208.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 10.0
  },
  {
    id: "del-st-29",
    name: "Shastri Park G.T. Road Approach",
    ward: "North East Delhi",
    fromIntersection: "Kashmere Gate Bridge",
    toIntersection: "Shastri Park Metro Hub",
    lengthM: 2100,
    waterDepthCm: 15.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.05,
    coordinates: [
      [28.67000, 77.24000],
      [28.67000, 77.25000],
      [28.67000, 77.26000]
    ],
    blocked: true,
    elevationM: 210.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 7.8
  },
  {
    id: "del-st-30",
    name: "Sarai Kale Khan Ring Road Interchange",
    ward: "South East Delhi",
    fromIntersection: "Pragati Maidan Ramp",
    toIntersection: "Sarai Kale Khan ISBT",
    lengthM: 1950,
    waterDepthCm: 9.5,
    riskLevel: "caution",
    flowVelocityMs: 0.65,
    coordinates: [
      [28.60500, 77.25500],
      [28.59500, 77.25800],
      [28.58500, 77.26000]
    ],
    blocked: false,
    elevationM: 214.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 6.5
  }
];

// Dense City-Wide Street Network for Bengaluru (30 Segments)
export const BENGALURU_STREETS: StreetSegment[] = [
  {
    id: "blr-st-01",
    name: "MG Road - Trinity Circle Central Link",
    ward: "Shantala Nagar (Ward 111)",
    fromIntersection: "Anil Kumble Circle",
    toIntersection: "Trinity Metro Station",
    lengthM: 1600,
    waterDepthCm: 3.2,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [12.97500, 77.60800],
      [12.97300, 77.61600],
      [12.97200, 77.62400]
    ],
    blocked: false,
    elevationM: 915.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 2.8
  },
  {
    id: "blr-st-02",
    name: "Brigade Road Commercial Promenade",
    ward: "Shantala Nagar (Ward 111)",
    fromIntersection: "MG Road Jn",
    toIntersection: "Hosur Road Junction",
    lengthM: 1400,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [12.97400, 77.60800],
      [12.96800, 77.60800],
      [12.96200, 77.60800]
    ],
    blocked: false,
    elevationM: 912.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 3.5
  },
  {
    id: "blr-st-03",
    name: "Vidhana Soudha / Ambedkar Veedhi",
    ward: "Shivajinagar (Ward 110)",
    fromIntersection: "GPO Circle",
    toIntersection: "High Court Gate",
    lengthM: 1200,
    waterDepthCm: 1.5,
    riskLevel: "safe",
    flowVelocityMs: 0.1,
    coordinates: [
      [12.98200, 77.59200],
      [12.97900, 77.59000],
      [12.97600, 77.58800]
    ],
    blocked: false,
    elevationM: 924.0,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 1.5
  },
  {
    id: "blr-st-04",
    name: "Kempegowda Majestic Bus Stand Ingress",
    ward: "Chickpet (Ward 109)",
    fromIntersection: "Majestic Railway Station",
    toIntersection: "Mysore Bank Circle",
    lengthM: 1500,
    waterDepthCm: 11.5,
    riskLevel: "caution",
    flowVelocityMs: 0.8,
    coordinates: [
      [12.97800, 77.57000],
      [12.97600, 77.57500],
      [12.97400, 77.58000]
    ],
    blocked: false,
    elevationM: 905.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 6.5
  },
  {
    id: "blr-st-05",
    name: "Richmond Circle Flyover Grade Separator",
    ward: "Sampangiram Nagar",
    fromIntersection: "Richmond Road",
    toIntersection: "Double Road Flyover",
    lengthM: 1300,
    waterDepthCm: 2.0,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [12.96200, 77.59600],
      [12.96000, 77.60000],
      [12.95800, 77.60400]
    ],
    blocked: false,
    elevationM: 918.0,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 2.2
  },
  {
    id: "blr-st-06",
    name: "Silk Board Junction Underpass",
    ward: "BTM Layout (Ward 176)",
    fromIntersection: "Hosur Road Ingress",
    toIntersection: "Madiwala Lake Outfall",
    lengthM: 1200,
    waterDepthCm: 28.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.75,
    coordinates: [
      [12.91700, 77.62200],
      [12.92100, 77.62500],
      [12.92500, 77.62800]
    ],
    blocked: true,
    elevationM: 878.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 11.8
  },
  {
    id: "blr-st-07",
    name: "Outer Ring Road (Bellandur Ecospace)",
    ward: "Bellandur (Ward 150)",
    fromIntersection: "Ecospace Tech Park Gate",
    toIntersection: "Devarabisanahalli Flyover",
    lengthM: 1950,
    waterDepthCm: 44.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.4,
    coordinates: [
      [12.92800, 77.67800],
      [12.93300, 77.68500],
      [12.93800, 77.69200]
    ],
    blocked: true,
    elevationM: 865.2,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 15.0
  },
  {
    id: "blr-st-08",
    name: "ORR Marathahalli Bridge Corridor",
    ward: "Marathahalli (Ward 85)",
    fromIntersection: "Kalamandir Multiplex",
    toIntersection: "Marathahalli Multiplex Jn",
    lengthM: 1800,
    waterDepthCm: 16.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.1,
    coordinates: [
      [12.95200, 77.69800],
      [12.95600, 77.70200],
      [12.96000, 77.70600]
    ],
    blocked: true,
    elevationM: 872.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 8.5
  },
  {
    id: "blr-st-09",
    name: "ORR Kadubeesanahalli Lowland Underpass",
    ward: "Kadubeesanahalli",
    fromIntersection: "Cisco Ingress Gate",
    toIntersection: "Panathur Railway Subway Link",
    lengthM: 1400,
    waterDepthCm: 36.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [12.93600, 77.69200],
      [12.94000, 77.69600],
      [12.94400, 77.70000]
    ],
    blocked: true,
    elevationM: 864.0,
    drainageCapacityM3s: 3.8,
    runoffInflowM3s: 13.0
  },
  {
    id: "blr-st-10",
    name: "Rainbow Drive Layout Ingress (Sarjapur)",
    ward: "Sarjapur Road",
    fromIntersection: "Sarjapur Main Gate",
    toIntersection: "Wipro Corporate Jn",
    lengthM: 1400,
    waterDepthCm: 52.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.8,
    coordinates: [
      [12.90500, 77.69500],
      [12.90900, 77.70100],
      [12.91400, 77.70800]
    ],
    blocked: true,
    elevationM: 860.5,
    drainageCapacityM3s: 3.2,
    runoffInflowM3s: 16.5
  },
  {
    id: "blr-st-11",
    name: "Sarjapur Main Road / Kaikondrahalli Lake",
    ward: "Bellandur (Ward 150)",
    fromIntersection: "Kaikondrahalli Lake Gate",
    toIntersection: "Carmelaram Station Cross",
    lengthM: 2200,
    waterDepthCm: 24.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.55,
    coordinates: [
      [12.91000, 77.67500],
      [12.91200, 77.68500],
      [12.91500, 77.69800]
    ],
    blocked: true,
    elevationM: 868.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 10.2
  },
  {
    id: "blr-st-12",
    name: "HSR Layout 27th Main (Sector 6 Lowland)",
    ward: "HSR Layout (Ward 174)",
    fromIntersection: "HSR 27th Main / 19th Cross",
    toIntersection: "Agara Lake Outfall Jn",
    lengthM: 1700,
    waterDepthCm: 32.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.95,
    coordinates: [
      [12.91200, 77.64000],
      [12.91500, 77.64500],
      [12.91800, 77.65000]
    ],
    blocked: true,
    elevationM: 870.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 12.0
  },
  {
    id: "blr-st-13",
    name: "Koramangala 80 Feet Road (Sony World)",
    ward: "Koramangala (Ward 151)",
    fromIntersection: "Sony World Signal",
    toIntersection: "Koramangala BDA Complex",
    lengthM: 1600,
    waterDepthCm: 21.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.35,
    coordinates: [
      [12.93500, 77.62200],
      [12.93500, 77.62800],
      [12.93500, 77.63500]
    ],
    blocked: true,
    elevationM: 876.0,
    drainageCapacityM3s: 4.8,
    runoffInflowM3s: 9.5
  },
  {
    id: "blr-st-14",
    name: "Koramangala 100 Feet Road (Inner Ring)",
    ward: "Koramangala (Ward 151)",
    fromIntersection: "Water Tank Jn",
    toIntersection: "Domlur Flyover Ramp",
    lengthM: 2800,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [12.93000, 77.62000],
      [12.94500, 77.63200],
      [12.96000, 77.64000]
    ],
    blocked: false,
    elevationM: 885.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 6.5
  },
  {
    id: "blr-st-15",
    name: "Indiranagar 100 Feet Road",
    ward: "Indiranagar (Ward 80)",
    fromIntersection: "Old Airport Road Jn",
    toIntersection: "CMH Road Metro Jn",
    lengthM: 2200,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [12.96500, 77.64000],
      [12.97500, 77.64000],
      [12.98500, 77.64000]
    ],
    blocked: false,
    elevationM: 905.0,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 4.5
  },
  {
    id: "blr-st-16",
    name: "Old Airport Road / Wind Tunnel Road",
    ward: "HAL Airport Area",
    fromIntersection: "Manipal Hospital Signal",
    toIntersection: "HAL Main Gate",
    lengthM: 2600,
    waterDepthCm: 13.5,
    riskLevel: "caution",
    flowVelocityMs: 0.9,
    coordinates: [
      [12.96000, 77.64500],
      [12.96000, 77.66000],
      [12.96000, 77.67500]
    ],
    blocked: false,
    elevationM: 888.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 7.5
  },
  {
    id: "blr-st-17",
    name: "Whitefield Main Road / ITPL Corridor",
    ward: "Whitefield (Ward 84)",
    fromIntersection: "Hope Farm Circle",
    toIntersection: "ITPL Main Gate",
    lengthM: 2700,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [12.98500, 77.75500],
      [12.97500, 77.75000],
      [12.96500, 77.74500]
    ],
    blocked: false,
    elevationM: 895.0,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 5.5
  },
  {
    id: "blr-st-18",
    name: "Varthur Kodi Lowland Lake Basin",
    ward: "Varthur (Ward 149)",
    fromIntersection: "Varthur Lake Sluice",
    toIntersection: "Gunjur Main Road",
    lengthM: 1950,
    waterDepthCm: 41.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.25,
    coordinates: [
      [12.94500, 77.73500],
      [12.94000, 77.74000],
      [12.93500, 77.74500]
    ],
    blocked: true,
    elevationM: 855.0,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 14.2
  },
  {
    id: "blr-st-19",
    name: "Hebbal Elevated Expressway Viaduct",
    ward: "Hebbal (Ward 21)",
    fromIntersection: "Hebbal Lake Ramp",
    toIntersection: "Airport Toll Corridor",
    lengthM: 3200,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [13.03500, 77.59100],
      [13.04800, 77.59500],
      [13.06000, 77.60000]
    ],
    blocked: false,
    elevationM: 920.0,
    drainageCapacityM3s: 10.0,
    runoffInflowM3s: 1.5
  },
  {
    id: "blr-st-20",
    name: "Manyata Tech Park Outer Ring Road",
    ward: "Nagawara (Ward 23)",
    fromIntersection: "Hebbal Flyover East",
    toIntersection: "Nagawara Lake Jn",
    lengthM: 2800,
    waterDepthCm: 17.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.15,
    coordinates: [
      [13.03500, 77.59500],
      [13.04000, 77.61000],
      [13.04500, 77.62500]
    ],
    blocked: true,
    elevationM: 888.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 8.8
  },
  {
    id: "blr-st-21",
    name: "Nagawara Junction / Thanisandra Main",
    ward: "Nagawara (Ward 23)",
    fromIntersection: "Nagawara Metro Cross",
    toIntersection: "Thanisandra Railway Bridge",
    lengthM: 2100,
    waterDepthCm: 23.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.45,
    coordinates: [
      [13.04500, 77.62500],
      [13.05500, 77.63000],
      [13.06500, 77.63200]
    ],
    blocked: true,
    elevationM: 882.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 9.8
  },
  {
    id: "blr-st-22",
    name: "Hennur Main Road Link",
    ward: "Hennur (Ward 24)",
    fromIntersection: "Outer Ring Road Hennur",
    toIntersection: "Hennur Cross Bus Stop",
    lengthM: 1900,
    waterDepthCm: 9.0,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [13.02500, 77.63500],
      [13.03200, 77.64000],
      [13.04000, 77.64500]
    ],
    blocked: false,
    elevationM: 895.0,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.0
  },
  {
    id: "blr-st-23",
    name: "KR Puram Hanging Bridge & Tin Factory",
    ward: "KR Puram (Ward 52)",
    fromIntersection: "Tin Factory Bus Stop",
    toIntersection: "KR Puram Cable Bridge",
    lengthM: 1700,
    waterDepthCm: 26.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.65,
    coordinates: [
      [12.99500, 77.67500],
      [12.99800, 77.68500],
      [13.00000, 77.69500]
    ],
    blocked: true,
    elevationM: 872.0,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 11.0
  },
  {
    id: "blr-st-24",
    name: "Tumkur Road / Yeshwanthpur Flyover",
    ward: "Yeshwanthpur (Ward 37)",
    fromIntersection: "Yeshwanthpur Circle",
    toIntersection: "Goraguntepalya Jn",
    lengthM: 2400,
    waterDepthCm: 4.0,
    riskLevel: "safe",
    flowVelocityMs: 0.25,
    coordinates: [
      [13.02000, 77.54500],
      [13.02500, 77.55000],
      [13.03000, 77.55500]
    ],
    blocked: false,
    elevationM: 915.0,
    drainageCapacityM3s: 9.0,
    runoffInflowM3s: 4.0
  },
  {
    id: "blr-st-25",
    name: "Rajajinagar 1st Block Chord Road",
    ward: "Rajajinagar (Ward 98)",
    fromIntersection: "Navrang Theatre Signal",
    toIntersection: "Rajajinagar Metro Station",
    lengthM: 2200,
    waterDepthCm: 3.5,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [12.99500, 77.55000],
      [12.99000, 77.55200],
      [12.98500, 77.55500]
    ],
    blocked: false,
    elevationM: 922.0,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 3.5
  },
  {
    id: "blr-st-26",
    name: "Mysore Road / Nayandahalli Flyover",
    ward: "Nayandahalli (Ward 131)",
    fromIntersection: "PES University Gate",
    toIntersection: "Nayandahalli Metro Jn",
    lengthM: 2600,
    waterDepthCm: 18.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.2,
    coordinates: [
      [12.94500, 77.53000],
      [12.94800, 77.53500],
      [12.95200, 77.54000]
    ],
    blocked: true,
    elevationM: 880.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 8.8
  },
  {
    id: "blr-st-27",
    name: "Bannerghatta Road / Dairy Circle",
    ward: "BTM Layout (Ward 176)",
    fromIntersection: "Dairy Circle Flyover",
    toIntersection: "Jayadeva Hospital Flyover",
    lengthM: 2300,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [12.93500, 77.59800],
      [12.92500, 77.59800],
      [12.91500, 77.59800]
    ],
    blocked: false,
    elevationM: 905.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 5.8
  },
  {
    id: "blr-st-28",
    name: "JP Nagar 24th Main Commercial Ring",
    ward: "JP Nagar (Ward 177)",
    fromIntersection: "RV Dental College Jn",
    toIntersection: "Sarakki Lake Ingress",
    lengthM: 1950,
    waterDepthCm: 14.5,
    riskLevel: "caution",
    flowVelocityMs: 0.95,
    coordinates: [
      [12.90800, 77.58500],
      [12.90500, 77.58800],
      [12.90200, 77.59200]
    ],
    blocked: false,
    elevationM: 892.0,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 7.5
  },
  {
    id: "blr-st-29",
    name: "BTM Layout 2nd Stage Ring Link",
    ward: "BTM Layout (Ward 176)",
    fromIntersection: "Udupi Garden Signal",
    toIntersection: "Silk Board Flyover Ramp",
    lengthM: 1600,
    waterDepthCm: 16.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.05,
    coordinates: [
      [12.91500, 77.61000],
      [12.91600, 77.61600],
      [12.91700, 77.62200]
    ],
    blocked: true,
    elevationM: 882.0,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 8.2
  },
  {
    id: "blr-st-30",
    name: "Majestic K.G. Road Commercial Corridor",
    ward: "Gandhinagar (Ward 94)",
    fromIntersection: "Mysore Bank Circle",
    toIntersection: "Upparpet Police Station",
    lengthM: 1300,
    waterDepthCm: 5.5,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [12.97400, 77.58000],
      [12.97600, 77.58200],
      [12.97800, 77.58500]
    ],
    blocked: false,
    elevationM: 915.0,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 4.5
  }
];

// Dense City-Wide Street Network for Kolkata (30 Segments)
export const KOLKATA_STREETS: StreetSegment[] = [
  {
    id: "kol-st-01",
    name: "CR Avenue (Central Avenue Lowland Basin)",
    ward: "Bowbazar (Ward 44)",
    fromIntersection: "Girish Park",
    toIntersection: "Esplanade Metro Crossing",
    lengthM: 2400,
    waterDepthCm: 36.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.05,
    coordinates: [
      [22.59500, 88.36200],
      [22.58000, 88.36000],
      [22.56500, 88.35500]
    ],
    blocked: true,
    elevationM: 4.2,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 13.5
  },
  {
    id: "kol-st-02",
    name: "Park Street / Camac Street Corridor",
    ward: "Park Street (Ward 63)",
    fromIntersection: "Chowringhee Crossing",
    toIntersection: "Mullick Bazar Jn",
    lengthM: 1800,
    waterDepthCm: 8.5,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [22.55200, 88.35000],
      [22.55200, 88.35500],
      [22.55200, 88.36500]
    ],
    blocked: false,
    elevationM: 6.8,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.0
  },
  {
    id: "kol-st-03",
    name: "Jawaharlal Nehru Road (Chowringhee)",
    ward: "New Market (Ward 46)",
    fromIntersection: "Esplanade Dharmatala",
    toIntersection: "Exide Crossing",
    lengthM: 2100,
    waterDepthCm: 6.0,
    riskLevel: "caution",
    flowVelocityMs: 0.4,
    coordinates: [
      [22.56500, 88.35200],
      [22.55500, 88.35000],
      [22.54000, 88.34800]
    ],
    blocked: false,
    elevationM: 7.2,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 5.2
  },
  {
    id: "kol-st-04",
    name: "BBD Bagh / Dalhousie Heritage Square",
    ward: "BBD Bagh (Ward 45)",
    fromIntersection: "Writers Building",
    toIntersection: "GPO Circle",
    lengthM: 1300,
    waterDepthCm: 11.5,
    riskLevel: "caution",
    flowVelocityMs: 0.75,
    coordinates: [
      [22.57200, 88.34500],
      [22.57000, 88.34800],
      [22.56800, 88.35000]
    ],
    blocked: false,
    elevationM: 5.8,
    drainageCapacityM3s: 5.8,
    runoffInflowM3s: 6.8
  },
  {
    id: "kol-st-05",
    name: "Strand Road / Hooghly Riverfront",
    ward: "Riverfront Corridor",
    fromIntersection: "Howrah Bridge Approach",
    toIntersection: "Babu Ghat",
    lengthM: 2200,
    waterDepthCm: 19.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.25,
    coordinates: [
      [22.58500, 88.34200],
      [22.57500, 88.34000],
      [22.56500, 88.33800]
    ],
    blocked: true,
    elevationM: 4.0,
    drainageCapacityM3s: 5.0,
    runoffInflowM3s: 9.5
  },
  {
    id: "kol-st-06",
    name: "MG Road Burrabazar Low Point",
    ward: "Burrabazar (Ward 42)",
    fromIntersection: "Howrah Bridge Approach",
    toIntersection: "Sealdah Flyover Link",
    lengthM: 2300,
    waterDepthCm: 31.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.85,
    coordinates: [
      [22.58500, 88.34500],
      [22.58500, 88.35500],
      [22.58500, 88.36800]
    ],
    blocked: true,
    elevationM: 4.5,
    drainageCapacityM3s: 4.2,
    runoffInflowM3s: 12.0
  },
  {
    id: "kol-st-07",
    name: "Sealdah Station Flyover Approach",
    ward: "Sealdah (Ward 49)",
    fromIntersection: "Sealdah Main Gate",
    toIntersection: "Koley Market Low Point",
    lengthM: 1400,
    waterDepthCm: 24.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.55,
    coordinates: [
      [22.56800, 88.37200],
      [22.56600, 88.37400],
      [22.56400, 88.37600]
    ],
    blocked: true,
    elevationM: 4.8,
    drainageCapacityM3s: 4.5,
    runoffInflowM3s: 10.5
  },
  {
    id: "kol-st-08",
    name: "Vidyasagar Setu Toll Plaza Approach",
    ward: "Hastings (Ward 75)",
    fromIntersection: "AJC Bose Flyover Ingress",
    toIntersection: "Toll Plaza Ramp",
    lengthM: 2600,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [22.55500, 88.34500],
      [22.55500, 88.33500],
      [22.55500, 88.32500]
    ],
    blocked: false,
    elevationM: 22.0,
    drainageCapacityM3s: 14.0,
    runoffInflowM3s: 0.8
  },
  {
    id: "kol-st-09",
    name: "Maa Flyover High Viaduct",
    ward: "Central Kolkata Corridor",
    fromIntersection: "Science City Ramp",
    toIntersection: "Park Circus Flyover Link",
    lengthM: 4200,
    waterDepthCm: 0.0,
    riskLevel: "safe",
    flowVelocityMs: 0.0,
    coordinates: [
      [22.54000, 88.39800],
      [22.54100, 88.38500],
      [22.54200, 88.37000]
    ],
    blocked: false,
    elevationM: 19.5,
    drainageCapacityM3s: 12.0,
    runoffInflowM3s: 0.8
  },
  {
    id: "kol-st-10",
    name: "Park Circus 7-Point Crossing",
    ward: "Ballygunge (Ward 64)",
    fromIntersection: "AJC Bose Flyover Ramp",
    toIntersection: "Suhrwardy Avenue",
    lengthM: 1500,
    waterDepthCm: 14.0,
    riskLevel: "caution",
    flowVelocityMs: 0.7,
    coordinates: [
      [22.54200, 88.36800],
      [22.54400, 88.37200],
      [22.54600, 88.37600]
    ],
    blocked: false,
    elevationM: 6.2,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 7.2
  },
  {
    id: "kol-st-11",
    name: "EM Bypass Science City Interchange",
    ward: "Topsia (Ward 58)",
    fromIntersection: "Maa Flyover Ramp",
    toIntersection: "Ruby Hospital Link",
    lengthM: 2800,
    waterDepthCm: 5.5,
    riskLevel: "caution",
    flowVelocityMs: 0.35,
    coordinates: [
      [22.54000, 88.39800],
      [22.53000, 88.40000],
      [22.51800, 88.40200]
    ],
    blocked: false,
    elevationM: 7.5,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 5.0
  },
  {
    id: "kol-st-12",
    name: "EM Bypass Ruby Hospital Rotary",
    ward: "Kasba (Ward 107)",
    fromIntersection: "Kasba Connector Jn",
    toIntersection: "Kalikapur Bridge",
    lengthM: 2200,
    waterDepthCm: 12.5,
    riskLevel: "caution",
    flowVelocityMs: 0.8,
    coordinates: [
      [22.51800, 88.40200],
      [22.51000, 88.40300],
      [22.50200, 88.40500]
    ],
    blocked: false,
    elevationM: 6.5,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 7.5
  },
  {
    id: "kol-st-13",
    name: "EM Bypass Chingrighata Flyover & Lowland",
    ward: "Beliaghata (Ward 57)",
    fromIntersection: "Salt Lake Sector V Link",
    toIntersection: "Science City Link",
    lengthM: 2100,
    waterDepthCm: 22.0,
    riskLevel: "impassable",
    flowVelocityMs: 1.4,
    coordinates: [
      [22.56500, 88.40200],
      [22.55200, 88.40000],
      [22.54000, 88.39800]
    ],
    blocked: true,
    elevationM: 5.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 9.8
  },
  {
    id: "kol-st-14",
    name: "Ballygunge Circular Road",
    ward: "Ballygunge (Ward 69)",
    fromIntersection: "Minto Park",
    toIntersection: "Gariahat Jn",
    lengthM: 2300,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [22.53800, 88.36000],
      [22.53000, 88.36500],
      [22.52200, 88.36800]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 4.2
  },
  {
    id: "kol-st-15",
    name: "Gariahat Junction Commercial Hub",
    ward: "Ballygunge (Ward 68)",
    fromIntersection: "Gariahat Flyover",
    toIntersection: "Golpark Circle",
    lengthM: 1600,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [22.52200, 88.36800],
      [22.51800, 88.36800],
      [22.51200, 88.36800]
    ],
    blocked: false,
    elevationM: 7.8,
    drainageCapacityM3s: 6.8,
    runoffInflowM3s: 5.8
  },
  {
    id: "kol-st-16",
    name: "Rashbehari Avenue / Kalighat Link",
    ward: "Kalighat (Ward 83)",
    fromIntersection: "Gariahat Flyover",
    toIntersection: "Chetla Bridge Ingress",
    lengthM: 2600,
    waterDepthCm: 16.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.1,
    coordinates: [
      [22.51800, 88.36800],
      [22.51800, 88.35500],
      [22.51800, 88.34200]
    ],
    blocked: true,
    elevationM: 5.5,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 8.5
  },
  {
    id: "kol-st-17",
    name: "Southern Avenue / Rabindra Sarobar",
    ward: "Dhakuria (Ward 90)",
    fromIntersection: "Golpark Circle",
    toIntersection: "Southern Avenue Lake Link",
    lengthM: 1900,
    waterDepthCm: 8.0,
    riskLevel: "caution",
    flowVelocityMs: 0.55,
    coordinates: [
      [22.51200, 88.36800],
      [22.51000, 88.36000],
      [22.50800, 88.35200]
    ],
    blocked: false,
    elevationM: 6.5,
    drainageCapacityM3s: 6.5,
    runoffInflowM3s: 6.2
  },
  {
    id: "kol-st-18",
    name: "Tollygunge Phari Lowland Basin",
    ward: "Tollygunge (Ward 88)",
    fromIntersection: "Charu Market",
    toIntersection: "Tollygunge Tram Depot",
    lengthM: 1800,
    waterDepthCm: 33.5,
    riskLevel: "impassable",
    flowVelocityMs: 2.1,
    coordinates: [
      [22.50800, 88.34500],
      [22.50000, 88.34500],
      [22.49200, 88.34500]
    ],
    blocked: true,
    elevationM: 3.8,
    drainageCapacityM3s: 3.5,
    runoffInflowM3s: 13.0
  },
  {
    id: "kol-st-19",
    name: "Prince Anwar Shah Road",
    ward: "Jadavpur (Ward 93)",
    fromIntersection: "Lords Bakery Jn",
    toIntersection: "South City Mall Ingress",
    lengthM: 2100,
    waterDepthCm: 11.0,
    riskLevel: "caution",
    flowVelocityMs: 0.75,
    coordinates: [
      [22.50000, 88.35500],
      [22.50000, 88.36200],
      [22.50000, 88.37000]
    ],
    blocked: false,
    elevationM: 7.0,
    drainageCapacityM3s: 6.0,
    runoffInflowM3s: 7.0
  },
  {
    id: "kol-st-20",
    name: "Taratala Diamond Harbour Highway",
    ward: "Behala (Ward 118)",
    fromIntersection: "Majerhat Bridge",
    toIntersection: "Taratala Flyover Jn",
    lengthM: 2400,
    waterDepthCm: 19.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.3,
    coordinates: [
      [22.51500, 88.32000],
      [22.50800, 88.31500],
      [22.50000, 88.31000]
    ],
    blocked: true,
    elevationM: 5.2,
    drainageCapacityM3s: 5.2,
    runoffInflowM3s: 9.2
  },
  {
    id: "kol-st-21",
    name: "Ultadanga Underpass (E.M. Bypass Ingress)",
    ward: "Ultadanga (Ward 14)",
    fromIntersection: "Hudco More",
    toIntersection: "VIP Road Flyover",
    lengthM: 1100,
    waterDepthCm: 41.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.9,
    coordinates: [
      [22.59500, 88.38800],
      [22.59800, 88.39300],
      [22.60100, 88.39800]
    ],
    blocked: true,
    elevationM: 4.8,
    drainageCapacityM3s: 3.8,
    runoffInflowM3s: 11.5
  },
  {
    id: "kol-st-22",
    name: "Shyambazar 5-Point Crossing",
    ward: "Shyambazar (Ward 10)",
    fromIntersection: "Netaji Statue Circle",
    toIntersection: "RG Kar Medical College Cross",
    lengthM: 1500,
    waterDepthCm: 13.5,
    riskLevel: "caution",
    flowVelocityMs: 0.85,
    coordinates: [
      [22.60200, 88.37000],
      [22.60200, 88.37500],
      [22.60200, 88.38000]
    ],
    blocked: false,
    elevationM: 6.5,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 7.5
  },
  {
    id: "kol-st-23",
    name: "VIP Road (Kankurgachi - Lake Town)",
    ward: "Lake Town (Ward 29)",
    fromIntersection: "Ultadanga Flyover",
    toIntersection: "Lake Town Clock Tower",
    lengthM: 2800,
    waterDepthCm: 7.5,
    riskLevel: "caution",
    flowVelocityMs: 0.5,
    coordinates: [
      [22.60100, 88.39800],
      [22.60800, 88.40800],
      [22.61500, 88.41800]
    ],
    blocked: false,
    elevationM: 7.2,
    drainageCapacityM3s: 8.0,
    runoffInflowM3s: 6.0
  },
  {
    id: "kol-st-24",
    name: "VIP Road (Baguiati Underpass Low Point)",
    ward: "Baguiati (Ward 18)",
    fromIntersection: "Baguiati Subway Ramp",
    toIntersection: "Joramandir Crossing",
    lengthM: 1600,
    waterDepthCm: 38.0,
    riskLevel: "impassable",
    flowVelocityMs: 2.25,
    coordinates: [
      [22.61800, 88.42200],
      [22.62200, 88.42800],
      [22.62600, 88.43400]
    ],
    blocked: true,
    elevationM: 4.0,
    drainageCapacityM3s: 4.0,
    runoffInflowM3s: 12.8
  },
  {
    id: "kol-st-25",
    name: "VIP Road (Airport Gate 1 No)",
    ward: "Dum Dum (Airport Zone)",
    fromIntersection: "Kaikhali Signal",
    toIntersection: "NSCB International Airport Hub",
    lengthM: 3100,
    waterDepthCm: 4.5,
    riskLevel: "safe",
    flowVelocityMs: 0.3,
    coordinates: [
      [22.63500, 88.44000],
      [22.64500, 88.44500],
      [22.65500, 88.44800]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 9.5,
    runoffInflowM3s: 4.8
  },
  {
    id: "kol-st-26",
    name: "Salt Lake Sector V (Webel / College More)",
    ward: "Bidhannagar (Sector V)",
    fromIntersection: "College More Jn",
    toIntersection: "Godrej Waterside Tower",
    lengthM: 2200,
    waterDepthCm: 9.0,
    riskLevel: "caution",
    flowVelocityMs: 0.6,
    coordinates: [
      [22.57200, 88.43000],
      [22.57200, 88.43500],
      [22.57200, 88.44000]
    ],
    blocked: false,
    elevationM: 6.2,
    drainageCapacityM3s: 7.5,
    runoffInflowM3s: 6.5
  },
  {
    id: "kol-st-27",
    name: "Salt Lake Karunamoyee Central Bus Hub",
    ward: "Bidhannagar (Central)",
    fromIntersection: "Central Park Gate",
    toIntersection: "Karunamoyee Metro Station",
    lengthM: 1700,
    waterDepthCm: 6.5,
    riskLevel: "caution",
    flowVelocityMs: 0.45,
    coordinates: [
      [22.58800, 88.41200],
      [22.58500, 88.41500],
      [22.58200, 88.41800]
    ],
    blocked: false,
    elevationM: 7.5,
    drainageCapacityM3s: 7.0,
    runoffInflowM3s: 5.5
  },
  {
    id: "kol-st-28",
    name: "Salt Lake Broadway Arterial Road",
    ward: "Bidhannagar (West)",
    fromIntersection: "Ultadanga Flyover East",
    toIntersection: "Salt Lake Stadium Gate",
    lengthM: 2400,
    waterDepthCm: 3.5,
    riskLevel: "safe",
    flowVelocityMs: 0.2,
    coordinates: [
      [22.59500, 88.40000],
      [22.58500, 88.40300],
      [22.57500, 88.40500]
    ],
    blocked: false,
    elevationM: 8.5,
    drainageCapacityM3s: 8.5,
    runoffInflowM3s: 3.8
  },
  {
    id: "kol-st-29",
    name: "New Town Major Arterial Road (MAR-1)",
    ward: "New Town (Action Area 1)",
    fromIntersection: "New Town Box Bridge",
    toIntersection: "Biswa Bangla Gate Rotary",
    lengthM: 3600,
    waterDepthCm: 2.5,
    riskLevel: "safe",
    flowVelocityMs: 0.15,
    coordinates: [
      [22.58500, 88.45000],
      [22.58800, 88.46000],
      [22.59200, 88.47000]
    ],
    blocked: false,
    elevationM: 9.0,
    drainageCapacityM3s: 11.0,
    runoffInflowM3s: 3.2
  },
  {
    id: "kol-st-30",
    name: "Chinar Park / Rajarhat Main Corridor",
    ward: "Rajarhat (Ward 12)",
    fromIntersection: "Chinar Park Crossing",
    toIntersection: "City Centre 2 Ingress",
    lengthM: 2300,
    waterDepthCm: 18.5,
    riskLevel: "impassable",
    flowVelocityMs: 1.2,
    coordinates: [
      [22.62500, 88.44500],
      [22.62800, 88.45200],
      [22.63200, 88.46000]
    ],
    blocked: true,
    elevationM: 5.5,
    drainageCapacityM3s: 5.5,
    runoffInflowM3s: 8.8
  }
];

export const DRAINAGE_NODES_HYD: DrainageNode[] = [
  {
    id: 'node-hyd-01',
    name: 'Hussain Sagar Sluice Gate Outfall',
    type: 'outfall',
    coordinates: [17.422, 78.472],
    rimElevationM: 513.5,
    invertElevationM: 508.2,
    surchargeDepthCm: 18.5,
    isFlooded: true,
    siltationIndex: 0.65,
    healthStatus: 'critical_blockage'
  },
  {
    id: 'node-hyd-02',
    name: 'Begumpet Nallah Inlet Box',
    type: 'inlet',
    coordinates: [17.441, 78.475],
    rimElevationM: 511.0,
    invertElevationM: 507.0,
    surchargeDepthCm: 24.2,
    isFlooded: true,
    siltationIndex: 0.72,
    healthStatus: 'critical_blockage'
  },
  {
    id: 'node-hyd-03',
    name: 'Khairatabad Junction Storm Manhole',
    type: 'manhole',
    coordinates: [17.408, 78.464],
    rimElevationM: 506.2,
    invertElevationM: 502.8,
    surchargeDepthCm: 32.0,
    isFlooded: true,
    siltationIndex: 0.58,
    healthStatus: 'critical_blockage'
  },
  {
    id: 'node-hyd-04',
    name: 'Banjara Hills Ridge Retention Pit',
    type: 'storage_basin',
    coordinates: [17.420, 78.441],
    rimElevationM: 546.0,
    invertElevationM: 541.5,
    surchargeDepthCm: 0.0,
    isFlooded: false,
    siltationIndex: 0.15,
    healthStatus: 'healthy'
  },
  {
    id: 'node-hyd-05',
    name: 'Somajiguda Trunk Manhole A-14',
    type: 'manhole',
    coordinates: [17.426, 78.458],
    rimElevationM: 523.0,
    invertElevationM: 519.2,
    surchargeDepthCm: 6.4,
    isFlooded: false,
    siltationIndex: 0.38,
    healthStatus: 'warning'
  }
];

export const DRAINAGE_CONDUITS_HYD: DrainageConduit[] = [
  {
    id: 'cond-hyd-01',
    fromNode: 'node-hyd-02',
    toNode: 'node-hyd-01',
    lengthM: 2400,
    diameterM: 2.2,
    slope: 0.0018,
    maxCapacityM3s: 6.5,
    currentFlowM3s: 9.8,
    utilizationPercent: 150.7,
    siltationFactor: 0.72,
    status: 'overflowing',
    coordinates: [
      [17.441, 78.475],
      [17.432, 78.473],
      [17.422, 78.472]
    ]
  },
  {
    id: 'cond-hyd-02',
    fromNode: 'node-hyd-03',
    toNode: 'node-hyd-01',
    lengthM: 1800,
    diameterM: 1.8,
    slope: 0.0022,
    maxCapacityM3s: 4.8,
    currentFlowM3s: 7.2,
    utilizationPercent: 150.0,
    siltationFactor: 0.58,
    status: 'overflowing',
    coordinates: [
      [17.408, 78.464],
      [17.415, 78.468],
      [17.422, 78.472]
    ]
  },
  {
    id: 'cond-hyd-03',
    fromNode: 'node-hyd-04',
    toNode: 'node-hyd-05',
    lengthM: 1600,
    diameterM: 1.5,
    slope: 0.012,
    maxCapacityM3s: 7.5,
    currentFlowM3s: 3.2,
    utilizationPercent: 42.6,
    siltationFactor: 0.15,
    status: 'optimal',
    coordinates: [
      [17.420, 78.441],
      [17.423, 78.449],
      [17.426, 78.458]
    ]
  },
  {
    id: 'cond-hyd-04',
    fromNode: 'node-hyd-05',
    toNode: 'node-hyd-01',
    lengthM: 1400,
    diameterM: 1.8,
    slope: 0.0045,
    maxCapacityM3s: 6.2,
    currentFlowM3s: 5.5,
    utilizationPercent: 88.7,
    siltationFactor: 0.38,
    status: 'congested',
    coordinates: [
      [17.426, 78.458],
      [17.424, 78.465],
      [17.422, 78.472]
    ]
  }
];

export const HISTORICAL_SCENARIOS: HistoricalStormScenario[] = [
  {
    id: 'scenario-hyd-2020',
    cityName: 'Hyderabad',
    eventTitle: 'October 2020 Severe Cloudburst & Lake Breach',
    date: '13-14 October 2020',
    peakRainfallMmHr: 114.5,
    totalRainfallMm: 324.0,
    description: 'Catastrophic deep depression over Telangana leading to historical 24-hr rainfall records, Musi river overflow, and city-wide arterial subway inundation.',
    frames: [
      {
        timeOffsetMin: -60,
        displayTime: '17:00 IST (Storm Inflow Initiation)',
        rainfallIntensityMmHr: 18.2,
        radarReflectivityDbz: 32,
        inundatedStreetsCount: 3,
        maxDepthCm: 4.5,
        streetsData: {
          'hyd-st-01': 3.2,
          'hyd-st-02': 4.5,
          'hyd-st-03': 6.0,
          'hyd-st-04': 0.0,
          'hyd-st-05': 1.5,
          'hyd-st-06': 0.5,
          'hyd-st-07': 4.0,
          'hyd-st-08': 3.0,
          'hyd-st-09': 0.0
        }
      },
      {
        timeOffsetMin: 0,
        displayTime: '18:00 IST (Peak Storm Intensity - 114 mm/hr)',
        rainfallIntensityMmHr: 114.5,
        radarReflectivityDbz: 58,
        inundatedStreetsCount: 18,
        maxDepthCm: 38.2,
        streetsData: {
          'hyd-st-01': 22.4,
          'hyd-st-02': 18.6,
          'hyd-st-03': 34.2,
          'hyd-st-04': 2.1,
          'hyd-st-05': 8.4,
          'hyd-st-06': 4.2,
          'hyd-st-07': 28.5,
          'hyd-st-08': 16.2,
          'hyd-st-09': 3.0,
          'hyd-st-20': 26.0,
          'hyd-st-21': 31.0,
          'hyd-st-33': 38.0,
          'hyd-st-34': 29.5,
          'hyd-st-35': 33.5
        }
      },
      {
        timeOffsetMin: 60,
        displayTime: '19:00 IST (Conduit Surcharge & Max Ponding)',
        rainfallIntensityMmHr: 62.0,
        radarReflectivityDbz: 48,
        inundatedStreetsCount: 24,
        maxDepthCm: 48.6,
        streetsData: {
          'hyd-st-01': 38.0,
          'hyd-st-02': 31.5,
          'hyd-st-03': 48.6,
          'hyd-st-04': 3.0,
          'hyd-st-05': 14.2,
          'hyd-st-06': 6.8,
          'hyd-st-07': 42.0,
          'hyd-st-08': 24.5,
          'hyd-st-09': 4.0,
          'hyd-st-20': 35.0,
          'hyd-st-21': 42.0,
          'hyd-st-33': 48.0,
          'hyd-st-34': 39.5,
          'hyd-st-35': 44.0
        }
      },
      {
        timeOffsetMin: 120,
        displayTime: '20:00 IST (Receding Storm - Finite Drainage-Down)',
        rainfallIntensityMmHr: 12.0,
        radarReflectivityDbz: 26,
        inundatedStreetsCount: 8,
        maxDepthCm: 26.0,
        streetsData: {
          'hyd-st-01': 19.5,
          'hyd-st-02': 14.0,
          'hyd-st-03': 26.0,
          'hyd-st-04': 0.0,
          'hyd-st-05': 4.5,
          'hyd-st-06': 1.0,
          'hyd-st-07': 22.0,
          'hyd-st-08': 11.0,
          'hyd-st-09': 0.0
        }
      }
    ]
  },
  {
    id: 'scenario-mum-2005',
    cityName: 'Mumbai',
    eventTitle: 'July 26 Historic Mega-Flood (944mm Cloudburst)',
    date: '26 July 2005',
    peakRainfallMmHr: 142.0,
    totalRainfallMm: 944.2,
    description: 'Extremely severe convective cloudburst coupled with astronomical high tide, shutting down subways, local rail network, and Mithi river drainage.',
    frames: [
      {
        timeOffsetMin: 0,
        displayTime: '14:30 IST (Tidal Surcharge + Cloudburst Peak)',
        rainfallIntensityMmHr: 142.0,
        radarReflectivityDbz: 62,
        inundatedStreetsCount: 15,
        maxDepthCm: 68.0,
        streetsData: {
          'mum-st-06': 28.0,
          'mum-st-09': 68.0,
          'mum-st-10': 45.0,
          'mum-st-11': 64.0,
          'mum-st-13': 48.0,
          'mum-st-17': 68.0,
          'mum-st-18': 58.0,
          'mum-st-19': 72.0,
          'mum-st-27': 54.5
        }
      },
      {
        timeOffsetMin: 60,
        displayTime: '15:30 IST (Subway Full Submersion)',
        rainfallIntensityMmHr: 98.0,
        radarReflectivityDbz: 55,
        inundatedStreetsCount: 18,
        maxDepthCm: 85.0,
        streetsData: {
          'mum-st-06': 35.0,
          'mum-st-09': 85.0,
          'mum-st-10': 55.0,
          'mum-st-11': 78.0,
          'mum-st-13': 58.0,
          'mum-st-17': 85.0,
          'mum-st-18': 72.0,
          'mum-st-19': 92.0,
          'mum-st-27': 64.0
        }
      }
    ]
  }
];

export const INITIAL_ALERTS: AlertNotification[] = [
  {
    id: 'alt-001',
    timestamp: 'Just now',
    title: 'IMPASSABLE BARRIER: Khairatabad Subway',
    message: 'Water depth reached 34.2 cm (> 15cm threshold). Road marked closed to vehicular traffic. Emergency diversion active.',
    riskLevel: 'impassable',
    locationName: 'Khairatabad Anand Nagar Subway',
    waterDepthCm: 34.2,
    coordinates: [17.408, 78.464]
  },
  {
    id: 'alt-002',
    timestamp: '2 mins ago',
    title: 'CRITICAL INUNDATION: Necklace Road',
    message: 'Water depth surged to 28.5 cm due to Hussain Sagar shoreline runoff surcharge. Avoid corridor.',
    riskLevel: 'impassable',
    locationName: 'Necklace Road (PV Ghat Shoreline)',
    waterDepthCm: 28.5,
    coordinates: [17.425, 78.463]
  },
  {
    id: 'alt-003',
    timestamp: '5 mins ago',
    title: 'CAUTION ADVISORY: Somajiguda Raj Bhavan Rd',
    message: 'Ponding detected at 8.4 cm. Traffic velocity reduced to 15 km/h. Quadratic routing penalty applied.',
    riskLevel: 'caution',
    locationName: 'Somajiguda Raj Bhavan Road',
    waterDepthCm: 8.4,
    coordinates: [17.426, 78.458]
  }
];

export function getCityStreets(cityId: string): StreetSegment[] {
  switch (cityId.toLowerCase()) {
    case 'mumbai':
      return MUMBAI_STREETS;
    case 'chennai':
      return CHENNAI_STREETS;
    case 'bengaluru':
      return BENGALURU_STREETS;
    case 'delhi':
      return DELHI_STREETS;
    case 'kolkata':
      return KOLKATA_STREETS;
    default:
      return HYDERABAD_STREETS;
  }
}
