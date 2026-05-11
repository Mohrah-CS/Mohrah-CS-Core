import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE - Ultimate Edition v11",
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

# --- 3. ADVANCED STYLING ---
st.markdown("""
<style>
.main { background-color: #ffffff; }
.header-box {
    text-align: center; padding: 50px;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: white; border-radius: 25px; margin-bottom: 40px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
}
.learning-card {
    background-color: #ffffff; padding: 35px; border-radius: 20px; 
    border-right: 8px solid #1e3a8a; border-left: 8px solid #1e3a8a;
    margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    line-height: 1.8;
}
.concept-badge {
    background-color: #1e3a8a; color: white; padding: 6px 18px; border-radius: 25px; 
    font-size: 14px; font-weight: bold; display: inline-block; margin-bottom: 15px;
}
.step-box {
    background-color: #f0f9ff; border: 2px solid #bae6fd; padding: 20px; 
    border-radius: 15px; margin: 20px 0; color: #0369a1;
}
.info-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 20px;
}
.info-item {
    background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;
}
h2, h3 { color: #1e3a8a; font-weight: 800; }
.comment-box {
    background-color: #f8fafc; padding: 15px; border-radius: 10px; 
    border: 1px solid #e2e8f0; margin-bottom: 15px;
}
.footer {
    text-align: center; padding: 40px; margin-top: 80px;
    border-top: 3px solid #1e3a8a; background-color: #f1f5f9; color: #0f172a;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class="header-box">
    <div style="font-size:40px;font-weight:900;">THE JEWEL OF COMPUTER SCIENCE</div>
    <div>MOHRAH ATIAH AL-JUHANI</div>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("Navigation")

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home Page"

main_subject = st.sidebar.selectbox(
    "Select Course:",
    ["Home Page", "Theory of Computation", "Operating Systems"]
)

if main_subject == "Theory of Computation":
    subject = st.sidebar.selectbox(
        "Select Lesson:",
        ["Foundations of TOC", "DFA Explorer", "NFA Masterclass"]
    )
    st.session_state.current_page = subject

elif main_subject == "Operating Systems":
    subject = st.sidebar.selectbox(
        "Select Lesson:",
        ["Introduction to OS", "Process Management", "Memory Management", "Storage & I/O"]
    )
    st.session_state.current_page = subject

else:
    st.session_state.current_page = "Home Page"

page = st.session_state.current_page

# =========================
# HOME
# =========================
if page == "Home Page":
    st.markdown("## Welcome to CS Portal")

# =========================
# FOUNDATIONS OF TOC
# =========================
elif page == "Foundations of TOC":
    st.markdown("## 📘 Foundations")

    st.markdown("""
    <div class="learning-card">
    <div class="concept-badge">Module 1</div>
    <h3>Theory of Computation</h3>
    <p>Study of computation models and formal languages.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>Alphabets</h3>
    <p>Finite set of symbols Σ = {0,1}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>Strings</h3>
    <p>Sequence of symbols over alphabet</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>Languages</h3>
    <p>Set of strings over Σ*</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DFA EXPLORER (START)
# =========================
elif page == "DFA Explorer":
    st.markdown("## ⚙️ DFA")

    st.markdown("""
    <div class="learning-card">
    <h3>DFA Definition</h3>
    <p>Q, Σ, δ, q0, F</p>
    </div>
    """, unsafe_allow_html=True)

    dfa = graphviz.Digraph()
    dfa.node("q0")
    dfa.node("q1", shape="doublecircle")
    dfa.edge("q0","q1",label="1")

    st.graphviz_chart(dfa)
    # =========================
# NFA MASTERCLASS
# =========================
elif page == "NFA Masterclass":
    st.markdown("## 🧠 NFA")

    st.markdown("""
    <div class="learning-card">
    <h3>Non-Deterministic Finite Automata</h3>
    <p>Allows multiple transitions + ε-moves</p>
    </div>
    """, unsafe_allow_html=True)

    nfa = graphviz.Digraph()
    nfa.node("q0")
    nfa.node("q1")
    nfa.node("q2", shape="doublecircle")

    nfa.edge("q0", "q0", label="0,1")
    nfa.edge("q0", "q1", label="0")
    nfa.edge("q1", "q2", label="1")

    st.graphviz_chart(nfa)

# =========================
# REGULAR EXPRESSIONS
# =========================
elif page == "Regular Expressions":
    st.markdown("## 🧩 Regular Expressions")

    st.markdown("""
    <div class="learning-card">
    <h3>Operations</h3>
    <ul>
        <li>Union: R1 ∪ R2</li>
        <li>Concatenation: R1R2</li>
        <li>Kleene Star: R*</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>Example</h3>
    <p>(0 ∪ 1)* 00 (0 ∪ 1)*</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DFA TO RE + PUMPING LEMMA
# =========================
elif page == "DFA to RE & Pumping Lemma":
    st.markdown("## 🔄 DFA to RE")

    st.markdown("""
    <div class="learning-card">
    <h3>State Elimination Method</h3>
    <p>Convert DFA → GNFA → RE</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🧪 Pumping Lemma")

    st.markdown("""
    <div class="learning-card">
    <p>If L is regular → ∃ p such that s = xyz</p>
    <ul>
        <li>|y| > 0</li>
        <li>|xy| ≤ p</li>
        <li>xyⁱz ∈ L</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CFG & CNF
# =========================
elif page == "CFG & Chomsky Form":
    st.markdown("## 📜 CFG")

    st.markdown("""
    <div class="learning-card">
    <h3>Context Free Grammar</h3>
    <p>G = (V, Σ, R, S)</p>
    </div>
    """, unsafe_allow_html=True)

    cfg = graphviz.Digraph()
    cfg.node("S")
    cfg.node("A")
    cfg.edge("S", "A")
    cfg.edge("A", "S")

    st.graphviz_chart(cfg)

    st.markdown("## 📐 CNF")
    st.markdown("""
    <div class="learning-card">
    <p>A → BC or A → a</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PDA
# =========================
elif page == "PDA & CFL Theory":
    st.markdown("## ⚙️ PDA")

    st.markdown("""
    <div class="learning-card">
    <h3>Pushdown Automata</h3>
    <p>FA + Stack</p>
    </div>
    """, unsafe_allow_html=True)

    pda = graphviz.Digraph()
    pda.node("q0")
    pda.node("q1")
    pda.edge("q0", "q1", label="push")
    pda.edge("q1", "q0", label="pop")

    st.graphviz_chart(pda)
    
# =========================
# TURING MACHINE
# =========================
elif page == "Turing Machines & Algorithms":
    st.markdown("## 📟 Turing Machine")

    st.markdown("""
    <div class="learning-card">
    <h3>Definition</h3>
    <p>7-tuple: (Q, Σ, Γ, δ, q0, qaccept, qreject)</p>
    </div>
    """, unsafe_allow_html=True)

    tm = graphviz.Digraph()
    tm.node("Tape")
    tm.node("Head")
    tm.node("Control")

    tm.edge("Control", "Head", label="read/write")
    tm.edge("Head", "Tape", label="move L/R")

    st.graphviz_chart(tm)

    st.markdown("## 🛑 Decidability")

    st.markdown("""
    <div class="learning-card">
    <ul>
        <li>Decidable: halts on all inputs</li>
        <li>Recognizable: may loop</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🔄 Variants")
    st.markdown("""
    <div class="learning-card">
    <ul>
        <li>Multi-tape TM</li>
        <li>Non-deterministic TM</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ⚙️ Encoding")
    st.markdown("""
    <div class="learning-card">
    <p>⟨M⟩ = encoding of machine</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# OPERATING SYSTEMS (FULL FIXED SECTION)
# =========================
elif page == "Introduction to OS":

    st.markdown("## ⚙️ Operating Systems")

    st.markdown("""
    <div class="learning-card">
    <h3>What is an Operating System?</h3>
    <p>An OS manages hardware and software resources.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>Main Functions</h3>
    <ul>
        <li>Process Management</li>
        <li>Memory Management</li>
        <li>File System</li>
        <li>I/O Management</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
    <h3>OS Types</h3>
    <ul>
        <li>Batch OS</li>
        <li>Time Sharing</li>
        <li>Distributed OS</li>
        <li>Real-Time OS</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PLACEHOLDERS (OS MODULES)
# =========================
elif page == "Process Management":
    st.info("Process Management under development")

elif page == "Memory Management":
    st.info("Memory Management under development")

elif page == "Storage & I/O":
    st.info("Storage & I/O under development")

# =========================
# FEEDBACK SYSTEM (FIXED + COMPLETE)
# =========================
elif page == "Community Feedback":

    st.markdown("## 💬 Feedback System")

    with st.form("form"):
        name = st.text_input("Name")
        msg = st.text_area("Message")

        submit = st.form_submit_button("Send")

        if submit:
            if name and msg:
                save_comment(name, msg)
                st.success("Saved successfully")

    st.markdown("---")

    comments = load_comments()

    for c in reversed(comments):
        st.markdown(f"""
        <div class="comment-box">
            <b>{c['u']}</b> - {c['t']}<br>
            {c['m']}
        </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
    <h4>© 2026 Mohrah Atiah Al-Juhani</h4>
    <p>All Rights Reserved - Academic Project</p>
</div>
""", unsafe_allow_html=True)