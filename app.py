import streamlit as st
from supabase import create_client

# 1. واجهة التطبيق وتصميم بسيط
st.set_page_config(page_title="Match AI", page_icon="✨")
st.markdown("<style>.stApp { background-color: #fff9fa; } .stButton>button { background-color: #ff4b6b; color: white; border-radius: 20px; }</style>", unsafe_allow_html=True)

# 2. بيانات الربط المباشرة (استخدام المفتاح الذي نسخته أنت بالكامل)
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30.FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"

try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error("خطأ في الاتصال الأولي")

# 3. محتوى التطبيق
st.title("Match AI 🧬✨")
tab1, tab2 = st.tabs(["🔍 البحث", "💬 المجتمع"])

with tab1:
    product = st.text_input("ابحثي عن منتج")
    if st.button("اكتشفي البديل"):
        if product:
            try:
                res = supabase.table("products").select("*").ilike("name", f"%{product}%").execute()
                if res.data:
                    for item in res.data:
                        st.success(f"✨ البديل: {item['name']}")
                else:
                    st.warning("غير موجود حالياً")
            except:
                st.error("تأكدي من وجود جدول products في Supabase")

with tab2:
    st.subheader("دردشة المجتمع")
    user = st.text_input("الاسم")
    msg = st.text_area("الرسالة")
    if st.button("إرسال"):
        if user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.success("تم الإرسال!")
                st.rerun()
            except:
                st.error("تأكدي من وجود جدول community_chat في Supabase")
    
    st.divider()
    try:
        chats = supabase.table("community_chat").select("*").order("created_at", desc=True).limit(5).execute()
        for c in chats.data:
            st.write(f"👤 **{c['username']}**: {c['message']}")
    except:
        st.write("لا توجد رسائل بعد")
        
