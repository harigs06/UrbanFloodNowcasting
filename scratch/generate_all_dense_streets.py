"""Full multi-city dense street network generator."""

import json
from pathlib import Path

# HYDERABAD (45 connected segments across all zones)
HYD_STREETS = [
    # Hussain Sagar & Central Corridor
    ("hyd-st-01", "Tank Bund Road (Hussain Sagar East)", "Secunderabad / Begumpet", "Sailing Club Jn", "Secretariat Circle", 2100, 22.4, 1.45, 512.1, 4.8, 9.2, True,
     [[17.432, 78.478], [17.426, 78.476], [17.418, 78.474], [17.412, 78.471]]),
    ("hyd-st-02", "Begumpet Airport Nallah Corridor", "Begumpet (Ward 148)", "Prakash Nagar Metro", "Rasoolpura Flyover", 1750, 18.6, 1.82, 508.3, 5.2, 8.7, True,
     [[17.443, 78.468], [17.441, 78.475], [17.438, 78.483]]),
    ("hyd-st-03", "Khairatabad Anand Nagar Subway", "Khairatabad (Ward 96)", "Khairatabad Rly Bridge", "Lakdikapul Jn", 980, 34.2, 2.10, 504.6, 3.1, 7.9, True,
     [[17.411, 78.462], [17.408, 78.464], [17.404, 78.466]]),
    ("hyd-st-04", "Banjara Hills Road No. 12 (Elevated Ridge)", "Banjara Hills (Ward 98)", "Cancer Hospital Jn", "MLA Colony Gate", 1600, 2.1, 0.20, 545.0, 6.5, 2.4, False,
     [[17.415, 78.435], [17.420, 78.441], [17.425, 78.448]]),
    ("hyd-st-05", "Somajiguda Raj Bhavan Road", "Somajiguda (Ward 97)", "Erramanzil Colony", "Raj Bhavan Quarters", 1250, 8.4, 0.75, 516.4, 4.0, 5.1, False,
     [[17.421, 78.452], [17.424, 78.456], [17.426, 78.458]]),
    ("hyd-st-06", "Panjagutta Main Flyover (High Clearance)", "Panjagutta (Ward 100)", "Nagarjuna Circle", "Ameerpet Metro", 1400, 4.2, 0.35, 528.2, 5.8, 3.2, False,
     [[17.425, 78.448], [17.429, 78.451], [17.435, 78.455]]),
    ("hyd-st-07", "Necklace Road (PV Ghat Shoreline)", "Khairatabad Basin", "Sanjeevaiah Park Gate", "Peoples Plaza Ingress", 1850, 28.5, 1.65, 506.0, 3.5, 8.4, True,
     [[17.435, 78.468], [17.430, 78.465], [17.425, 78.463], [17.418, 78.465]]),
    ("hyd-st-08", "Lower Tank Bund Road (Kavadiguda Channel)", "Musheerabad (Ward 87)", "Bible House Jn", "Indira Park Gate", 1650, 16.2, 1.30, 507.5, 4.2, 7.5, True,
     [[17.425, 78.482], [17.420, 78.481], [17.415, 78.480], [17.410, 78.479]]),
    ("hyd-st-09", "Basheerbagh - Liberty Circle Arterial", "Himayatnagar (Ward 83)", "Liberty Circle", "Basheerbagh Flyover", 1100, 3.0, 0.15, 520.0, 5.0, 2.1, False,
     [[17.402, 78.475], [17.405, 78.478], [17.408, 78.482]]),
    ("hyd-st-10", "Himayatnagar Main Road", "Himayatnagar (Ward 84)", "Himayatnagar Y-Jn", "Narayanaguda Flyover", 1300, 6.5, 0.45, 518.0, 4.5, 4.2, False,
     [[17.405, 78.485], [17.402, 78.490], [17.398, 78.494]]),
    ("hyd-st-11", "RTC X Roads - Chikkadpally Corridor", "Chikkadpally (Ward 86)", "RTC X Roads", "Narayanaguda Jn", 1450, 11.2, 0.85, 512.0, 4.0, 6.1, False,
     [[17.408, 78.495], [17.403, 78.496], [17.398, 78.494]]),
    ("hyd-st-12", "Musheerabad - Kavadiguda Link", "Musheerabad (Ward 88)", "Musheerabad Jn", "Kavadiguda Cross Roads", 1200, 13.8, 0.95, 510.5, 3.8, 6.9, False,
     [[17.420, 78.500], [17.416, 78.492], [17.412, 78.485]]),
    
    # Secunderabad & North Corridor
    ("hyd-st-13", "MG Road Secunderabad (Central Commercial)", "Secunderabad (Ward 147)", "Paradise Circle", "Secunderabad Station", 1600, 7.8, 0.55, 522.0, 5.5, 5.0, False,
     [[17.442, 78.487], [17.440, 78.498], [17.437, 78.504]]),
    ("hyd-st-14", "SP Road / Parade Ground Link", "Secunderabad (Ward 146)", "Rasoolpura Jn", "Sangeet Cinema Jn", 1900, 4.0, 0.30, 525.0, 6.0, 3.8, False,
     [[17.441, 78.475], [17.440, 78.485], [17.442, 78.502]]),
    ("hyd-st-15", "Bowenpally National Highway NH-44", "Bowenpally (Ward 131)", "Tadbund Cross Roads", "Bowenpally Checkpost", 2200, 5.5, 0.40, 532.0, 6.5, 4.5, False,
     [[17.458, 78.488], [17.465, 78.486], [17.472, 78.484]]),
    ("hyd-st-16", "Trimulgherry - Alwal Corridor", "Alwal (Ward 133)", "Trimulgherry Cross Roads", "Lothkunta Jn", 2400, 9.2, 0.65, 530.0, 5.0, 5.8, False,
     [[17.475, 78.510], [17.488, 78.512], [17.502, 78.515]]),
    ("hyd-st-17", "Malkajgiri Railway Overbridge Approach", "Malkajgiri (Ward 139)", "Malkajgiri Jn", "Anandbagh Cross Roads", 1700, 14.5, 1.10, 515.0, 4.0, 6.8, False,
     [[17.448, 78.525], [17.452, 78.530], [17.458, 78.538]]),
    ("hyd-st-18", "Tarnaka Flyover & University Link", "Tarnaka (Ward 142)", "Sangeet Jn", "Tarnaka Cross Roads", 2100, 2.5, 0.20, 535.0, 7.0, 2.8, False,
     [[17.438, 78.515], [17.432, 78.525], [17.428, 78.532]]),
    ("hyd-st-19", "Habsiguda - Uppal Ring Road Corridor", "Uppal (Ward 7)", "Tarnaka Cross Roads", "Uppal Ring Road Jn", 2800, 8.0, 0.60, 518.0, 5.5, 5.5, False,
     [[17.428, 78.532], [17.415, 78.545], [17.400, 78.560]]),
    ("hyd-st-20", "Ramanthapur Lake Road Corridor", "Amberpet (Ward 81)", "Uppal Ring Road Jn", "Amberpet Causeway", 2300, 26.0, 1.70, 502.0, 3.5, 9.5, True,
     [[17.400, 78.560], [17.395, 78.535], [17.388, 78.515]]),
    ("hyd-st-21", "Amberpet Causeway & Nallah Crossing", "Amberpet (Ward 82)", "Amberpet Bridge", "Nimboliadda Jn", 1500, 31.0, 1.95, 498.0, 3.2, 10.8, True,
     [[17.388, 78.515], [17.382, 78.502], [17.378, 78.495]]),

    # West Zone / Cyberabad & Hitec City
    ("hyd-st-22", "Hitec City Cyber Towers Flyover", "Madhapur (Ward 107)", "Cyber Gateway", "Cyber Towers Rotary", 1400, 3.5, 0.25, 552.0, 7.5, 2.8, False,
     [[17.452, 78.370], [17.449, 78.375], [17.447, 78.380]]),
    ("hyd-st-23", "Mindspace - Inorbit Mall Arterial", "Madhapur (Ward 106)", "Cyber Towers Rotary", "Inorbit Mall Ingress", 1650, 7.2, 0.50, 546.0, 6.0, 4.8, False,
     [[17.447, 78.380], [17.440, 78.383], [17.435, 78.387]]),
    ("hyd-st-24", "Durgam Cheruvu Cable Bridge Approach", "Jubilee Hills Link", "Inorbit Mall Ingress", "Jubilee Hills Rd 45 Jn", 1800, 2.0, 0.15, 558.0, 8.0, 1.9, False,
     [[17.435, 78.387], [17.432, 78.395], [17.430, 78.405]]),
    ("hyd-st-25", "Road No. 36 Jubilee Hills", "Jubilee Hills (Ward 104)", "Jubilee Hills Rd 45 Jn", "Jubilee Hills Checkpost", 2100, 4.0, 0.30, 560.0, 7.0, 3.0, False,
     [[17.430, 78.405], [17.431, 78.412], [17.430, 78.420]]),
    ("hyd-st-26", "Road No. 10 Banjara Hills Connector", "Banjara Hills (Ward 99)", "Jubilee Hills Checkpost", "Banjara Hills Rd 1 Jn", 1900, 5.0, 0.35, 548.0, 6.5, 3.6, False,
     [[17.430, 78.420], [17.425, 78.435], [17.422, 78.450]]),
    ("hyd-st-27", "Gachibowli Flyover & Bio-Diversity Jn", "Gachibowli (Ward 105)", "Bio-Diversity Park Jn", "Gachibowli Stadium Cross", 2200, 6.0, 0.40, 550.0, 6.8, 4.2, False,
     [[17.440, 78.365], [17.440, 78.355], [17.440, 78.348]]),
    ("hyd-st-28", "Financial District ISB Main Road", "Nanakramguda (Ward 108)", "Gachibowli Stadium Cross", "Wipro Circle Nanakramguda", 2600, 3.2, 0.20, 555.0, 7.5, 2.5, False,
     [[17.440, 78.348], [17.428, 78.345], [17.418, 78.342]]),
    ("hyd-st-29", "Kondapur Main Road / Botanical Garden", "Kondapur (Ward 109)", "Botanical Garden Jn", "Kothaguda Cross Roads", 1750, 8.5, 0.60, 544.0, 5.5, 5.2, False,
     [[17.455, 78.358], [17.460, 78.365], [17.463, 78.372]]),
    ("hyd-st-30", "KPHB Colony Main Road Phase 1", "Kukatpally (Ward 114)", "JNTU Metro Station", "KPHB Phase 1 Rotary", 1900, 13.5, 0.90, 528.0, 4.8, 6.5, False,
     [[17.498, 78.390], [17.493, 78.390], [17.487, 78.392]]),
    ("hyd-st-31", "Kukatpally Y-Junction National Highway", "Kukatpally (Ward 115)", "KPHB Phase 1 Rotary", "Moosapet Metro Jn", 2100, 16.5, 1.25, 518.0, 4.2, 7.8, True,
     [[17.487, 78.392], [17.480, 78.405], [17.472, 78.432]]),
    ("hyd-st-32", "Balanagar Industrial Main Road", "Balanagar (Ward 120)", "Moosapet Metro Jn", "IDPL Colony Cross Roads", 2300, 19.8, 1.40, 514.0, 4.0, 8.5, True,
     [[17.472, 78.432], [17.468, 78.448], [17.465, 78.462]]),

    # South Zone / Musi River & Old City Corridor
    ("hyd-st-33", "Moosarambagh Lowland Causeway", "Malakpet (Ward 24)", "Moosarambagh Bridge", "Amberpet Old Bridge", 1100, 38.0, 2.30, 492.0, 2.8, 13.5, True,
     [[17.375, 78.505], [17.378, 78.508], [17.382, 78.512]]),
    ("hyd-st-34", "Chaderghat Bridge & Musi River Bank", "Chaderghat (Ward 26)", "Chaderghat Rotary", "Rang Mahal Jn", 1350, 29.5, 1.85, 495.0, 3.0, 11.2, True,
     [[17.378, 78.488], [17.375, 78.484], [17.372, 78.480]]),
    ("hyd-st-35", "Malakpet Railway Underpass Corridor", "Malakpet (Ward 25)", "Chaderghat Rotary", "Malakpet Gunj Jn", 1500, 33.5, 2.05, 494.0, 3.1, 12.0, True,
     [[17.378, 78.488], [17.372, 78.492], [17.368, 78.502]]),
    ("hyd-st-36", "Dilsukhnagar Main Commercial Highway", "Dilsukhnagar (Ward 21)", "Malakpet Gunj Jn", "Dilsukhnagar Bus Depot", 2200, 7.5, 0.50, 510.0, 6.0, 5.0, False,
     [[17.368, 78.502], [17.368, 78.515], [17.368, 78.525]]),
    ("hyd-st-37", "LB Nagar Ring Road Multi-tier Jn", "LB Nagar (Ward 11)", "Dilsukhnagar Bus Depot", "LB Nagar Metro Hub", 2600, 4.5, 0.30, 520.0, 7.0, 3.5, False,
     [[17.368, 78.525], [17.360, 78.540], [17.350, 78.550]]),
    ("hyd-st-38", "Nayapul / High Court Musi River Road", "Old City (Ward 53)", "Madina Chowk", "High Court Gate Jn", 1200, 24.5, 1.55, 497.0, 3.4, 9.8, True,
     [[17.367, 78.475], [17.369, 78.473], [17.372, 78.470]]),
    ("hyd-st-39", "Charminar Pedestrian & Heritage Ring", "Charminar (Ward 50)", "Madina Chowk", "Charminar Monument Circle", 1100, 6.0, 0.40, 510.0, 5.2, 4.0, False,
     [[17.365, 78.475], [17.363, 78.474], [17.361, 78.474]]),
    ("hyd-st-40", "Puranapul Bridge & Riverbank Road", "Puranapul (Ward 55)", "City College Cross", "Puranapul Darwaza", 1300, 27.5, 1.75, 496.0, 3.2, 10.5, True,
     [[17.366, 78.468], [17.364, 78.464], [17.364, 78.460]]),
    ("hyd-st-41", "Bahadurpura Zoo Park Corridor", "Bahadurpura (Ward 58)", "Puranapul Darwaza", "Nehru Zoo Park Main Gate", 1800, 11.5, 0.80, 508.0, 4.5, 6.2, False,
     [[17.364, 78.460], [17.358, 78.458], [17.350, 78.455]]),
    ("hyd-st-42", "Falaknuma Palace Hilltop Link", "Falaknuma (Ward 62)", "Falaknuma Rly Station", "Palace Gate Main", 1600, 1.5, 0.10, 548.0, 7.5, 1.8, False,
     [[17.338, 78.465], [17.334, 78.467], [17.330, 78.468]]),
    ("hyd-st-43", "Chandrayangutta Flyover Jn", "Chandrayangutta (Ward 64)", "Falaknuma Rly Station", "Chandrayangutta Cross Roads", 1900, 8.2, 0.55, 515.0, 5.8, 5.2, False,
     [[17.338, 78.465], [17.330, 78.472], [17.320, 78.480]]),
    ("hyd-st-44", "Santoshnagar Main Road Corridor", "Santoshnagar (Ward 44)", "Chandrayangutta Cross Roads", "IS Sadan Cross Roads", 2100, 12.0, 0.85, 518.0, 4.8, 6.5, False,
     [[17.320, 78.480], [17.330, 78.495], [17.340, 78.510]]),
    ("hyd-st-45", "PVNR Elevated Expressway (Airport Bypass)", "Mehdipatnam to Aramghar", "Mehdipatnam Rotary", "Aramghar Jn", 4500, 0.0, 0.0, 560.0, 15.0, 0.5, False,
     [[17.395, 78.440], [17.385, 78.435], [17.375, 78.430], [17.365, 78.425], [17.355, 78.420]]),
]

