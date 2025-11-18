import streamlit as st
import requests

BACKEND_URL = "https://b501f01d3de3.ngrok-free.app/webhook/insider-purchases"
# ตอนย้ายไป production อย่าลืมเปลี่ยนเป็น Production URL นะครับ

st.title("📈 Insider Signal")
st.write("ค้นหาธุรกรรมซื้อหุ้นของ Insider (Form 4)")

ticker = st.text_input("Ticker (เช่น AAPL, NVDA, TSLA)", "AAPL")

if st.button("ค้นหา"):
    url = BACKEND_URL
    params = {"symbol": ticker.strip().upper()}

    with st.spinner("กำลังดึงข้อมูลจาก n8n..."):
        resp = requests.get(url, params=params)

    if resp.status_code != 200:
        st.error("เกิดข้อผิดพลาดจาก backend (status code: {})".format(resp.status_code))
    else:
        try:
            data = resp.json()
        except Exception:
            st.error("ข้อมูลที่ได้รับไม่ใช่ JSON ที่ถูกต้อง")
        else:
            purchases = data.get("purchases", [])  # list ที่ผ่านการ filter แล้วจาก n8n

            if len(purchases) == 0:
                st.warning("ไม่พบการซื้อหุ้น (Purchase) จาก Insider")
            else:
                # ถ้าอยากให้เรียบจริง ๆ เอาแค่บรรทัดเดียวนี้ก็พอ
                st.success("พบการซื้อหุ้น (Purchase) จาก Insider")

                # ถ้าในอนาคตอยากโชว์จำนวนด้วย ก็ปลด comment ได้
                # st.success(f"พบการซื้อหุ้น (Purchase) จาก Insider จำนวน {len(purchases)} รายการ")

