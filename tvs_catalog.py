import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TVS Two-Wheeler Catalogue",
    page_icon="🏍️",
    layout="wide"
)

# Inventory Dataset mapped precisely from your stock list
# Image URLs use clean, reliable placeholder/representative images as requested
inventory_data = [
    {
        "model": "Apache RTR 160 2V Disc",
        "category": "Motorcycle",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "abs_system": "Single-Channel ABS",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Apache RTR 160 2V Disc BT",
        "category": "Motorcycle",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "abs_system": "Single-Channel ABS",
        "bluetooth": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Apache RTR 160 2V Disc BT Race Edition",
        "category": "Motorcycle",
        "engine": "159.7 cc",
        "mileage": "45 kmpl",
        "abs_system": "Single-Channel ABS",
        "bluetooth": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Apache RTR 160 4V Disc",
        "category": "Motorcycle",
        "engine": "159.7 cc (4V)",
        "mileage": "42 kmpl",
        "abs_system": "Single-Channel ABS",
        "bluetooth": "Yes (SmartXonnect variants available)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum/Disc options",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Apache RTR 160 4V Disc LE Special Edition",
        "category": "Motorcycle",
        "engine": "159.7 cc (4V)",
        "mileage": "42 kmpl",
        "abs_system": "Single-Channel ABS",
        "bluetooth": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Disc",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Raider Drum 125",
        "category": "Motorcycle",
        "engine": "124.8 cc",
        "mileage": "67 kmpl",
        "abs_system": "Sync Braking System (SBS)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981285-6f0c94be58bb?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Raider Disc 125 BSVI SS",
        "category": "Motorcycle",
        "engine": "124.8 cc",
        "mileage": "67 kmpl",
        "abs_system": "Sync Braking System (SBS)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981285-6f0c94be58bb?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Raider Disc 125 SX BT",
        "category": "Motorcycle",
        "engine": "124.8 cc",
        "mileage": "67 kmpl",
        "abs_system": "Sync Braking System (SBS)",
        "bluetooth": "Yes (SmartXonnect TFT Display)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558981285-6f0c94be58bb?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "XL 100 Heavy Duty Kick",
        "category": "Moped",
        "engine": "99.7 cc",
        "mileage": "80 kmpl",
        "abs_system": "None (Drum Brakes)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1543666680-e6274d816a43?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "XL 100 HD Self",
        "category": "Moped",
        "engine": "99.7 cc",
        "mileage": "80 kmpl",
        "abs_system": "None (Drum Brakes)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1543666680-e6274d816a43?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "XL 100 Comfort / Winner Edition",
        "category": "Moped",
        "engine": "99.7 cc",
        "mileage": "80 kmpl",
        "abs_system": "None (Drum Brakes)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1543666680-e6274d816a43?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Sports ES BSVI MWL",
        "category": "Commuter",
        "engine": "109.7 cc",
        "mileage": "70 kmpl",
        "abs_system": "Synchronized Braking Technology",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Sports ES BSVI MWL Graphics",
        "category": "Commuter",
        "engine": "109.7 cc",
        "mileage": "70 kmpl",
        "abs_system": "Synchronized Braking Technology",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Radeon BSVI ES MWL Drum",
        "category": "Commuter",
        "engine": "109.7 cc",
        "mileage": "65 kmpl",
        "abs_system": "Synchronized Braking Technology",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Star City BSVI ES Drum",
        "category": "Commuter",
        "engine": "109.7 cc",
        "mileage": "68 kmpl",
        "abs_system": "Synchronized Braking Technology",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Jupiter 110 Drum Alloy",
        "category": "Scooter",
        "engine": "113.3 cc",
        "mileage": "50 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1571188654248-7a89213933e7?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Jupiter 110 Drum Alloy SXC Digital Meter",
        "category": "Scooter",
        "engine": "113.3 cc",
        "mileage": "50 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1571188654248-7a89213933e7?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Jupiter 110 Disc SXC Digital Meter",
        "category": "Scooter",
        "engine": "113.3 cc",
        "mileage": "50 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "Yes (SmartXonnect)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1571188654248-7a89213933e7?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Jupiter 110 Alloy BSVI Basic Drum",
        "category": "Scooter",
        "engine": "113.3 cc",
        "mileage": "50 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "No",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1571188654248-7a89213933e7?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "Jupiter 125 BSVI Drum Alloy",
        "category": "Scooter",
        "engine": "124.8 cc",
        "mileage": "57 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "Optional variants available",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Drum, Rear Drum",
        "image": "https://images.unsplash.com/photo-1571188654248-7a89213933e7?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "NTORQ 125 Race XP",
        "category": "Scooter",
        "engine": "124.8 cc",
        "mileage": "47 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "Yes (SmartXonnect with Voice Assist)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "NTORQ 125 XT",
        "category": "Scooter",
        "engine": "124.8 cc",
        "mileage": "47 kmpl",
        "abs_system": "Sync Brake System (SBS)",
        "bluetooth": "Yes (SmartXonnect TFT & LCD Hybrid)",
        "bs_rating": "BS6 Phase 2",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&auto=format&fit=crop&q=60"
    },
    {
        "model": "iQube Electric SX 3P75",
        "category": "Electric Scooter",
        "engine": "Electric Hub Motor (BLDC)",
        "mileage": "100+ km per charge",
        "abs_system": "Combi-Braking System",
        "bluetooth": "Yes (SmartXonnect Connected Cluster)",
        "bs_rating": "EV Zero Emission",
        "brakes": "Front Disc, Rear Drum",
        "image": "https://images.unsplash.com/photo-1558980664-3a031cf67ea8?w=500&auto=format&fit=crop&q=60"
    }
]

# App Header
st.title("🏍️ TVS Two-Wheeler Showroom Catalogue")
st.write("Browse your complete inventory line-up and explore detailed customer specifications instantly.")

# Sidebar Filters
st.sidebar.header("Catalogue Controls")
selected_category = st.sidebar.selectbox(
    "Filter by Category",
    ["All"] + list(set([item["category"] for item in inventory_data]))
)

search_query = st.sidebar.text_input("Search Model Name", "").lower()

# Filter logic
filtered_inventory = inventory_data
if selected_category != "All":
    filtered_inventory = [item for item in filtered_inventory if item["category"] == selected_category]

if search_query:
    filtered_inventory = [item for item in filtered_inventory if search_query in item["model"].lower()]

st.markdown(f"Showing **{len(filtered_inventory)}** models matching your selection.")
st.divider()

# Display Catalogue in Grid format (3 columns)
cols = st.columns(3)
for index, vehicle in enumerate(filtered_inventory):
    col = cols[index % 3]
    with col:
        st.image(vehicle["image"], use_column_width=True)
        st.subheader(vehicle["model"])
        st.caption(f"Category: {vehicle['category']}")
        
        # Expandable specifications for customer inquiry
        with st.expander("View Full Customer Specs"):
            st.write(f"**Engine Displacement:** {vehicle['engine']}")
            st.write(f"**Mileage / Range:** {vehicle['mileage']}")
            st.write(f"**Braking & ABS:** {vehicle['abs_system']}")
            st.write(f"**Brakes:** {vehicle['brakes']}")
            st.write(f"**Bluetooth Connectivity:** {vehicle['bluetooth']}")
            st.write(f"**Emission Standard:** {vehicle['bs_rating']}")
            
        st.markdown("---")
