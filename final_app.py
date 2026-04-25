import streamlit as st
import time
import graphviz
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. PERSISTENT STORAGE FUNCTIONS ---
def load_comments():
    if not os.path.exists("comments.txt"):
        return [{"u": "Academic Support", "m": "Welcome to Mohrah's Lab!", "t": "09:00 AM"}]
    with open("comments.txt", "r", encoding="utf-8") as f:
        import json
        return json.load(f)

def save_comment(name, msg):
    comments = load_comments()
    comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
    with open("comments.txt", "w", encoding="utf-8") as f:
        import json
        json.dump(comments, f, ensure_ascii=False)

# --- 3. VISITOR COUNTER ---
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1 # يبدأ من 1 الآن
else:
    st.session_state.visitor_count += 1

# --- 4. ADVANCED STYLING ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-box {
        text-align: center; padding: 40px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white; border-radius: 20px; margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .visitor-badge {
        padding: 10px; background-color: #f1f5f9; border-radius: 10px;
        text-align: center; border: 1px solid #1e3a8a; color: #1e3a8a; font-weight: bold;
    }
    .comment-box {
        padding: 15px; border-radius: 10px; background-color: #f8f9fa;
        border-left: 5px solid #1e3a8a; margin-bottom: 10px; color: #1e3a8a;
    }
    .footer {
        text-align: center; padding: 30px; margin-top: 60px;
        border-top: 3px solid #1e3a8a; background-color: #f1f5f9; color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. HEADER ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: clamp(24px, 5vw, 48px); font-weight: bold; letter-spacing: 2px;">THE JEWEL OF COMPUTER SCIENCE</div>
        <div style="font-size: clamp(16px, 3vw, 24px); font-weight: 300; margin-top: 15px; border-top: 1px solid rgba(255,255,255,0.3); display: inline-block; padding-top: 10px;">
            MOHRAH ATIAH AL-JUHANI | مهره عطيه الجهني
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 6. SIDEBAR ---
st.sidebar.title("💎 Navigation")
st.sidebar.markdown(f"""<div class="visitor-badge">👁️ Visitors: {st.session_state.visitor_count}</div>""", unsafe_allow_html=True)
st.sidebar.write("---")

subject = st.sidebar.selectbox(
    "Choose a Module:",
    ["Home Page", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 7. MODULES ---
if subject == "Contact Developer":
    st.markdown("### 📧 Contact the Developer")
    st.info("🏛️ Academic: 451000518@stu.ut.edu.sa")
    st.success("📩 Personal: mohrah.atiiah@icloud.com")

elif subject == "Community Feedback":
    st.markdown("### 💬 Community Discussion Board")
    with st.form("feedback_form"):
        name = st.text_input("Name:")
        msg = st.text_area("Feedback:")
        if st.form_submit_button("Post"):
            if name and msg:
                save_comment(name, msg)
                st.success("Comment saved permanently!")
    
    st.markdown("---")
    all_comments = load_comments()
    for c in reversed(all_comments):
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small><br>{c['m']}</div>""", unsafe_allow_html=True)

elif subject == "Theory of Computation":
    st.markdown("### 🤖 Theory of Computation: PDA Simulator")
    st.info("💡 المحتوى العلمي مبني على مناهج جامعة تبوك.")
    # (كود الـ PDA يظل كما هو ليعمل المختبر)

elif subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.write("هذه المنصة هي مبادرة طلابية تعليمية مستمدة من مناهج جامعة تبوك.")

# --- 8. FOOTER (Updated to 2026) ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px;">📖 المحتوى العلمي مستمد من مناهج جامعة تبوك.</p>
    </div>
    """, unsafe_allow_html=True)