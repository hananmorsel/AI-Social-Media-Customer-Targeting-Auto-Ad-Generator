import streamlit as st
import pandas as pd
from ad_generator import generate_ad
from persona_analyzer import build_persona
from message_generator import generate_message
from posting_optimizer import recommend_post_times
from performance_predictor import predict_performance

st.set_page_config(page_title="AI Social Media Ad Assistant", layout="wide")

st.title("📣 AI Social Media Ad Assistant")
st.subheader("Grow your business using AI-powered marketing tools")

st.sidebar.header("Business Information")
business_name = st.sidebar.text_input("Business Name")
product = st.sidebar.text_area("Describe your product or service")
audience = st.sidebar.text_area("Describe your target audience")
platform = st.sidebar.selectbox("Select Platform", ["Instagram", "Facebook", "TikTok", "LinkedIn"])

st.header("🧠 Customer Persona Generator")
if st.button("Generate Persona"):
    persona = build_persona(product, audience)
    st.write(persona)

st.header("💬 AI Customer Message Generator")
tone = st.selectbox("Select Tone", ["Friendly", "Professional", "Luxury", "Persuasive", "Excited"])
if st.button("Generate Outreach Message"):
    msg = generate_message(product, audience, tone, platform)
    st.write(msg)

st.header("🎯 AI Social Media Ad Generator")
cta = st.text_input("Call To Action", value="Shop Now")
if st.button("Generate Ad"):
    ad = generate_ad(product, audience, platform, cta)
    st.write(ad)

st.header("⏰ Best Time To Post")
uploaded_file = st.file_uploader("Upload engagement CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    result = recommend_post_times(df)
    st.write(result)

st.header("📈 Engagement Performance Predictor")
ad_text = st.text_area("Paste your ad text for prediction")
if st.button("Predict Performance"):
    score = predict_performance(ad_text)
    st.metric("Predicted Engagement Score", score)
