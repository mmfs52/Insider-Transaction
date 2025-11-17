import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "https://xxxxx.ngrok-free.app/webhook-test/insider-purchases"

...

if st.button("ค้นหา"):
    url = BACKEND_URL
    params = {"symbol": ticker}  # <-- ส่งชื่อ parameter ว่า symbol

    with st.spinner("กำลังยิงไปที่ n8n..."):
        resp = requests.get(url, params=params)

    st.write("DEBUG status:", resp.status_code)
    st.write("DEBUG body:", resp.text)


