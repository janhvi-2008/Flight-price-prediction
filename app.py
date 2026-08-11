import streamlit as st
import pandas as pd
import pickle

# -----------------------------------
# Page Settings
# -----------------------------------

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------------
# Load Model
# -----------------------------------

with open("flight_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------------
# Custom CSS - Dark Brown Theme
# -----------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #2b1608 0%,
            #4a2410 25%,
            #6b3415 50%,
            #8a4b20 75%,
            #d6a15c 100%
        );
        color: white;
    }

    /* Main content */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #ffe4b5;
        margin-top: 10px;
        margin-bottom: 5px;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #f8d9ad;
        margin-bottom: 30px;
    }

    /* Section heading */
    .section-title {
        background: linear-gradient(
            90deg,
            #3b1d0b,
            #6f3515,
            #9a5a28
        );
        color: #ffe4b5;
        padding: 14px 22px;
        border-radius: 14px;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 22px;
        border: 1px solid #b7793d;
        box-shadow: 0 7px 20px rgba(0, 0, 0, 0.35);
    }

    /* Labels */
    label {
        color: #ffe4b5 !important;
        font-weight: 700 !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #fff8ed !important;
        border: 2px solid #b7793d !important;
        border-radius: 10px !important;
        min-height: 48px !important;
    }

    /* Selected value */
    div[data-baseweb="select"] span {
        color: #3b1d0b !important;
        font-weight: 700 !important;
    }

    /* Dropdown options */
    div[role="option"] {
        color: #3b1d0b !important;
        background-color: #fff8ed !important;
        font-weight: 600 !important;
    }

    div[role="option"]:hover {
        background-color: #f3d5ad !important;
    }

    /* Number inputs */
    div[data-testid="stNumberInput"] input {
        background-color: #fff8ed !important;
        color: #3b1d0b !important;
        font-weight: 700 !important;
        border: 2px solid #b7793d !important;
        border-radius: 10px !important;
    }

    /* Predict button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(
            90deg,
            #3b1d0b,
            #6f3515,
            #a45f25
        );
        color: #ffe4b5;
        border: 2px solid #c58a4b;
        border-radius: 14px;
        padding: 14px;
        font-size: 19px;
        font-weight: 700;
        box-shadow: 0 7px 20px rgba(0, 0, 0, 0.35);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #5a2a0d,
            #8a451b,
            #b87333
        );
        color: white;
        transform: translateY(-2px);
    }

    /* Prediction result */
    .result-box {
        background: linear-gradient(
            135deg,
            #2b1608,
            #4a2410,
            #7a3f18,
            #a9672d
        );
        color: white;
        padding: 32px;
        border-radius: 22px;
        text-align: center;
        margin-top: 30px;
        border: 2px solid #c58a4b;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.45);
    }

    .result-box h2 {
        color: #ffe4b5;
        font-size: 25px;
        margin-bottom: 12px;
    }

    .price {
        color: #ffffff;
        font-size: 52px;
        font-weight: 800;
        margin: 10px;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.45);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #f8d9ad;
        font-size: 16px;
        margin-top: 30px;
        padding: 15px;
    }

    /* Mobile */
    @media (max-width: 768px) {

        .main-title {
            font-size: 32px;
        }

        .subtitle {
            font-size: 16px;
        }

        .section-title {
            font-size: 19px;
            padding: 12px 16px;
        }

        div[data-baseweb="select"] > div {
            min-height: 52px !important;
        }

        div[data-baseweb="select"] span {
            font-size: 16px !important;
            font-weight: 700 !important;
        }

        .price {
            font-size: 40px;
        }

        .result-box {
            padding: 25px 15px;
        }

        .result-box h2 {
            font-size: 21px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# Header
# -----------------------------------

st.markdown(
    '<div class="main-title">✈️ Flight Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict your estimated flight ticket price using Machine Learning</div>',
    unsafe_allow_html=True
)

# -----------------------------------
# Flight Details
# -----------------------------------

st.markdown(
    '<div class="section-title">🛫 Enter Flight Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# -----------------------------------
# Column 1
# -----------------------------------

with col1:

    airline = st.selectbox(
        "✈️ Airline",
        [
            "IndiGo",
            "Air India",
            "Vistara",
            "SpiceJet",
            "AirAsia"
        ]
    )

    source = st.selectbox(
        "📍 Source",
        [
            "Delhi",
            "Mumbai",
            "Bangalore",
            "Kolkata",
            "Chennai",
            "Hyderabad"
        ]
    )

    destination = st.selectbox(
        "🎯 Destination",
        [
            "Delhi",
            "Mumbai",
            "Bangalore",
            "Kolkata",
            "Chennai",
            "Hyderabad"
        ]
    )

    departure_time = st.selectbox(
        "🕐 Departure Time",
        [
            "Morning",
            "Afternoon",
            "Evening",
            "Night"
        ]
    )

# -----------------------------------
# Column 2
# -----------------------------------

with col2:

    duration = st.number_input(
        "⏱️ Flight Duration (Hours)",
        min_value=1.0,
        max_value=15.0,
        value=2.0,
        step=0.1
    )

    stops = st.selectbox(
        "🛑 Total Stops",
        [0, 1, 2]
    )

    days_left = st.number_input(
        "📅 Days Left",
        min_value=1,
        max_value=60,
        value=15
    )

    flight_class = st.selectbox(
        "💺 Class",
        [
            "Economy",
            "Business"
        ]
    )

# -----------------------------------
# Prediction
# -----------------------------------

st.write("")

if st.button("✈️ Predict Flight Price", use_container_width=True):

    new_flight = pd.DataFrame({
        "Airline": [airline],
        "Source": [source],
        "Destination": [destination],
        "Departure_Time": [departure_time],
        "Duration_Hours": [duration],
        "Total_Stops": [stops],
        "Days_Left": [days_left],
        "Class": [flight_class]
    })

    try:

        prediction = model.predict(new_flight)

        price = prediction[0]

        st.markdown(
            f"""
            <div class="result-box">
                <h2>💰 Estimated Flight Ticket Price</h2>
                <div class="price">₹{price:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("❌ Prediction failed.")
        st.exception(e)

# -----------------------------------
# Footer
# -----------------------------------

st.markdown(
    """
    <div class="footer">
        ✈️ Flight Price Prediction
        <br>
        <span style="font-size: 14px;">Created by JMM</span>
    </div>
    """,
    unsafe_allow_html=True
)




