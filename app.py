import streamlit as st
from supabase import create_client

# إعدادات الواجهة
st.set_page_config(page_title="Match AI", page_icon="✨")

# بيانات الربط (استخدم الرابط والمفتاح كما هما هنا)
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = (
    "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30."
    "FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"
)

supabase = create_client(URL, KEY)

st.title("Match AI 🧬✨")
tab1, tab2 = st.tabs(["🔍 البحث", "💬 المجتمع"])

with tab1:
    search = st.text_input("ابحثي عن منتج (مثلاً: C-Firma)")
    if st.button("اكتشفي البديل"):
        if search:
            try:
                # محاولة جلب البيانات مباشرة
                res = supabase.table("products").select("*").ilike("name", f"%{search}%").execute()
                if res.data:
                    for item in res.data:
                        st.success(f"✨ البديل لـ {item['name']}")
                        st.info(f"الماركة: {item['brand']} | السعر: {item['price']}$")
                else:
                    st.warning("المنتج غير متوفر حالياً في قاعدة البيانات.")
            except Exception as e:
                st.error(f"خطأ في الوصول للجداول: {e}")

with tab2:
    st.subheader("دردشة المجتمع")
    user = st.text_input("الاسم")
    msg = st.text_area("الرسالة")
    if st.button("نشر"):
        if user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.rerun()
            except Exception as e:
                st.error("فشل الإرسال، تحققي من إعدادات Supabase")
                        
