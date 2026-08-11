import streamlit as st
import pandas as pd
import pickle

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Flight Price Prediction",
    page_icon="✈️",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

with open("flight_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    /* --------------------------------------
       MAIN BACKGROUND
       -------------------------------------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #fff9fb 0%,
            #fce7ef 35%,
            #f5d1dc 70%,
            #e8a0b8 100%
        );
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }


    /* --------------------------------------
       MAIN TITLE
       -------------------------------------- */

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #5A1028;
        margin-top: 10px;
        margin-bottom: 5px;
        text-shadow: 1px 2px 5px rgba(90, 16, 40, 0.15);
    }


    /* --------------------------------------
       SUBTITLE
       -------------------------------------- */

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #7A1737;
        margin-bottom: 30px;
    }


    /* --------------------------------------
       SECTION HEADER
       -------------------------------------- */

    .section-title {
        background: linear-gradient(
            90deg,
            #5A1028,
            #7A1737,
            #A52A50
        );

        color: #FFE8EF;

        padding: 14px 22px;

        border-radius: 14px;

        font-size: 22px;

        font-weight: 700;

        margin-bottom: 22px;

        box-shadow:
            0 7px 20px rgba(90, 16, 40, 0.25);
    }


    /* --------------------------------------
       LABELS
       -------------------------------------- */

    label {
        color: #5A1028 !important;
        font-weight: 700 !important;
    }


    /* --------------------------------------
       SELECT BOX
       -------------------------------------- */

    div[data-baseweb="select"] > div {

        background-color: #FFFFFF !important;

        border: 2px solid #E8A0B8 !important;

        border-radius: 10px !important;

        min-height: 48px !important;

        box-shadow:
            0 3px 10px rgba(90, 16, 40, 0.08);
    }


    /* Selected value */

    div[data-baseweb="select"] span {

        color: #5A1028 !important;

        font-weight: 700 !important;
    }


    /* Dropdown options */

    div[role="option"] {

        color: #5A1028 !important;

        background-color: #FFFFFF !important;

        font-weight: 600 !important;
    }


    div[role="option"]:hover {

        background-color: #FCE7EF !important;
    }


    /* --------------------------------------
       NUMBER INPUT
       -------------------------------------- */

    div[data-testid="stNumberInput"] input {

        background-color: #FFFFFF !important;

        color: #5A1028 !important;

        font-weight: 700 !important;

        border: 2px solid #E8A0B8 !important;

        border-radius: 10px !important;
    }


    /* --------------------------------------
       PREDICT BUTTON
       -------------------------------------- */

    .stButton > button {

        width: 100%;

        background: linear-gradient(
            90deg,
            #5A1028,
            #7A1737,
            #A52A50
        );

        color: #FFE8EF;

        border: none;

        border-radius: 14px;

        padding: 14px;

        font-size: 19px;

        font-weight: 700;

        box-shadow:
            0 7px 20px rgba(90, 16, 40, 0.30);

        transition: all 0.3s ease;
    }


    .stButton > button:hover {

        background: linear-gradient(
            90deg,
            #7A1737,
            #A52A50,
            #C44C70
        );

        color: white;

        transform: translateY(-2px);

        box-shadow:
            0 10px 25px rgba(90, 16, 40, 0.35);
    }


    /* --------------------------------------
       RESULT CARD
       -------------------------------------- */

    .result-box {

        background: linear-gradient(
            135deg,
            #5A1028,
            #7A1737,
            #A52A50
        );

        color: white;

        padding: 32px;

        border-radius: 20px;

        text-align: center;

        margin-top: 30px;

        border: 2px solid #E8A0B8;

        box-shadow:
            0 12px 30px rgba(90, 16, 40, 0.30);
    }


    .result-box h2 {

        color: #FFE8EF;

        font-size: 25px;

        margin-bottom: 12px;
    }


    .price {

        color: #FFFFFF;

        font-size: 52px;

        font-weight: 800;

        margin: 10px;

        text-shadow:
            1px 2px 6px rgba(0, 0, 0, 0.25);
    }


    /* --------------------------------------
       FOOTER
       -------------------------------------- */

    .footer {

        text-align: center;

        color: #7A1737;

        font-size: 16px;

        margin-top: 30px;

        padding: 15px;
    }


    /* --------------------------------------
       MOBILE DESIGN
       -------------------------------------- */

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

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">✈️ Flight Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict your estimated flight ticket price using Machine Learning</div>',
    unsafe_allow_html=True
)

# ==========================================
# FLIGHT DETAILS
# ==========================================

st.markdown(
    '<div class="section-title">🛫 Enter Flight Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# ==========================================
# LEFT COLUMN
# ==========================================

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

# ==========================================
# RIGHT COLUMN
# ==========================================

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

# ==========================================
# PREDICTION
# ==========================================

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

# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <div class="footer">
        ✈️ Flight Price Prediction
        <br>
        <span style="font-size: 14px;">
            Created by JMM
        </span>
    </div>
    """,
    unsafe_allow_html=True
)


        