# MUMBAI (35 segments across Island City, Western & Eastern Suburbs)
MUM_STREETS = [
    # South Mumbai / Coastal
    ("mum-st-01", "Marine Drive Promenade Outer Lane", "Nariman Point (Ward A)", "NCPA Circle", "Churchgate Flyover", 1900, 7.5, 0.5, 5.5, 8.0, 6.5, False,
     [[18.925, 72.822], [18.935, 72.824], [18.945, 72.825]]),
    ("mum-st-02", "Colaba Causeway Main Commercial", "Colaba (Ward A)", "Regal Cinema Circle", "Colaba Post Office", 1600, 5.2, 0.35, 6.2, 7.5, 5.0, False,
     [[18.922, 72.832], [18.918, 72.830], [18.912, 72.826]]),
    ("mum-st-03", "CST / Dr. DN Road Heritage Corridor", "Fort (Ward A)", "CST Station Plaza", "Flora Fountain Circle", 1400, 9.8, 0.70, 7.5, 6.0, 6.2, False,
     [[18.940, 72.835], [18.936, 72.833], [18.932, 72.831]]),
    ("mum-st-04", "JJ Flyover Elevated Viaduct", "Byculla to CST", "JJ Hospital Ingress", "CST Flyover Ramp", 2400, 0.0, 0.0, 18.0, 12.0, 0.8, False,
     [[18.960, 72.838], [18.950, 72.836], [18.942, 72.835]]),
    ("mum-st-05", "Peddar Road / Cumballa Hill Ridge", "Malabar Hill (Ward D)", "Kemps Corner", "Haji Ali Jn", 1800, 2.0, 0.15, 32.0, 8.5, 2.2, False,
     [[18.965, 72.808], [18.972, 72.810], [18.978, 72.812]]),
    ("mum-st-06", "Haji Ali Junction Coastal Lowland", "Worli (Ward G/South)", "Haji Ali Circle", "Lotus Cinema Jn", 1300, 22.5, 1.45, 3.8, 4.0, 10.5, True,
     [[18.978, 72.812], [18.985, 72.814], [18.992, 72.815]]),
    ("mum-st-07", "Worli Seaface Coastal Boulevard", "Worli (Ward G/South)", "Worli Dairy", "Bandra-Worli Sea Link Ingress", 2100, 8.5, 0.60, 5.0, 7.5, 7.2, False,
     [[18.995, 72.815], [19.005, 72.816], [19.015, 72.818]]),
    ("mum-st-08", "Senapati Bapat Marg / Lower Parel", "Lower Parel (Ward G/South)", "Currey Road Jn", "Kamala Mills Gate", 1700, 14.2, 0.95, 6.5, 4.5, 7.8, False,
     [[18.992, 72.830], [18.998, 72.830], [19.006, 72.832]]),

    # Central Hotspots / Lowland Basins
    ("mum-st-09", "Hindmata Cinema TT Circle Low Point", "Parel (Ward F/South)", "Dadar Tram Jn", "Parel TT Circle", 1300, 38.5, 2.10, 3.2, 3.0, 14.5, True,
     [[19.012, 72.842], [19.016, 72.844], [19.020, 72.846]]),
    ("mum-st-10", "Dadar TT Circle Commercial Hub", "Dadar (Ward F/North)", "Khodadad Circle", "Chitra Cinema Jn", 1500, 18.2, 1.20, 5.8, 4.2, 8.5, True,
     [[19.018, 72.844], [19.022, 72.846], [19.025, 72.848]]),
    ("mum-st-11", "King's Circle / Gandhi Market Basin", "Matunga (Ward F/North)", "Maheshwari Udyan", "Sion Hospital Jn", 1600, 42.0, 2.30, 2.8, 2.8, 15.0, True,
     [[19.028, 72.852], [19.032, 72.855], [19.036, 72.858]]),
    ("mum-st-12", "Sion Circle & Highway Junction", "Sion (Ward F/North)", "Sion Hospital Jn", "Sion Fort Cross", 1400, 16.5, 1.10, 5.5, 4.5, 8.2, True,
     [[19.036, 72.858], [19.040, 72.862], [19.044, 72.865]]),
    ("mum-st-13", "Dharavi 90 Feet Road Catchment", "Dharavi (Ward G/North)", "Kala Killa Jn", "Mahim Nature Park Gate", 1900, 28.0, 1.65, 3.5, 3.5, 11.8, True,
     [[19.040, 72.850], [19.043, 72.854], [19.046, 72.858]]),
    ("mum-st-14", "Mahim Causeway Marine Link", "Mahim (Ward G/North)", "Mahim Church Circle", "Bandra Reclamation Ramp", 1600, 6.0, 0.40, 6.2, 7.0, 5.5, False,
     [[19.038, 72.840], [19.044, 72.836], [19.048, 72.830]]),

    # Western Suburbs
    ("mum-st-15", "Bandra-Kurla Complex (BKC) Connector", "Bandra East (Ward H/East)", "Kalanagar Jn", "BKC Bharat Diamond Bourse", 2100, 11.2, 0.85, 6.8, 7.2, 7.9, False,
     [[19.058, 72.852], [19.063, 72.861], [19.068, 72.869]]),
    ("mum-st-16", "BKC Central Avenue Financial Corridor", "BKC (Ward H/East)", "BKC Connector Jn", "MTNL Building Circle", 1800, 4.5, 0.30, 8.2, 8.5, 4.2, False,
     [[19.068, 72.869], [19.065, 72.875], [19.062, 72.880]]),
    ("mum-st-17", "Milan Subway Lowland Crossing", "Santacruz (Ward H/West)", "Santacruz West Station", "Milan Flyover Ingress", 850, 48.0, 2.60, 2.1, 2.5, 16.5, True,
     [[19.085, 72.842], [19.083, 72.845], [19.081, 72.848]]),
    ("mum-st-18", "Khar Subway Lowland Corridor", "Khar (Ward H/West)", "Khar West Market", "Khar East S.V. Link", 780, 44.5, 2.45, 2.3, 2.6, 15.8, True,
     [[19.070, 72.836], [19.070, 72.839], [19.071, 72.842]]),
    ("mum-st-19", "Andheri Subway Critical Underpass", "Andheri (Ward K/West)", "Andheri West Market", "Andheri East Highway Ingress", 920, 52.0, 2.80, 1.8, 2.2, 18.0, True,
     [[19.118, 72.842], [19.118, 72.845], [19.119, 72.848]]),
    ("mum-st-20", "Western Express Highway (Bandra - Airport)", "Santacruz East", "Kalanagar Flyover", "Domestic Airport Flyover", 3400, 3.5, 0.25, 14.0, 10.0, 3.8, False,
     [[19.058, 72.852], [19.075, 72.850], [19.095, 72.852]]),
    ("mum-st-21", "Western Express Highway (Andheri - Goregaon)", "Goregaon (Ward P/South)", "WEH Andheri Metro", "Goregaon Hub Mall Flyover", 3800, 4.0, 0.30, 16.5, 10.5, 4.5, False,
     [[19.118, 72.852], [19.138, 72.855], [19.158, 72.858]]),
    ("mum-st-22", "Western Express Highway (Malad - Borivali)", "Borivali (Ward R/Central)", "Malad Inorbit Link", "Borivali National Park Jn", 4200, 3.0, 0.20, 18.0, 11.0, 3.2, False,
     [[19.180, 72.860], [19.205, 72.862], [19.228, 72.865]]),
    ("mum-st-23", "S.V. Road Bandra to Santacruz", "Bandra (Ward H/West)", "Lucky Restaurant Jn", "Santacruz Station West", 2300, 13.5, 0.90, 6.0, 5.0, 7.5, False,
     [[19.055, 72.835], [19.070, 72.835], [19.085, 72.836]]),
    ("mum-st-24", "Linking Road Shopping Corridor", "Khar (Ward H/West)", "Waterfield Road Jn", "Santacruz Linking Road Jn", 1900, 8.0, 0.55, 7.2, 6.5, 5.8, False,
     [[19.060, 72.832], [19.072, 72.833], [19.082, 72.834]]),
    ("mum-st-25", "JVLR (Jogeshwari-Vikhroli Link Road)", "Jogeshwari East", "WEH Jogeshwari Jn", "SEEPZ Tech Corridor", 3100, 7.0, 0.45, 15.0, 8.5, 6.0, False,
     [[19.135, 72.855], [19.130, 72.870], [19.125, 72.885]]),

    # Eastern Suburbs & Freeways
    ("mum-st-26", "Eastern Freeway High Viaduct", "Chembur to South Bombay", "Bhakti Park Ramp", "Wadala Gate", 3500, 0.0, 0.0, 18.5, 10.0, 1.2, False,
     [[19.030, 72.880], [19.015, 72.875], [18.995, 72.865]]),
    ("mum-st-27", "Kurla LBS Marg Mithi River Lowland", "Kurla (Ward L)", "Kurla Kalpana Cinema", "Kurla Bus Depot Jn", 1800, 36.0, 2.15, 3.0, 3.2, 13.8, True,
     [[19.065, 72.875], [19.068, 72.878], [19.072, 72.882]]),
    ("mum-st-28", "SCLR (Santacruz-Chembur Link Road)", "Kurla East", "BKC Connector East", "Amar Mahal Jn", 2800, 6.5, 0.45, 14.5, 8.0, 5.5, False,
     [[19.068, 72.869], [19.072, 72.880], [19.065, 72.895]]),
    ("mum-st-29", "Eastern Express Highway (Sion - Ghatkopar)", "Ghatkopar (Ward N)", "Priyadarshini Circle", "Ghatkopar Pant Nagar Jn", 3600, 4.5, 0.30, 12.0, 9.5, 4.5, False,
     [[19.045, 72.870], [19.065, 72.890], [19.085, 72.910]]),
    ("mum-st-30", "Eastern Express Highway (Vikhroli - Mulund)", "Bhandup / Mulund", "Vikhroli Godrej Flyover", "Mulund Toll Naka", 4500, 3.8, 0.25, 14.0, 10.0, 4.0, False,
     [[19.110, 72.925], [19.145, 72.940], [19.175, 72.955]]),
    ("mum-st-31", "Chembur Naka Commercial Corridor", "Chembur (Ward M/West)", "Diamond Garden", "Chembur Railway Station Jn", 1600, 9.5, 0.65, 8.5, 6.0, 6.2, False,
     [[19.055, 72.895], [19.058, 72.900], [19.062, 72.905]]),
    ("mum-st-32", "Ghatkopar Andheri Link Road (GALR)", "Ghatkopar (Ward N)", "Asalpha Metro Station", "Ghatkopar Station West", 2200, 14.8, 1.05, 7.0, 4.8, 7.5, False,
     [[19.102, 72.892], [19.095, 72.902], [19.088, 72.910]]),
    ("mum-st-33", "Bhandup LBS Marg Low Point", "Bhandup (Ward S)", "Bhandup Station West", "Kanjurmarg Nallah Crossing", 1750, 24.5, 1.60, 4.5, 3.8, 10.2, True,
     [[19.145, 72.930], [19.148, 72.935], [19.152, 72.938]]),
    ("mum-st-34", "Chunabhatti Sion-Trombay Link", "Chunabhatti (Ward L)", "Chunabhatti Flyover Ramp", "Kurla Priyadarshini Link", 1500, 21.0, 1.40, 4.0, 4.0, 9.2, True,
     [[19.048, 72.872], [19.052, 72.876], [19.056, 72.880]]),
    ("mum-st-35", "Sion-Panvel Highway Deonar Corridor", "Deonar (Ward M/East)", "Mankhurd Flyover Jn", "Vashi Creek Bridge Ingress", 3200, 5.0, 0.35, 9.5, 8.0, 5.0, False,
     [[19.048, 72.915], [19.040, 72.935], [19.035, 72.955]]),
]

