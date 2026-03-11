import streamlit as st
from supabase import create_client

# 1. إعدادات الهوية البصرية والتصميم
st.set_page_config(page_title="Match AI", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fff9fa; }
    h1, h2, h3 { color: #d63384 !important; text-align: center; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ff4b6b;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #d63384; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. بيانات الربط الصحيحة (تأكد من نسخ المفتاح كاملاً)
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30.FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"
supabase = create_client(URL, KEY)

# 3. هيكل التطبيق
st.title("Match AI 🧬✨")

tabs = st.tabs(["🔍 البحث عن بديل", "💬 المجتمع"])

# --- تبويب البحث ---
with tabs[0]:
    st.subheader("ابحثي عن منتجكِ المفضل")
    search = st.text_input("", placeholder="اكتبي اسم المنتج (مثلاً: C-Firma)...", key="search_input")
    if st.button("اكتشفي البديل الأوفر"):
        if search:
            try:
                res = supabase.table("products").select("*").ilike("name", f"%{search}%").execute()
                if res.data:
                    for item in res.data:
                        with st.expander(f"✨ البديل لـ {item['name']}"):
                            st.write(f"**الماركة:** {item['brand']}")
                            st.write(f"**السعر:** {item['price']}$")
                            st.write(f"**المكونات:** {item['ingredients']}")
                else:
                    st.warning("لم نجد هذا المنتج في قاعدة البيانات حالياً.")
            except Exception:
                st.error("خطأ في الاتصال بقاعدة البيانات. تأكدي من إعدادات Supabase.")

# --- تبويب المجتمع ---
with tabs[1]:
    st.subheader("تجارب مشتركات Match")
    with st.form("chat_form", clear_on_submit=True):
        user = st.text_input("الاسم المستعار")
        msg = st.text_area("رسالتكِ...")
        submit = st.form_submit_button("إرسال")
        
        if submit and user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.success("تم النشر بنجاح!")
                st.rerun()
            except Exception:
                st.error("فشل الإرسال، تأكدي من إعدادات قاعدة البيانات.")

    st.divider()
    try:
        chats = supabase.table("community_chat").select("*").order("created_at", desc=True).limit(5).execute()
        if chats.data:
            for c in chats.data:
                with st.chat_message("user"):
                    st.write(f"**{c['username']}**: {c['message']}")
    except:
        st.caption("الدردشة قيد التحديث...")
        
