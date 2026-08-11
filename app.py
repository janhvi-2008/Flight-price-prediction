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

st.markdown(
    """
    <style>

    /* ===== MAIN BACKGROUND ===== */

    .stApp {
        background: linear-gradient(
            135deg,
            #fffaf3 0%,
            #f7eee3 45%,
            #ead8c4 100%
        );
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* ===== TITLE ===== */

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #4a2c20;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #795548;
        margin-bottom: 30px;
    }


    /* ===== SECTION TITLE ===== */

    .section-title {
        background: linear-gradient(
            90deg,
            #4a2c20,
            #6f4937
        );

        color: #f8e6c8;

        padding: 14px 22px;

        border-radius: 12px;

        font-size: 22px;

        font-weight: 700;

        margin-bottom: 22px;

        box-shadow:
            0 6px 18px rgba(74, 44, 32, 0.20);
    }


    /* ===== LABELS ===== */

    label {
        color: #4a2c20 !important;
        font-weight: 700 !important;
    }


    /* ===== SELECT BOX ===== */

    div[data-baseweb="select"] > div {

        background-color: #ffffff !important;

        border: 1.5px solid #c7a17a !important;

        border-radius: 10px !important;

        min-height: 48px !important;

        box-shadow:
            0 2px 7px rgba(74, 44, 32, 0.08);
    }


    /* Selected value */

    div[data-baseweb="select"] span {

        color: #4a2c20 !important;

        font-weight: 700 !important;
    }


    /* Dropdown */

    div[role="option"] {

        color: #4a2c20 !important;

        background-color: #ffffff !important;

        font-weight: 600 !important;
    }


    div[role="option"]:hover {

        background-color: #f5e7d6 !important;
    }


    /* ===== NUMBER INPUT ===== */

    div[data-testid="stNumberInput"] input {

        background-color: #ffffff !important;

        color: #4a2c20 !important;

        font-weight: 700 !important;

        border: 1.5px solid #c7a17a !important;

        border-radius: 10px !important;
    }


    /* ===== BUTTON ===== */

    .stButton > button {

        width: 100%;

        background: linear-gradient(
            90deg,
            #4a2c20,
            #6f4937
        );

        color: #f8e6c8;

        border: none;

        border-radius: 12px;

        padding: 14px;

        font-size: 19px;

        font-weight: 700;

        box-shadow:
            0 6px 16px rgba(74, 44, 32, 0.25);

        transition: 0.3s;
    }


    .stButton > button:hover {

        background: linear-gradient(
            90deg,
            #5a3728,
            #805846
        );

        color: #ffffff;

        transform: translateY(-2px);
    }


    /* ===== RESULT CARD ===== */

    .result-box {

        background: linear-gradient(
            135deg,
            #ffffff,
            #fff8ef
        );

        color: #4a2c20;

        padding: 32px;

        border-radius: 18px;

        text-align: center;

        margin-top: 30px;

        border: 2px solid #c7a17a;

        box-shadow:
            0 10px 30px rgba(74, 44, 32, 0.15);
    }


    .result-box h2 {

        color: #6f4937;

        font-size: 25px;

        margin-bottom: 12px;
    }


    .price {

        color: #4a2c20;

        font-size: 52px;

        font-weight: 800;

        margin: 10px;
    }


    /* ===== FOOTER ===== */

    .footer {

        text-align: center;

        color: #795548;

        font-size: 16px;

        margin-top: 30px;

        padding: 15px;
    }


    /* ===== MOBILE ===== */

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




