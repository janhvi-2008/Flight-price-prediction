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
# Pink Gradient CSS
st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #fff0f6 0%,
            #fce7f3 35%,
            #f3e8ff 70%,
            #ffffff 100%
        );
    }

    /* Title */
    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #831843;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #6b214f;
        margin-bottom: 30px;
    }

    /* Section heading */
    .section-title {
        background: linear-gradient(
            90deg,
            #ec4899,
            #d946ef,
            #a855f7
        );
        color: white;
        padding: 13px 22px;
        border-radius: 14px;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(236, 72, 153, 0.25);
    }

    /* Labels */
    label {
        color: #831843 !important;
        font-weight: 700 !important;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        border: 2px solid #f9a8d4 !important;
        border-radius: 10px !important;
        min-height: 48px !important;
    }

    /* Selected value inside selectbox */
    div[data-baseweb="select"] span {
        color: #831843 !important;
        font-weight: 700 !important;
    }

    /* Selectbox text */
    div[data-baseweb="select"] input {
        color: #831843 !important;
    }

    /* Dropdown options */
    div[role="option"] {
        color: #831843 !important;
        background-color: white !important;
        font-weight: 600 !important;
    }

    div[role="option"]:hover {
        background-color: #fce7f3 !important;
    }

    /* Number input */
    div[data-testid="stNumberInput"] input {
        background-color: white !important;
        color: #831843 !important;
        font-weight: 700 !important;
        border: 2px solid #f9a8d4 !important;
    }

    /* Predict button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(
            90deg,
            #ec4899,
            #d946ef,
            #a855f7
        );
        color: white;
        border: none;
        border-radius: 14px;
        padding: 14px;
        font-size: 19px;
        font-weight: 700;
        box-shadow: 0 6px 18px rgba(236, 72, 153, 0.30);
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #db2777,
            #c026d3,
            #9333ea
        );
        color: white;
    }

    /* Prediction result */
    .result-box {
        background: linear-gradient(
            135deg,
            #ec4899,
            #d946ef,
            #9333ea
        );
        color: white;
        padding: 32px;
        border-radius: 22px;
        text-align: center;
        margin-top: 30px;
        box-shadow: 0 10px 30px rgba(190, 24, 93, 0.25);
    }

    .result-box h2 {
        color: white;
        font-size: 25px;
    }

    .price {
        color: white;
        font-size: 52px;
        font-weight: 800;
    }

    .result-box p {
        color: #fce7f3;
        font-size: 16px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #831843;
        font-size: 15px;
        margin-top: 25px;
        padding: 15px;
    }

    /* Mobile optimization */
    @media (max-width: 768px) {

        .main-title {
            font-size: 32px;
        }

        .subtitle {
            font-size: 16px;
        }

        .section-title {
            font-size: 19px;
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

if st.button("✈️ Predict Flight Price"):

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

    <div class="price">
        ₹{price:,.0f}
    </div>

</div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("❌ Prediction failed.")

        st.exception(e)

# -----------------------------------
# Footer
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