# CHENNAI (32 segments)
CHN_STREETS = [
    # Coastal & Central
    ("chn-st-01", "Kamarajar Salai (Marina Beach Road)", "Mylapore (Zone 9)", "War Memorial Circle", "Light House Jn", 2800, 5.0, 0.35, 4.5, 8.0, 5.5, False,
     [[13.078, 80.285], [13.055, 80.282], [13.038, 80.280]]),
    ("chn-st-02", "Santhome High Road Coastal Corridor", "Mylapore (Zone 9)", "Light House Jn", "Foreshore Estate Bus Stand", 1900, 7.5, 0.50, 4.2, 7.5, 6.2, False,
     [[13.038, 80.280], [13.028, 80.278], [13.018, 80.275]]),
    ("chn-st-03", "Anna Salai (Mount Road Central)", "Teynampet (Zone 9)", "Gemini Flyover", "Saidapet Bridge Ingress", 3100, 6.2, 0.40, 9.5, 8.5, 5.8, False,
     [[13.052, 80.250], [13.035, 80.235], [13.020, 80.222]]),
    ("chn-st-04", "Gemini / Anna Flyover (High Clearance)", "Teynampet (Zone 9)", "Cathedral Road Jn", "Nungambakkam High Rd Link", 1600, 1.5, 0.10, 16.0, 10.0, 1.8, False,
     [[13.055, 80.252], [13.052, 80.250], [13.048, 80.248]]),
    ("chn-st-05", "T. Nagar G.N. Chetty Road Commercial", "T. Nagar (Zone 10)", "Panagal Park Circle", "Vani Mahal Jn", 1500, 12.5, 0.85, 7.8, 5.2, 7.0, False,
     [[13.040, 80.235], [13.042, 80.240], [13.045, 80.245]]),
    ("chn-st-06", "Usman Road Flyover & Lowland Approach", "T. Nagar (Zone 10)", "T. Nagar Bus Terminus", "Ranganathan Street Jn", 1700, 18.5, 1.25, 6.5, 4.5, 8.5, True,
     [[13.032, 80.228], [13.038, 80.232], [13.044, 80.235]]),
    ("chn-st-07", "Nungambakkam High Road Corridor", "Nungambakkam (Zone 9)", "Sterling Road Jn", "Gemini Flyover Link", 1900, 8.0, 0.55, 8.5, 6.5, 6.0, False,
     [[13.065, 80.240], [13.058, 80.245], [13.052, 80.250]]),
    ("chn-st-08", "Chetpet / Harrington Road Subway", "Chetpet (Zone 8)", "Chetpet Railway Station", "Harrington Rd Cross", 1100, 32.0, 2.05, 3.8, 3.2, 11.5, True,
     [[13.072, 80.236], [13.070, 80.238], [13.068, 80.240]]),
    ("chn-st-09", "Poonamallee High Road (EVR Periyar)", "Kilpauk (Zone 8)", "Chennai Central Station", "Kilpauk Medical College Jn", 2900, 11.0, 0.75, 7.5, 6.0, 7.2, False,
     [[13.082, 80.275], [13.078, 78.255], [13.075, 80.235]]),

    # South Zone / IT Corridor & Lakes
    ("chn-st-10", "Velachery Main Road (Lake Marsh Corridor)", "Velachery (Zone 13)", "Vijayanagar Bus Terminus", "Kaiveli Jn", 2200, 38.5, 2.30, 4.2, 3.5, 13.5, True,
     [[12.978, 80.218], [12.971, 80.222], [12.965, 80.226]]),
    ("chn-st-11", "Velachery Bypass Road Corridor", "Velachery (Zone 13)", "Guru Nanak College Jn", "Vijayanagar Bus Terminus", 1850, 24.0, 1.55, 5.0, 4.2, 9.8, True,
     [[12.985, 80.212], [12.980, 80.215], [12.978, 80.218]]),
    ("chn-st-12", "Madipakkam Lake Basin Road", "Madipakkam (Zone 14)", "Kaiveli Jn", "Koot Road Madipakkam", 1600, 34.0, 2.10, 3.8, 3.0, 12.2, True,
     [[12.965, 80.226], [12.962, 80.210], [12.960, 80.198]]),
    ("chn-st-13", "Adyar Thiru Vi Ka Bridge Riverbank", "Adyar (Zone 13)", "Malar Hospital Jn", "Adyar Signal", 1500, 16.5, 1.10, 5.2, 5.0, 8.5, True,
     [[13.010, 80.260], [13.005, 80.258], [13.002, 80.255]]),
    ("chn-st-14", "Sardar Patel Road / Guindy Highway", "Guindy (Zone 9)", "Adyar Signal", "Kathipara Cloverleaf", 3200, 5.5, 0.40, 12.0, 8.5, 5.2, False,
     [[13.002, 80.255], [13.005, 80.230], [13.008, 80.203]]),
    ("chn-st-15", "Kathipara Multi-Level Grade Separator", "Guindy (Zone 9)", "Kathipara Rotary", "Airport GST Flyover Ingress", 2100, 1.0, 0.05, 22.0, 12.0, 1.5, False,
     [[13.008, 80.203], [13.002, 80.198], [12.998, 80.192]]),
    ("chn-st-16", "GST Road (Guindy - Airport Link)", "Guindy / Meenambakkam", "Kathipara Cloverleaf", "Chennai Airport Main Gate", 2800, 9.5, 0.70, 11.4, 8.5, 8.0, False,
     [[13.008, 80.203], [12.998, 80.192], [12.985, 80.180]]),
    ("chn-st-17", "OMR Elevated IT Expressway (Perungudi)", "Perungudi (Zone 14)", "Tidel Park Jn", "Thoraipakkam Toll", 3600, 2.2, 0.10, 14.5, 12.0, 3.5, False,
     [[12.988, 80.248], [12.968, 80.244], [12.948, 80.240]]),
    ("chn-st-18", "OMR Lowland Service Road (Sholinganallur)", "Sholinganallur (Zone 15)", "Thoraipakkam Toll", "Sholinganallur ELCOT Jn", 3800, 21.5, 1.40, 4.8, 5.0, 10.2, True,
     [[12.948, 80.240], [12.925, 80.235], [12.900, 80.228]]),
    ("chn-st-19", "ECR Coastal Highway (Thiruvanmiyur)", "Thiruvanmiyur (Zone 13)", "Thiruvanmiyur Signal", "Neelankarai Beach Link", 3400, 4.8, 0.30, 8.5, 8.0, 5.0, False,
     [[12.980, 80.260], [12.965, 80.260], [12.950, 80.260]]),
    ("chn-st-20", "Pallikaranai Marshland 200 Feet Radial", "Pallikaranai (Zone 14)", "Thoraipakkam Radial Ingress", "Medavakkam Jn", 3900, 29.5, 1.80, 3.5, 4.0, 12.5, True,
     [[12.940, 80.235], [12.935, 80.215], [12.930, 80.195]]),
    ("chn-st-21", "Medavakkam Main Road", "Medavakkam (Zone 14)", "Medavakkam Jn", "Kovilambakkam Lowland", 2400, 18.0, 1.15, 6.0, 4.8, 8.0, True,
     [[12.930, 80.195], [12.940, 80.185], [12.950, 80.175]]),
    ("chn-st-22", "Tambaram GST Highway Corridor", "Tambaram (Zone 15)", "Chromepet Flyover", "Tambaram Sanatorium Bus Stand", 3100, 7.0, 0.45, 15.0, 8.5, 6.2, False,
     [[12.950, 80.145], [12.938, 80.135], [12.925, 80.125]]),

    # North & West Zone
    ("chn-st-23", "Chennai Central Railway Station Approach", "Park Town (Zone 5)", "Central Station Plaza", "Ripon Building Gate", 1200, 14.5, 0.95, 6.2, 5.0, 7.5, False,
     [[13.082, 80.275], [13.080, 80.272], [13.078, 80.270]]),
    ("chn-st-24", "Rajaji Salai / Port Access Corridor", "George Town (Zone 5)", "Central Station Plaza", "Chennai Port Gate 1", 1800, 8.0, 0.55, 5.5, 6.5, 6.0, False,
     [[13.082, 80.275], [13.088, 80.285], [13.095, 80.292]]),
    ("chn-st-25", "Vyasarpadi Jeeva Railway Subway", "Vyasarpadi (Zone 4)", "Vyasarpadi Station Road", "GNT Road Link", 950, 46.0, 2.50, 2.2, 2.5, 15.5, True,
     [[13.105, 80.260], [13.107, 80.263], [13.110, 80.265]]),
    ("chn-st-26", "Perambur High Road Underpass Corridor", "Perambur (Zone 4)", "Perambur Loco Works", "Perambur Flyover Ramp", 1750, 28.5, 1.70, 4.0, 3.8, 11.0, True,
     [[13.110, 80.245], [13.108, 80.240], [13.105, 80.235]]),
    ("chn-st-27", "Madhavaram GNT Highway NH-16", "Madhavaram (Zone 3)", "Madhavaram Roundabout", "Puzhal Lake Ingress", 3300, 6.5, 0.40, 14.0, 8.5, 5.8, False,
     [[13.125, 80.230], [13.140, 80.220], [13.155, 80.210]]),
    ("chn-st-28", "100 Feet Inner Ring Road (Vadapalani)", "Vadapalani (Zone 10)", "Koyambedu CMBT Jn", "Vadapalani Signal", 2600, 8.5, 0.60, 9.2, 7.5, 6.5, False,
     [[13.070, 80.195], [13.060, 80.202], [13.050, 80.210]]),
    ("chn-st-29", "Koyambedu CMBT Bus Hub Corridor", "Koyambedu (Zone 7)", "Poonamallee High Rd Jn", "CMBT Bus Terminal Entrance", 1900, 19.5, 1.30, 6.0, 4.5, 9.2, True,
     [[13.075, 80.190], [13.072, 80.195], [13.068, 80.198]]),
    ("chn-st-30", "Arcot Road Kodambakkam Corridor", "Kodambakkam (Zone 10)", "Vadapalani Signal", "Kodambakkam Power House", 2100, 13.5, 0.90, 7.5, 5.5, 7.2, False,
     [[13.050, 80.210], [13.052, 80.220], [13.055, 80.230]]),
    ("chn-st-31", "Royapuram Bridge Coastal Road", "Royapuram (Zone 5)", "Royapuram Station", "Kasimedu Fishing Harbour", 1700, 9.0, 0.60, 5.8, 6.5, 6.5, False,
     [[13.110, 80.295], [13.120, 80.298], [13.130, 80.300]]),
    ("chn-st-32", "Thirumangalam Metro - Anna Nagar West", "Anna Nagar (Zone 8)", "Thirumangalam Jn", "Anna Nagar Roundabout", 2200, 4.0, 0.25, 15.5, 8.5, 4.0, False,
     [[13.085, 80.190], [13.085, 80.205], [13.085, 80.215]]),
]

