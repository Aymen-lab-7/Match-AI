import streamlit as st
from supabase import create_client

# استبدل بالبيانات التي نسختها من Supabase Settings -> API
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = "tblfgqeqryudpabwwhyc"
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Match AI", layout="centered")

st.title("Match AI 🧬")

menu = st.tabs(["🔍 البحث", "💬 المجتمع"])

with menu[1]:
    st.subheader("💬 دردشة مجتمع Match")
    user = st.text_input("الاسم المستعار")
    msg = st.text_area("اكتبي رسالتكِ هنا...")
    
    if st.button("إرسال"):
        if user and msg:
            try:
                supabase.table("community_chat").insert({"username": user, "message": msg}).execute()
                st.success("تم إرسال رسالتكِ بنجاح! ✨")
                st.rerun()
            except Exception as e:
                st.error(f"عذراً، هناك مشكلة تقنية: {e}")

    st.divider()
    st.write("🕒 أحدث الرسائل:")
    try:
        # محاولة عرض آخر 5 رسائل بدون ترتيب معقد لتجنب الأخطاء
        chats = supabase.table("community_chat").select("*").limit(5).execute()
        if chats.data:
            for c in chats.data:
                st.info(f"👤 **{c.get('username', 'مجهولة')}**: {c.get('message', '')}")
        else:
            st.write("لا توجد رسائل بعد، كوني أول من يشارك! 🌸")
    except:
        st.warning("الدردشة قيد التحديث، يمكنكِ المحاولة لاحقاً.")
        
