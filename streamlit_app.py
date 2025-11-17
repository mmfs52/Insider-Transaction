import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "https://fb84f936ca48.ngrok-free.app/webhook-test/insider-purchases"

st.title("📈 Insider Signal")
st.write("ค้นหาธุรกรรมซื้อหุ้นของ Insider (Form 4)")

ticker = st.text_input("Ticker (เช่น AAPL, NVDA, TSLA)", "AAPL")

if st.button("ค้นหา"):
    url = BACKEND_URL
    params = {"symbol": ticker}

    with st.spinner("กำลังดึงข้อมูลจาก n8n..."):
        resp = requests.get(url, params=params)

    # 👇 เพิ่มสองบรรทัดนี้เพื่อตรวจ status + เนื้อหา
    st.write("DEBUG status:", resp.status_code)
    st.write("DEBUG body:", resp.text)

    if resp.status_code != 200:
        st.error("เกิดข้อผิดพลาดจาก backend")
    else:
        data = resp.json()
        purchases = data.get("purchases", [])

        if len(purchases) == 0:
            st.warning("ไม่พบการซื้อหุ้น (Purchase) จาก Insider")
        else:
            df = pd.DataFrame(purchases)
            st.dataframe(df)


