import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TVS Two-Wheeler Catalog",
    page_icon="🏍️",
    layout="wide"
)

# Catalog database with exact models from your inventory list
inventory_catalog = {
    "Apache RTR 160 2V Disc": {
        "category": "Motorcycle",
        "engine": "159.7 cc, Single Cylinder, 4-Stroke",
        "power": "16.04 PS @ 8400 rpm",
        "torque": "13.85 Nm @ 7000 rpm",
        "mileage": "45 - 50 kmpl",
        "braking": "Single Disc (Front), Drum (Rear)",
        "abs": "Single-Channel ABS",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "12 Litres",
        "colors": ["Glossy Black", "Matte Blue", "Tornado Black", "Pearl White", "Racing Red"]
    },
    "Apache RTR 160 2V Disc BT": {
        "category": "Motorcycle",
        "engine": "159.7 cc, Single Cylinder, 4-Stroke",
        "power": "16.04 PS @ 8400 rpm",
        "torque": "13.85 Nm @ 7000 rpm",
        "mileage": "45 - 50 kmpl",
        "braking": "Single Disc (Front), Drum (Rear)",
        "abs": "Single-Channel ABS",
        "connectivity": "Yes (SmartXonnect with Turn-by-Turn Navigation)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "12 Litres",
        "colors": ["Matte Blue", "Glossy Black", "Pearl White"]
    },
    "Apache RTR 160 2V Disc BT Race Edition": {
        "category": "Motorcycle",
        "engine": "159.7 cc, Single Cylinder, 4-Stroke",
        "power": "16.04 PS @ 8400 rpm",
        "torque": "13.85 Nm @ 7000 rpm",
        "mileage": "45 - 50 kmpl",
        "braking": "Single Disc (Front), Drum (Rear)",
        "abs": "Single-Channel ABS",
        "connectivity": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "12 Litres",
        "colors": ["Matte Black (Race Edition Graphics)"]
    },
    "Apache RTR 160 4V Disc": {
        "category": "Motorcycle",
        "engine": "159.7 cc, 4-Valve, Oil-Cooled",
        "power": "17.55 PS @ 9250 rpm",
        "torque": "14.73 Nm @ 7250 rpm",
        "mileage": "40 - 45 kmpl",
        "braking": "Disc (Front), Disc (Rear)",
        "abs": "Single-Channel ABS",
        "connectivity": "Optional / Variant Dependent",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "12 Litres",
        "colors": ["Knight Black", "Lightning Blue", "Matte Black", "Racing Red"]
    },
    "Apache RTR 160 4V Disc LE Special Edition": {
        "category": "Motorcycle",
        "engine": "159.7 cc, 4-Valve, Oil-Cooled",
        "power": "17.55 PS @ 9250 rpm",
        "torque": "14.73 Nm @ 7250 rpm",
        "mileage": "40 - 45 kmpl",
        "braking": "Disc (Front), Disc (Rear)",
        "abs": "Single-Channel ABS",
        "connectivity": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "12 Litres",
        "colors": ["Lightning Blue (Special Edition Graphics)"]
    },
    "Raider Drum 125": {
        "category": "Motorcycle",
        "engine": "124.8 cc, 3-Valve, Air-Oil Cooled",
        "power": "11.38 PS @ 7500 rpm",
        "torque": "11.2 Nm @ 6000 rpm",
        "mileage": "65 - 67 kmpl",
        "braking": "Drum (Front), Drum (Rear) with ET-Fi",
        "abs": "Sync Braking Technology (CBS)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Wicked Black", "Fiery Yellow"]
    },
    "Raider Disc 125 BSVI SS": {
        "category": "Motorcycle",
        "engine": "124.8 cc, 3-Valve, Air-Oil Cooled",
        "power": "11.38 PS @ 7500 rpm",
        "torque": "11.2 Nm @ 6000 rpm",
        "mileage": "65 - 67 kmpl",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (CBS)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Striking Red", "Blazing Black"]
    },
    "Raider Disc 125 SX BT": {
        "category": "Motorcycle",
        "engine": "124.8 cc, 3-Valve, Air-Oil Cooled",
        "power": "11.38 PS @ 7500 rpm",
        "torque": "11.2 Nm @ 6000 rpm",
        "mileage": "65 - 67 kmpl",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (CBS)",
        "connectivity": "Yes (SmartXonnect with TFT Screen & Voice Assist)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Glossy Yellow", "Glossy Black"]
    },
    "XL 100 Heavy Duty Kick": {
        "category": "Moped",
        "engine": "99.7 cc, 4-Stroke, Single Cylinder",
        "power": "4.4 PS @ 6000 rpm",
        "torque": "6.5 Nm @ 3500 rpm",
        "mileage": "60 - 65 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "CBS (Combined Braking System)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "4 Litres",
        "colors": ["Black", "Blue", "Grey", "Red"]
    },
    "XL 100 HD Self": {
        "category": "Moped",
        "engine": "99.7 cc, 4-Stroke, Single Cylinder with Self Start",
        "power": "4.4 PS @ 6000 rpm",
        "torque": "6.5 Nm @ 3500 rpm",
        "mileage": "60 - 65 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "CBS (Combined Braking System)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "4 Litres",
        "colors": ["Matte Black", "Brown", "Red"]
    },
    "XL 100 Comfort / Winner Edition": {
        "category": "Moped",
        "engine": "99.7 cc, 4-Stroke, Single Cylinder",
        "power": "4.4 PS @ 6000 rpm",
        "torque": "6.5 Nm @ 3500 rpm",
        "mileage": "60 - 65 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "CBS (Combined Braking System)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "4 Litres",
        "colors": ["Winner Edition Special Graphics", "Teal Blue", "Mineral Purple"]
    },
    "Sports ES BSVI MWL": {
        "category": "Commuter Motorcycle",
        "engine": "109.7 cc, 4-Stroke, DuraLife Engine",
        "power": "8.29 PS @ 7350 rpm",
        "torque": "8.7 Nm @ 4500 rpm",
        "mileage": "70 - 73 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Black Blue", "Black Red", "Metallic Blue"]
    },
    "Sports ES BSVI MWL Graphics": {
        "category": "Commuter Motorcycle",
        "engine": "109.7 cc, 4-Stroke, DuraLife Engine",
        "power": "8.29 PS @ 7350 rpm",
        "torque": "8.7 Nm @ 4500 rpm",
        "mileage": "70 - 73 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Special Edition Premium Graphics Scheme"]
    },
    "Radeon BSVI ES MWL Drum": {
        "category": "Commuter Motorcycle",
        "engine": "109.7 cc, ET-Fi Air-Cooled",
        "power": "8.19 PS @ 7350 rpm",
        "torque": "8.7 Nm @ 4500 rpm",
        "mileage": "68 - 73 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Metal Black", "Royal Blue", "Titanium Grey", "Stitch Beige"]
    },
    "Star City BSVI ES Drum": {
        "category": "Commuter Motorcycle",
        "engine": "109.7 cc, Ecothrust Fuel Injection (ET-Fi)",
        "power": "8.19 PS @ 7350 rpm",
        "torque": "8.7 Nm @ 4500 rpm",
        "mileage": "70 - 75 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "10 Litres",
        "colors": ["Majestic Black", "Grey-Blue", "Red-Black"]
    },
    "Jupiter 110 Drum Alloy": {
        "category": "Scooter",
        "engine": "113.3 cc, Single Cylinder, Air-Cooled",
        "power": "7.89 PS @ 6500 rpm",
        "torque": "9.8 Nm @ 5000 rpm",
        "mileage": "50 - 55 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "6 Litres",
        "colors": ["Titanium Grey", "Midnight Black", "Mystic Gold"]
    },
    "Jupiter 110 Drum Alloy SXC Digital Meter": {
        "category": "Scooter",
        "engine": "113.3 cc, Single Cylinder, Air-Cooled",
        "power": "7.89 PS @ 6500 rpm",
        "torque": "9.8 Nm @ 5000 rpm",
        "mileage": "50 - 55 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (SBT)",
        "connectivity": "Yes (SmartXonnect Digital Cluster)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "6 Litres",
        "colors": ["Starlight Blue", "Royal Wine"]
    },
    "Jupiter 110 Disc SXC Digital Meter": {
        "category": "Scooter",
        "engine": "113.3 cc, Single Cylinder, Air-Cooled",
        "power": "7.89 PS @ 6500 rpm",
        "torque": "9.8 Nm @ 5000 rpm",
        "mileage": "50 - 55 kmpl",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (SBT)",
        "connectivity": "Yes (SmartXonnect Digital Cluster)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "6 Litres",
        "colors": ["Matte Copper Bronze", "Lunar White"]
    },
    "Jupiter 110 Alloy BSVI Basic Drum": {
        "category": "Scooter",
        "engine": "113.3 cc, Single Cylinder, Air-Cooled",
        "power": "7.47 PS @ 6500 rpm",
        "torque": "8.4 Nm @ 5000 rpm",
        "mileage": "50 - 55 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "6 Litres",
        "colors": ["Metallic Silver", "Plain Black"]
    },
    "Jupiter 125 BSVI Drum Alloy": {
        "category": "Scooter",
        "engine": "124.8 cc, Single Cylinder, Air-Cooled",
        "power": "8.15 PS @ 6500 rpm",
        "torque": "10.5 Nm @ 4500 rpm",
        "mileage": "55 - 57 kmpl",
        "braking": "Drum (Front), Drum (Rear)",
        "abs": "Sync Braking Technology (SBT)",
        "connectivity": "No",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "5.1 Litres",
        "colors": ["Indiblue", "Dawn Orange", "Metallic Black"]
    },
    "NTORQ 125 Race XP": {
        "category": "Scooter",
        "engine": "124.8 cc, 3-Valve, Air-Cooled",
        "power": "10.2 HP @ 7000 rpm",
        "torque": "10.8 Nm @ 5500 rpm",
        "mileage": "45 - 48 kmpl",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "Yes (SmartXonnect with Dual Ride Modes - Street/Race)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "5.8 Litres",
        "colors": ["Race Edition Red-Black", "Matte Black Red"]
    },
    "NTORQ 125 XT": {
        "category": "Scooter",
        "engine": "124.8 cc, 3-Valve, Air-Cooled",
        "power": "9.25 HP @ 7000 rpm",
        "torque": "10.5 Nm @ 5500 rpm",
        "mileage": "45 - 48 kmpl",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Synchronized Braking Technology (SBT)",
        "connectivity": "Yes (SmartXonnect with Smart TFT & Voice Assist)",
        "bs_rating": "BS6 Phase 2",
        "fuel_tank": "5.8 Litres",
        "colors": ["Neon Green"]
    },
    "Iqube Electric SX 9P75": {
        "category": "Electric Scooter",
        "engine": "BLDC Hub Motor (Electric)",
        "power": "4.4 kW (Peak Power)",
        "torque": "33 Nm",
        "mileage": "Approx. 100 km per full charge",
        "braking": "Disc (Front), Drum (Rear)",
        "abs": "Combined Braking System (CBS)",
        "connectivity": "Yes (Advanced SmartXonnect, Navigation, Geo-fencing)",
        "bs_rating": "Zero Emission Electric",
        "fuel_tank": "Battery Pack (3.04 kWh Lithium-ion)",
        "colors": ["Mercury Grey", "Copper Bronze", "Mint Blue"]
    }
}

