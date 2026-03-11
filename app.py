import streamlit as st
from supabase import create_client

# 1. إعدادات التصميم
st.set_page_config(page_title="Match AI", page_icon="✨")
st.markdown("<style>.stApp { background-color: #fff9fa; } .stButton>button { background-color: #ff4b6b; color: white; border-radius: 20px; }</style>", unsafe_allow_html=True)

# 2. بيانات الربط الصحيحة
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30.FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"
supabase = create_client(URL, KEY)

# 3. واجهة التطبيق
st.title("Match AI 🧬✨")
tabs = st.tabs(["🔍 البحث عن بديل", "💬 المجتمع"])

with tabs[0]:
    search = st.text_input("ابحثي عن منتج (مثلاً: C-Firma)")
    if st.button("اكتشفي البديل الأوفر"):
        if search:
            try:
                # التأكد من البحث في جدول products
                res = supabase.table("products").select("*").ilike("name", f"%{search}%").execute()
                if res.data:
                    for item in res.data:
                        st.success(f"✨ البديل: {item['name']}")
                        st.info(f"💰 السعر: {item['price']}$")
                else:
                    st.warning("لم نجد هذا المنتج بعد في قاعدة البيانات.")
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")

with tabs[1]:
    st.subheader("دردشة المجتمع")
    user = st.text_input("الاسم المستعار")
    msg = st.text_area("رسالتكِ هنا...")
    if st.button("إرسال"):
        if user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.rerun()
            except Exception as e:
                st.error(f"فشل الإرسال: {e}")
    
    st.divider()
    try:
        # عرض آخر 5 رسائل
        chats = supabase.table("community_chat").select("*").order("created_at", desc=True).limit(5).execute()
        if chats.data:
            for c in chats.data:
                st.write(f"👤 **{c['username']}**: {c['message']}")
    except:
        st.write("الدردشة قيد التحديث...")
        