# DELHI NCR (30 segments)
DEL_STREETS = [
    # Central & NDMC
    ("del-st-01", "Minto Bridge Railway Underpass", "Connaught Place (Ward 78)", "Deen Dayal Upadhyaya Marg", "Connaught Circus Ramp", 650, 56.0, 2.50, 208.5, 3.0, 14.0, True,
     [[28.634, 77.228], [28.636, 77.230], [28.638, 77.232]]),
    ("del-st-02", "Connaught Place Outer Circle", "Connaught Place (Ward 78)", "Barakhamba Road Radial", "Janpath Radial Cross", 2200, 8.5, 0.60, 216.0, 7.0, 6.0, False,
     [[28.632, 77.218], [28.635, 77.222], [28.630, 77.225]]),
    ("del-st-03", "Tilak Bridge Railway Underpass", "ITO (Ward 80)", "Bahadur Shah Zafar Marg", "Tilak Marg Cross", 820, 42.0, 2.20, 209.0, 3.2, 12.5, True,
     [[28.626, 77.238], [28.628, 77.240], [28.630, 77.242]]),
    ("del-st-04", "ITO Junction Yamuna Lowland Corridor", "IP Estate (Ward 80)", "Vikas Minar Jn", "Pragati Maidan Gate", 1800, 18.5, 1.25, 211.0, 6.5, 8.8, True,
     [[28.628, 77.242], [28.625, 77.246], [28.621, 77.249]]),
    ("del-st-05", "Pragati Maidan Integrated Tunnel", "Central Delhi Tunnel", "Purana Qila Ramp", "Ring Road Ingress", 1600, 32.0, 1.85, 206.0, 4.0, 11.0, True,
     [[28.620, 77.240], [28.620, 77.245], [28.620, 77.252]]),
    ("del-st-06", "Kartavya Path / Rajpath Boulevard", "New Delhi (NDMC)", "Rashtrapati Bhavan", "India Gate C-Hexagon", 2600, 1.5, 0.10, 222.0, 10.0, 2.0, False,
     [[28.614, 77.198], [28.614, 77.218], [28.613, 77.229]]),
    ("del-st-07", "India Gate C-Hexagon Arterial", "New Delhi (NDMC)", "Ashoka Road Ingress", "Shahjahan Road Ingress", 1800, 3.0, 0.20, 220.0, 9.0, 3.2, False,
     [[28.616, 77.226], [28.613, 77.229], [28.608, 77.230]]),
    ("del-st-08", "Barapullah Elevated Corridor", "South Delhi Expressway", "Sarai Kale Khan Ramp", "INA Market Terminus", 3800, 0.0, 0.0, 228.0, 10.0, 1.0, False,
     [[28.588, 77.255], [28.579, 77.240], [28.572, 77.218]]),

    # Ring Road & Yamuna Floodplain
    ("del-st-09", "Ring Road Kashmere Gate ISBT Low Point", "Kashmere Gate (Ward 72)", "ISBT Bus Ingress", "Monastery Market Jn", 1950, 36.5, 2.10, 207.0, 4.2, 13.0, True,
     [[28.668, 77.228], [28.668, 77.232], [28.670, 77.236]]),
    ("del-st-10", "Yamuna Bazar Lowland River Corridor", "Old Delhi (Ward 74)", "Hanuman Mandir Yamuna", "Salimgarh Fort Link", 1500, 48.0, 2.45, 205.5, 2.8, 15.2, True,
     [[28.665, 77.235], [28.662, 77.238], [28.658, 77.240]]),
    ("del-st-11", "Vikas Marg (Laxmi Nagar - ITO Bridge)", "East Delhi (Ward 90)", "Laxmi Nagar Metro", "ITO Yamuna Bridge", 2400, 14.0, 0.95, 212.0, 6.0, 7.5, False,
     [[28.630, 77.275], [28.629, 77.260], [28.628, 77.248]]),
    ("del-st-12", "Akshardham NH-9 Highway Corridor", "East Delhi (Ward 92)", "Akshardham Temple Gate", "Mayur Vihar Flyover", 3200, 5.0, 0.35, 215.0, 8.5, 5.2, False,
     [[28.615, 77.280], [28.608, 77.288], [28.600, 77.295]]),
    ("del-st-13", "DND Flyway Elevated Viaduct", "Delhi-Noida Link", "Maharani Bagh Ramp", "Noida Toll Plaza", 4200, 0.0, 0.0, 225.0, 14.0, 0.8, False,
     [[28.580, 77.265], [28.580, 77.285], [28.580, 77.305]]),
    ("del-st-14", "Ashram Chowk Underpass & Ring Road", "Ashram (Ward 62)", "Mathura Road Cross", "Lajpat Nagar Ring Link", 1600, 28.5, 1.70, 210.0, 4.5, 10.5, True,
     [[28.570, 77.255], [28.570, 77.260], [28.570, 77.265]]),
    ("del-st-15", "Moolchand Underpass Ring Road", "Lajpat Nagar (Ward 60)", "Moolchand Hospital Jn", "Lajpat Nagar Metro Cross", 980, 38.0, 2.15, 209.5, 3.5, 12.8, True,
     [[28.568, 77.232], [28.565, 77.230], [28.562, 77.228]]),
    ("del-st-16", "AIIMS Flyover Grade Separator", "South Delhi (Ward 58)", "AIIMS Main Gate", "Safdarjung Hospital Jn", 1900, 2.5, 0.15, 226.0, 9.0, 2.8, False,
     [[28.570, 77.215], [28.570, 77.210], [28.570, 77.205]]),
    ("del-st-17", "Dhaula Kuan Multi-tier Interchange", "South West Delhi", "Dhaula Kuan Metro", "Sardar Patel Marg Ingress", 2300, 3.5, 0.20, 235.0, 10.0, 3.5, False,
     [[28.595, 77.165], [28.598, 77.170], [28.602, 77.175]]),

    # South, West & NCR Links
    ("del-st-18", "Mehrauli-Badarpur Road (MB Road)", "Saket (Ward 52)", "Saket Metro Station", "Khanpur Extension Jn", 2800, 19.5, 1.25, 215.0, 5.0, 9.0, True,
     [[28.515, 77.205], [28.512, 77.225], [28.510, 77.250]]),
    ("del-st-19", "Outer Ring Road (Munirka - IIT Gate)", "Hauz Khas (Ward 55)", "Munirka Flyover", "IIT Delhi Main Gate", 2400, 4.0, 0.25, 230.0, 8.5, 4.2, False,
     [[28.555, 77.170], [28.550, 77.185], [28.545, 77.195]]),
    ("del-st-20", "Rohtak Road Punjabi Bagh Lowland", "Punjabi Bagh (Ward 35)", "Punjabi Bagh Club", "Zakhira Flyover Ramp", 2100, 26.5, 1.65, 210.0, 4.0, 10.5, True,
     [[28.665, 77.125], [28.665, 77.135], [28.665, 77.145]]),
    ("del-st-21", "Najafgarh Drain Perimeter Road", "West Delhi (Ward 40)", "Uttam Nagar East", "Janakpuri District Centre", 2600, 22.0, 1.45, 212.0, 4.8, 9.5, True,
     [[28.625, 77.065], [28.628, 77.075], [28.630, 77.085]]),
    ("del-st-22", "Noida Expressway (Sector 18 - 62)", "Noida Expressway", "Film City Flyover", "Sector 62 Ingress", 4500, 2.0, 0.15, 218.0, 12.0, 2.5, False,
     [[28.570, 77.320], [28.550, 77.340], [28.530, 77.360]]),
    ("del-st-23", "NH-48 Cyber City Highway Corridor", "Gurugram / DLF", "Ambience Mall Ingress", "Cyber Hub Underpass Link", 2800, 6.0, 0.40, 225.0, 9.0, 5.5, False,
     [[28.505, 77.095], [28.495, 77.090], [28.485, 77.085]]),
    ("del-st-24", "Hero Honda Chowk Low Point (Gurugram)", "Gurugram NH-48", "Rajiv Chowk Gurugram", "Hero Honda Chowk Flyover", 2900, 34.5, 2.10, 214.0, 4.0, 13.5, True,
     [[28.460, 77.045], [28.450, 77.030], [28.440, 77.015]]),
    ("del-st-25", "Subhash Chowk Sohna Road Corridor", "Gurugram Central", "Subhash Chowk", "Vatika City Jn", 2600, 16.0, 1.10, 218.0, 5.5, 8.0, True,
     [[28.435, 77.040], [28.420, 77.045], [28.405, 77.050]]),
    ("del-st-26", "Dwarka Expressway Link (Sector 21)", "Dwarka (Ward 48)", "Dwarka Sector 21 Metro", "Bijwasan Rly Bridge", 3100, 4.5, 0.30, 222.0, 8.5, 4.5, False,
     [[28.550, 77.060], [28.535, 77.055], [28.520, 77.050]]),
    ("del-st-27", "Civil Lines Boulevard (Ridge Ingress)", "Civil Lines (Ward 70)", "Delhi University Metro", "Tis Hazari Court Link", 2300, 3.0, 0.20, 232.0, 8.0, 3.0, False,
     [[28.690, 77.215], [28.675, 77.220], [28.665, 77.220]]),
    ("del-st-28", "Majnu Ka Tilla Outer Ring Road", "Civil Lines (Ward 70)", "Wazirabad Bridge Ingress", "ISBT Kashmere Gate", 2500, 21.5, 1.40, 208.0, 5.0, 10.0, True,
     [[28.705, 77.230], [28.685, 77.228], [28.668, 77.228]]),
    ("del-st-29", "Shastri Park G.T. Road Approach", "North East Delhi", "Kashmere Gate Bridge", "Shastri Park Metro Hub", 2100, 15.5, 1.05, 210.0, 5.5, 7.8, True,
     [[28.670, 77.240], [28.670, 77.250], [28.670, 77.260]]),
    ("del-st-30", "Sarai Kale Khan Ring Road Interchange", "South East Delhi", "Pragati Maidan Ramp", "Sarai Kale Khan ISBT", 1950, 9.5, 0.65, 214.0, 7.0, 6.5, False,
     [[28.605, 77.255], [28.595, 77.258], [28.585, 77.260]]),
]

