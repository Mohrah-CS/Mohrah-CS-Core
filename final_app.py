import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. PERSISTENT STORAGE FUNCTIONS ---
def load_comments():
    if not os.path.exists("comments.json"):
        return [{"u": "Academic Support", "m": "Welcome to Mohrah's Lab! Your feedback is valued.", "t": "09:00 AM"}]
    try:
        with open("comments.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_comment(name, msg):
    comments = load_comments()
    comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
    with open("comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False)

# --- 3. SMART PERSISTENT VISITOR COUNTER ---
def get_total_visitors():
    file_path = "visitors.json"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump({"count": 1}, f)
        return 1
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        if 'has_counted_visit' not in st.session_state:
            data["count"] += 1
            st.session_state.has_counted_visit = True
            with open(file_path, "w") as f:
                json.dump(data, f)
        return data["count"]
    except:
        return 1

total_visitors = get_total_visitors()

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
        border-top: 2px solid #1e3a8a; background-color: #f8fafc; color: #1e3a8a;
    }
    .learning-card {
        background-color: #f8fafc; padding: 25px; border-radius: 15px; border-left: 6px solid #1e3a8a; margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .quiz-section {
        background-color: #ffffff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 15px;
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
st.sidebar.markdown(f"""<div class="visitor-badge">👁️ Total Visitors: {total_visitors}</div>""", unsafe_allow_html=True)
st.sidebar.write("---")

subject = st.sidebar.selectbox(
    "Choose a Module:",
    ["Home Page", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 7. MODULES ---
if subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    هذه المنصة هي **مبادرة طلابية تعليمية** تهدف إلى تحويل المفاهيم النظرية في علوم الحاسب إلى نماذج تفاعلية ملموسة.
    **المصدر العلمي (Academic Source):**
    جميع الدروس والأمثلة البرمجية المقدمة في هذه المنصة مستمدة من المناهج الأكاديمية المعتمدة في **جامعة تبوك**، ويتم تقديمها هنا لغرض الشرح والتوضيح وتسهيل الفهم.
    """)

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 PDA Comprehensive Study Guide")
    tab1, tab2 = st.tabs(["📖 Summary", "🧠 Quiz"])
    with tab1:
        st.markdown("""
        <div class="learning-card">
        <h3>1. Introduction to PDA</h3>
        <p>A PDA is a type of automata that uses a <b>Stack</b> for Context-Free Languages.</p>
        <h3>2. The 7-Tuple Definition</h3>
        <p>(Q, Σ, Γ, δ, q0, Z0, F)</p>
        <h3>3. Stack Operations</h3>
        <ul><li><b>Push:</b> Add to stack.</li><li><b>Pop:</b> Remove from stack.</li></ul>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("### Knowledge Quiz")
        q1 = st.radio("1. What memory does PDA use?", ["Queue", "Stack", "Array"])
        if st.button("Check Q1"):
            if q1 == "Stack": st.success("Correct!")
            else: st.error("Incorrect.")
        # ... (يمكن إضافة بقية الأسئلة الـ 6 هنا لضمان الشمولية)

elif subject == "Theory of Computation":
    st.markdown("### 🤖 PDA Simulator")
    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
        dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
        dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')
        dot.edge('S', 'q0'); dot.edge('q0', 'q0', label='a, Z0/AZ0'); dot.edge('q0', 'q1', label='b, A/ε'); dot.edge('q1', 'q1', label='b, A/ε'); dot.edge('q1', 'f', label='ε, Z0/Z0')
        return dot
    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        diagram_placeholder = st.empty()
        diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))
    with col_input:
        test_string = st.text_input("Enter String (e.g., aabb):", "aabb")
        sim_speed = st.slider("Speed:", 0.5, 2.0, 1.0)
        if st.button("Run Simulation 🚀"):
            stack, current_state, history, failed = ["Z0"], "q0", [], False
            table_placeholder = st.empty()
            for i, char in enumerate(test_string):
                action = "Push A" if char == 'a' else "Pop A"
                history.append({"Step": i+1, "Input": char, "State": current_state, "Stack": str(stack[::-1]), "Action": action})
                diagram_placeholder.graphviz_chart(generate_pda_diagram(current_state))
                table_placeholder.table(pd.DataFrame(history))
                if current_state == "q0":
                    if char == 'a': stack.append('A')
                    elif char == 'b' and len(stack) > 1: stack.pop(); current_state = "q1"
                    else: failed = True; break
                elif current_state == "q1":
                    if char == 'b' and len(stack) > 1: stack.pop()
                    else: failed = True; break
                time.sleep(sim_speed)
            if not failed and current_state == "q1" and len(stack) == 1:
                diagram_placeholder.graphviz_chart(generate_pda_diagram('accepted'))
                st.success("✅ Accepted")
            else: st.error("❌ Rejected")

elif subject == "Contact Developer":
    st.markdown("### 📧 Contact Details")
    st.info("Academic: 451000518@stu.ut.edu.sa")
    st.success("Personal: mohrah.atiiah@icloud.com")

elif subject == "Community Feedback":
    st.markdown("### 💬 Feedback Board")
    with st.form("f"):
        name = st.text_input("Name:")
        msg = st.text_area("Feedback:")
        if st.form_submit_button("Post"):
            if name and msg: save_comment(name, msg); st.success("Saved!")
    for c in reversed(load_comments()):
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small><br>{c['m']}</div>""", unsafe_allow_html=True)

# --- 8. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
            <br> Reuse or redistribution without permission is not allowed.
        </p>
    </div>
    """, unsafe_allow_html=True)