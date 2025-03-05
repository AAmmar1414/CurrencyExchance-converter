import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Enhanced Currency Converter", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #000000; /* Black background */
    }
    .stButton>button {
        background-color: #FF5733; /* Vibrant orange */
        color: #FFFFFF; /* White text */
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #FFC300; /* Yellow border */
    }
    .stSelectbox {
        border-radius: 10px;
        background-color: #333333; /* Dark grey background */
        color: #FFFFFF; /* White text */
    }
    .success-message {
        padding: 20px;
        border-radius: 10px;
        background-color: #1D8348; /* Dark green */
        border: 1px solid #28B463; /* Bright green border */
        color: #D5F5E3; /* Soft green text */
    }
    </style>
    """, unsafe_allow_html=True)

# Function to fetch exchange rates
def fetch_exchange_rates():
    # Placeholder for exchange rates; in a real application, fetch from a reliable API
    return {
        'USD': 1.0,
        'EUR': 0.91,
        'GBP': 0.76,
        'INR': 82.15,
        'JPY': 136.50,
        'AUD': 1.44,
        'CAD': 1.36,
        'CHF': 0.92,
        'CNY': 6.90,
        'NZD': 1.55
    }

# Currency conversion function
def currency_converter(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        st.error("Currency not supported.")
        return None
    if from_currency == 'USD':
        converted_amount = amount * rates[to_currency]
    elif to_currency == 'USD':
        converted_amount = amount / rates[from_currency]
    else:
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

def main():
    st.markdown("""
    <div style='background: linear-gradient(45deg, #000000, #333333); padding: 20px; border-radius: 15px;'>
        <h1 style='color: #FF5733; text-align: center;'>✨ Enhanced Currency Converter ✨</h1>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar with gradient background
    with st.sidebar:
        st.markdown("""
            <div style='background: linear-gradient(45deg, #1D8348, #28B463); padding: 10px; border-radius: 10px;'>
                <h2 style='color: #D5F5E3; text-align: center;'>Settings</h2>
            </div>
        """, unsafe_allow_html=True)

        # Fetch exchange rates
        rates = fetch_exchange_rates()
        currencies = list(rates.keys())

        from_currency = st.selectbox("From", currencies)
        to_currency = st.selectbox("To", currencies)

    # Main conversion interface
    st.markdown("""
        <div style='background: #000000; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <h3 style='color: #FF5733;'>Convert Currency</h3>
        </div>
    """, unsafe_allow_html=True)

    amount = st.number_input("Enter amount to convert", value=0.0)

    if st.button("Convert!"):
        result = currency_converter(amount, from_currency, to_currency, rates)
        if result is not None:
            st.balloons()  # Celebration effect
            st.markdown(f"""
                <div class='success-message'>
                    <h3>🎉 Result:</h3>
                    <p>{amount} {from_currency} = {result:.4f} {to_currency}</p>
                </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 30px; padding: 20px; background: #000000; border-radius: 10px; color: #FFFFFF;'>
            <p>Made with Codehub with Ammar❤️ | Current time: {}</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