# BENGALURU (30 segments)
BLR_STREETS = [
    # Central & CBD
    ("blr-st-01", "MG Road - Trinity Circle Central Link", "Shantala Nagar (Ward 111)", "Anil Kumble Circle", "Trinity Metro Station", 1600, 3.2, 0.20, 915.0, 7.0, 2.8, False,
     [[12.975, 77.608], [12.973, 77.616], [12.972, 77.624]]),
    ("blr-st-02", "Brigade Road Commercial Promenade", "Shantala Nagar (Ward 111)", "MG Road Jn", "Hosur Road Junction", 1400, 4.5, 0.30, 912.0, 6.5, 3.5, False,
     [[12.974, 77.608], [12.968, 77.608], [12.962, 77.608]]),
    ("blr-st-03", "Vidhana Soudha / Ambedkar Veedhi", "Shivajinagar (Ward 110)", "GPO Circle", "High Court Gate", 1200, 1.5, 0.10, 924.0, 8.5, 1.5, False,
     [[12.982, 77.592], [12.979, 77.590], [12.976, 77.588]]),
    ("blr-st-04", "Kempegowda Majestic Bus Stand Ingress", "Chickpet (Ward 109)", "Majestic Railway Station", "Mysore Bank Circle", 1500, 11.5, 0.80, 905.0, 5.5, 6.5, False,
     [[12.978, 77.570], [12.976, 77.575], [12.974, 77.580]]),
    ("blr-st-05", "Richmond Circle Flyover Grade Separator", "Sampangiram Nagar", "Richmond Road", "Double Road Flyover", 1300, 2.0, 0.15, 918.0, 8.0, 2.2, False,
     [[12.962, 77.596], [12.960, 77.600], [12.958, 77.604]]),

    # Tech Corridors & Lake Basins
    ("blr-st-06", "Silk Board Junction Underpass", "BTM Layout (Ward 176)", "Hosur Road Ingress", "Madiwala Lake Outfall", 1200, 28.5, 1.75, 878.0, 5.5, 11.8, True,
     [[12.917, 77.622], [12.921, 77.625], [12.925, 77.628]]),
    ("blr-st-07", "Outer Ring Road (Bellandur Ecospace)", "Bellandur (Ward 150)", "Ecospace Tech Park Gate", "Devarabisanahalli Flyover", 1950, 44.5, 2.40, 865.2, 4.5, 15.0, True,
     [[12.928, 77.678], [12.933, 77.685], [12.938, 77.692]]),
    ("blr-st-08", "ORR Marathahalli Bridge Corridor", "Marathahalli (Ward 85)", "Kalamandir Multiplex", "Marathahalli Multiplex Jn", 1800, 16.5, 1.10, 872.0, 6.0, 8.5, True,
     [[12.952, 77.698], [12.956, 77.702], [12.960, 77.706]]),
    ("blr-st-09", "ORR Kadubeesanahalli Lowland Underpass", "Kadubeesanahalli", "Cisco Ingress Gate", "Panathur Railway Subway Link", 1400, 36.0, 2.10, 864.0, 3.8, 13.0, True,
     [[12.936, 77.692], [12.940, 77.696], [12.944, 77.700]]),
    ("blr-st-10", "Rainbow Drive Layout Ingress (Sarjapur)", "Sarjapur Road", "Sarjapur Main Gate", "Wipro Corporate Jn", 1400, 52.0, 2.80, 860.5, 3.2, 16.5, True,
     [[12.905, 77.695], [12.909, 77.701], [12.914, 77.708]]),
    ("blr-st-11", "Sarjapur Main Road / Kaikondrahalli Lake", "Bellandur (Ward 150)", "Kaikondrahalli Lake Gate", "Carmelaram Station Cross", 2200, 24.5, 1.55, 868.0, 5.0, 10.2, True,
     [[12.910, 77.675], [12.912, 77.685], [12.915, 77.698]]),
    ("blr-st-12", "HSR Layout 27th Main (Sector 6 Lowland)", "HSR Layout (Ward 174)", "HSR 27th Main / 19th Cross", "Agara Lake Outfall Jn", 1700, 32.5, 1.95, 870.0, 4.0, 12.0, True,
     [[12.912, 77.640], [12.915, 77.645], [12.918, 77.650]]),
    ("blr-st-13", "Koramangala 80 Feet Road (Sony World)", "Koramangala (Ward 151)", "Sony World Signal", "Koramangala BDA Complex", 1600, 21.0, 1.35, 876.0, 4.8, 9.5, True,
     [[12.935, 77.622], [12.935, 77.628], [12.935, 77.635]]),
    ("blr-st-14", "Koramangala 100 Feet Road (Inner Ring)", "Koramangala (Ward 151)", "Water Tank Jn", "Domlur Flyover Ramp", 2800, 8.5, 0.60, 885.0, 7.5, 6.5, False,
     [[12.930, 77.620], [12.945, 77.632], [12.960, 77.640]]),
    ("blr-st-15", "Indiranagar 100 Feet Road", "Indiranagar (Ward 80)", "Old Airport Road Jn", "CMH Road Metro Jn", 2200, 4.5, 0.30, 905.0, 8.0, 4.5, False,
     [[12.965, 77.640], [12.975, 77.640], [12.985, 77.640]]),
    ("blr-st-16", "Old Airport Road / Wind Tunnel Road", "HAL Airport Area", "Manipal Hospital Signal", "HAL Main Gate", 2600, 13.5, 0.90, 888.0, 6.0, 7.5, False,
     [[12.960, 77.645], [12.960, 77.660], [12.960, 77.675]]),
    ("blr-st-17", "Whitefield Main Road / ITPL Corridor", "Whitefield (Ward 84)", "Hope Farm Circle", "ITPL Main Gate", 2700, 6.0, 0.40, 895.0, 7.5, 5.5, False,
     [[12.985, 77.755], [12.975, 77.750], [12.965, 77.745]]),
    ("blr-st-18", "Varthur Kodi Lowland Lake Basin", "Varthur (Ward 149)", "Varthur Lake Sluice", "Gunjur Main Road", 1950, 41.0, 2.25, 855.0, 3.5, 14.2, True,
     [[12.945, 77.735], [12.940, 77.740], [12.935, 77.745]]),

    # North, West & South
    ("blr-st-19", "Hebbal Elevated Expressway Viaduct", "Hebbal (Ward 21)", "Hebbal Lake Ramp", "Airport Toll Corridor", 3200, 0.0, 0.0, 920.0, 10.0, 1.5, False,
     [[13.035, 77.591], [13.048, 77.595], [13.060, 77.600]]),
    ("blr-st-20", "Manyata Tech Park Outer Ring Road", "Nagawara (Ward 23)", "Hebbal Flyover East", "Nagawara Lake Jn", 2800, 17.5, 1.15, 888.0, 6.5, 8.8, True,
     [[13.035, 77.595], [13.040, 77.610], [13.045, 77.625]]),
    ("blr-st-21", "Nagawara Junction / Thanisandra Main", "Nagawara (Ward 23)", "Nagawara Metro Cross", "Thanisandra Railway Bridge", 2100, 23.0, 1.45, 882.0, 5.0, 9.8, True,
     [[13.045, 77.625], [13.055, 77.630], [13.065, 77.632]]),
    ("blr-st-22", "Hennur Main Road Link", "Hennur (Ward 24)", "Outer Ring Road Hennur", "Hennur Cross Bus Stop", 1900, 9.0, 0.60, 895.0, 6.5, 6.0, False,
     [[13.025, 77.635], [13.032, 77.640], [13.040, 77.645]]),
    ("blr-st-23", "KR Puram Hanging Bridge & Tin Factory", "KR Puram (Ward 52)", "Tin Factory Bus Stop", "KR Puram Cable Bridge", 1700, 26.0, 1.65, 872.0, 5.2, 11.0, True,
     [[12.995, 77.675], [12.998, 77.685], [13.000, 77.695]]),
    ("blr-st-24", "Tumkur Road / Yeshwanthpur Flyover", "Yeshwanthpur (Ward 37)", "Yeshwanthpur Circle", "Goraguntepalya Jn", 2400, 4.0, 0.25, 915.0, 9.0, 4.0, False,
     [[13.020, 77.545], [13.025, 77.550], [13.030, 77.555]]),
    ("blr-st-25", "Rajajinagar 1st Block Chord Road", "Rajajinagar (Ward 98)", "Navrang Theatre Signal", "Rajajinagar Metro Station", 2200, 3.5, 0.20, 922.0, 8.0, 3.5, False,
     [[12.995, 77.550], [12.990, 77.552], [12.985, 77.555]]),
    ("blr-st-26", "Mysore Road / Nayandahalli Flyover", "Nayandahalli (Ward 131)", "PES University Gate", "Nayandahalli Metro Jn", 2600, 18.0, 1.20, 880.0, 6.0, 8.8, True,
     [[12.945, 77.530], [12.948, 77.535], [12.952, 77.540]]),
    ("blr-st-27", "Bannerghatta Road / Dairy Circle", "BTM Layout (Ward 176)", "Dairy Circle Flyover", "Jayadeva Hospital Flyover", 2300, 7.5, 0.50, 905.0, 7.0, 5.8, False,
     [[12.935, 77.598], [12.925, 77.598], [12.915, 77.598]]),
    ("blr-st-28", "JP Nagar 24th Main Commercial Ring", "JP Nagar (Ward 177)", "RV Dental College Jn", "Sarakki Lake Ingress", 1950, 14.5, 0.95, 892.0, 5.5, 7.5, False,
     [[12.908, 77.585], [12.905, 77.588], [12.902, 77.592]]),
    ("blr-st-29", "BTM Layout 2nd Stage Ring Link", "BTM Layout (Ward 176)", "Udupi Garden Signal", "Silk Board Flyover Ramp", 1600, 16.0, 1.05, 882.0, 5.2, 8.2, True,
     [[12.915, 77.610], [12.916, 77.616], [12.917, 77.622]]),
    ("blr-st-30", "Majestic K.G. Road Commercial Corridor", "Gandhinagar (Ward 94)", "Mysore Bank Circle", "Upparpet Police Station", 1300, 5.5, 0.35, 915.0, 7.0, 4.5, False,
     [[12.974, 77.580], [12.976, 77.582], [12.978, 77.585]]),
]

