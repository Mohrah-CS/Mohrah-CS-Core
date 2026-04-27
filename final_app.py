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

# --- 3. ADVANCED STYLING ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-box {
        text-align: center; padding: 40px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white; border-radius: 20px; margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
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
    .concept-badge {
        background-color: #1e3a8a; color: white; padding: 4px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; display: inline-block; margin-bottom: 10px;
    }
    .quiz-section {
        background-color: #ffffff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 15px;
    }
    h3 { color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
    .highlight { color: #3b82f6; font-weight: bold; }
    .step-box {
        background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 10px; border-radius: 10px; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: clamp(24px, 5vw, 48px); font-weight: bold; letter-spacing: 2px;">THE JEWEL OF COMPUTER SCIENCE</div>
        <div style="font-size: clamp(16px, 3vw, 24px); font-weight: 300; margin-top: 15px; border-top: 1px solid rgba(255,255,255,0.3); display: inline-block; padding-top: 10px;">
            MOHRAH ATIAH AL-JUHANI | مهره عطيه الجهني
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
st.sidebar.title("💎 Navigation")
st.sidebar.write("---")

subject = st.sidebar.selectbox(
    "Choose a Module:",
    ["Home Page", "Foundations of TOC", "DFA Explorer", "NFA Masterclass", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 6. MODULES ---
if subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    هذه المنصة هي **مبادرة طلابية تعليمية** تهدف إلى تحويل المفاهيم النظرية في علوم الحاسب إلى نماذج تفاعلية ملموسة.
    **المصدر العلمي (Academic Source):**
    جميع الدروس والأمثلة البرمجية المقدمة في هذه المنصة مستمدة من المناهج الأكاديمية المعتمدة في **جامعة تبوك**، ويتم تقديمها هنا لغرض الشرح والتوضيح وتسهيل الفهم.
    """)

elif subject == "Foundations of TOC":
    st.markdown("## 📘 Foundations of Theory of Computation")
    tab1, tab2, tab3, tab4 = st.tabs(["🔤 Alphabets & Strings", "📊 Set Theory", "⚙️ Functions", "🧠 Boolean Logic"])
    with tab1:
        st.markdown("""<div class="learning-card"><h3>Alphabets, Strings, and Languages</h3><ul><li><b>Alphabet (Σ):</b> Finite set of symbols.</li><li><b>String (w):</b> Sequence of symbols.</li><li><b>Empty String (ε):</b> Zero length string.</li></ul></div>""", unsafe_allow_html=True)
    with tab2:
        st.markdown("""<div class="learning-card"><h3>Set Theory</h3><ul><li>Union, Intersection, Complement, Power Set.</li></ul></div>""", unsafe_allow_html=True)
    with tab3:
        st.markdown("""<div class="learning-card"><h3>Functions</h3><ul><li>Domain, Codomain, Range.</li></ul></div>""", unsafe_allow_html=True)
    with tab4:
        st.markdown("""<div class="learning-card"><h3>Boolean Logic</h3><ul><li>AND, OR, NOT, XOR.</li></ul></div>""", unsafe_allow_html=True)

elif subject == "DFA Explorer":
    st.markdown("## ⚙️ Deterministic Finite Automata (DFA)")
    tab_info, tab_viz, tab_sim, tab_quiz = st.tabs(["📖 DFA Definition", "🎨 Visual Examples", "🚀 DFA Simulator", "🧠 DFA Quiz"])
    
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <h3>What is a DFA?</h3>
        <p>A <b>DFA</b> is a 5-tuple (Q, Σ, δ, q0, F). It is <b>Deterministic</b> because for every state and symbol, there is exactly ONE transition.</p>
        <div class="step-box">
        <b>💡 How to determine Acceptance in DFA?</b>  

        1. Start at q0.  

        2. Read the input string symbol by symbol.  

        3. Follow the unique transition for each symbol.  

        4. After the LAST symbol, if the machine is in a state <b>q ∈ F</b> (Final State), the string is <b>Accepted</b>. Otherwise, it is <b>Rejected</b>.
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab_viz:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 1. Even Number of '0's")
            dfa1 = graphviz.Digraph()
            dfa1.attr(rankdir='LR', bgcolor='transparent')
            dfa1.node('S', '', shape='none'); dfa1.node('q_even', 'Even (q0)', shape='doublecircle', color='green'); dfa1.node('q_odd', 'Odd (q1)', shape='circle')
            dfa1.edge('S', 'q_even'); dfa1.edge('q_even', 'q_odd', label='0'); dfa1.edge('q_odd', 'q_even', label='0'); dfa1.edge('q_even', 'q_even', label='1'); dfa1.edge('q_odd', 'q_odd', label='1')
            st.graphviz_chart(dfa1)
        with col2:
            st.markdown("#### 2. Starts with 'a'")
            dfa2 = graphviz.Digraph()
            dfa2.attr(rankdir='LR', bgcolor='transparent')
            dfa2.node('S', '', shape='none'); dfa2.node('q0', 'Start', shape='circle'); dfa2.node('q1', 'Accept', shape='doublecircle', color='green'); dfa2.node('q2', 'Trap', shape='circle', color='red')
            dfa2.edge('S', 'q0'); dfa2.edge('q0', 'q1', label='a'); dfa2.edge('q0', 'q2', label='b'); dfa2.edge('q1', 'q1', label='a, b'); dfa2.edge('q2', 'q2', label='a, b')
            st.graphviz_chart(dfa2)

    with tab_sim:
        st.markdown("### 🚀 DFA Interactive Simulator (Pattern '101')")
        def generate_dfa_sim_diagram(active_state):
            dot = graphviz.Digraph()
            dot.attr(rankdir='LR', size='8,5', bgcolor='transparent')
            dot.node('S', '', shape='none')
            states = {'q0': {'label': 'Start', 'shape': 'circle'}, 'q1': {'label': 'Got 1', 'shape': 'circle'}, 'q2': {'label': 'Got 10', 'shape': 'circle'}, 'q3': {'label': 'Got 101 (Accept)', 'shape': 'doublecircle'}}
            for node, attr in states.items():
                color = '#3b82f6' if active_state == node else 'black'
                dot.node(node, attr['label'], shape=attr['shape'], color=color, penwidth='4' if active_state == node else '1')
            dot.edge('S', 'q0'); dot.edge('q0', 'q0', label='0'); dot.edge('q0', 'q1', label='1'); dot.edge('q1', 'q1', label='1'); dot.edge('q1', 'q2', label='0'); dot.edge('q2', 'q0', label='0'); dot.edge('q2', 'q3', label='1'); dot.edge('q3', 'q3', label='0, 1')
            return dot
        col_sim_graph, col_sim_input = st.columns([2, 1])
        with col_sim_graph:
            dfa_placeholder = st.empty(); dfa_placeholder.graphviz_chart(generate_dfa_sim_diagram('q0'))
        with col_sim_input:
            dfa_input_str = st.text_input("Enter Binary String:", "11010")
            dfa_speed = st.slider("Simulation Speed:", 0.5, 3.0, 1.5)
            if st.button("Start DFA Simulation ⚡"):
                current_state, dfa_history = 'q0', []
                dfa_table_placeholder = st.empty()
                transitions = {'q0': {'0': 'q0', '1': 'q1'}, 'q1': {'0': 'q2', '1': 'q1'}, 'q2': {'0': 'q0', '1': 'q3'}, 'q3': {'0': 'q3', '1': 'q3'}}
                for i, char in enumerate(dfa_input_str):
                    prev_state = current_state
                    current_state = transitions[prev_state][char]
                    dfa_history.append({"Step": i + 1, "Input": char, "From": prev_state, "To": current_state})
                    dfa_placeholder.graphviz_chart(generate_dfa_sim_diagram(current_state))
                    dfa_table_placeholder.table(pd.DataFrame(dfa_history))
                    time.sleep(dfa_speed)
                if current_state == 'q3': st.success("✅ Accepted!")
                else: st.error("❌ Rejected!")

    with tab_quiz:
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        dq1 = st.radio("1. How many transitions per state in DFA (Σ={0,1})?", ["One", "Two", "Unlimited"])
        if st.button("Check DFA Q1"):
            if dq1 == "Two": st.success("Correct!")
        st.markdown('</div>', unsafe_allow_html=True)

elif subject == "NFA Masterclass":
    st.markdown("## 🌀 Non-deterministic Finite Automata (NFA)")
    tab_nfa_info, tab_diff, tab_conv, tab_nfa_sim, tab_nfa_quiz = st.tabs(["📖 NFA Definition", "⚖️ DFA vs NFA", "🔄 Conversion", "🚀 NFA Simulator", "🧠 NFA Quiz"])
    
    with tab_nfa_info:
        st.markdown("""<div class="learning-card"><h3>What is an NFA?</h3><ul><li>Multiple transitions for one symbol.</li><li>ε-Transitions (no input needed).</li><li>Accepts if AT LEAST ONE path leads to a final state.</li></ul></div>""", unsafe_allow_html=True)

    with tab_diff:
        st.markdown("### ⚖️ Comparison: DFA vs NFA (Ends with '01')")
        col_d, col_n = st.columns(2)
        with col_d:
            st.subheader("DFA (Complex)")
            d_comp = graphviz.Digraph(); d_comp.attr(rankdir='LR', bgcolor='transparent')
            d_comp.node('S', '', shape='none'); d_comp.node('q0', 'q0'); d_comp.node('q1', 'q1'); d_comp.node('q2', 'q2', shape='doublecircle', color='green')
            d_comp.edge('S', 'q0'); d_comp.edge('q0', 'q0', label='1'); d_comp.edge('q0', 'q1', label='0'); d_comp.edge('q1', 'q1', label='0'); d_comp.edge('q1', 'q2', label='1'); d_comp.edge('q2', 'q1', label='0'); d_comp.edge('q2', 'q0', label='1')
            st.graphviz_chart(d_comp)
        with col_n:
            st.subheader("NFA (Simple)")
            n_comp = graphviz.Digraph(); n_comp.attr(rankdir='LR', bgcolor='transparent')
            n_comp.node('S', '', shape='none'); n_comp.node('q0', 'q0'); n_comp.node('q1', 'q1'); n_comp.node('q2', 'q2', shape='doublecircle', color='green')
            n_comp.edge('S', 'q0'); n_comp.edge('q0', 'q0', label='0,1'); n_comp.edge('q0', 'q1', label='0'); n_comp.edge('q1', 'q2', label='1')
            st.graphviz_chart(n_comp)

    with tab_conv:
        st.markdown("### 🔄 Conversion Techniques")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""<div class="learning-card"><h4>1. NFA to DFA (Subset Construction)</h4><div class="step-box">1. Start with NFA start state set.  
2. Find transitions for each set.  
3. Final states are sets containing NFA final states.</div></div>""", unsafe_allow_html=True)
            conv1 = graphviz.Digraph(); conv1.attr(rankdir='LR'); conv1.node('N', '{q0}'); conv1.node('D', '[q0, q1]', shape='box', color='blue'); conv1.edge('N', 'D', label='Convert'); st.graphviz_chart(conv1)
        with c2:
            st.markdown("""<div class="learning-card"><h4>2. DFA to NFA</h4><div class="step-box">Every DFA is already an NFA. No changes needed!</div></div>""", unsafe_allow_html=True)

    with tab_nfa_sim:
        st.markdown("### 🚀 NFA Simulator (Ends with '01')")
        def gen_nfa_diag(active_states):
            dot = graphviz.Digraph(); dot.attr(rankdir='LR', bgcolor='transparent')
            dot.node('S', '', shape='none')
            nodes = {'q0': 'Start', 'q1': 'Saw 0', 'q2': 'Accept (01)'}
            for n, l in nodes.items():
                color = '#3b82f6' if n in active_states else 'black'
                dot.node(n, l, shape='doublecircle' if n == 'q2' else 'circle', color=color, penwidth='4' if n in active_states else '1')
            dot.edge('S', 'q0'); dot.edge('q0', 'q0', label='0,1'); dot.edge('q0', 'q1', label='0'); dot.edge('q1', 'q2', label='1')
            return dot
        col_g, col_i = st.columns([2, 1])
        with col_g:
            nfa_placeholder = st.empty(); nfa_placeholder.graphviz_chart(gen_nfa_diag(['q0']))
        with col_i:
            n_input = st.text_input("Enter String (0/1):", "101", key="n_in")
            n_speed = st.slider("Speed:", 0.5, 3.0, 1.5, key="n_sp")
            if st.button("Run NFA Simulation"):
                current_states = {'q0'}
                n_history = []
                for i, char in enumerate(n_input):
                    next_states = set()
                    for s in current_states:
                        if s == 'q0':
                            next_states.add('q0')
                            if char == '0': next_states.add('q1')
                        elif s == 'q1' and char == '1': next_states.add('q2')
                    n_history.append({"Step": i+1, "Input": char, "Active States": str(list(next_states))})
                    current_states = next_states
                    nfa_placeholder.graphviz_chart(gen_nfa_diag(current_states))
                    st.table(pd.DataFrame(n_history))
                    time.sleep(n_speed)
                if 'q2' in current_states: st.success("✅ Accepted!")
                else: st.error("❌ Rejected!")

    with tab_nfa_quiz:
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        nq1 = st.radio("1. Can NFA have multiple transitions for one symbol?", ["Yes", "No"])
        if st.button("Check NFA Q1"):
            if nq1 == "Yes": st.success("Correct!")
        st.markdown('</div>', unsafe_allow_html=True)

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 Pushdown Automata (PDA)")
    # (PDA Content...)

elif subject == "Theory of Computation":
    st.markdown("### 🤖 PDA Simulator")
    # (PDA Simulator Content...)

elif subject == "Contact Developer":
    st.markdown("### 📧 Contact")
    st.info("451000518@stu.ut.edu.sa")

elif subject == "Community Feedback":
    st.markdown("### 💬 Feedback")
    # (Feedback Content...)

st.markdown("""<div class="footer"><p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p></div>""", unsafe_allow_html=True)