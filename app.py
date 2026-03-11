import streamlit as st
from supabase import create_client

# 1. إعدادات هوية التطبيق وتصميمه (CSS) لجعله يبدو احترافياً
st.set_page_config(page_title="Match AI | بدائل التجميل", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fff9fa; }
    h1, h2, h3 { color: #d63384 !important; font-family: 'Arial'; }
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        background-color: #ff4b6b;
        color: white;
        border: none;
        height: 3em;
        font-weight: bold;
    }
    .stButton>button:hover { background-color: #d63384; color: white; }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b6b;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. الربط بقاعدة البيانات باستخدام المفتاح الذي أرسلته
URL = "https://tblfgqeqryudpabwwhyc.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRibGZncWVxcnl1ZHBhYnd3aHljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzMyNjc4MzMsImV4cCI6MjA4ODg0MzgzM30.FexbPZYgH0cFq_xrysx89m6ZUNXjP6GKF7tqY5sbtlQ"
supabase = create_client(URL, KEY)

# 3. واجهة المستخدم الرئيسية
st.title("Match AI 🧬✨")
st.write("دليلكِ الذكي لبدائل منتجات العناية العالمية بأسعار توفيرية")

tabs = st.tabs(["🔍 البحث عن بديل", "💬 مجتمع Match", "💡 نصيحة اليوم"])

# --- التبويب الأول: البحث ---
with tabs[0]:
    st.subheader("ابحثي عن منتجكِ المفضل")
    search_query = st.text_input("", placeholder="مثلاً: Tatcha, Drunk Elephant...")
    
    if st.button("اكتشفي البديل الأوفر"):
        if search_query:
            try:
                res = supabase.table("products").select("*").ilike("name", f"%{search_query}%").execute()
                if res.data:
                    for item in res.data:
                        st.markdown(f"""
                        <div class="result-card">
                            <h4>✨ البديل لـ: {item['name']}</h4>
                            <p><b>الماركة الأرخص:</b> {item['brand']}</p>
                            <p><b>السعر:</b> {item['price']}$</p>
                            <p><b>المكونات:</b> {item['ingredients']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("عذراً، لم نجد هذا المنتج بعد. جربي البحث عن Tatcha!")
            except Exception:
                st.error("خطأ في الاتصال. تأكدي من إعدادات قاعدة البيانات.")

# --- التبويب الثاني: الدردشة ---
with tabs[1]:
    st.subheader("تجارب مشتركات Match")
    with st.form("chat_form", clear_on_submit=True):
        user_name = st.text_input("الاسم المستعار")
        user_msg = st.text_area("رسالتكِ...")
        submit = st.form_submit_button("نشر التعليق")
        
        if submit and user_name and user_msg:
            try:
                supabase.table("community_chat").insert({"username": user_name, "message": user_msg}).execute()
                st.rerun()
            except:
                st.error("فشل الإرسال.")

    st.divider()
    try:
        chats = supabase.table("community_chat").select("*").order("created_at", desc=True).limit(5).execute()
        for c in chats.data:
            with st.chat_message("user"):
                st.write(f"**{c['username']}**: {c['message']}")
    except:
        st.caption("الدردشة تتحدث...")

# --- التبويب الثالث: النصائح ---
with tabs[2]:
    st.info("💡 **نصيحة اليوم:** فيتامين C يعمل بفعالية مضاعفة عند وضعه تحت واقي الشمس صباحاً!")
    st.write("✅ شرب 8 أكواب ماء يومياً هو أول خطوة لجمال بشرتكِ.")
    