# KOLKATA (30 segments)
KOL_STREETS = [
    # Central & Riverfront
    ("kol-st-01", "CR Avenue (Central Avenue Lowland Basin)", "Bowbazar (Ward 44)", "Girish Park", "Esplanade Metro Crossing", 2400, 36.5, 2.05, 4.2, 4.0, 13.5, True,
     [[28.595, 88.362], [22.580, 88.360], [22.565, 88.355]]),
    ("kol-st-02", "Park Street / Camac Street Corridor", "Park Street (Ward 63)", "Chowringhee Crossing", "Mullick Bazar Jn", 1800, 8.5, 0.55, 6.8, 6.5, 6.0, False,
     [[22.552, 88.350], [22.552, 88.355], [22.552, 88.365]]),
    ("kol-st-03", "Jawaharlal Nehru Road (Chowringhee)", "New Market (Ward 46)", "Esplanade Dharmatala", "Exide Crossing", 2100, 6.0, 0.40, 7.2, 7.5, 5.2, False,
     [[22.565, 88.352], [22.555, 88.350], [22.540, 88.348]]),
    ("kol-st-04", "BBD Bagh / Dalhousie Heritage Square", "BBD Bagh (Ward 45)", "Writers Building", "GPO Circle", 1300, 11.5, 0.75, 5.8, 5.8, 6.8, False,
     [[22.572, 88.345], [22.570, 88.348], [22.568, 88.350]]),
    ("kol-st-05", "Strand Road / Hooghly Riverfront", "Riverfront Corridor", "Howrah Bridge Approach", "Babu Ghat", 2200, 19.5, 1.25, 4.0, 5.0, 9.5, True,
     [[22.585, 88.342], [22.575, 88.340], [22.565, 88.338]]),
    ("kol-st-06", "MG Road Burrabazar Low Point", "Burrabazar (Ward 42)", "Howrah Bridge Approach", "Sealdah Flyover Link", 2300, 31.0, 1.85, 4.5, 4.2, 12.0, True,
     [[22.585, 88.345], [22.585, 88.355], [22.585, 88.368]]),
    ("kol-st-07", "Sealdah Station Flyover Approach", "Sealdah (Ward 49)", "Sealdah Main Gate", "Koley Market Low Point", 1400, 24.5, 1.55, 4.8, 4.5, 10.5, True,
     [[22.568, 88.372], [22.566, 88.374], [22.564, 88.376]]),
    ("kol-st-08", "Vidyasagar Setu Toll Plaza Approach", "Hastings (Ward 75)", "AJC Bose Flyover Ingress", "Toll Plaza Ramp", 2600, 0.0, 0.0, 22.0, 14.0, 0.8, False,
     [[22.555, 88.345], [22.555, 88.335], [22.555, 88.325]]),

    # East & South Zone
    ("kol-st-09", "Maa Flyover High Viaduct", "Central Kolkata Corridor", "Science City Ramp", "Park Circus Flyover Link", 4200, 0.0, 0.0, 19.5, 12.0, 0.8, False,
     [[22.540, 88.398], [22.541, 88.385], [22.542, 88.370]]),
    ("kol-st-10", "Park Circus 7-Point Crossing", "Ballygunge (Ward 64)", "AJC Bose Flyover Ramp", "Suhrwardy Avenue", 1500, 14.0, 0.70, 6.2, 5.5, 7.2, False,
     [[22.542, 88.368], [22.544, 88.372], [22.546, 88.376]]),
    ("kol-st-11", "EM Bypass Science City Interchange", "Topsia (Ward 58)", "Maa Flyover Ramp", "Ruby Hospital Link", 2800, 5.5, 0.35, 7.5, 8.5, 5.0, False,
     [[22.540, 88.398], [22.530, 88.400], [22.518, 88.402]]),
    ("kol-st-12", "EM Bypass Ruby Hospital Rotary", "Kasba (Ward 107)", "Kasba Connector Jn", "Kalikapur Bridge", 2200, 12.5, 0.80, 6.5, 7.0, 7.5, False,
     [[22.518, 88.402], [22.510, 88.403], [22.502, 88.405]]),
    ("kol-st-13", "EM Bypass Chingrighata Flyover & Lowland", "Beliaghata (Ward 57)", "Salt Lake Sector V Link", "Science City Link", 2100, 22.0, 1.40, 5.0, 6.0, 9.8, True,
     [[22.565, 88.402], [22.552, 88.400], [22.540, 88.398]]),
    ("kol-st-14", "Ballygunge Circular Road", "Ballygunge (Ward 69)", "Minto Park", "Gariahat Jn", 2300, 4.5, 0.30, 8.5, 8.0, 4.2, False,
     [[22.538, 88.360], [22.530, 88.365], [22.522, 88.368]]),
    ("kol-st-15", "Gariahat Junction Commercial Hub", "Ballygunge (Ward 68)", "Gariahat Flyover", "Golpark Circle", 1600, 7.5, 0.50, 7.8, 6.8, 5.8, False,
     [[22.522, 88.368], [22.518, 88.368], [22.512, 88.368]]),
    ("kol-st-16", "Rashbehari Avenue / Kalighat Link", "Kalighat (Ward 83)", "Gariahat Flyover", "Chetla Bridge Ingress", 2600, 16.5, 1.10, 5.5, 5.5, 8.5, True,
     [[22.518, 88.368], [22.518, 88.355], [22.518, 88.342]]),
    ("kol-st-17", "Southern Avenue / Rabindra Sarobar", "Dhakuria (Ward 90)", "Golpark Circle", "Southern Avenue Lake Link", 1900, 8.0, 0.55, 6.5, 6.5, 6.2, False,
     [[22.512, 88.368], [22.510, 88.360], [22.508, 88.352]]),
    ("kol-st-18", "Tollygunge Phari Lowland Basin", "Tollygunge (Ward 88)", "Charu Market", "Tollygunge Tram Depot", 1800, 33.5, 2.10, 3.8, 3.5, 13.0, True,
     [[22.508, 88.345], [22.500, 88.345], [22.492, 88.345]]),
    ("kol-st-19", "Prince Anwar Shah Road", "Jadavpur (Ward 93)", "Lords Bakery Jn", "South City Mall Ingress", 2100, 11.0, 0.75, 7.0, 6.0, 7.0, False,
     [[22.500, 88.355], [22.500, 88.362], [22.500, 88.370]]),
    ("kol-st-20", "Taratala Diamond Harbour Highway", "Behala (Ward 118)", "Majerhat Bridge", "Taratala Flyover Jn", 2400, 19.5, 1.30, 5.2, 5.2, 9.2, True,
     [[22.515, 88.320], [22.508, 88.315], [22.500, 88.310]]),

    # North & Salt Lake / New Town
    ("kol-st-21", "Ultadanga Underpass (E.M. Bypass Ingress)", "Ultadanga (Ward 14)", "Hudco More", "VIP Road Flyover", 1100, 41.5, 1.90, 4.8, 3.8, 11.5, True,
     [[22.595, 88.388], [22.598, 88.393], [22.601, 88.398]]),
    ("kol-st-22", "Shyambazar 5-Point Crossing", "Shyambazar (Ward 10)", "Netaji Statue Circle", "RG Kar Medical College Cross", 1500, 13.5, 0.85, 6.5, 5.5, 7.5, False,
     [[22.602, 88.370], [22.602, 88.375], [22.602, 88.380]]),
    ("kol-st-23", "VIP Road (Kankurgachi - Lake Town)", "Lake Town (Ward 29)", "Ultadanga Flyover", "Lake Town Clock Tower", 2800, 7.5, 0.50, 7.2, 8.0, 6.0, False,
     [[22.601, 88.398], [22.608, 88.408], [22.615, 88.418]]),
    ("kol-st-24", "VIP Road (Baguiati Underpass Low Point)", "Baguiati (Ward 18)", "Baguiati Subway Ramp", "Joramandir Crossing", 1600, 38.0, 2.25, 4.0, 4.0, 12.8, True,
     [[22.618, 88.422], [22.622, 88.428], [22.626, 88.434]]),
    ("kol-st-25", "VIP Road (Airport Gate 1 No)", "Dum Dum (Airport Zone)", "Kaikhali Signal", "NSCB International Airport Hub", 3100, 4.5, 0.30, 8.5, 9.5, 4.8, False,
     [[22.635, 88.440], [22.645, 88.445], [22.655, 88.448]]),
    ("kol-st-26", "Salt Lake Sector V (Webel / College More)", "Bidhannagar (Sector V)", "College More Jn", "Godrej Waterside Tower", 2200, 9.0, 0.60, 6.2, 7.5, 6.5, False,
     [[22.572, 88.430], [22.572, 88.435], [22.572, 88.440]]),
    ("kol-st-27", "Salt Lake Karunamoyee Central Bus Hub", "Bidhannagar (Central)", "Central Park Gate", "Karunamoyee Metro Station", 1700, 6.5, 0.45, 7.5, 7.0, 5.5, False,
     [[22.588, 88.412], [22.585, 88.415], [22.582, 88.418]]),
    ("kol-st-28", "Salt Lake Broadway Arterial Road", "Bidhannagar (West)", "Ultadanga Flyover East", "Salt Lake Stadium Gate", 2400, 3.5, 0.20, 8.5, 8.5, 3.8, False,
     [[22.595, 88.400], [22.585, 88.403], [22.575, 88.405]]),
    ("kol-st-29", "New Town Major Arterial Road (MAR-1)", "New Town (Action Area 1)", "New Town Box Bridge", "Biswa Bangla Gate Rotary", 3600, 2.5, 0.15, 9.0, 11.0, 3.2, False,
     [[22.585, 88.450], [22.588, 88.460], [22.592, 88.470]]),
    ("kol-st-30", "Chinar Park / Rajarhat Main Corridor", "Rajarhat (Ward 12)", "Chinar Park Crossing", "City Centre 2 Ingress", 2300, 18.5, 1.20, 5.5, 5.5, 8.8, True,
     [[22.625, 88.445], [22.628, 88.452], [22.632, 88.460]]),
]

