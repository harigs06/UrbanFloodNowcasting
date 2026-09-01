"""Dense City Streets Network Database for Multi-City Navigation & Hydraulic Mapping."""

from typing import Dict, List, Tuple, Any

CITY_ROUTING_NETWORKS: Dict[str, Tuple[List[Dict[str, Any]], Dict[str, Tuple[float, float]]]] = {
  "hyderabad": [
    [
      {
        "id": "hyd-st-01",
        "name": "Tank Bund Road (Hussain Sagar East)",
        "from_intersection_id": "int-sailing-club-jn",
        "to_intersection_id": "int-secretariat-circle",
        "length_m": 2100.0,
        "water_depth_cm": 22.4,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.478,
            17.432
          ],
          [
            78.476,
            17.426
          ],
          [
            78.474,
            17.418
          ],
          [
            78.471,
            17.412
          ]
        ]
      },
      {
        "id": "hyd-st-02",
        "name": "Begumpet Airport Nallah Corridor",
        "from_intersection_id": "int-prakash-nagar-metro",
        "to_intersection_id": "int-rasoolpura-flyover",
        "length_m": 1750.0,
        "water_depth_cm": 18.6,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.468,
            17.443
          ],
          [
            78.475,
            17.441
          ],
          [
            78.483,
            17.438
          ]
        ]
      },
      {
        "id": "hyd-st-03",
        "name": "Khairatabad Anand Nagar Subway",
        "from_intersection_id": "int-khairatabad-rly-bridge",
        "to_intersection_id": "int-lakdikapul-jn",
        "length_m": 980.0,
        "water_depth_cm": 34.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.462,
            17.411
          ],
          [
            78.464,
            17.408
          ],
          [
            78.466,
            17.404
          ]
        ]
      },
      {
        "id": "hyd-st-04",
        "name": "Banjara Hills Road No. 12 (Elevated Ridge)",
        "from_intersection_id": "int-cancer-hospital-jn",
        "to_intersection_id": "int-mla-colony-gate",
        "length_m": 1600.0,
        "water_depth_cm": 2.1,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.435,
            17.415
          ],
          [
            78.441,
            17.42
          ],
          [
            78.448,
            17.425
          ]
        ]
      },
      {
        "id": "hyd-st-05",
        "name": "Somajiguda Raj Bhavan Road",
        "from_intersection_id": "int-erramanzil-colony",
        "to_intersection_id": "int-raj-bhavan-quarters",
        "length_m": 1250.0,
        "water_depth_cm": 8.4,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.452,
            17.421
          ],
          [
            78.456,
            17.424
          ],
          [
            78.458,
            17.426
          ]
        ]
      },
      {
        "id": "hyd-st-06",
        "name": "Panjagutta Main Flyover (High Clearance)",
        "from_intersection_id": "int-nagarjuna-circle",
        "to_intersection_id": "int-ameerpet-metro",
        "length_m": 1400.0,
        "water_depth_cm": 4.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.448,
            17.425
          ],
          [
            78.451,
            17.429
          ],
          [
            78.455,
            17.435
          ]
        ]
      },
      {
        "id": "hyd-st-07",
        "name": "Necklace Road (PV Ghat Shoreline)",
        "from_intersection_id": "int-sanjeevaiah-park-gate",
        "to_intersection_id": "int-peoples-plaza-ingress",
        "length_m": 1850.0,
        "water_depth_cm": 28.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.468,
            17.435
          ],
          [
            78.465,
            17.43
          ],
          [
            78.463,
            17.425
          ],
          [
            78.465,
            17.418
          ]
        ]
      },
      {
        "id": "hyd-st-08",
        "name": "Lower Tank Bund Road (Kavadiguda Channel)",
        "from_intersection_id": "int-bible-house-jn",
        "to_intersection_id": "int-indira-park-gate",
        "length_m": 1650.0,
        "water_depth_cm": 16.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.482,
            17.425
          ],
          [
            78.481,
            17.42
          ],
          [
            78.48,
            17.415
          ],
          [
            78.479,
            17.41
          ]
        ]
      },
      {
        "id": "hyd-st-09",
        "name": "Basheerbagh - Liberty Circle Arterial",
        "from_intersection_id": "int-liberty-circle",
        "to_intersection_id": "int-basheerbagh-flyover",
        "length_m": 1100.0,
        "water_depth_cm": 3.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.475,
            17.402
          ],
          [
            78.478,
            17.405
          ],
          [
            78.482,
            17.408
          ]
        ]
      },
      {
        "id": "hyd-st-10",
        "name": "Himayatnagar Main Road",
        "from_intersection_id": "int-himayatnagar-y-jn",
        "to_intersection_id": "int-narayanaguda-flyover",
        "length_m": 1300.0,
        "water_depth_cm": 6.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.485,
            17.405
          ],
          [
            78.49,
            17.402
          ],
          [
            78.494,
            17.398
          ]
        ]
      },
      {
        "id": "hyd-st-11",
        "name": "RTC X Roads - Chikkadpally Corridor",
        "from_intersection_id": "int-rtc-x-roads",
        "to_intersection_id": "int-narayanaguda-jn",
        "length_m": 1450.0,
        "water_depth_cm": 11.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.495,
            17.408
          ],
          [
            78.496,
            17.403
          ],
          [
            78.494,
            17.398
          ]
        ]
      },
      {
        "id": "hyd-st-12",
        "name": "Musheerabad - Kavadiguda Link",
        "from_intersection_id": "int-musheerabad-jn",
        "to_intersection_id": "int-kavadiguda-cross-roads",
        "length_m": 1200.0,
        "water_depth_cm": 13.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.5,
            17.42
          ],
          [
            78.492,
            17.416
          ],
          [
            78.485,
            17.412
          ]
        ]
      },
      {
        "id": "hyd-st-13",
        "name": "MG Road Secunderabad (Central Commercial)",
        "from_intersection_id": "int-paradise-circle",
        "to_intersection_id": "int-secunderabad-station",
        "length_m": 1600.0,
        "water_depth_cm": 7.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.487,
            17.442
          ],
          [
            78.498,
            17.44
          ],
          [
            78.504,
            17.437
          ]
        ]
      },
      {
        "id": "hyd-st-14",
        "name": "SP Road / Parade Ground Link",
        "from_intersection_id": "int-rasoolpura-jn",
        "to_intersection_id": "int-sangeet-cinema-jn",
        "length_m": 1900.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.475,
            17.441
          ],
          [
            78.485,
            17.44
          ],
          [
            78.502,
            17.442
          ]
        ]
      },
      {
        "id": "hyd-st-15",
        "name": "Bowenpally National Highway NH-44",
        "from_intersection_id": "int-tadbund-cross-roads",
        "to_intersection_id": "int-bowenpally-checkpost",
        "length_m": 2200.0,
        "water_depth_cm": 5.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.488,
            17.458
          ],
          [
            78.486,
            17.465
          ],
          [
            78.484,
            17.472
          ]
        ]
      },
      {
        "id": "hyd-st-16",
        "name": "Trimulgherry - Alwal Corridor",
        "from_intersection_id": "int-trimulgherry-cross-roads",
        "to_intersection_id": "int-lothkunta-jn",
        "length_m": 2400.0,
        "water_depth_cm": 9.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.51,
            17.475
          ],
          [
            78.512,
            17.488
          ],
          [
            78.515,
            17.502
          ]
        ]
      },
      {
        "id": "hyd-st-17",
        "name": "Malkajgiri Railway Overbridge Approach",
        "from_intersection_id": "int-malkajgiri-jn",
        "to_intersection_id": "int-anandbagh-cross-roads",
        "length_m": 1700.0,
        "water_depth_cm": 14.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.525,
            17.448
          ],
          [
            78.53,
            17.452
          ],
          [
            78.538,
            17.458
          ]
        ]
      },
      {
        "id": "hyd-st-18",
        "name": "Tarnaka Flyover & University Link",
        "from_intersection_id": "int-sangeet-jn",
        "to_intersection_id": "int-tarnaka-cross-roads",
        "length_m": 2100.0,
        "water_depth_cm": 2.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.515,
            17.438
          ],
          [
            78.525,
            17.432
          ],
          [
            78.532,
            17.428
          ]
        ]
      },
      {
        "id": "hyd-st-19",
        "name": "Habsiguda - Uppal Ring Road Corridor",
        "from_intersection_id": "int-tarnaka-cross-roads",
        "to_intersection_id": "int-uppal-ring-road-jn",
        "length_m": 2800.0,
        "water_depth_cm": 8.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.532,
            17.428
          ],
          [
            78.545,
            17.415
          ],
          [
            78.56,
            17.4
          ]
        ]
      },
      {
        "id": "hyd-st-20",
        "name": "Ramanthapur Lake Road Corridor",
        "from_intersection_id": "int-uppal-ring-road-jn",
        "to_intersection_id": "int-amberpet-causeway",
        "length_m": 2300.0,
        "water_depth_cm": 26.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.56,
            17.4
          ],
          [
            78.535,
            17.395
          ],
          [
            78.515,
            17.388
          ]
        ]
      },
      {
        "id": "hyd-st-21",
        "name": "Amberpet Causeway & Nallah Crossing",
        "from_intersection_id": "int-amberpet-bridge",
        "to_intersection_id": "int-nimboliadda-jn",
        "length_m": 1500.0,
        "water_depth_cm": 31.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.515,
            17.388
          ],
          [
            78.502,
            17.382
          ],
          [
            78.495,
            17.378
          ]
        ]
      },
      {
        "id": "hyd-st-22",
        "name": "Hitec City Cyber Towers Flyover",
        "from_intersection_id": "int-cyber-gateway",
        "to_intersection_id": "int-cyber-towers-rotary",
        "length_m": 1400.0,
        "water_depth_cm": 3.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.37,
            17.452
          ],
          [
            78.375,
            17.449
          ],
          [
            78.38,
            17.447
          ]
        ]
      },
      {
        "id": "hyd-st-23",
        "name": "Mindspace - Inorbit Mall Arterial",
        "from_intersection_id": "int-cyber-towers-rotary",
        "to_intersection_id": "int-inorbit-mall-ingress",
        "length_m": 1650.0,
        "water_depth_cm": 7.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.38,
            17.447
          ],
          [
            78.383,
            17.44
          ],
          [
            78.387,
            17.435
          ]
        ]
      },
      {
        "id": "hyd-st-24",
        "name": "Durgam Cheruvu Cable Bridge Approach",
        "from_intersection_id": "int-inorbit-mall-ingress",
        "to_intersection_id": "int-jubilee-hills-rd-45-jn",
        "length_m": 1800.0,
        "water_depth_cm": 2.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.387,
            17.435
          ],
          [
            78.395,
            17.432
          ],
          [
            78.405,
            17.43
          ]
        ]
      },
      {
        "id": "hyd-st-25",
        "name": "Road No. 36 Jubilee Hills",
        "from_intersection_id": "int-jubilee-hills-rd-45-jn",
        "to_intersection_id": "int-jubilee-hills-checkpost",
        "length_m": 2100.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.405,
            17.43
          ],
          [
            78.412,
            17.431
          ],
          [
            78.42,
            17.43
          ]
        ]
      },
      {
        "id": "hyd-st-26",
        "name": "Road No. 10 Banjara Hills Connector",
        "from_intersection_id": "int-jubilee-hills-checkpost",
        "to_intersection_id": "int-banjara-hills-rd-1-jn",
        "length_m": 1900.0,
        "water_depth_cm": 5.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.42,
            17.43
          ],
          [
            78.435,
            17.425
          ],
          [
            78.45,
            17.422
          ]
        ]
      },
      {
        "id": "hyd-st-27",
        "name": "Gachibowli Flyover & Bio-Diversity Jn",
        "from_intersection_id": "int-bio-diversity-park-jn",
        "to_intersection_id": "int-gachibowli-stadium-cross",
        "length_m": 2200.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.365,
            17.44
          ],
          [
            78.355,
            17.44
          ],
          [
            78.348,
            17.44
          ]
        ]
      },
      {
        "id": "hyd-st-28",
        "name": "Financial District ISB Main Road",
        "from_intersection_id": "int-gachibowli-stadium-cross",
        "to_intersection_id": "int-wipro-circle-nanakramguda",
        "length_m": 2600.0,
        "water_depth_cm": 3.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.348,
            17.44
          ],
          [
            78.345,
            17.428
          ],
          [
            78.342,
            17.418
          ]
        ]
      },
      {
        "id": "hyd-st-29",
        "name": "Kondapur Main Road / Botanical Garden",
        "from_intersection_id": "int-botanical-garden-jn",
        "to_intersection_id": "int-kothaguda-cross-roads",
        "length_m": 1750.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.358,
            17.455
          ],
          [
            78.365,
            17.46
          ],
          [
            78.372,
            17.463
          ]
        ]
      },
      {
        "id": "hyd-st-30",
        "name": "KPHB Colony Main Road Phase 1",
        "from_intersection_id": "int-jntu-metro-station",
        "to_intersection_id": "int-kphb-phase-1-rotary",
        "length_m": 1900.0,
        "water_depth_cm": 13.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.39,
            17.498
          ],
          [
            78.39,
            17.493
          ],
          [
            78.392,
            17.487
          ]
        ]
      },
      {
        "id": "hyd-st-31",
        "name": "Kukatpally Y-Junction National Highway",
        "from_intersection_id": "int-kphb-phase-1-rotary",
        "to_intersection_id": "int-moosapet-metro-jn",
        "length_m": 2100.0,
        "water_depth_cm": 16.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.392,
            17.487
          ],
          [
            78.405,
            17.48
          ],
          [
            78.432,
            17.472
          ]
        ]
      },
      {
        "id": "hyd-st-32",
        "name": "Balanagar Industrial Main Road",
        "from_intersection_id": "int-moosapet-metro-jn",
        "to_intersection_id": "int-idpl-colony-cross-roads",
        "length_m": 2300.0,
        "water_depth_cm": 19.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.432,
            17.472
          ],
          [
            78.448,
            17.468
          ],
          [
            78.462,
            17.465
          ]
        ]
      },
      {
        "id": "hyd-st-33",
        "name": "Moosarambagh Lowland Causeway",
        "from_intersection_id": "int-moosarambagh-bridge",
        "to_intersection_id": "int-amberpet-old-bridge",
        "length_m": 1100.0,
        "water_depth_cm": 38.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.505,
            17.375
          ],
          [
            78.508,
            17.378
          ],
          [
            78.512,
            17.382
          ]
        ]
      },
      {
        "id": "hyd-st-34",
        "name": "Chaderghat Bridge & Musi River Bank",
        "from_intersection_id": "int-chaderghat-rotary",
        "to_intersection_id": "int-rang-mahal-jn",
        "length_m": 1350.0,
        "water_depth_cm": 29.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.488,
            17.378
          ],
          [
            78.484,
            17.375
          ],
          [
            78.48,
            17.372
          ]
        ]
      },
      {
        "id": "hyd-st-35",
        "name": "Malakpet Railway Underpass Corridor",
        "from_intersection_id": "int-chaderghat-rotary",
        "to_intersection_id": "int-malakpet-gunj-jn",
        "length_m": 1500.0,
        "water_depth_cm": 33.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.488,
            17.378
          ],
          [
            78.492,
            17.372
          ],
          [
            78.502,
            17.368
          ]
        ]
      },
      {
        "id": "hyd-st-36",
        "name": "Dilsukhnagar Main Commercial Highway",
        "from_intersection_id": "int-malakpet-gunj-jn",
        "to_intersection_id": "int-dilsukhnagar-bus-depot",
        "length_m": 2200.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.502,
            17.368
          ],
          [
            78.515,
            17.368
          ],
          [
            78.525,
            17.368
          ]
        ]
      },
      {
        "id": "hyd-st-37",
        "name": "LB Nagar Ring Road Multi-tier Jn",
        "from_intersection_id": "int-dilsukhnagar-bus-depot",
        "to_intersection_id": "int-lb-nagar-metro-hub",
        "length_m": 2600.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.525,
            17.368
          ],
          [
            78.54,
            17.36
          ],
          [
            78.55,
            17.35
          ]
        ]
      },
      {
        "id": "hyd-st-38",
        "name": "Nayapul / High Court Musi River Road",
        "from_intersection_id": "int-madina-chowk",
        "to_intersection_id": "int-high-court-gate-jn",
        "length_m": 1200.0,
        "water_depth_cm": 24.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.475,
            17.367
          ],
          [
            78.473,
            17.369
          ],
          [
            78.47,
            17.372
          ]
        ]
      },
      {
        "id": "hyd-st-39",
        "name": "Charminar Pedestrian & Heritage Ring",
        "from_intersection_id": "int-madina-chowk",
        "to_intersection_id": "int-charminar-monument-circle",
        "length_m": 1100.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.475,
            17.365
          ],
          [
            78.474,
            17.363
          ],
          [
            78.474,
            17.361
          ]
        ]
      },
      {
        "id": "hyd-st-40",
        "name": "Puranapul Bridge & Riverbank Road",
        "from_intersection_id": "int-city-college-cross",
        "to_intersection_id": "int-puranapul-darwaza",
        "length_m": 1300.0,
        "water_depth_cm": 27.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.468,
            17.366
          ],
          [
            78.464,
            17.364
          ],
          [
            78.46,
            17.364
          ]
        ]
      },
      {
        "id": "hyd-st-41",
        "name": "Bahadurpura Zoo Park Corridor",
        "from_intersection_id": "int-puranapul-darwaza",
        "to_intersection_id": "int-nehru-zoo-park-main-gate",
        "length_m": 1800.0,
        "water_depth_cm": 11.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.46,
            17.364
          ],
          [
            78.458,
            17.358
          ],
          [
            78.455,
            17.35
          ]
        ]
      },
      {
        "id": "hyd-st-42",
        "name": "Falaknuma Palace Hilltop Link",
        "from_intersection_id": "int-falaknuma-rly-station",
        "to_intersection_id": "int-palace-gate-main",
        "length_m": 1600.0,
        "water_depth_cm": 1.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.465,
            17.338
          ],
          [
            78.467,
            17.334
          ],
          [
            78.468,
            17.33
          ]
        ]
      },
      {
        "id": "hyd-st-43",
        "name": "Chandrayangutta Flyover Jn",
        "from_intersection_id": "int-falaknuma-rly-station",
        "to_intersection_id": "int-chandrayangutta-cross-roads",
        "length_m": 1900.0,
        "water_depth_cm": 8.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.465,
            17.338
          ],
          [
            78.472,
            17.33
          ],
          [
            78.48,
            17.32
          ]
        ]
      },
      {
        "id": "hyd-st-44",
        "name": "Santoshnagar Main Road Corridor",
        "from_intersection_id": "int-chandrayangutta-cross-roads",
        "to_intersection_id": "int-is-sadan-cross-roads",
        "length_m": 2100.0,
        "water_depth_cm": 12.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.48,
            17.32
          ],
          [
            78.495,
            17.33
          ],
          [
            78.51,
            17.34
          ]
        ]
      },
      {
        "id": "hyd-st-45",
        "name": "PVNR Elevated Expressway (Airport Bypass)",
        "from_intersection_id": "int-mehdipatnam-rotary",
        "to_intersection_id": "int-aramghar-jn",
        "length_m": 4500.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            78.44,
            17.395
          ],
          [
            78.435,
            17.385
          ],
          [
            78.43,
            17.375
          ],
          [
            78.425,
            17.365
          ],
          [
            78.42,
            17.355
          ]
        ]
      }
    ],
    {
      "int-sailing-club-jn": [
        78.478,
        17.432
      ],
      "int-secretariat-circle": [
        78.471,
        17.412
      ],
      "int-prakash-nagar-metro": [
        78.468,
        17.443
      ],
      "int-rasoolpura-flyover": [
        78.483,
        17.438
      ],
      "int-khairatabad-rly-bridge": [
        78.462,
        17.411
      ],
      "int-lakdikapul-jn": [
        78.466,
        17.404
      ],
      "int-cancer-hospital-jn": [
        78.435,
        17.415
      ],
      "int-mla-colony-gate": [
        78.448,
        17.425
      ],
      "int-erramanzil-colony": [
        78.452,
        17.421
      ],
      "int-raj-bhavan-quarters": [
        78.458,
        17.426
      ],
      "int-nagarjuna-circle": [
        78.448,
        17.425
      ],
      "int-ameerpet-metro": [
        78.455,
        17.435
      ],
      "int-sanjeevaiah-park-gate": [
        78.468,
        17.435
      ],
      "int-peoples-plaza-ingress": [
        78.465,
        17.418
      ],
      "int-bible-house-jn": [
        78.482,
        17.425
      ],
      "int-indira-park-gate": [
        78.479,
        17.41
      ],
      "int-liberty-circle": [
        78.475,
        17.402
      ],
      "int-basheerbagh-flyover": [
        78.482,
        17.408
      ],
      "int-himayatnagar-y-jn": [
        78.485,
        17.405
      ],
      "int-narayanaguda-flyover": [
        78.494,
        17.398
      ],
      "int-rtc-x-roads": [
        78.495,
        17.408
      ],
      "int-narayanaguda-jn": [
        78.494,
        17.398
      ],
      "int-musheerabad-jn": [
        78.5,
        17.42
      ],
      "int-kavadiguda-cross-roads": [
        78.485,
        17.412
      ],
      "int-paradise-circle": [
        78.487,
        17.442
      ],
      "int-secunderabad-station": [
        78.504,
        17.437
      ],
      "int-rasoolpura-jn": [
        78.475,
        17.441
      ],
      "int-sangeet-cinema-jn": [
        78.502,
        17.442
      ],
      "int-tadbund-cross-roads": [
        78.488,
        17.458
      ],
      "int-bowenpally-checkpost": [
        78.484,
        17.472
      ],
      "int-trimulgherry-cross-roads": [
        78.51,
        17.475
      ],
      "int-lothkunta-jn": [
        78.515,
        17.502
      ],
      "int-malkajgiri-jn": [
        78.525,
        17.448
      ],
      "int-anandbagh-cross-roads": [
        78.538,
        17.458
      ],
      "int-sangeet-jn": [
        78.515,
        17.438
      ],
      "int-tarnaka-cross-roads": [
        78.532,
        17.428
      ],
      "int-uppal-ring-road-jn": [
        78.56,
        17.4
      ],
      "int-amberpet-causeway": [
        78.515,
        17.388
      ],
      "int-amberpet-bridge": [
        78.515,
        17.388
      ],
      "int-nimboliadda-jn": [
        78.495,
        17.378
      ],
      "int-cyber-gateway": [
        78.37,
        17.452
      ],
      "int-cyber-towers-rotary": [
        78.38,
        17.447
      ],
      "int-inorbit-mall-ingress": [
        78.387,
        17.435
      ],
      "int-jubilee-hills-rd-45-jn": [
        78.405,
        17.43
      ],
      "int-jubilee-hills-checkpost": [
        78.42,
        17.43
      ],
      "int-banjara-hills-rd-1-jn": [
        78.45,
        17.422
      ],
      "int-bio-diversity-park-jn": [
        78.365,
        17.44
      ],
      "int-gachibowli-stadium-cross": [
        78.348,
        17.44
      ],
      "int-wipro-circle-nanakramguda": [
        78.342,
        17.418
      ],
      "int-botanical-garden-jn": [
        78.358,
        17.455
      ],
      "int-kothaguda-cross-roads": [
        78.372,
        17.463
      ],
      "int-jntu-metro-station": [
        78.39,
        17.498
      ],
      "int-kphb-phase-1-rotary": [
        78.392,
        17.487
      ],
      "int-moosapet-metro-jn": [
        78.432,
        17.472
      ],
      "int-idpl-colony-cross-roads": [
        78.462,
        17.465
      ],
      "int-moosarambagh-bridge": [
        78.505,
        17.375
      ],
      "int-amberpet-old-bridge": [
        78.512,
        17.382
      ],
      "int-chaderghat-rotary": [
        78.488,
        17.378
      ],
      "int-rang-mahal-jn": [
        78.48,
        17.372
      ],
      "int-malakpet-gunj-jn": [
        78.502,
        17.368
      ],
      "int-dilsukhnagar-bus-depot": [
        78.525,
        17.368
      ],
      "int-lb-nagar-metro-hub": [
        78.55,
        17.35
      ],
      "int-madina-chowk": [
        78.475,
        17.365
      ],
      "int-high-court-gate-jn": [
        78.47,
        17.372
      ],
      "int-charminar-monument-circle": [
        78.474,
        17.361
      ],
      "int-city-college-cross": [
        78.468,
        17.366
      ],
      "int-puranapul-darwaza": [
        78.46,
        17.364
      ],
      "int-nehru-zoo-park-main-gate": [
        78.455,
        17.35
      ],
      "int-falaknuma-rly-station": [
        78.465,
        17.338
      ],
      "int-palace-gate-main": [
        78.468,
        17.33
      ],
      "int-chandrayangutta-cross-roads": [
        78.48,
        17.32
      ],
      "int-is-sadan-cross-roads": [
        78.51,
        17.34
      ],
      "int-mehdipatnam-rotary": [
        78.44,
        17.395
      ],
      "int-aramghar-jn": [
        78.42,
        17.355
      ]
    }
  ],
  "mumbai": [
    [
      {
        "id": "mum-st-01",
        "name": "Marine Drive Promenade Outer Lane",
        "from_intersection_id": "int-ncpa-circle",
        "to_intersection_id": "int-churchgate-flyover",
        "length_m": 1900.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.822,
            18.925
          ],
          [
            72.824,
            18.935
          ],
          [
            72.825,
            18.945
          ]
        ]
      },
      {
        "id": "mum-st-02",
        "name": "Colaba Causeway Main Commercial",
        "from_intersection_id": "int-regal-cinema-circle",
        "to_intersection_id": "int-colaba-post-office",
        "length_m": 1600.0,
        "water_depth_cm": 5.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.832,
            18.922
          ],
          [
            72.83,
            18.918
          ],
          [
            72.826,
            18.912
          ]
        ]
      },
      {
        "id": "mum-st-03",
        "name": "CST / Dr. DN Road Heritage Corridor",
        "from_intersection_id": "int-cst-station-plaza",
        "to_intersection_id": "int-flora-fountain-circle",
        "length_m": 1400.0,
        "water_depth_cm": 9.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.835,
            18.94
          ],
          [
            72.833,
            18.936
          ],
          [
            72.831,
            18.932
          ]
        ]
      },
      {
        "id": "mum-st-04",
        "name": "JJ Flyover Elevated Viaduct",
        "from_intersection_id": "int-jj-hospital-ingress",
        "to_intersection_id": "int-cst-flyover-ramp",
        "length_m": 2400.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.838,
            18.96
          ],
          [
            72.836,
            18.95
          ],
          [
            72.835,
            18.942
          ]
        ]
      },
      {
        "id": "mum-st-05",
        "name": "Peddar Road / Cumballa Hill Ridge",
        "from_intersection_id": "int-kemps-corner",
        "to_intersection_id": "int-haji-ali-jn",
        "length_m": 1800.0,
        "water_depth_cm": 2.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.808,
            18.965
          ],
          [
            72.81,
            18.972
          ],
          [
            72.812,
            18.978
          ]
        ]
      },
      {
        "id": "mum-st-06",
        "name": "Haji Ali Junction Coastal Lowland",
        "from_intersection_id": "int-haji-ali-circle",
        "to_intersection_id": "int-lotus-cinema-jn",
        "length_m": 1300.0,
        "water_depth_cm": 22.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.812,
            18.978
          ],
          [
            72.814,
            18.985
          ],
          [
            72.815,
            18.992
          ]
        ]
      },
      {
        "id": "mum-st-07",
        "name": "Worli Seaface Coastal Boulevard",
        "from_intersection_id": "int-worli-dairy",
        "to_intersection_id": "int-bandra-worli-sea-link-ingress",
        "length_m": 2100.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.815,
            18.995
          ],
          [
            72.816,
            19.005
          ],
          [
            72.818,
            19.015
          ]
        ]
      },
      {
        "id": "mum-st-08",
        "name": "Senapati Bapat Marg / Lower Parel",
        "from_intersection_id": "int-currey-road-jn",
        "to_intersection_id": "int-kamala-mills-gate",
        "length_m": 1700.0,
        "water_depth_cm": 14.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.83,
            18.992
          ],
          [
            72.83,
            18.998
          ],
          [
            72.832,
            19.006
          ]
        ]
      },
      {
        "id": "mum-st-09",
        "name": "Hindmata Cinema TT Circle Low Point",
        "from_intersection_id": "int-dadar-tram-jn",
        "to_intersection_id": "int-parel-tt-circle",
        "length_m": 1300.0,
        "water_depth_cm": 38.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.842,
            19.012
          ],
          [
            72.844,
            19.016
          ],
          [
            72.846,
            19.02
          ]
        ]
      },
      {
        "id": "mum-st-10",
        "name": "Dadar TT Circle Commercial Hub",
        "from_intersection_id": "int-khodadad-circle",
        "to_intersection_id": "int-chitra-cinema-jn",
        "length_m": 1500.0,
        "water_depth_cm": 18.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.844,
            19.018
          ],
          [
            72.846,
            19.022
          ],
          [
            72.848,
            19.025
          ]
        ]
      },
      {
        "id": "mum-st-11",
        "name": "King's Circle / Gandhi Market Basin",
        "from_intersection_id": "int-maheshwari-udyan",
        "to_intersection_id": "int-sion-hospital-jn",
        "length_m": 1600.0,
        "water_depth_cm": 42.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.852,
            19.028
          ],
          [
            72.855,
            19.032
          ],
          [
            72.858,
            19.036
          ]
        ]
      },
      {
        "id": "mum-st-12",
        "name": "Sion Circle & Highway Junction",
        "from_intersection_id": "int-sion-hospital-jn",
        "to_intersection_id": "int-sion-fort-cross",
        "length_m": 1400.0,
        "water_depth_cm": 16.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.858,
            19.036
          ],
          [
            72.862,
            19.04
          ],
          [
            72.865,
            19.044
          ]
        ]
      },
      {
        "id": "mum-st-13",
        "name": "Dharavi 90 Feet Road Catchment",
        "from_intersection_id": "int-kala-killa-jn",
        "to_intersection_id": "int-mahim-nature-park-gate",
        "length_m": 1900.0,
        "water_depth_cm": 28.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.85,
            19.04
          ],
          [
            72.854,
            19.043
          ],
          [
            72.858,
            19.046
          ]
        ]
      },
      {
        "id": "mum-st-14",
        "name": "Mahim Causeway Marine Link",
        "from_intersection_id": "int-mahim-church-circle",
        "to_intersection_id": "int-bandra-reclamation-ramp",
        "length_m": 1600.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.84,
            19.038
          ],
          [
            72.836,
            19.044
          ],
          [
            72.83,
            19.048
          ]
        ]
      },
      {
        "id": "mum-st-15",
        "name": "Bandra-Kurla Complex (BKC) Connector",
        "from_intersection_id": "int-kalanagar-jn",
        "to_intersection_id": "int-bkc-bharat-diamond-bourse",
        "length_m": 2100.0,
        "water_depth_cm": 11.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.852,
            19.058
          ],
          [
            72.861,
            19.063
          ],
          [
            72.869,
            19.068
          ]
        ]
      },
      {
        "id": "mum-st-16",
        "name": "BKC Central Avenue Financial Corridor",
        "from_intersection_id": "int-bkc-connector-jn",
        "to_intersection_id": "int-mtnl-building-circle",
        "length_m": 1800.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.869,
            19.068
          ],
          [
            72.875,
            19.065
          ],
          [
            72.88,
            19.062
          ]
        ]
      },
      {
        "id": "mum-st-17",
        "name": "Milan Subway Lowland Crossing",
        "from_intersection_id": "int-santacruz-west-station",
        "to_intersection_id": "int-milan-flyover-ingress",
        "length_m": 850.0,
        "water_depth_cm": 48.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.842,
            19.085
          ],
          [
            72.845,
            19.083
          ],
          [
            72.848,
            19.081
          ]
        ]
      },
      {
        "id": "mum-st-18",
        "name": "Khar Subway Lowland Corridor",
        "from_intersection_id": "int-khar-west-market",
        "to_intersection_id": "int-khar-east-sv-link",
        "length_m": 780.0,
        "water_depth_cm": 44.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.836,
            19.07
          ],
          [
            72.839,
            19.07
          ],
          [
            72.842,
            19.071
          ]
        ]
      },
      {
        "id": "mum-st-19",
        "name": "Andheri Subway Critical Underpass",
        "from_intersection_id": "int-andheri-west-market",
        "to_intersection_id": "int-andheri-east-highway-ingress",
        "length_m": 920.0,
        "water_depth_cm": 52.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.842,
            19.118
          ],
          [
            72.845,
            19.118
          ],
          [
            72.848,
            19.119
          ]
        ]
      },
      {
        "id": "mum-st-20",
        "name": "Western Express Highway (Bandra - Airport)",
        "from_intersection_id": "int-kalanagar-flyover",
        "to_intersection_id": "int-domestic-airport-flyover",
        "length_m": 3400.0,
        "water_depth_cm": 3.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.852,
            19.058
          ],
          [
            72.85,
            19.075
          ],
          [
            72.852,
            19.095
          ]
        ]
      },
      {
        "id": "mum-st-21",
        "name": "Western Express Highway (Andheri - Goregaon)",
        "from_intersection_id": "int-weh-andheri-metro",
        "to_intersection_id": "int-goregaon-hub-mall-flyover",
        "length_m": 3800.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.852,
            19.118
          ],
          [
            72.855,
            19.138
          ],
          [
            72.858,
            19.158
          ]
        ]
      },
      {
        "id": "mum-st-22",
        "name": "Western Express Highway (Malad - Borivali)",
        "from_intersection_id": "int-malad-inorbit-link",
        "to_intersection_id": "int-borivali-national-park-jn",
        "length_m": 4200.0,
        "water_depth_cm": 3.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.86,
            19.18
          ],
          [
            72.862,
            19.205
          ],
          [
            72.865,
            19.228
          ]
        ]
      },
      {
        "id": "mum-st-23",
        "name": "S.V. Road Bandra to Santacruz",
        "from_intersection_id": "int-lucky-restaurant-jn",
        "to_intersection_id": "int-santacruz-station-west",
        "length_m": 2300.0,
        "water_depth_cm": 13.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.835,
            19.055
          ],
          [
            72.835,
            19.07
          ],
          [
            72.836,
            19.085
          ]
        ]
      },
      {
        "id": "mum-st-24",
        "name": "Linking Road Shopping Corridor",
        "from_intersection_id": "int-waterfield-road-jn",
        "to_intersection_id": "int-santacruz-linking-road-jn",
        "length_m": 1900.0,
        "water_depth_cm": 8.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.832,
            19.06
          ],
          [
            72.833,
            19.072
          ],
          [
            72.834,
            19.082
          ]
        ]
      },
      {
        "id": "mum-st-25",
        "name": "JVLR (Jogeshwari-Vikhroli Link Road)",
        "from_intersection_id": "int-weh-jogeshwari-jn",
        "to_intersection_id": "int-seepz-tech-corridor",
        "length_m": 3100.0,
        "water_depth_cm": 7.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.855,
            19.135
          ],
          [
            72.87,
            19.13
          ],
          [
            72.885,
            19.125
          ]
        ]
      },
      {
        "id": "mum-st-26",
        "name": "Eastern Freeway High Viaduct",
        "from_intersection_id": "int-bhakti-park-ramp",
        "to_intersection_id": "int-wadala-gate",
        "length_m": 3500.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.88,
            19.03
          ],
          [
            72.875,
            19.015
          ],
          [
            72.865,
            18.995
          ]
        ]
      },
      {
        "id": "mum-st-27",
        "name": "Kurla LBS Marg Mithi River Lowland",
        "from_intersection_id": "int-kurla-kalpana-cinema",
        "to_intersection_id": "int-kurla-bus-depot-jn",
        "length_m": 1800.0,
        "water_depth_cm": 36.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.875,
            19.065
          ],
          [
            72.878,
            19.068
          ],
          [
            72.882,
            19.072
          ]
        ]
      },
      {
        "id": "mum-st-28",
        "name": "SCLR (Santacruz-Chembur Link Road)",
        "from_intersection_id": "int-bkc-connector-east",
        "to_intersection_id": "int-amar-mahal-jn",
        "length_m": 2800.0,
        "water_depth_cm": 6.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.869,
            19.068
          ],
          [
            72.88,
            19.072
          ],
          [
            72.895,
            19.065
          ]
        ]
      },
      {
        "id": "mum-st-29",
        "name": "Eastern Express Highway (Sion - Ghatkopar)",
        "from_intersection_id": "int-priyadarshini-circle",
        "to_intersection_id": "int-ghatkopar-pant-nagar-jn",
        "length_m": 3600.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.87,
            19.045
          ],
          [
            72.89,
            19.065
          ],
          [
            72.91,
            19.085
          ]
        ]
      },
      {
        "id": "mum-st-30",
        "name": "Eastern Express Highway (Vikhroli - Mulund)",
        "from_intersection_id": "int-vikhroli-godrej-flyover",
        "to_intersection_id": "int-mulund-toll-naka",
        "length_m": 4500.0,
        "water_depth_cm": 3.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.925,
            19.11
          ],
          [
            72.94,
            19.145
          ],
          [
            72.955,
            19.175
          ]
        ]
      },
      {
        "id": "mum-st-31",
        "name": "Chembur Naka Commercial Corridor",
        "from_intersection_id": "int-diamond-garden",
        "to_intersection_id": "int-chembur-railway-station-jn",
        "length_m": 1600.0,
        "water_depth_cm": 9.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.895,
            19.055
          ],
          [
            72.9,
            19.058
          ],
          [
            72.905,
            19.062
          ]
        ]
      },
      {
        "id": "mum-st-32",
        "name": "Ghatkopar Andheri Link Road (GALR)",
        "from_intersection_id": "int-asalpha-metro-station",
        "to_intersection_id": "int-ghatkopar-station-west",
        "length_m": 2200.0,
        "water_depth_cm": 14.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.892,
            19.102
          ],
          [
            72.902,
            19.095
          ],
          [
            72.91,
            19.088
          ]
        ]
      },
      {
        "id": "mum-st-33",
        "name": "Bhandup LBS Marg Low Point",
        "from_intersection_id": "int-bhandup-station-west",
        "to_intersection_id": "int-kanjurmarg-nallah-crossing",
        "length_m": 1750.0,
        "water_depth_cm": 24.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.93,
            19.145
          ],
          [
            72.935,
            19.148
          ],
          [
            72.938,
            19.152
          ]
        ]
      },
      {
        "id": "mum-st-34",
        "name": "Chunabhatti Sion-Trombay Link",
        "from_intersection_id": "int-chunabhatti-flyover-ramp",
        "to_intersection_id": "int-kurla-priyadarshini-link",
        "length_m": 1500.0,
        "water_depth_cm": 21.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.872,
            19.048
          ],
          [
            72.876,
            19.052
          ],
          [
            72.88,
            19.056
          ]
        ]
      },
      {
        "id": "mum-st-35",
        "name": "Sion-Panvel Highway Deonar Corridor",
        "from_intersection_id": "int-mankhurd-flyover-jn",
        "to_intersection_id": "int-vashi-creek-bridge-ingress",
        "length_m": 3200.0,
        "water_depth_cm": 5.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            72.915,
            19.048
          ],
          [
            72.935,
            19.04
          ],
          [
            72.955,
            19.035
          ]
        ]
      }
    ],
    {
      "int-ncpa-circle": [
        72.822,
        18.925
      ],
      "int-churchgate-flyover": [
        72.825,
        18.945
      ],
      "int-regal-cinema-circle": [
        72.832,
        18.922
      ],
      "int-colaba-post-office": [
        72.826,
        18.912
      ],
      "int-cst-station-plaza": [
        72.835,
        18.94
      ],
      "int-flora-fountain-circle": [
        72.831,
        18.932
      ],
      "int-jj-hospital-ingress": [
        72.838,
        18.96
      ],
      "int-cst-flyover-ramp": [
        72.835,
        18.942
      ],
      "int-kemps-corner": [
        72.808,
        18.965
      ],
      "int-haji-ali-jn": [
        72.812,
        18.978
      ],
      "int-haji-ali-circle": [
        72.812,
        18.978
      ],
      "int-lotus-cinema-jn": [
        72.815,
        18.992
      ],
      "int-worli-dairy": [
        72.815,
        18.995
      ],
      "int-bandra-worli-sea-link-ingress": [
        72.818,
        19.015
      ],
      "int-currey-road-jn": [
        72.83,
        18.992
      ],
      "int-kamala-mills-gate": [
        72.832,
        19.006
      ],
      "int-dadar-tram-jn": [
        72.842,
        19.012
      ],
      "int-parel-tt-circle": [
        72.846,
        19.02
      ],
      "int-khodadad-circle": [
        72.844,
        19.018
      ],
      "int-chitra-cinema-jn": [
        72.848,
        19.025
      ],
      "int-maheshwari-udyan": [
        72.852,
        19.028
      ],
      "int-sion-hospital-jn": [
        72.858,
        19.036
      ],
      "int-sion-fort-cross": [
        72.865,
        19.044
      ],
      "int-kala-killa-jn": [
        72.85,
        19.04
      ],
      "int-mahim-nature-park-gate": [
        72.858,
        19.046
      ],
      "int-mahim-church-circle": [
        72.84,
        19.038
      ],
      "int-bandra-reclamation-ramp": [
        72.83,
        19.048
      ],
      "int-kalanagar-jn": [
        72.852,
        19.058
      ],
      "int-bkc-bharat-diamond-bourse": [
        72.869,
        19.068
      ],
      "int-bkc-connector-jn": [
        72.869,
        19.068
      ],
      "int-mtnl-building-circle": [
        72.88,
        19.062
      ],
      "int-santacruz-west-station": [
        72.842,
        19.085
      ],
      "int-milan-flyover-ingress": [
        72.848,
        19.081
      ],
      "int-khar-west-market": [
        72.836,
        19.07
      ],
      "int-khar-east-sv-link": [
        72.842,
        19.071
      ],
      "int-andheri-west-market": [
        72.842,
        19.118
      ],
      "int-andheri-east-highway-ingress": [
        72.848,
        19.119
      ],
      "int-kalanagar-flyover": [
        72.852,
        19.058
      ],
      "int-domestic-airport-flyover": [
        72.852,
        19.095
      ],
      "int-weh-andheri-metro": [
        72.852,
        19.118
      ],
      "int-goregaon-hub-mall-flyover": [
        72.858,
        19.158
      ],
      "int-malad-inorbit-link": [
        72.86,
        19.18
      ],
      "int-borivali-national-park-jn": [
        72.865,
        19.228
      ],
      "int-lucky-restaurant-jn": [
        72.835,
        19.055
      ],
      "int-santacruz-station-west": [
        72.836,
        19.085
      ],
      "int-waterfield-road-jn": [
        72.832,
        19.06
      ],
      "int-santacruz-linking-road-jn": [
        72.834,
        19.082
      ],
      "int-weh-jogeshwari-jn": [
        72.855,
        19.135
      ],
      "int-seepz-tech-corridor": [
        72.885,
        19.125
      ],
      "int-bhakti-park-ramp": [
        72.88,
        19.03
      ],
      "int-wadala-gate": [
        72.865,
        18.995
      ],
      "int-kurla-kalpana-cinema": [
        72.875,
        19.065
      ],
      "int-kurla-bus-depot-jn": [
        72.882,
        19.072
      ],
      "int-bkc-connector-east": [
        72.869,
        19.068
      ],
      "int-amar-mahal-jn": [
        72.895,
        19.065
      ],
      "int-priyadarshini-circle": [
        72.87,
        19.045
      ],
      "int-ghatkopar-pant-nagar-jn": [
        72.91,
        19.085
      ],
      "int-vikhroli-godrej-flyover": [
        72.925,
        19.11
      ],
      "int-mulund-toll-naka": [
        72.955,
        19.175
      ],
      "int-diamond-garden": [
        72.895,
        19.055
      ],
      "int-chembur-railway-station-jn": [
        72.905,
        19.062
      ],
      "int-asalpha-metro-station": [
        72.892,
        19.102
      ],
      "int-ghatkopar-station-west": [
        72.91,
        19.088
      ],
      "int-bhandup-station-west": [
        72.93,
        19.145
      ],
      "int-kanjurmarg-nallah-crossing": [
        72.938,
        19.152
      ],
      "int-chunabhatti-flyover-ramp": [
        72.872,
        19.048
      ],
      "int-kurla-priyadarshini-link": [
        72.88,
        19.056
      ],
      "int-mankhurd-flyover-jn": [
        72.915,
        19.048
      ],
      "int-vashi-creek-bridge-ingress": [
        72.955,
        19.035
      ]
    }
  ],
  "chennai": [
    [
      {
        "id": "chn-st-01",
        "name": "Kamarajar Salai (Marina Beach Road)",
        "from_intersection_id": "int-war-memorial-circle",
        "to_intersection_id": "int-light-house-jn",
        "length_m": 2800.0,
        "water_depth_cm": 5.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.285,
            13.078
          ],
          [
            80.282,
            13.055
          ],
          [
            80.28,
            13.038
          ]
        ]
      },
      {
        "id": "chn-st-02",
        "name": "Santhome High Road Coastal Corridor",
        "from_intersection_id": "int-light-house-jn",
        "to_intersection_id": "int-foreshore-estate-bus-stand",
        "length_m": 1900.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.28,
            13.038
          ],
          [
            80.278,
            13.028
          ],
          [
            80.275,
            13.018
          ]
        ]
      },
      {
        "id": "chn-st-03",
        "name": "Anna Salai (Mount Road Central)",
        "from_intersection_id": "int-gemini-flyover",
        "to_intersection_id": "int-saidapet-bridge-ingress",
        "length_m": 3100.0,
        "water_depth_cm": 6.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.25,
            13.052
          ],
          [
            80.235,
            13.035
          ],
          [
            80.222,
            13.02
          ]
        ]
      },
      {
        "id": "chn-st-04",
        "name": "Gemini / Anna Flyover (High Clearance)",
        "from_intersection_id": "int-cathedral-road-jn",
        "to_intersection_id": "int-nungambakkam-high-rd-link",
        "length_m": 1600.0,
        "water_depth_cm": 1.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.252,
            13.055
          ],
          [
            80.25,
            13.052
          ],
          [
            80.248,
            13.048
          ]
        ]
      },
      {
        "id": "chn-st-05",
        "name": "T. Nagar G.N. Chetty Road Commercial",
        "from_intersection_id": "int-panagal-park-circle",
        "to_intersection_id": "int-vani-mahal-jn",
        "length_m": 1500.0,
        "water_depth_cm": 12.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.235,
            13.04
          ],
          [
            80.24,
            13.042
          ],
          [
            80.245,
            13.045
          ]
        ]
      },
      {
        "id": "chn-st-06",
        "name": "Usman Road Flyover & Lowland Approach",
        "from_intersection_id": "int-t-nagar-bus-terminus",
        "to_intersection_id": "int-ranganathan-street-jn",
        "length_m": 1700.0,
        "water_depth_cm": 18.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.228,
            13.032
          ],
          [
            80.232,
            13.038
          ],
          [
            80.235,
            13.044
          ]
        ]
      },
      {
        "id": "chn-st-07",
        "name": "Nungambakkam High Road Corridor",
        "from_intersection_id": "int-sterling-road-jn",
        "to_intersection_id": "int-gemini-flyover-link",
        "length_m": 1900.0,
        "water_depth_cm": 8.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.24,
            13.065
          ],
          [
            80.245,
            13.058
          ],
          [
            80.25,
            13.052
          ]
        ]
      },
      {
        "id": "chn-st-08",
        "name": "Chetpet / Harrington Road Subway",
        "from_intersection_id": "int-chetpet-railway-station",
        "to_intersection_id": "int-harrington-rd-cross",
        "length_m": 1100.0,
        "water_depth_cm": 32.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.236,
            13.072
          ],
          [
            80.238,
            13.07
          ],
          [
            80.24,
            13.068
          ]
        ]
      },
      {
        "id": "chn-st-09",
        "name": "Poonamallee High Road (EVR Periyar)",
        "from_intersection_id": "int-chennai-central-station",
        "to_intersection_id": "int-kilpauk-medical-college-jn",
        "length_m": 2900.0,
        "water_depth_cm": 11.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.275,
            13.082
          ],
          [
            80.255,
            13.078
          ],
          [
            80.235,
            13.075
          ]
        ]
      },
      {
        "id": "chn-st-10",
        "name": "Velachery Main Road (Lake Marsh Corridor)",
        "from_intersection_id": "int-vijayanagar-bus-terminus",
        "to_intersection_id": "int-kaiveli-jn",
        "length_m": 2200.0,
        "water_depth_cm": 38.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.218,
            12.978
          ],
          [
            80.222,
            12.971
          ],
          [
            80.226,
            12.965
          ]
        ]
      },
      {
        "id": "chn-st-11",
        "name": "Velachery Bypass Road Corridor",
        "from_intersection_id": "int-guru-nanak-college-jn",
        "to_intersection_id": "int-vijayanagar-bus-terminus",
        "length_m": 1850.0,
        "water_depth_cm": 24.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.212,
            12.985
          ],
          [
            80.215,
            12.98
          ],
          [
            80.218,
            12.978
          ]
        ]
      },
      {
        "id": "chn-st-12",
        "name": "Madipakkam Lake Basin Road",
        "from_intersection_id": "int-kaiveli-jn",
        "to_intersection_id": "int-koot-road-madipakkam",
        "length_m": 1600.0,
        "water_depth_cm": 34.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.226,
            12.965
          ],
          [
            80.21,
            12.962
          ],
          [
            80.198,
            12.96
          ]
        ]
      },
      {
        "id": "chn-st-13",
        "name": "Adyar Thiru Vi Ka Bridge Riverbank",
        "from_intersection_id": "int-malar-hospital-jn",
        "to_intersection_id": "int-adyar-signal",
        "length_m": 1500.0,
        "water_depth_cm": 16.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.26,
            13.01
          ],
          [
            80.258,
            13.005
          ],
          [
            80.255,
            13.002
          ]
        ]
      },
      {
        "id": "chn-st-14",
        "name": "Sardar Patel Road / Guindy Highway",
        "from_intersection_id": "int-adyar-signal",
        "to_intersection_id": "int-kathipara-cloverleaf",
        "length_m": 3200.0,
        "water_depth_cm": 5.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.255,
            13.002
          ],
          [
            80.23,
            13.005
          ],
          [
            80.203,
            13.008
          ]
        ]
      },
      {
        "id": "chn-st-15",
        "name": "Kathipara Multi-Level Grade Separator",
        "from_intersection_id": "int-kathipara-rotary",
        "to_intersection_id": "int-airport-gst-flyover-ingress",
        "length_m": 2100.0,
        "water_depth_cm": 1.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.203,
            13.008
          ],
          [
            80.198,
            13.002
          ],
          [
            80.192,
            12.998
          ]
        ]
      },
      {
        "id": "chn-st-16",
        "name": "GST Road (Guindy - Airport Link)",
        "from_intersection_id": "int-kathipara-cloverleaf",
        "to_intersection_id": "int-chennai-airport-main-gate",
        "length_m": 2800.0,
        "water_depth_cm": 9.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.203,
            13.008
          ],
          [
            80.192,
            12.998
          ],
          [
            80.18,
            12.985
          ]
        ]
      },
      {
        "id": "chn-st-17",
        "name": "OMR Elevated IT Expressway (Perungudi)",
        "from_intersection_id": "int-tidel-park-jn",
        "to_intersection_id": "int-thoraipakkam-toll",
        "length_m": 3600.0,
        "water_depth_cm": 2.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.248,
            12.988
          ],
          [
            80.244,
            12.968
          ],
          [
            80.24,
            12.948
          ]
        ]
      },
      {
        "id": "chn-st-18",
        "name": "OMR Lowland Service Road (Sholinganallur)",
        "from_intersection_id": "int-thoraipakkam-toll",
        "to_intersection_id": "int-sholinganallur-elcot-jn",
        "length_m": 3800.0,
        "water_depth_cm": 21.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.24,
            12.948
          ],
          [
            80.235,
            12.925
          ],
          [
            80.228,
            12.9
          ]
        ]
      },
      {
        "id": "chn-st-19",
        "name": "ECR Coastal Highway (Thiruvanmiyur)",
        "from_intersection_id": "int-thiruvanmiyur-signal",
        "to_intersection_id": "int-neelankarai-beach-link",
        "length_m": 3400.0,
        "water_depth_cm": 4.8,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.26,
            12.98
          ],
          [
            80.26,
            12.965
          ],
          [
            80.26,
            12.95
          ]
        ]
      },
      {
        "id": "chn-st-20",
        "name": "Pallikaranai Marshland 200 Feet Radial",
        "from_intersection_id": "int-thoraipakkam-radial-ingress",
        "to_intersection_id": "int-medavakkam-jn",
        "length_m": 3900.0,
        "water_depth_cm": 29.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.235,
            12.94
          ],
          [
            80.215,
            12.935
          ],
          [
            80.195,
            12.93
          ]
        ]
      },
      {
        "id": "chn-st-21",
        "name": "Medavakkam Main Road",
        "from_intersection_id": "int-medavakkam-jn",
        "to_intersection_id": "int-kovilambakkam-lowland",
        "length_m": 2400.0,
        "water_depth_cm": 18.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.195,
            12.93
          ],
          [
            80.185,
            12.94
          ],
          [
            80.175,
            12.95
          ]
        ]
      },
      {
        "id": "chn-st-22",
        "name": "Tambaram GST Highway Corridor",
        "from_intersection_id": "int-chromepet-flyover",
        "to_intersection_id": "int-tambaram-sanatorium-bus-stand",
        "length_m": 3100.0,
        "water_depth_cm": 7.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.145,
            12.95
          ],
          [
            80.135,
            12.938
          ],
          [
            80.125,
            12.925
          ]
        ]
      },
      {
        "id": "chn-st-23",
        "name": "Chennai Central Railway Station Approach",
        "from_intersection_id": "int-central-station-plaza",
        "to_intersection_id": "int-ripon-building-gate",
        "length_m": 1200.0,
        "water_depth_cm": 14.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.275,
            13.082
          ],
          [
            80.272,
            13.08
          ],
          [
            80.27,
            13.078
          ]
        ]
      },
      {
        "id": "chn-st-24",
        "name": "Rajaji Salai / Port Access Corridor",
        "from_intersection_id": "int-central-station-plaza",
        "to_intersection_id": "int-chennai-port-gate-1",
        "length_m": 1800.0,
        "water_depth_cm": 8.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.275,
            13.082
          ],
          [
            80.285,
            13.088
          ],
          [
            80.292,
            13.095
          ]
        ]
      },
      {
        "id": "chn-st-25",
        "name": "Vyasarpadi Jeeva Railway Subway",
        "from_intersection_id": "int-vyasarpadi-station-road",
        "to_intersection_id": "int-gnt-road-link",
        "length_m": 950.0,
        "water_depth_cm": 46.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.26,
            13.105
          ],
          [
            80.263,
            13.107
          ],
          [
            80.265,
            13.11
          ]
        ]
      },
      {
        "id": "chn-st-26",
        "name": "Perambur High Road Underpass Corridor",
        "from_intersection_id": "int-perambur-loco-works",
        "to_intersection_id": "int-perambur-flyover-ramp",
        "length_m": 1750.0,
        "water_depth_cm": 28.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.245,
            13.11
          ],
          [
            80.24,
            13.108
          ],
          [
            80.235,
            13.105
          ]
        ]
      },
      {
        "id": "chn-st-27",
        "name": "Madhavaram GNT Highway NH-16",
        "from_intersection_id": "int-madhavaram-roundabout",
        "to_intersection_id": "int-puzhal-lake-ingress",
        "length_m": 3300.0,
        "water_depth_cm": 6.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.23,
            13.125
          ],
          [
            80.22,
            13.14
          ],
          [
            80.21,
            13.155
          ]
        ]
      },
      {
        "id": "chn-st-28",
        "name": "100 Feet Inner Ring Road (Vadapalani)",
        "from_intersection_id": "int-koyambedu-cmbt-jn",
        "to_intersection_id": "int-vadapalani-signal",
        "length_m": 2600.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.195,
            13.07
          ],
          [
            80.202,
            13.06
          ],
          [
            80.21,
            13.05
          ]
        ]
      },
      {
        "id": "chn-st-29",
        "name": "Koyambedu CMBT Bus Hub Corridor",
        "from_intersection_id": "int-poonamallee-high-rd-jn",
        "to_intersection_id": "int-cmbt-bus-terminal-entrance",
        "length_m": 1900.0,
        "water_depth_cm": 19.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.19,
            13.075
          ],
          [
            80.195,
            13.072
          ],
          [
            80.198,
            13.068
          ]
        ]
      },
      {
        "id": "chn-st-30",
        "name": "Arcot Road Kodambakkam Corridor",
        "from_intersection_id": "int-vadapalani-signal",
        "to_intersection_id": "int-kodambakkam-power-house",
        "length_m": 2100.0,
        "water_depth_cm": 13.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.21,
            13.05
          ],
          [
            80.22,
            13.052
          ],
          [
            80.23,
            13.055
          ]
        ]
      },
      {
        "id": "chn-st-31",
        "name": "Royapuram Bridge Coastal Road",
        "from_intersection_id": "int-royapuram-station",
        "to_intersection_id": "int-kasimedu-fishing-harbour",
        "length_m": 1700.0,
        "water_depth_cm": 9.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.295,
            13.11
          ],
          [
            80.298,
            13.12
          ],
          [
            80.3,
            13.13
          ]
        ]
      },
      {
        "id": "chn-st-32",
        "name": "Thirumangalam Metro - Anna Nagar West",
        "from_intersection_id": "int-thirumangalam-jn",
        "to_intersection_id": "int-anna-nagar-roundabout",
        "length_m": 2200.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            80.19,
            13.085
          ],
          [
            80.205,
            13.085
          ],
          [
            80.215,
            13.085
          ]
        ]
      }
    ],
    {
      "int-war-memorial-circle": [
        80.285,
        13.078
      ],
      "int-light-house-jn": [
        80.28,
        13.038
      ],
      "int-foreshore-estate-bus-stand": [
        80.275,
        13.018
      ],
      "int-gemini-flyover": [
        80.25,
        13.052
      ],
      "int-saidapet-bridge-ingress": [
        80.222,
        13.02
      ],
      "int-cathedral-road-jn": [
        80.252,
        13.055
      ],
      "int-nungambakkam-high-rd-link": [
        80.248,
        13.048
      ],
      "int-panagal-park-circle": [
        80.235,
        13.04
      ],
      "int-vani-mahal-jn": [
        80.245,
        13.045
      ],
      "int-t-nagar-bus-terminus": [
        80.228,
        13.032
      ],
      "int-ranganathan-street-jn": [
        80.235,
        13.044
      ],
      "int-sterling-road-jn": [
        80.24,
        13.065
      ],
      "int-gemini-flyover-link": [
        80.25,
        13.052
      ],
      "int-chetpet-railway-station": [
        80.236,
        13.072
      ],
      "int-harrington-rd-cross": [
        80.24,
        13.068
      ],
      "int-chennai-central-station": [
        80.275,
        13.082
      ],
      "int-kilpauk-medical-college-jn": [
        80.235,
        13.075
      ],
      "int-vijayanagar-bus-terminus": [
        80.218,
        12.978
      ],
      "int-kaiveli-jn": [
        80.226,
        12.965
      ],
      "int-guru-nanak-college-jn": [
        80.212,
        12.985
      ],
      "int-koot-road-madipakkam": [
        80.198,
        12.96
      ],
      "int-malar-hospital-jn": [
        80.26,
        13.01
      ],
      "int-adyar-signal": [
        80.255,
        13.002
      ],
      "int-kathipara-cloverleaf": [
        80.203,
        13.008
      ],
      "int-kathipara-rotary": [
        80.203,
        13.008
      ],
      "int-airport-gst-flyover-ingress": [
        80.192,
        12.998
      ],
      "int-chennai-airport-main-gate": [
        80.18,
        12.985
      ],
      "int-tidel-park-jn": [
        80.248,
        12.988
      ],
      "int-thoraipakkam-toll": [
        80.24,
        12.948
      ],
      "int-sholinganallur-elcot-jn": [
        80.228,
        12.9
      ],
      "int-thiruvanmiyur-signal": [
        80.26,
        12.98
      ],
      "int-neelankarai-beach-link": [
        80.26,
        12.95
      ],
      "int-thoraipakkam-radial-ingress": [
        80.235,
        12.94
      ],
      "int-medavakkam-jn": [
        80.195,
        12.93
      ],
      "int-kovilambakkam-lowland": [
        80.175,
        12.95
      ],
      "int-chromepet-flyover": [
        80.145,
        12.95
      ],
      "int-tambaram-sanatorium-bus-stand": [
        80.125,
        12.925
      ],
      "int-central-station-plaza": [
        80.275,
        13.082
      ],
      "int-ripon-building-gate": [
        80.27,
        13.078
      ],
      "int-chennai-port-gate-1": [
        80.292,
        13.095
      ],
      "int-vyasarpadi-station-road": [
        80.26,
        13.105
      ],
      "int-gnt-road-link": [
        80.265,
        13.11
      ],
      "int-perambur-loco-works": [
        80.245,
        13.11
      ],
      "int-perambur-flyover-ramp": [
        80.235,
        13.105
      ],
      "int-madhavaram-roundabout": [
        80.23,
        13.125
      ],
      "int-puzhal-lake-ingress": [
        80.21,
        13.155
      ],
      "int-koyambedu-cmbt-jn": [
        80.195,
        13.07
      ],
      "int-vadapalani-signal": [
        80.21,
        13.05
      ],
      "int-poonamallee-high-rd-jn": [
        80.19,
        13.075
      ],
      "int-cmbt-bus-terminal-entrance": [
        80.198,
        13.068
      ],
      "int-kodambakkam-power-house": [
        80.23,
        13.055
      ],
      "int-royapuram-station": [
        80.295,
        13.11
      ],
      "int-kasimedu-fishing-harbour": [
        80.3,
        13.13
      ],
      "int-thirumangalam-jn": [
        80.19,
        13.085
      ],
      "int-anna-nagar-roundabout": [
        80.215,
        13.085
      ]
    }
  ],
  "delhi": [
    [
      {
        "id": "del-st-01",
        "name": "Minto Bridge Railway Underpass",
        "from_intersection_id": "int-deen-dayal-upadhyaya-marg",
        "to_intersection_id": "int-connaught-circus-ramp",
        "length_m": 650.0,
        "water_depth_cm": 56.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.228,
            28.634
          ],
          [
            77.23,
            28.636
          ],
          [
            77.232,
            28.638
          ]
        ]
      },
      {
        "id": "del-st-02",
        "name": "Connaught Place Outer Circle",
        "from_intersection_id": "int-barakhamba-road-radial",
        "to_intersection_id": "int-janpath-radial-cross",
        "length_m": 2200.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.218,
            28.632
          ],
          [
            77.222,
            28.635
          ],
          [
            77.225,
            28.63
          ]
        ]
      },
      {
        "id": "del-st-03",
        "name": "Tilak Bridge Railway Underpass",
        "from_intersection_id": "int-bahadur-shah-zafar-marg",
        "to_intersection_id": "int-tilak-marg-cross",
        "length_m": 820.0,
        "water_depth_cm": 42.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.238,
            28.626
          ],
          [
            77.24,
            28.628
          ],
          [
            77.242,
            28.63
          ]
        ]
      },
      {
        "id": "del-st-04",
        "name": "ITO Junction Yamuna Lowland Corridor",
        "from_intersection_id": "int-vikas-minar-jn",
        "to_intersection_id": "int-pragati-maidan-gate",
        "length_m": 1800.0,
        "water_depth_cm": 18.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.242,
            28.628
          ],
          [
            77.246,
            28.625
          ],
          [
            77.249,
            28.621
          ]
        ]
      },
      {
        "id": "del-st-05",
        "name": "Pragati Maidan Integrated Tunnel",
        "from_intersection_id": "int-purana-qila-ramp",
        "to_intersection_id": "int-ring-road-ingress",
        "length_m": 1600.0,
        "water_depth_cm": 32.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.24,
            28.62
          ],
          [
            77.245,
            28.62
          ],
          [
            77.252,
            28.62
          ]
        ]
      },
      {
        "id": "del-st-06",
        "name": "Kartavya Path / Rajpath Boulevard",
        "from_intersection_id": "int-rashtrapati-bhavan",
        "to_intersection_id": "int-india-gate-c-hexagon",
        "length_m": 2600.0,
        "water_depth_cm": 1.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.198,
            28.614
          ],
          [
            77.218,
            28.614
          ],
          [
            77.229,
            28.613
          ]
        ]
      },
      {
        "id": "del-st-07",
        "name": "India Gate C-Hexagon Arterial",
        "from_intersection_id": "int-ashoka-road-ingress",
        "to_intersection_id": "int-shahjahan-road-ingress",
        "length_m": 1800.0,
        "water_depth_cm": 3.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.226,
            28.616
          ],
          [
            77.229,
            28.613
          ],
          [
            77.23,
            28.608
          ]
        ]
      },
      {
        "id": "del-st-08",
        "name": "Barapullah Elevated Corridor",
        "from_intersection_id": "int-sarai-kale-khan-ramp",
        "to_intersection_id": "int-ina-market-terminus",
        "length_m": 3800.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.255,
            28.588
          ],
          [
            77.24,
            28.579
          ],
          [
            77.218,
            28.572
          ]
        ]
      },
      {
        "id": "del-st-09",
        "name": "Ring Road Kashmere Gate ISBT Low Point",
        "from_intersection_id": "int-isbt-bus-ingress",
        "to_intersection_id": "int-monastery-market-jn",
        "length_m": 1950.0,
        "water_depth_cm": 36.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.228,
            28.668
          ],
          [
            77.232,
            28.668
          ],
          [
            77.236,
            28.67
          ]
        ]
      },
      {
        "id": "del-st-10",
        "name": "Yamuna Bazar Lowland River Corridor",
        "from_intersection_id": "int-hanuman-mandir-yamuna",
        "to_intersection_id": "int-salimgarh-fort-link",
        "length_m": 1500.0,
        "water_depth_cm": 48.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.235,
            28.665
          ],
          [
            77.238,
            28.662
          ],
          [
            77.24,
            28.658
          ]
        ]
      },
      {
        "id": "del-st-11",
        "name": "Vikas Marg (Laxmi Nagar - ITO Bridge)",
        "from_intersection_id": "int-laxmi-nagar-metro",
        "to_intersection_id": "int-ito-yamuna-bridge",
        "length_m": 2400.0,
        "water_depth_cm": 14.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.275,
            28.63
          ],
          [
            77.26,
            28.629
          ],
          [
            77.248,
            28.628
          ]
        ]
      },
      {
        "id": "del-st-12",
        "name": "Akshardham NH-9 Highway Corridor",
        "from_intersection_id": "int-akshardham-temple-gate",
        "to_intersection_id": "int-mayur-vihar-flyover",
        "length_m": 3200.0,
        "water_depth_cm": 5.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.28,
            28.615
          ],
          [
            77.288,
            28.608
          ],
          [
            77.295,
            28.6
          ]
        ]
      },
      {
        "id": "del-st-13",
        "name": "DND Flyway Elevated Viaduct",
        "from_intersection_id": "int-maharani-bagh-ramp",
        "to_intersection_id": "int-noida-toll-plaza",
        "length_m": 4200.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.265,
            28.58
          ],
          [
            77.285,
            28.58
          ],
          [
            77.305,
            28.58
          ]
        ]
      },
      {
        "id": "del-st-14",
        "name": "Ashram Chowk Underpass & Ring Road",
        "from_intersection_id": "int-mathura-road-cross",
        "to_intersection_id": "int-lajpat-nagar-ring-link",
        "length_m": 1600.0,
        "water_depth_cm": 28.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.255,
            28.57
          ],
          [
            77.26,
            28.57
          ],
          [
            77.265,
            28.57
          ]
        ]
      },
      {
        "id": "del-st-15",
        "name": "Moolchand Underpass Ring Road",
        "from_intersection_id": "int-moolchand-hospital-jn",
        "to_intersection_id": "int-lajpat-nagar-metro-cross",
        "length_m": 980.0,
        "water_depth_cm": 38.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.232,
            28.568
          ],
          [
            77.23,
            28.565
          ],
          [
            77.228,
            28.562
          ]
        ]
      },
      {
        "id": "del-st-16",
        "name": "AIIMS Flyover Grade Separator",
        "from_intersection_id": "int-aiims-main-gate",
        "to_intersection_id": "int-safdarjung-hospital-jn",
        "length_m": 1900.0,
        "water_depth_cm": 2.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.215,
            28.57
          ],
          [
            77.21,
            28.57
          ],
          [
            77.205,
            28.57
          ]
        ]
      },
      {
        "id": "del-st-17",
        "name": "Dhaula Kuan Multi-tier Interchange",
        "from_intersection_id": "int-dhaula-kuan-metro",
        "to_intersection_id": "int-sardar-patel-marg-ingress",
        "length_m": 2300.0,
        "water_depth_cm": 3.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.165,
            28.595
          ],
          [
            77.17,
            28.598
          ],
          [
            77.175,
            28.602
          ]
        ]
      },
      {
        "id": "del-st-18",
        "name": "Mehrauli-Badarpur Road (MB Road)",
        "from_intersection_id": "int-saket-metro-station",
        "to_intersection_id": "int-khanpur-extension-jn",
        "length_m": 2800.0,
        "water_depth_cm": 19.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.205,
            28.515
          ],
          [
            77.225,
            28.512
          ],
          [
            77.25,
            28.51
          ]
        ]
      },
      {
        "id": "del-st-19",
        "name": "Outer Ring Road (Munirka - IIT Gate)",
        "from_intersection_id": "int-munirka-flyover",
        "to_intersection_id": "int-iit-delhi-main-gate",
        "length_m": 2400.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.17,
            28.555
          ],
          [
            77.185,
            28.55
          ],
          [
            77.195,
            28.545
          ]
        ]
      },
      {
        "id": "del-st-20",
        "name": "Rohtak Road Punjabi Bagh Lowland",
        "from_intersection_id": "int-punjabi-bagh-club",
        "to_intersection_id": "int-zakhira-flyover-ramp",
        "length_m": 2100.0,
        "water_depth_cm": 26.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.125,
            28.665
          ],
          [
            77.135,
            28.665
          ],
          [
            77.145,
            28.665
          ]
        ]
      },
      {
        "id": "del-st-21",
        "name": "Najafgarh Drain Perimeter Road",
        "from_intersection_id": "int-uttam-nagar-east",
        "to_intersection_id": "int-janakpuri-district-centre",
        "length_m": 2600.0,
        "water_depth_cm": 22.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.065,
            28.625
          ],
          [
            77.075,
            28.628
          ],
          [
            77.085,
            28.63
          ]
        ]
      },
      {
        "id": "del-st-22",
        "name": "Noida Expressway (Sector 18 - 62)",
        "from_intersection_id": "int-film-city-flyover",
        "to_intersection_id": "int-sector-62-ingress",
        "length_m": 4500.0,
        "water_depth_cm": 2.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.32,
            28.57
          ],
          [
            77.34,
            28.55
          ],
          [
            77.36,
            28.53
          ]
        ]
      },
      {
        "id": "del-st-23",
        "name": "NH-48 Cyber City Highway Corridor",
        "from_intersection_id": "int-ambience-mall-ingress",
        "to_intersection_id": "int-cyber-hub-underpass-link",
        "length_m": 2800.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.095,
            28.505
          ],
          [
            77.09,
            28.495
          ],
          [
            77.085,
            28.485
          ]
        ]
      },
      {
        "id": "del-st-24",
        "name": "Hero Honda Chowk Low Point (Gurugram)",
        "from_intersection_id": "int-rajiv-chowk-gurugram",
        "to_intersection_id": "int-hero-honda-chowk-flyover",
        "length_m": 2900.0,
        "water_depth_cm": 34.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.045,
            28.46
          ],
          [
            77.03,
            28.45
          ],
          [
            77.015,
            28.44
          ]
        ]
      },
      {
        "id": "del-st-25",
        "name": "Subhash Chowk Sohna Road Corridor",
        "from_intersection_id": "int-subhash-chowk",
        "to_intersection_id": "int-vatika-city-jn",
        "length_m": 2600.0,
        "water_depth_cm": 16.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.04,
            28.435
          ],
          [
            77.045,
            28.42
          ],
          [
            77.05,
            28.405
          ]
        ]
      },
      {
        "id": "del-st-26",
        "name": "Dwarka Expressway Link (Sector 21)",
        "from_intersection_id": "int-dwarka-sector-21-metro",
        "to_intersection_id": "int-bijwasan-rly-bridge",
        "length_m": 3100.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.06,
            28.55
          ],
          [
            77.055,
            28.535
          ],
          [
            77.05,
            28.52
          ]
        ]
      },
      {
        "id": "del-st-27",
        "name": "Civil Lines Boulevard (Ridge Ingress)",
        "from_intersection_id": "int-delhi-university-metro",
        "to_intersection_id": "int-tis-hazari-court-link",
        "length_m": 2300.0,
        "water_depth_cm": 3.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.215,
            28.69
          ],
          [
            77.22,
            28.675
          ],
          [
            77.22,
            28.665
          ]
        ]
      },
      {
        "id": "del-st-28",
        "name": "Majnu Ka Tilla Outer Ring Road",
        "from_intersection_id": "int-wazirabad-bridge-ingress",
        "to_intersection_id": "int-isbt-kashmere-gate",
        "length_m": 2500.0,
        "water_depth_cm": 21.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.23,
            28.705
          ],
          [
            77.228,
            28.685
          ],
          [
            77.228,
            28.668
          ]
        ]
      },
      {
        "id": "del-st-29",
        "name": "Shastri Park G.T. Road Approach",
        "from_intersection_id": "int-kashmere-gate-bridge",
        "to_intersection_id": "int-shastri-park-metro-hub",
        "length_m": 2100.0,
        "water_depth_cm": 15.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.24,
            28.67
          ],
          [
            77.25,
            28.67
          ],
          [
            77.26,
            28.67
          ]
        ]
      },
      {
        "id": "del-st-30",
        "name": "Sarai Kale Khan Ring Road Interchange",
        "from_intersection_id": "int-pragati-maidan-ramp",
        "to_intersection_id": "int-sarai-kale-khan-isbt",
        "length_m": 1950.0,
        "water_depth_cm": 9.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.255,
            28.605
          ],
          [
            77.258,
            28.595
          ],
          [
            77.26,
            28.585
          ]
        ]
      }
    ],
    {
      "int-deen-dayal-upadhyaya-marg": [
        77.228,
        28.634
      ],
      "int-connaught-circus-ramp": [
        77.232,
        28.638
      ],
      "int-barakhamba-road-radial": [
        77.218,
        28.632
      ],
      "int-janpath-radial-cross": [
        77.225,
        28.63
      ],
      "int-bahadur-shah-zafar-marg": [
        77.238,
        28.626
      ],
      "int-tilak-marg-cross": [
        77.242,
        28.63
      ],
      "int-vikas-minar-jn": [
        77.242,
        28.628
      ],
      "int-pragati-maidan-gate": [
        77.249,
        28.621
      ],
      "int-purana-qila-ramp": [
        77.24,
        28.62
      ],
      "int-ring-road-ingress": [
        77.252,
        28.62
      ],
      "int-rashtrapati-bhavan": [
        77.198,
        28.614
      ],
      "int-india-gate-c-hexagon": [
        77.229,
        28.613
      ],
      "int-ashoka-road-ingress": [
        77.226,
        28.616
      ],
      "int-shahjahan-road-ingress": [
        77.23,
        28.608
      ],
      "int-sarai-kale-khan-ramp": [
        77.255,
        28.588
      ],
      "int-ina-market-terminus": [
        77.218,
        28.572
      ],
      "int-isbt-bus-ingress": [
        77.228,
        28.668
      ],
      "int-monastery-market-jn": [
        77.236,
        28.67
      ],
      "int-hanuman-mandir-yamuna": [
        77.235,
        28.665
      ],
      "int-salimgarh-fort-link": [
        77.24,
        28.658
      ],
      "int-laxmi-nagar-metro": [
        77.275,
        28.63
      ],
      "int-ito-yamuna-bridge": [
        77.248,
        28.628
      ],
      "int-akshardham-temple-gate": [
        77.28,
        28.615
      ],
      "int-mayur-vihar-flyover": [
        77.295,
        28.6
      ],
      "int-maharani-bagh-ramp": [
        77.265,
        28.58
      ],
      "int-noida-toll-plaza": [
        77.305,
        28.58
      ],
      "int-mathura-road-cross": [
        77.255,
        28.57
      ],
      "int-lajpat-nagar-ring-link": [
        77.265,
        28.57
      ],
      "int-moolchand-hospital-jn": [
        77.232,
        28.568
      ],
      "int-lajpat-nagar-metro-cross": [
        77.228,
        28.562
      ],
      "int-aiims-main-gate": [
        77.215,
        28.57
      ],
      "int-safdarjung-hospital-jn": [
        77.205,
        28.57
      ],
      "int-dhaula-kuan-metro": [
        77.165,
        28.595
      ],
      "int-sardar-patel-marg-ingress": [
        77.175,
        28.602
      ],
      "int-saket-metro-station": [
        77.205,
        28.515
      ],
      "int-khanpur-extension-jn": [
        77.25,
        28.51
      ],
      "int-munirka-flyover": [
        77.17,
        28.555
      ],
      "int-iit-delhi-main-gate": [
        77.195,
        28.545
      ],
      "int-punjabi-bagh-club": [
        77.125,
        28.665
      ],
      "int-zakhira-flyover-ramp": [
        77.145,
        28.665
      ],
      "int-uttam-nagar-east": [
        77.065,
        28.625
      ],
      "int-janakpuri-district-centre": [
        77.085,
        28.63
      ],
      "int-film-city-flyover": [
        77.32,
        28.57
      ],
      "int-sector-62-ingress": [
        77.36,
        28.53
      ],
      "int-ambience-mall-ingress": [
        77.095,
        28.505
      ],
      "int-cyber-hub-underpass-link": [
        77.085,
        28.485
      ],
      "int-rajiv-chowk-gurugram": [
        77.045,
        28.46
      ],
      "int-hero-honda-chowk-flyover": [
        77.015,
        28.44
      ],
      "int-subhash-chowk": [
        77.04,
        28.435
      ],
      "int-vatika-city-jn": [
        77.05,
        28.405
      ],
      "int-dwarka-sector-21-metro": [
        77.06,
        28.55
      ],
      "int-bijwasan-rly-bridge": [
        77.05,
        28.52
      ],
      "int-delhi-university-metro": [
        77.215,
        28.69
      ],
      "int-tis-hazari-court-link": [
        77.22,
        28.665
      ],
      "int-wazirabad-bridge-ingress": [
        77.23,
        28.705
      ],
      "int-isbt-kashmere-gate": [
        77.228,
        28.668
      ],
      "int-kashmere-gate-bridge": [
        77.24,
        28.67
      ],
      "int-shastri-park-metro-hub": [
        77.26,
        28.67
      ],
      "int-pragati-maidan-ramp": [
        77.255,
        28.605
      ],
      "int-sarai-kale-khan-isbt": [
        77.26,
        28.585
      ]
    }
  ],
  "bengaluru": [
    [
      {
        "id": "blr-st-01",
        "name": "MG Road - Trinity Circle Central Link",
        "from_intersection_id": "int-anil-kumble-circle",
        "to_intersection_id": "int-trinity-metro-station",
        "length_m": 1600.0,
        "water_depth_cm": 3.2,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.608,
            12.975
          ],
          [
            77.616,
            12.973
          ],
          [
            77.624,
            12.972
          ]
        ]
      },
      {
        "id": "blr-st-02",
        "name": "Brigade Road Commercial Promenade",
        "from_intersection_id": "int-mg-road-jn",
        "to_intersection_id": "int-hosur-road-junction",
        "length_m": 1400.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.608,
            12.974
          ],
          [
            77.608,
            12.968
          ],
          [
            77.608,
            12.962
          ]
        ]
      },
      {
        "id": "blr-st-03",
        "name": "Vidhana Soudha / Ambedkar Veedhi",
        "from_intersection_id": "int-gpo-circle",
        "to_intersection_id": "int-high-court-gate",
        "length_m": 1200.0,
        "water_depth_cm": 1.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.592,
            12.982
          ],
          [
            77.59,
            12.979
          ],
          [
            77.588,
            12.976
          ]
        ]
      },
      {
        "id": "blr-st-04",
        "name": "Kempegowda Majestic Bus Stand Ingress",
        "from_intersection_id": "int-majestic-railway-station",
        "to_intersection_id": "int-mysore-bank-circle",
        "length_m": 1500.0,
        "water_depth_cm": 11.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.57,
            12.978
          ],
          [
            77.575,
            12.976
          ],
          [
            77.58,
            12.974
          ]
        ]
      },
      {
        "id": "blr-st-05",
        "name": "Richmond Circle Flyover Grade Separator",
        "from_intersection_id": "int-richmond-road",
        "to_intersection_id": "int-double-road-flyover",
        "length_m": 1300.0,
        "water_depth_cm": 2.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.596,
            12.962
          ],
          [
            77.6,
            12.96
          ],
          [
            77.604,
            12.958
          ]
        ]
      },
      {
        "id": "blr-st-06",
        "name": "Silk Board Junction Underpass",
        "from_intersection_id": "int-hosur-road-ingress",
        "to_intersection_id": "int-madiwala-lake-outfall",
        "length_m": 1200.0,
        "water_depth_cm": 28.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.622,
            12.917
          ],
          [
            77.625,
            12.921
          ],
          [
            77.628,
            12.925
          ]
        ]
      },
      {
        "id": "blr-st-07",
        "name": "Outer Ring Road (Bellandur Ecospace)",
        "from_intersection_id": "int-ecospace-tech-park-gate",
        "to_intersection_id": "int-devarabisanahalli-flyover",
        "length_m": 1950.0,
        "water_depth_cm": 44.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.678,
            12.928
          ],
          [
            77.685,
            12.933
          ],
          [
            77.692,
            12.938
          ]
        ]
      },
      {
        "id": "blr-st-08",
        "name": "ORR Marathahalli Bridge Corridor",
        "from_intersection_id": "int-kalamandir-multiplex",
        "to_intersection_id": "int-marathahalli-multiplex-jn",
        "length_m": 1800.0,
        "water_depth_cm": 16.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.698,
            12.952
          ],
          [
            77.702,
            12.956
          ],
          [
            77.706,
            12.96
          ]
        ]
      },
      {
        "id": "blr-st-09",
        "name": "ORR Kadubeesanahalli Lowland Underpass",
        "from_intersection_id": "int-cisco-ingress-gate",
        "to_intersection_id": "int-panathur-railway-subway-link",
        "length_m": 1400.0,
        "water_depth_cm": 36.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.692,
            12.936
          ],
          [
            77.696,
            12.94
          ],
          [
            77.7,
            12.944
          ]
        ]
      },
      {
        "id": "blr-st-10",
        "name": "Rainbow Drive Layout Ingress (Sarjapur)",
        "from_intersection_id": "int-sarjapur-main-gate",
        "to_intersection_id": "int-wipro-corporate-jn",
        "length_m": 1400.0,
        "water_depth_cm": 52.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.695,
            12.905
          ],
          [
            77.701,
            12.909
          ],
          [
            77.708,
            12.914
          ]
        ]
      },
      {
        "id": "blr-st-11",
        "name": "Sarjapur Main Road / Kaikondrahalli Lake",
        "from_intersection_id": "int-kaikondrahalli-lake-gate",
        "to_intersection_id": "int-carmelaram-station-cross",
        "length_m": 2200.0,
        "water_depth_cm": 24.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.675,
            12.91
          ],
          [
            77.685,
            12.912
          ],
          [
            77.698,
            12.915
          ]
        ]
      },
      {
        "id": "blr-st-12",
        "name": "HSR Layout 27th Main (Sector 6 Lowland)",
        "from_intersection_id": "int-hsr-27th-main---19th-cross",
        "to_intersection_id": "int-agara-lake-outfall-jn",
        "length_m": 1700.0,
        "water_depth_cm": 32.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.64,
            12.912
          ],
          [
            77.645,
            12.915
          ],
          [
            77.65,
            12.918
          ]
        ]
      },
      {
        "id": "blr-st-13",
        "name": "Koramangala 80 Feet Road (Sony World)",
        "from_intersection_id": "int-sony-world-signal",
        "to_intersection_id": "int-koramangala-bda-complex",
        "length_m": 1600.0,
        "water_depth_cm": 21.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.622,
            12.935
          ],
          [
            77.628,
            12.935
          ],
          [
            77.635,
            12.935
          ]
        ]
      },
      {
        "id": "blr-st-14",
        "name": "Koramangala 100 Feet Road (Inner Ring)",
        "from_intersection_id": "int-water-tank-jn",
        "to_intersection_id": "int-domlur-flyover-ramp",
        "length_m": 2800.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.62,
            12.93
          ],
          [
            77.632,
            12.945
          ],
          [
            77.64,
            12.96
          ]
        ]
      },
      {
        "id": "blr-st-15",
        "name": "Indiranagar 100 Feet Road",
        "from_intersection_id": "int-old-airport-road-jn",
        "to_intersection_id": "int-cmh-road-metro-jn",
        "length_m": 2200.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.64,
            12.965
          ],
          [
            77.64,
            12.975
          ],
          [
            77.64,
            12.985
          ]
        ]
      },
      {
        "id": "blr-st-16",
        "name": "Old Airport Road / Wind Tunnel Road",
        "from_intersection_id": "int-manipal-hospital-signal",
        "to_intersection_id": "int-hal-main-gate",
        "length_m": 2600.0,
        "water_depth_cm": 13.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.645,
            12.96
          ],
          [
            77.66,
            12.96
          ],
          [
            77.675,
            12.96
          ]
        ]
      },
      {
        "id": "blr-st-17",
        "name": "Whitefield Main Road / ITPL Corridor",
        "from_intersection_id": "int-hope-farm-circle",
        "to_intersection_id": "int-itpl-main-gate",
        "length_m": 2700.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.755,
            12.985
          ],
          [
            77.75,
            12.975
          ],
          [
            77.745,
            12.965
          ]
        ]
      },
      {
        "id": "blr-st-18",
        "name": "Varthur Kodi Lowland Lake Basin",
        "from_intersection_id": "int-varthur-lake-sluice",
        "to_intersection_id": "int-gunjur-main-road",
        "length_m": 1950.0,
        "water_depth_cm": 41.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.735,
            12.945
          ],
          [
            77.74,
            12.94
          ],
          [
            77.745,
            12.935
          ]
        ]
      },
      {
        "id": "blr-st-19",
        "name": "Hebbal Elevated Expressway Viaduct",
        "from_intersection_id": "int-hebbal-lake-ramp",
        "to_intersection_id": "int-airport-toll-corridor",
        "length_m": 3200.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.591,
            13.035
          ],
          [
            77.595,
            13.048
          ],
          [
            77.6,
            13.06
          ]
        ]
      },
      {
        "id": "blr-st-20",
        "name": "Manyata Tech Park Outer Ring Road",
        "from_intersection_id": "int-hebbal-flyover-east",
        "to_intersection_id": "int-nagawara-lake-jn",
        "length_m": 2800.0,
        "water_depth_cm": 17.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.595,
            13.035
          ],
          [
            77.61,
            13.04
          ],
          [
            77.625,
            13.045
          ]
        ]
      },
      {
        "id": "blr-st-21",
        "name": "Nagawara Junction / Thanisandra Main",
        "from_intersection_id": "int-nagawara-metro-cross",
        "to_intersection_id": "int-thanisandra-railway-bridge",
        "length_m": 2100.0,
        "water_depth_cm": 23.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.625,
            13.045
          ],
          [
            77.63,
            13.055
          ],
          [
            77.632,
            13.065
          ]
        ]
      },
      {
        "id": "blr-st-22",
        "name": "Hennur Main Road Link",
        "from_intersection_id": "int-outer-ring-road-hennur",
        "to_intersection_id": "int-hennur-cross-bus-stop",
        "length_m": 1900.0,
        "water_depth_cm": 9.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.635,
            13.025
          ],
          [
            77.64,
            13.032
          ],
          [
            77.645,
            13.04
          ]
        ]
      },
      {
        "id": "blr-st-23",
        "name": "KR Puram Hanging Bridge & Tin Factory",
        "from_intersection_id": "int-tin-factory-bus-stop",
        "to_intersection_id": "int-kr-puram-cable-bridge",
        "length_m": 1700.0,
        "water_depth_cm": 26.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.675,
            12.995
          ],
          [
            77.685,
            12.998
          ],
          [
            77.695,
            13.0
          ]
        ]
      },
      {
        "id": "blr-st-24",
        "name": "Tumkur Road / Yeshwanthpur Flyover",
        "from_intersection_id": "int-yeshwanthpur-circle",
        "to_intersection_id": "int-goraguntepalya-jn",
        "length_m": 2400.0,
        "water_depth_cm": 4.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.545,
            13.02
          ],
          [
            77.55,
            13.025
          ],
          [
            77.555,
            13.03
          ]
        ]
      },
      {
        "id": "blr-st-25",
        "name": "Rajajinagar 1st Block Chord Road",
        "from_intersection_id": "int-navrang-theatre-signal",
        "to_intersection_id": "int-rajajinagar-metro-station",
        "length_m": 2200.0,
        "water_depth_cm": 3.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.55,
            12.995
          ],
          [
            77.552,
            12.99
          ],
          [
            77.555,
            12.985
          ]
        ]
      },
      {
        "id": "blr-st-26",
        "name": "Mysore Road / Nayandahalli Flyover",
        "from_intersection_id": "int-pes-university-gate",
        "to_intersection_id": "int-nayandahalli-metro-jn",
        "length_m": 2600.0,
        "water_depth_cm": 18.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.53,
            12.945
          ],
          [
            77.535,
            12.948
          ],
          [
            77.54,
            12.952
          ]
        ]
      },
      {
        "id": "blr-st-27",
        "name": "Bannerghatta Road / Dairy Circle",
        "from_intersection_id": "int-dairy-circle-flyover",
        "to_intersection_id": "int-jayadeva-hospital-flyover",
        "length_m": 2300.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.598,
            12.935
          ],
          [
            77.598,
            12.925
          ],
          [
            77.598,
            12.915
          ]
        ]
      },
      {
        "id": "blr-st-28",
        "name": "JP Nagar 24th Main Commercial Ring",
        "from_intersection_id": "int-rv-dental-college-jn",
        "to_intersection_id": "int-sarakki-lake-ingress",
        "length_m": 1950.0,
        "water_depth_cm": 14.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.585,
            12.908
          ],
          [
            77.588,
            12.905
          ],
          [
            77.592,
            12.902
          ]
        ]
      },
      {
        "id": "blr-st-29",
        "name": "BTM Layout 2nd Stage Ring Link",
        "from_intersection_id": "int-udupi-garden-signal",
        "to_intersection_id": "int-silk-board-flyover-ramp",
        "length_m": 1600.0,
        "water_depth_cm": 16.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.61,
            12.915
          ],
          [
            77.616,
            12.916
          ],
          [
            77.622,
            12.917
          ]
        ]
      },
      {
        "id": "blr-st-30",
        "name": "Majestic K.G. Road Commercial Corridor",
        "from_intersection_id": "int-mysore-bank-circle",
        "to_intersection_id": "int-upparpet-police-station",
        "length_m": 1300.0,
        "water_depth_cm": 5.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            77.58,
            12.974
          ],
          [
            77.582,
            12.976
          ],
          [
            77.585,
            12.978
          ]
        ]
      }
    ],
    {
      "int-anil-kumble-circle": [
        77.608,
        12.975
      ],
      "int-trinity-metro-station": [
        77.624,
        12.972
      ],
      "int-mg-road-jn": [
        77.608,
        12.974
      ],
      "int-hosur-road-junction": [
        77.608,
        12.962
      ],
      "int-gpo-circle": [
        77.592,
        12.982
      ],
      "int-high-court-gate": [
        77.588,
        12.976
      ],
      "int-majestic-railway-station": [
        77.57,
        12.978
      ],
      "int-mysore-bank-circle": [
        77.58,
        12.974
      ],
      "int-richmond-road": [
        77.596,
        12.962
      ],
      "int-double-road-flyover": [
        77.604,
        12.958
      ],
      "int-hosur-road-ingress": [
        77.622,
        12.917
      ],
      "int-madiwala-lake-outfall": [
        77.628,
        12.925
      ],
      "int-ecospace-tech-park-gate": [
        77.678,
        12.928
      ],
      "int-devarabisanahalli-flyover": [
        77.692,
        12.938
      ],
      "int-kalamandir-multiplex": [
        77.698,
        12.952
      ],
      "int-marathahalli-multiplex-jn": [
        77.706,
        12.96
      ],
      "int-cisco-ingress-gate": [
        77.692,
        12.936
      ],
      "int-panathur-railway-subway-link": [
        77.7,
        12.944
      ],
      "int-sarjapur-main-gate": [
        77.695,
        12.905
      ],
      "int-wipro-corporate-jn": [
        77.708,
        12.914
      ],
      "int-kaikondrahalli-lake-gate": [
        77.675,
        12.91
      ],
      "int-carmelaram-station-cross": [
        77.698,
        12.915
      ],
      "int-hsr-27th-main---19th-cross": [
        77.64,
        12.912
      ],
      "int-agara-lake-outfall-jn": [
        77.65,
        12.918
      ],
      "int-sony-world-signal": [
        77.622,
        12.935
      ],
      "int-koramangala-bda-complex": [
        77.635,
        12.935
      ],
      "int-water-tank-jn": [
        77.62,
        12.93
      ],
      "int-domlur-flyover-ramp": [
        77.64,
        12.96
      ],
      "int-old-airport-road-jn": [
        77.64,
        12.965
      ],
      "int-cmh-road-metro-jn": [
        77.64,
        12.985
      ],
      "int-manipal-hospital-signal": [
        77.645,
        12.96
      ],
      "int-hal-main-gate": [
        77.675,
        12.96
      ],
      "int-hope-farm-circle": [
        77.755,
        12.985
      ],
      "int-itpl-main-gate": [
        77.745,
        12.965
      ],
      "int-varthur-lake-sluice": [
        77.735,
        12.945
      ],
      "int-gunjur-main-road": [
        77.745,
        12.935
      ],
      "int-hebbal-lake-ramp": [
        77.591,
        13.035
      ],
      "int-airport-toll-corridor": [
        77.6,
        13.06
      ],
      "int-hebbal-flyover-east": [
        77.595,
        13.035
      ],
      "int-nagawara-lake-jn": [
        77.625,
        13.045
      ],
      "int-nagawara-metro-cross": [
        77.625,
        13.045
      ],
      "int-thanisandra-railway-bridge": [
        77.632,
        13.065
      ],
      "int-outer-ring-road-hennur": [
        77.635,
        13.025
      ],
      "int-hennur-cross-bus-stop": [
        77.645,
        13.04
      ],
      "int-tin-factory-bus-stop": [
        77.675,
        12.995
      ],
      "int-kr-puram-cable-bridge": [
        77.695,
        13.0
      ],
      "int-yeshwanthpur-circle": [
        77.545,
        13.02
      ],
      "int-goraguntepalya-jn": [
        77.555,
        13.03
      ],
      "int-navrang-theatre-signal": [
        77.55,
        12.995
      ],
      "int-rajajinagar-metro-station": [
        77.555,
        12.985
      ],
      "int-pes-university-gate": [
        77.53,
        12.945
      ],
      "int-nayandahalli-metro-jn": [
        77.54,
        12.952
      ],
      "int-dairy-circle-flyover": [
        77.598,
        12.935
      ],
      "int-jayadeva-hospital-flyover": [
        77.598,
        12.915
      ],
      "int-rv-dental-college-jn": [
        77.585,
        12.908
      ],
      "int-sarakki-lake-ingress": [
        77.592,
        12.902
      ],
      "int-udupi-garden-signal": [
        77.61,
        12.915
      ],
      "int-silk-board-flyover-ramp": [
        77.622,
        12.917
      ],
      "int-upparpet-police-station": [
        77.585,
        12.978
      ]
    }
  ],
  "kolkata": [
    [
      {
        "id": "kol-st-01",
        "name": "CR Avenue (Central Avenue Lowland Basin)",
        "from_intersection_id": "int-girish-park",
        "to_intersection_id": "int-esplanade-metro-crossing",
        "length_m": 2400.0,
        "water_depth_cm": 36.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.362,
            22.595
          ],
          [
            88.36,
            22.58
          ],
          [
            88.355,
            22.565
          ]
        ]
      },
      {
        "id": "kol-st-02",
        "name": "Park Street / Camac Street Corridor",
        "from_intersection_id": "int-chowringhee-crossing",
        "to_intersection_id": "int-mullick-bazar-jn",
        "length_m": 1800.0,
        "water_depth_cm": 8.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.35,
            22.552
          ],
          [
            88.355,
            22.552
          ],
          [
            88.365,
            22.552
          ]
        ]
      },
      {
        "id": "kol-st-03",
        "name": "Jawaharlal Nehru Road (Chowringhee)",
        "from_intersection_id": "int-esplanade-dharmatala",
        "to_intersection_id": "int-exide-crossing",
        "length_m": 2100.0,
        "water_depth_cm": 6.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.352,
            22.565
          ],
          [
            88.35,
            22.555
          ],
          [
            88.348,
            22.54
          ]
        ]
      },
      {
        "id": "kol-st-04",
        "name": "BBD Bagh / Dalhousie Heritage Square",
        "from_intersection_id": "int-writers-building",
        "to_intersection_id": "int-gpo-circle",
        "length_m": 1300.0,
        "water_depth_cm": 11.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.345,
            22.572
          ],
          [
            88.348,
            22.57
          ],
          [
            88.35,
            22.568
          ]
        ]
      },
      {
        "id": "kol-st-05",
        "name": "Strand Road / Hooghly Riverfront",
        "from_intersection_id": "int-howrah-bridge-approach",
        "to_intersection_id": "int-babu-ghat",
        "length_m": 2200.0,
        "water_depth_cm": 19.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.342,
            22.585
          ],
          [
            88.34,
            22.575
          ],
          [
            88.338,
            22.565
          ]
        ]
      },
      {
        "id": "kol-st-06",
        "name": "MG Road Burrabazar Low Point",
        "from_intersection_id": "int-howrah-bridge-approach",
        "to_intersection_id": "int-sealdah-flyover-link",
        "length_m": 2300.0,
        "water_depth_cm": 31.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.345,
            22.585
          ],
          [
            88.355,
            22.585
          ],
          [
            88.368,
            22.585
          ]
        ]
      },
      {
        "id": "kol-st-07",
        "name": "Sealdah Station Flyover Approach",
        "from_intersection_id": "int-sealdah-main-gate",
        "to_intersection_id": "int-koley-market-low-point",
        "length_m": 1400.0,
        "water_depth_cm": 24.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.372,
            22.568
          ],
          [
            88.374,
            22.566
          ],
          [
            88.376,
            22.564
          ]
        ]
      },
      {
        "id": "kol-st-08",
        "name": "Vidyasagar Setu Toll Plaza Approach",
        "from_intersection_id": "int-ajc-bose-flyover-ingress",
        "to_intersection_id": "int-toll-plaza-ramp",
        "length_m": 2600.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.345,
            22.555
          ],
          [
            88.335,
            22.555
          ],
          [
            88.325,
            22.555
          ]
        ]
      },
      {
        "id": "kol-st-09",
        "name": "Maa Flyover High Viaduct",
        "from_intersection_id": "int-science-city-ramp",
        "to_intersection_id": "int-park-circus-flyover-link",
        "length_m": 4200.0,
        "water_depth_cm": 0.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.398,
            22.54
          ],
          [
            88.385,
            22.541
          ],
          [
            88.37,
            22.542
          ]
        ]
      },
      {
        "id": "kol-st-10",
        "name": "Park Circus 7-Point Crossing",
        "from_intersection_id": "int-ajc-bose-flyover-ramp",
        "to_intersection_id": "int-suhrwardy-avenue",
        "length_m": 1500.0,
        "water_depth_cm": 14.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.368,
            22.542
          ],
          [
            88.372,
            22.544
          ],
          [
            88.376,
            22.546
          ]
        ]
      },
      {
        "id": "kol-st-11",
        "name": "EM Bypass Science City Interchange",
        "from_intersection_id": "int-maa-flyover-ramp",
        "to_intersection_id": "int-ruby-hospital-link",
        "length_m": 2800.0,
        "water_depth_cm": 5.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.398,
            22.54
          ],
          [
            88.4,
            22.53
          ],
          [
            88.402,
            22.518
          ]
        ]
      },
      {
        "id": "kol-st-12",
        "name": "EM Bypass Ruby Hospital Rotary",
        "from_intersection_id": "int-kasba-connector-jn",
        "to_intersection_id": "int-kalikapur-bridge",
        "length_m": 2200.0,
        "water_depth_cm": 12.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.402,
            22.518
          ],
          [
            88.403,
            22.51
          ],
          [
            88.405,
            22.502
          ]
        ]
      },
      {
        "id": "kol-st-13",
        "name": "EM Bypass Chingrighata Flyover & Lowland",
        "from_intersection_id": "int-salt-lake-sector-v-link",
        "to_intersection_id": "int-science-city-link",
        "length_m": 2100.0,
        "water_depth_cm": 22.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.402,
            22.565
          ],
          [
            88.4,
            22.552
          ],
          [
            88.398,
            22.54
          ]
        ]
      },
      {
        "id": "kol-st-14",
        "name": "Ballygunge Circular Road",
        "from_intersection_id": "int-minto-park",
        "to_intersection_id": "int-gariahat-jn",
        "length_m": 2300.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.36,
            22.538
          ],
          [
            88.365,
            22.53
          ],
          [
            88.368,
            22.522
          ]
        ]
      },
      {
        "id": "kol-st-15",
        "name": "Gariahat Junction Commercial Hub",
        "from_intersection_id": "int-gariahat-flyover",
        "to_intersection_id": "int-golpark-circle",
        "length_m": 1600.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.368,
            22.522
          ],
          [
            88.368,
            22.518
          ],
          [
            88.368,
            22.512
          ]
        ]
      },
      {
        "id": "kol-st-16",
        "name": "Rashbehari Avenue / Kalighat Link",
        "from_intersection_id": "int-gariahat-flyover",
        "to_intersection_id": "int-chetla-bridge-ingress",
        "length_m": 2600.0,
        "water_depth_cm": 16.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.368,
            22.518
          ],
          [
            88.355,
            22.518
          ],
          [
            88.342,
            22.518
          ]
        ]
      },
      {
        "id": "kol-st-17",
        "name": "Southern Avenue / Rabindra Sarobar",
        "from_intersection_id": "int-golpark-circle",
        "to_intersection_id": "int-southern-avenue-lake-link",
        "length_m": 1900.0,
        "water_depth_cm": 8.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.368,
            22.512
          ],
          [
            88.36,
            22.51
          ],
          [
            88.352,
            22.508
          ]
        ]
      },
      {
        "id": "kol-st-18",
        "name": "Tollygunge Phari Lowland Basin",
        "from_intersection_id": "int-charu-market",
        "to_intersection_id": "int-tollygunge-tram-depot",
        "length_m": 1800.0,
        "water_depth_cm": 33.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.345,
            22.508
          ],
          [
            88.345,
            22.5
          ],
          [
            88.345,
            22.492
          ]
        ]
      },
      {
        "id": "kol-st-19",
        "name": "Prince Anwar Shah Road",
        "from_intersection_id": "int-lords-bakery-jn",
        "to_intersection_id": "int-south-city-mall-ingress",
        "length_m": 2100.0,
        "water_depth_cm": 11.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.355,
            22.5
          ],
          [
            88.362,
            22.5
          ],
          [
            88.37,
            22.5
          ]
        ]
      },
      {
        "id": "kol-st-20",
        "name": "Taratala Diamond Harbour Highway",
        "from_intersection_id": "int-majerhat-bridge",
        "to_intersection_id": "int-taratala-flyover-jn",
        "length_m": 2400.0,
        "water_depth_cm": 19.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.32,
            22.515
          ],
          [
            88.315,
            22.508
          ],
          [
            88.31,
            22.5
          ]
        ]
      },
      {
        "id": "kol-st-21",
        "name": "Ultadanga Underpass (E.M. Bypass Ingress)",
        "from_intersection_id": "int-hudco-more",
        "to_intersection_id": "int-vip-road-flyover",
        "length_m": 1100.0,
        "water_depth_cm": 41.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.388,
            22.595
          ],
          [
            88.393,
            22.598
          ],
          [
            88.398,
            22.601
          ]
        ]
      },
      {
        "id": "kol-st-22",
        "name": "Shyambazar 5-Point Crossing",
        "from_intersection_id": "int-netaji-statue-circle",
        "to_intersection_id": "int-rg-kar-medical-college-cross",
        "length_m": 1500.0,
        "water_depth_cm": 13.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.37,
            22.602
          ],
          [
            88.375,
            22.602
          ],
          [
            88.38,
            22.602
          ]
        ]
      },
      {
        "id": "kol-st-23",
        "name": "VIP Road (Kankurgachi - Lake Town)",
        "from_intersection_id": "int-ultadanga-flyover",
        "to_intersection_id": "int-lake-town-clock-tower",
        "length_m": 2800.0,
        "water_depth_cm": 7.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.398,
            22.601
          ],
          [
            88.408,
            22.608
          ],
          [
            88.418,
            22.615
          ]
        ]
      },
      {
        "id": "kol-st-24",
        "name": "VIP Road (Baguiati Underpass Low Point)",
        "from_intersection_id": "int-baguiati-subway-ramp",
        "to_intersection_id": "int-joramandir-crossing",
        "length_m": 1600.0,
        "water_depth_cm": 38.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.422,
            22.618
          ],
          [
            88.428,
            22.622
          ],
          [
            88.434,
            22.626
          ]
        ]
      },
      {
        "id": "kol-st-25",
        "name": "VIP Road (Airport Gate 1 No)",
        "from_intersection_id": "int-kaikhali-signal",
        "to_intersection_id": "int-nscb-international-airport-hub",
        "length_m": 3100.0,
        "water_depth_cm": 4.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.44,
            22.635
          ],
          [
            88.445,
            22.645
          ],
          [
            88.448,
            22.655
          ]
        ]
      },
      {
        "id": "kol-st-26",
        "name": "Salt Lake Sector V (Webel / College More)",
        "from_intersection_id": "int-college-more-jn",
        "to_intersection_id": "int-godrej-waterside-tower",
        "length_m": 2200.0,
        "water_depth_cm": 9.0,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.43,
            22.572
          ],
          [
            88.435,
            22.572
          ],
          [
            88.44,
            22.572
          ]
        ]
      },
      {
        "id": "kol-st-27",
        "name": "Salt Lake Karunamoyee Central Bus Hub",
        "from_intersection_id": "int-central-park-gate",
        "to_intersection_id": "int-karunamoyee-metro-station",
        "length_m": 1700.0,
        "water_depth_cm": 6.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.412,
            22.588
          ],
          [
            88.415,
            22.585
          ],
          [
            88.418,
            22.582
          ]
        ]
      },
      {
        "id": "kol-st-28",
        "name": "Salt Lake Broadway Arterial Road",
        "from_intersection_id": "int-ultadanga-flyover-east",
        "to_intersection_id": "int-salt-lake-stadium-gate",
        "length_m": 2400.0,
        "water_depth_cm": 3.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.4,
            22.595
          ],
          [
            88.403,
            22.585
          ],
          [
            88.405,
            22.575
          ]
        ]
      },
      {
        "id": "kol-st-29",
        "name": "New Town Major Arterial Road (MAR-1)",
        "from_intersection_id": "int-new-town-box-bridge",
        "to_intersection_id": "int-biswa-bangla-gate-rotary",
        "length_m": 3600.0,
        "water_depth_cm": 2.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.45,
            22.585
          ],
          [
            88.46,
            22.588
          ],
          [
            88.47,
            22.592
          ]
        ]
      },
      {
        "id": "kol-st-30",
        "name": "Chinar Park / Rajarhat Main Corridor",
        "from_intersection_id": "int-chinar-park-crossing",
        "to_intersection_id": "int-city-centre-2-ingress",
        "length_m": 2300.0,
        "water_depth_cm": 18.5,
        "nearest_node_id": "node-01",
        "coordinates_json": [
          [
            88.445,
            22.625
          ],
          [
            88.452,
            22.628
          ],
          [
            88.46,
            22.632
          ]
        ]
      }
    ],
    {
      "int-girish-park": [
        88.362,
        22.595
      ],
      "int-esplanade-metro-crossing": [
        88.355,
        22.565
      ],
      "int-chowringhee-crossing": [
        88.35,
        22.552
      ],
      "int-mullick-bazar-jn": [
        88.365,
        22.552
      ],
      "int-esplanade-dharmatala": [
        88.352,
        22.565
      ],
      "int-exide-crossing": [
        88.348,
        22.54
      ],
      "int-writers-building": [
        88.345,
        22.572
      ],
      "int-gpo-circle": [
        88.35,
        22.568
      ],
      "int-howrah-bridge-approach": [
        88.345,
        22.585
      ],
      "int-babu-ghat": [
        88.338,
        22.565
      ],
      "int-sealdah-flyover-link": [
        88.368,
        22.585
      ],
      "int-sealdah-main-gate": [
        88.372,
        22.568
      ],
      "int-koley-market-low-point": [
        88.376,
        22.564
      ],
      "int-ajc-bose-flyover-ingress": [
        88.345,
        22.555
      ],
      "int-toll-plaza-ramp": [
        88.325,
        22.555
      ],
      "int-science-city-ramp": [
        88.398,
        22.54
      ],
      "int-park-circus-flyover-link": [
        88.37,
        22.542
      ],
      "int-ajc-bose-flyover-ramp": [
        88.368,
        22.542
      ],
      "int-suhrwardy-avenue": [
        88.376,
        22.546
      ],
      "int-maa-flyover-ramp": [
        88.398,
        22.54
      ],
      "int-ruby-hospital-link": [
        88.402,
        22.518
      ],
      "int-kasba-connector-jn": [
        88.402,
        22.518
      ],
      "int-kalikapur-bridge": [
        88.405,
        22.502
      ],
      "int-salt-lake-sector-v-link": [
        88.402,
        22.565
      ],
      "int-science-city-link": [
        88.398,
        22.54
      ],
      "int-minto-park": [
        88.36,
        22.538
      ],
      "int-gariahat-jn": [
        88.368,
        22.522
      ],
      "int-gariahat-flyover": [
        88.368,
        22.518
      ],
      "int-golpark-circle": [
        88.368,
        22.512
      ],
      "int-chetla-bridge-ingress": [
        88.342,
        22.518
      ],
      "int-southern-avenue-lake-link": [
        88.352,
        22.508
      ],
      "int-charu-market": [
        88.345,
        22.508
      ],
      "int-tollygunge-tram-depot": [
        88.345,
        22.492
      ],
      "int-lords-bakery-jn": [
        88.355,
        22.5
      ],
      "int-south-city-mall-ingress": [
        88.37,
        22.5
      ],
      "int-majerhat-bridge": [
        88.32,
        22.515
      ],
      "int-taratala-flyover-jn": [
        88.31,
        22.5
      ],
      "int-hudco-more": [
        88.388,
        22.595
      ],
      "int-vip-road-flyover": [
        88.398,
        22.601
      ],
      "int-netaji-statue-circle": [
        88.37,
        22.602
      ],
      "int-rg-kar-medical-college-cross": [
        88.38,
        22.602
      ],
      "int-ultadanga-flyover": [
        88.398,
        22.601
      ],
      "int-lake-town-clock-tower": [
        88.418,
        22.615
      ],
      "int-baguiati-subway-ramp": [
        88.422,
        22.618
      ],
      "int-joramandir-crossing": [
        88.434,
        22.626
      ],
      "int-kaikhali-signal": [
        88.44,
        22.635
      ],
      "int-nscb-international-airport-hub": [
        88.448,
        22.655
      ],
      "int-college-more-jn": [
        88.43,
        22.572
      ],
      "int-godrej-waterside-tower": [
        88.44,
        22.572
      ],
      "int-central-park-gate": [
        88.412,
        22.588
      ],
      "int-karunamoyee-metro-station": [
        88.418,
        22.582
      ],
      "int-ultadanga-flyover-east": [
        88.4,
        22.595
      ],
      "int-salt-lake-stadium-gate": [
        88.405,
        22.575
      ],
      "int-new-town-box-bridge": [
        88.45,
        22.585
      ],
      "int-biswa-bangla-gate-rotary": [
        88.47,
        22.592
      ],
      "int-chinar-park-crossing": [
        88.445,
        22.625
      ],
      "int-city-centre-2-ingress": [
        88.46,
        22.632
      ]
    }
  ]
}
