import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TVS Inventory & Customer Catalog",
    page_icon="🏍️",
    layout="wide"
)

# Catalog database with clean studio/plain stock photos for each model
inventory_catalog = {
    "Apache RTR 160 2V Disc": {
        "category": "Motorcycle",
        "image": "https://www.tvsmotor.com/-/media/Feature/Brands/Apache/Apache-RTR-160/Colors/glossy-black.png",
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
        "image": "https://www.tvsmotor.com/-/media/Feature/Brands/Apache/Apache-RTR-160/Colors/glossy-black.png",
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
        "image": "https://www.tvsmotor.com/-/media/Feature/Brands/Apache/Apache-RTR-160/Colors/glossy-black.png",
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
        "image": "
