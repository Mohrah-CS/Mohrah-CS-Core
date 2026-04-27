import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="MOHRAH CS CORE", layout="wide", page_icon="💎")

# --- 2. PERSISTENT STORAGE ---
def load_comments():
    if not os.path.exists("comments.json"):
        return [{"u": "Academic Support", "m": "Welcome to Mohrah's Lab!", "t": "09:00 AM"}]
    try:
        with open("comments.json", "r", encoding="utf-8") as f: return json.load(f)
    except: return []

def save_comment(name, msg):
    comments = load_comments()
    comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
    with open("comments.json", "w", encoding="utf-8") as f: json.dump(comments, f, ensure_ascii=False)

# --- 3. VISITOR COUNTER ---
if 'visitor_count' not in st.session_state: st.session_state.visitor_count = 1
else: st.session_state.visitor_count += 1

# --- 4. STYLING ---
st.markdown("""
    <style>
    .header-box { text-align: center; padding: 40px; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); color: white; border-radius: 20px; margin-bottom: 30px; }
    .visitor-badge { padding: 10px; background-color: #f1f5f9; border-radius: 10px; text-align: center; border: 1px solid #1e3a8a; color: #1e3a8a; font-weight: bold; }
    .comment-box { padding: 15px; border-radius: 10px; background-color: #f8f9fa; border-left: 5px solid #1e3a8a; margin-bottom: 10px; }
    .footer { text-align: center; padding: 30px; margin-top: 60px; border-top: 2px solid #1e3a8a; background-color: #f8fafc; }
    .state-active { color: #3b82f6; font-weight: bold; border: 2px solid #3b82f6; padding: 5px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- 5. HEADER ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: 40px; font-weight: bold;">THE JEWEL OF COMPUTER SCIENCE</div>
        <div style="font-size: 20px; margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.3); padding-top: 10px;">
            MOHRAH ATIAH AL-JUHANI | مهره عطيه الجهني
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 6. SIDEBAR ---
st.sidebar.title("💎 Navigation")
st.sidebar.markdown(f"""<div class="visitor-badge">👁️ Visitors: {st.session_state.visitor_count}</div>""", unsafe_allow_html=True)
subject = st.sidebar.selectbox("Choose a Module:", ["Home Page", "Theory of Computation", "Contact Developer", "Community Feedback"])

# --- 7. MODULES ---
if subject == "Theory of Computation":
    st.markdown("### 🤖 Advanced PDA Step-by-Step Simulator")
    st.info("هذا المحاكي المطور يتيح لك تتبع حركة الآلة (States) وتغير الـ Stack في كل خطوة.")

    def get_pda_map(current):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('start', '', shape='none')
        # States styling
        s0_attr = {'color': 'blue', 'penwidth': '4'} if current == 'q0' else {}
        s1_attr = {'color': 'blue', 'penwidth': '4'} if current == 'q1' else {}
        sf_attr = {'color': 'green', 'penwidth': '4'} if current == 'accepted' else {}
        
        dot.node('q0', 'q0 (Push)', shape='circle', **s0_attr)
        dot.node('q1', 'q1 (Pop)', shape='circle', **s1_attr)
        dot.node('f', 'Accept', shape='doublecircle', **sf_attr)
        
        dot.edge('start', 'q0')
        dot.edge('q0', 'q0', label='a, Z0/AZ0\na, A/AA')
        dot.edge('q0', 'q1', label='b, A/ε')
        dot.edge('q1', 'q1', label='b, A/ε')
        dot.edge('q1', 'f', label='ε, Z0/Z0')
        return dot

    col_viz, col_ctrl = st.columns([2, 1])
    
    with col_ctrl:
        test_str = st.text_input("Enter String (e.g., aaabbb):", "aabb")
        speed = st.slider("Simulation Speed (sec):", 0.5, 2.0, 1.0)
        run_btn = st.button("Start Tracking 🚀")

    if run_btn:
        stack, state, history = ["Z0"], "q0", []
        placeholder_graph = col_viz.empty()
        placeholder_table = st.empty()
        
        failed = False
        for i, char in enumerate(test_str):
            # Record step
            action = "Push A" if char == 'a' else "Pop A"
            history.append({"Step": i+1, "Input": char, "State": state, "Stack": str(stack[::-1]), "Action": action})
            
            # Update Viz
            placeholder_graph.graphviz_chart(get_pda_map(state))
            placeholder_table.table(pd.DataFrame(history))
            
            # Logic
            if state == "q0":
                if char == 'a': stack.append('A')
                elif char == 'b' and len(stack) > 1: stack.pop(); state = "q1"
                else: failed = True; break
            elif state == "q1":
                if char == 'b' and len(stack) > 1: stack.pop()
                else: failed = True; break
            time.sleep(speed)

        if not failed and state == "q1" and len(stack) == 1:
            placeholder_graph.graphviz_chart(get_pda_map('accepted'))
            history.append({"Step": "Final", "Input": "ε", "State": "Accept", "Stack": "['Z0']", "Action": "Success"})
            placeholder_table.table(pd.DataFrame(history))
            st.success("✅ String Accepted! The stack is empty (only Z0 remains).")
        else:
            st.error("❌ String Rejected! The machine could not reach the accept state.")

elif subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.write("هذه المنصة مبادرة طلابية من الكلية الجامعية بالوجه لتطوير مهارات علوم الحاسب.")

elif subject == "Contact Developer":
    st.markdown("### 📧 Contact Details")
    st.info("Academic: 451000518@stu.ut.edu.sa")
    st.success("Personal: mohrah.atiiah@icloud.com")

elif subject == "Community Feedback":
    st.markdown("### 💬 Feedback")
    with st.form("f"):
        n = st.text_input("Name")
        m = st.text_area("Message")
        if st.form_submit_button("Send"):
            save_comment(n, m); st.success("Saved!")
    for c in reversed(load_comments()):
        st.markdown(f"**{c['u']}**: {c['m']} <small>({c['t']})</small>")

# --- 8. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
            <br> Reuse or redistribution without permission is not allowed.
        </p>
    </div>
    """, unsafe_allow_html=True)