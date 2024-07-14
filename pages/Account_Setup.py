# Home.py
import streamlit as st
from models.credentials import Credentials

# Initialize the session state for credentials if it doesn't exist
if "credentials" not in st.session_state:
    st.session_state.credentials = Credentials()

st.title("Connect Account to Facebook")

st.write("Please provide your Facebook API credentials to connect your account.")

# Input fields for credentials
st.session_state.credentials.ACCESS_TOKEN = st.text_input(
    "Access Token", value=st.session_state.credentials.ACCESS_TOKEN, type="password"
)
st.session_state.credentials.AD_ACCOUNT_ID = st.text_input(
    "Ad Account ID", value=st.session_state.credentials.AD_ACCOUNT_ID
)
st.session_state.credentials.APP_ID = st.text_input(
    "App ID", value=st.session_state.credentials.APP_ID
)
st.session_state.credentials.APP_SECRET = st.text_input(
    "App Secret", value=st.session_state.credentials.APP_SECRET, type="password"
)

# Button to save and display credentials
if st.button("Save and Display Credentials"):
    st.write("Your credentials are:")
    st.write(f"Access Token: {st.session_state.credentials.ACCESS_TOKEN}")
    st.write(f"Ad Account ID: {st.session_state.credentials.AD_ACCOUNT_ID}")
    st.write(f"App ID: {st.session_state.credentials.APP_ID}")
    st.write(f"App Secret: {st.session_state.credentials.APP_SECRET}")

# Always display the credentials if they are set
if st.session_state.credentials.ACCESS_TOKEN:
    st.write("Current credentials:")
    st.write(f"Access Token: {st.session_state.credentials.ACCESS_TOKEN}")
    st.write(f"Ad Account ID: {st.session_state.credentials.AD_ACCOUNT_ID}")
    st.write(f"App ID: {st.session_state.credentials.APP_ID}")
    st.write(f"App Secret: {st.session_state.credentials.APP_SECRET}")
