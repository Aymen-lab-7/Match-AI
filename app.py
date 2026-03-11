import streamlit as st
from supabase import create_client

# استبدل بالبيانات التي نسختها من Supabase Settings -> API
URL = "tblfgqeqryudpabwwhyc"
KEY = "tblfgqeqryudpabwwhyc"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Match AI", layout="centered")

st.title("Match AI 🧬")

menu = st.tabs(["🔍 البحث", "💬 المجتمع"])

with menu[0]:
    search = st.text_input("ابحثي عن منتج (مثلاً: C-Firma)")
    if st.button("ابحث عن البديل"):
        res = supabase.table("products").select("*").ilike("name", f"%{search}%").execute()
        if res.data:
            for item in res.data:
                st.success(f"البديل: {item['name']}")
                st.info(f"السعر: {item['price']}$")
        else:
            st.warning("لم نجد البديل بعد!")

with menu[1]:
    st.subheader("دردشة مجتمع Match")
    user = st.text_input("الاسم")
    msg = st.text_area("الرسالة")
    if st.button("إرسال"):
        if user and msg:
            supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
            st.rerun()
    
    chats = supabase.table("community_chat").select("*").order("created_at", desc=True).limit(5).execute()
    for c in chats.data:
        st.write(f"👤 **{c['username']}**: {c['message']}")
      