def format_street_ts(street_tuple):
    sid, name, ward, f_int, t_int, l_m, d_cm, vel, elev, cap, inf, blk, coords = street_tuple
    risk = "impassable" if d_cm >= 15 else "caution" if d_cm >= 5 else "safe"
    coords_str = ",\n      ".join(f"[{lat:.5f}, {lon:.5f}]" for lat, lon in coords)
    
    return f"""  {{
    id: '{sid}',
    name: '{name}',
    ward: '{ward}',
    fromIntersection: '{f_int}',
    toIntersection: '{t_int}',
    lengthM: {l_m},
    waterDepthCm: {d_cm},
    riskLevel: '{risk}',
    flowVelocityMs: {vel},
    elevationM: {elev},
    drainageCapacityM3s: {cap},
    runoffInflowM3s: {inf},
    blocked: {str(blk).lower()},
    coordinates: [
      {coords_str}
    ]
  }}"""

TRAILING_TS = """export const DRAINAGE_NODES_HYD: DrainageNode[] = [
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
"""

ts_lines = [
    "import { CityConfig, StreetSegment, DrainageNode, DrainageConduit, HistoricalStormScenario, AlertNotification } from '../types';",
    "",
    """export const CITIES: CityConfig[] = [
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
];""",
    "",
    "// Dense City-Wide Street Network for Hyderabad (45 Segments)",
    "export const HYDERABAD_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in HYD_STREETS),
    "];",
    "",
    "// Dense City-Wide Street Network for Mumbai (35 Segments)",
    "export const MUMBAI_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in MUM_STREETS),
    "];",
    "",
    "// Dense City-Wide Street Network for Chennai (32 Segments)",
    "export const CHENNAI_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in CHN_STREETS),
    "];",
    "",
    "// Dense City-Wide Street Network for Delhi NCR (30 Segments)",
    "export const DELHI_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in DEL_STREETS),
    "];",
    "",
    "// Dense City-Wide Street Network for Bengaluru (30 Segments)",
    "export const BENGALURU_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in BLR_STREETS),
    "];",
    "",
    "// Dense City-Wide Street Network for Kolkata (30 Segments)",
    "export const KOLKATA_STREETS: StreetSegment[] = [",
    ",\n".join(format_street_ts(s) for s in KOL_STREETS),
    "];",
    "",
    TRAILING_TS
]

orig_path = Path("frontend/src/data/mockData.ts")
final_ts = "\n".join(ts_lines)
with open(orig_path, "w", encoding="utf-8") as f:
    f.write(final_ts)

print(f"Successfully generated clean mockData.ts with {len(final_ts)} characters!")

