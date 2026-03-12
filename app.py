import streamlit as st
from supabase import create_client

# إعدادات الواجهة
st.set_page_config(page_title="Match AI", page_icon="✨")

# استخدام متغيرات واضحة جداً لتجنب أخطاء النسخ
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
# هذا هو المفتاح الكامل الذي صورته لي، وضعته في سطر واحد طويل
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30.FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"

# الربط
try:
    supabase = create_client(URL, KEY)
except:
    st.error("مشكلة في الربط")

st.title("Match AI 🧬✨")
tab1, tab2 = st.tabs(["🔍 البحث", "💬 المجتمع"])

with tab1:
    search = st.text_input("ابحثي عن منتج")
    if st.button("اكتشفي البديل"):
        if search:
            try:
                # سطر البحث
                res = supabase.table("products").select("*").ilike("name", f"%{search}%").execute()
                if res.data:
                    for item in res.data:
                        st.success(f"✅ البديل: {item['name']}")
                else:
                    st.warning("المنتج غير موجود في الجداول")
            except Exception as e:
                # هذه الرسالة ستظهر إذا كان المفتاح لا يزال به مشكلة
                st.error(f"عذراً، لا يزال هناك خطأ في المفتاح: {e}")

with tab2:
    st.subheader("دردشة المجتمع")
    user = st.text_input("الاسم")
    msg = st.text_area("الرسالة")
    if st.button("إرسال"):
        if user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.rerun()
            except:
                st.error("فشل الإرسال")
                
