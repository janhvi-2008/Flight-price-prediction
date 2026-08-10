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
# CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #FFF4F8;
}


/* Header */

.header {
    background: linear-gradient(
        135deg,
        #6D1837,
        #A91B60,
        #D94F8A
    );

    padding: 35px;

    border-radius: 20px;

    text-align: center;

    margin-bottom: 30px;

    box-shadow: 0 8px 25px rgba(109,24,55,0.20);
}

.header h1 {
    color: white;
    font-size: 42px;
    margin: 0;
}

.header p {
    color: #FFE5F0;
    font-size: 18px;
    margin-top: 8px;
}


/* Section heading */

.section-title {
    color: #7A2048;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 18px;
}


/* Labels */

label {
    color: #71304D !important;
    font-weight: 600 !important;
}


/* Input boxes */

.stSelectbox > div > div,
.stNumberInput > div > div {
    background-color: white;
    border-radius: 10px;
}


/* Button */

.stButton > button {

    width: 100%;

    height: 55px;

    border-radius: 12px;

    border: none;

    background: linear-gradient(
        90deg,
        #A91B60,
        #D94F8A
    );

    color: white;

    font-size: 19px;

    font-weight: 700;

    box-shadow: 0 5px 15px rgba(169,27,96,0.25);
}

.stButton > button:hover {

    background: linear-gradient(
        90deg,
        #6D1837,
        #A91B60
    );

    color: white;
}


/* Result */

.result {

    background: linear-gradient(
        135deg,
        #D94F8A,
        #F08AB5
    );

    padding: 30px;

    border-radius: 20px;

    text-align: center;

    margin-top: 25px;

    box-shadow: 0 8px 25px rgba(217,79,138,0.25);
}

.result h2 {
    color: white;
    font-size: 22px;
    margin: 0;
}

.result h1 {
    color: white;
    font-size: 48px;
    margin: 10px;
}

.result p {
    color: #FFF0F6;
}


/* Footer */

.footer {
    text-align: center;
    color: #9A647A;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# Header
# -----------------------------------

st.markdown("""
<div class="header">

<h1>✈️ Flight Price Prediction</h1>

<p>Smart Flight Ticket Price Prediction using Machine Learning</p>

</div>
""", unsafe_allow_html=True)


# -----------------------------------
# Flight Details
# -----------------------------------

st.markdown(
    '<div class="section-title">🛫 Enter Flight Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


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

if st.button("✈️  Predict Flight Price"):

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

    prediction = model.predict(new_flight)

    price = prediction[0]

    st.markdown(
        f"""
        <div class="result">

        <h2>Estimated Flight Ticket Price</h2>

        <h1>₹{price:,.0f}</h1>

        <p>Powered by Random Forest Regression</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------
# Footer
# -----------------------------------

st.markdown("""
<div class="footer">

✈️ Flight Price Prediction
&nbsp; | &nbsp;
Random Forest Regression

</div>
""", unsafe_allow_html=True)