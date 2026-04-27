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
        return [{"u": "Academic Support", "m": "Welcome to Mohrah's Lab!", "t": "09:00 AM"}]

def save_comment(name, msg):
    comments = load_comments()
    comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
    with open("comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False)

# --- 3. VISITOR COUNTER ---
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1 
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
        border-top: 2px solid #1e3a8a; background-color: #f8fafc; color: #1e3a8a;
    }
    .quiz-card {
        background-color: #f1f5f9; padding: 20px; border-radius: 15px; border-left: 5px solid #3b82f6; margin-bottom: 20px;
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
    ["Home Page", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 7. MODULES ---
if subject == "PDA Learning Hub":
    st.markdown("### 📚 PDA Comprehensive Summary")
    col_summary, col_quiz = st.columns(2)
    
    with col_summary:
        st.markdown("""
        <div class="quiz-card">
        <h4>What is a Pushdown Automata (PDA)?</h4>
        <p>A PDA is a type of automata that employs a <b>Stack</b> as auxiliary memory. It is used to recognize <b>Context-Free Languages (CFLs)</b>.</p>
        <hr>
        <h4>Core Logic (LIFO):</h4>
        <ul>
            <li><b>Push:</b> Adding a symbol to the top of the stack.</li>
            <li><b>Pop:</b> Removing the top symbol from the stack.</li>
            <li><b>Stack Memory:</b> Allows the machine to remember information (like counting the number of 'a's to match with 'b's).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_quiz:
        st.markdown("<h4>🧠 Quick Knowledge Quiz</h4>", unsafe_allow_html=True)
        q1 = st.radio("1. What is the main difference between FA and PDA?", ["Number of states", "Presence of a Stack", "Processing speed"])
        if st.button("Check Q1"):
            if q1 == "Presence of a Stack": st.success("Correct! 🎯")
            else: st.error("Try again! The Stack is the key memory.")
            
        st.write("---")
        q2 = st.radio("2. What does LIFO stand for in Stack logic?", ["Last In, First Out", "Long Input, Fast Output", "Level In, Final Out"])
        if st.button("Check Q2"):
            if q2 == "Last In, First Out": st.success("Correct! 🎯")
            else: st.error("Incorrect. It means the last item added is the first one removed.")

elif subject == "Theory of Computation":
    st.markdown("### 🤖 Theory of Computation: PDA Simulator")
    st.info("💡 هذا المحاكي يتيح لك تتبع حركة الآلة (States) وتغير الـ Stack خطوة بخطوة.")
    
    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
        dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
        dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')
        dot.edge('S', 'q0')
        dot.edge('q0', 'q0', label='a, Z0 / AZ0\\na, A / AA')
        dot.edge('q0', 'q1', label='b, A / ε')
        dot.edge('q1', 'q1', label='b, A / ε')
        dot.edge('q1', 'f', label='ε, Z0 / Z0')
        return dot

    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        diagram_placeholder = st.empty()
        diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))
    with col_input:
        test_string = st.text_input("Enter Input String (e.g., aabb):", "aabb")
        sim_speed = st.slider("Simulation Speed (sec):", 0.5, 2.0, 1.0)
        run_btn = st.button("Run Simulation 🚀")

    if run_btn:
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
            history.append({"Step": "End", "Input": "ε", "State": "Accept", "Stack": "['Z0']", "Action": "Success"})
            table_placeholder.table(pd.DataFrame(history))
            st.success("✅ Result: String Accepted")
        else: st.error("❌ Result: String Rejected")

elif subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    هذه المنصة هي **مبادرة طلابية تعليمية** تهدف إلى تحويل المفاهيم النظرية في علوم الحاسب إلى نماذج تفاعلية ملموسة.
    **المصدر العلمي (Academic Source):**
    جميع الدروس والأمثلة البرمجية المقدمة في هذه المنصة مستمدة من المناهج الأكاديمية المعتمدة في **جامعة تبوك**، ويتم تقديمها هنا لغرض الشرح والتوضيح وتسهيل الفهم.
    """)

elif subject == "Contact Developer":
    st.markdown("### 📧 Contact the Developer / تواصل مع المبرمجة")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🏛️ **Academic Email**")
        st.code("451000518@stu.ut.edu.sa")
    with col2:
        st.success("📩 **Personal Email**")
        st.code("mohrah.atiiah@icloud.com")

elif subject == "Community Feedback":
    st.markdown("### 💬 Community Discussion Board")
    with st.form("feedback_form"):
        name = st.text_input("Name:")
        msg = st.text_area("Feedback:")
        if st.form_submit_button("Post"):
            if name and msg: save_comment(name, msg); st.success("Comment saved!")
    st.markdown("---")
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