# App Layout
st.title("🏍️ TVS Inventory & Customer Catalog")
st.write("Browse through available models and click on any vehicle to view complete specifications.")

# Sidebar filter for categories
categories = ["All Models"] + list(set([data["category"] for data in inventory_catalog.values()]))
selected_category = st.sidebar.selectbox("Filter by Category", categories)

# Search filter
search_query = st.sidebar.text_input("Search Model Name", "")

# Filter the catalog
filtered_catalog = {}
for model_name, specs in inventory_catalog.items":
    if selected_category != "All Models" and specs["category"] != selected_category:
        continue
    if search_query.lower() not in model_name.lower():
        continue
    filtered_catalog[model_name] = specs

# Main layout split into two columns (Catalog list on left, details on right)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Select a Vehicle")
    if not filtered_catalog:
        st.warning("No models match your search criteria.")
    else:
        selected_bike = st.radio(
            "Inventory List:",
            list(filtered_catalog.keys()),
            label_visibility="collapsed"
        )

with col2:
    st.subheader("Vehicle Specifications")
    if selected_bike in inventory_catalog:
        bike_data = inventory_catalog[selected_bike]
        
        st.markdown(f"### **{selected_bike}**")
        st.caption(f"Category: {bike_data['category']}")
        
        st.divider()
        
        # Displaying all customer-facing details excluding price/quantity/availability
        st.markdown(f"**Engine / Motor:** {bike_data['engine']}")
        st.markdown(f"**Max Power:** {bike_data['power']}")
        st.markdown(f"**Torque:** {bike_data['torque']}")
        st.markdown(f"**Mileage / Range:** {bike_data['mileage']}")
        st.markdown(f"**Braking Setup:** {bike_data['braking']}")
        st.markdown(f"**ABS / Safety System:** {bike_data['abs']}")
        st.markdown(f"**Bluetooth Connectivity:** {bike_data['connectivity']}")
        st.markdown(f"**BS Rating / Emission:** {bike_data['bs_rating']}")
        st.markdown(f"**Fuel Tank / Battery Capacity:** {bike_data['fuel_tank']}")
        
        st.divider()
        
        # Color options display
        st.markdown("**Available Color Options:**")
        for color in bike_data['colors']:
            st.markdown(f"- {color}")
