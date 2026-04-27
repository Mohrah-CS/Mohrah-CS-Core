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
        background-color: #ffffff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 15px; margin-bottom: 20px;
    }
    h3 { color: #1e3a8a; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
    .highlight { color: #3b82f6; font-weight: bold; }
    .step-box {
        background-color: #eff6ff; border: 1px dashed #3b82f6; padding: 15px; border-radius: 10px; margin-top: 10px;
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
    ["Home Page", "Foundations of TOC", "DFA Explorer", "NFA Masterclass", "PDA Learning Hub", "Theory of Computation (Simulator)", "Contact Developer", "Community Feedback"]
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
    tab1, tab2, tab3, tab4, tab_q = st.tabs(["🔤 Alphabets", "📊 Sets", "⚙️ Functions", "🧠 Logic", "📝 Quiz (10 Qs)"])
    
    with tab1:
        st.markdown("""<div class="learning-card"><h3>Alphabets & Strings</h3><p>Σ is a finite set of symbols. Strings are sequences. ε is the empty string.</p></div>""", unsafe_allow_html=True)
    with tab2:
        st.markdown("""<div class="learning-card"><h3>Set Theory</h3><p>Union, Intersection, Power Sets, and Cartesian Products.</p></div>""", unsafe_allow_html=True)
    with tab3:
        st.markdown("""<div class="learning-card"><h3>Functions</h3><p>Mapping from Domain to Codomain. Transition functions are the heart of Automata.</p></div>""", unsafe_allow_html=True)
    with tab4:
        st.markdown("""<div class="learning-card"><h3>Boolean Logic</h3><p>AND, OR, NOT, XOR, and De Morgan's Laws.</p></div>""", unsafe_allow_html=True)
    
    with tab_q:
        st.markdown("### 📝 Foundations Quiz")
        questions = [
            ("What is Σ?", ["Alphabet", "Number", "Function"], "Alphabet"),
            ("Length of empty string ε?", ["0", "1", "Undefined"], "0"),
            ("Σ* includes ε?", ["Yes", "No", "Sometimes"], "Yes"),
            ("Intersection means?", ["Common elements", "All elements", "Difference"], "Common elements"),
            ("Power set of {a,b} size?", ["4", "2", "3"], "4"),
            ("Function domain is?", ["Input set", "Output set", "Relation"], "Input set"),
            ("NOT True is?", ["False", "True", "Null"], "False"),
            ("A ∪ B is?", ["Union", "Intersection", "Subset"], "Union"),
            ("Σ+ is Σ* minus?", ["ε", "0", "1"], "ε"),
            ("De Morgan's ¬(A∨B) is?", ["¬A∧¬B", "¬A∨¬B", "A∧B"], "¬A∧¬B")
        ]
        score = 0
        for i, (q, opts, ans) in enumerate(questions):
            user_ans = st.radio(f"{i+1}. {q}", opts, key=f"fq_{i}")
            if user_ans == ans: score += 1
        if st.button("Submit Foundations Quiz"): st.success(f"Your Score: {score}/10")

elif subject == "DFA Explorer":
    st.markdown("## ⚙️ Deterministic Finite Automata (DFA)")
    tab_info, tab_viz, tab_sim, tab_q = st.tabs(["📖 Definition", "🎨 Visuals", "🚀 Simulator", "📝 Quiz (10 Qs)"])
    
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <h3>DFA Definition & Acceptance</h3>
        <p>DFA = (Q, Σ, δ, q0, F). Deterministic means 1 transition per symbol.</p>
        <div class="step-box">
        <b>💡 How to determine Acceptance in DFA?</b>  

        1. Start at q0 (Start State).  

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
            dfa1 = graphviz.Digraph(); dfa1.attr(rankdir='LR', bgcolor='transparent')
            dfa1.node('S', '', shape='none'); dfa1.node('q_even', 'Even (q0)', shape='doublecircle', color='green'); dfa1.node('q_odd', 'Odd (q1)', shape='circle')
            dfa1.edge('S', 'q_even'); dfa1.edge('q_even', 'q_odd', label='0'); dfa1.edge('q_odd', 'q_even', label='0'); dfa1.edge('q_even', 'q_even', label='1'); dfa1.edge('q_odd', 'q_odd', label='1')
            st.graphviz_chart(dfa1)
        with col2:
            st.markdown("#### 2. Starts with 'a'")
            dfa2 = graphviz.Digraph(); dfa2.attr(rankdir='LR', bgcolor='transparent')
            dfa2.node('S', '', shape='none'); dfa2.node('q0', 'Start', shape='circle'); dfa2.node('q1', 'Accept', shape='doublecircle', color='green'); dfa2.node('q2', 'Trap', shape='circle', color='red')
            dfa2.edge('S', 'q0'); dfa2.edge('q0', 'q1', label='a'); dfa2.edge('q0', 'q2', label='b'); dfa2.edge('q1', 'q1', label='a, b'); dfa2.edge('q2', 'q2', label='a, b')
            st.graphviz_chart(dfa2)

    with tab_sim:
        st.markdown("### 🚀 DFA Simulator (Pattern '101')")
        def generate_dfa_sim_diagram(active_state):
            dot = graphviz.Digraph(); dot.attr(rankdir='LR', size='8,5', bgcolor='transparent')
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
            dfa_input_str = st.text_input("Enter Binary String:", "11010", key="dfa_in")
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

    with tab_q:
        st.markdown("### 📝 DFA Quiz")
        dfa_qs = [
            ("DFA stands for?", ["Deterministic", "Dynamic", "Digital"], "Deterministic"),
            ("How many transitions per state?", ["Exactly one per symbol", "Many", "Zero"], "Exactly one per symbol"),
            ("Start state count?", ["Exactly 1", "At least 1", "Many"], "Exactly 1"),
            ("Final state symbol?", ["Double circle", "Single circle", "Square"], "Double circle"),
            ("δ: Q × Σ → ?", ["Q", "Σ", "F"], "Q"),
            ("Can DFA have ε-transitions?", ["No", "Yes", "Only at start"], "No"),
            ("DFA is a 5-tuple?", ["Yes", "No", "7-tuple"], "Yes"),
            ("Trap state is for?", ["Rejected paths", "Accepted paths", "Start"], "Rejected paths"),
            ("Is DFA a type of NFA?", ["Yes", "No", "Opposite"], "Yes"),
            ("DFA recognizes?", ["Regular Languages", "CFG", "CSL"], "Regular Languages")
        ]
        d_score = 0
        for i, (q, opts, ans) in enumerate(dfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dq_{i}")
            if u_ans == ans: d_score += 1
        if st.button("Submit DFA Quiz"): st.success(f"Your Score: {d_score}/10")

elif subject == "NFA Masterclass":
    st.markdown("## 🌀 NFA Masterclass & Conversions")
    tab_nfa, tab_diff, tab_conv, tab_sim, tab_q = st.tabs(["📖 NFA Info", "⚖️ DFA vs NFA", "🔄 Conversions", "🚀 Simulator", "📝 Quiz (10 Qs)"])
    
    with tab_nfa:
        st.markdown("""
        <div class="learning-card">
        <h3>Non-deterministic Finite Automata (NFA)</h3>
        <p>An NFA is a theoretical model where for a given state and input symbol, the machine can move to <b>multiple states</b> simultaneously.</p>
        <ul>
            <li><b>ε-Transitions:</b> Can change state without any input.</li>
            <li><b>Acceptance:</b> Accepted if <i>at least one</i> path leads to a final state.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tab_diff:
        st.markdown("### ⚖️ Comparison: DFA vs NFA")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**DFA (Deterministic)**")
            st.write("- Exactly one transition per symbol.")
            st.write("- No ε-transitions allowed.")
            st.write("- Easier to implement in hardware.")
        with col2:
            st.success("**NFA (Non-deterministic)**")
            st.write("- Multiple transitions per symbol.")
            st.write("- ε-transitions are allowed.")
            st.write("- Easier to design for complex languages.")

    with tab_conv:
        st.markdown("### 🔄 Conversion Techniques")
        st.subheader("1. NFA to DFA (Subset Construction)")
        col_text, col_graph = st.columns([1, 1])
        with col_text:
            st.markdown("""
            <div class="step-box">
            <b>Steps to Convert NFA → DFA:</b>  

            1. <b>Start State:</b> Find the ε-closure of the NFA start state.  

            2. <b>Transitions:</b> For each new DFA state (which is a set of NFA states), find all reachable NFA states for each symbol.  

            3. <b>New States:</b> If a reachable set is new, add it to the DFA states list.  

            4. <b>Final States:</b> Any DFA state (set) that contains at least one NFA final state becomes a DFA final state.
            </div>
            """, unsafe_allow_html=True)
        with col_graph:
            g = graphviz.Digraph(); g.attr(rankdir='LR', bgcolor='transparent')
            g.node("NFA", "{q0, q1}", shape="circle")
            g.node("DFA", "[q0, q1]", shape="box", color="blue")
            g.edge("NFA", "DFA", label="Subset Construction")
            st.graphviz_chart(g)
            
        st.subheader("2. DFA to NFA")
        st.markdown("""
        <div class="step-box">
        <b>The Rule:</b> Every DFA is already an NFA by definition. A DFA is simply an NFA with the restriction of having exactly one transition per symbol and no ε-transitions.
        </div>
        """, unsafe_allow_html=True)

    with tab_sim:
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
                n_table = st.empty()
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
                    n_table.table(pd.DataFrame(n_history))
                    time.sleep(n_speed)
                if 'q2' in current_states: st.success("✅ Accepted!")
                else: st.error("❌ Rejected!")

    with tab_q:
        st.markdown("### 📝 NFA Quiz")
        nfa_qs = [
            ("NFA allows ε-transitions?", ["Yes", "No", "Only in DFA"], "Yes"),
            ("NFA to DFA conversion name?", ["Subset Construction", "LIFO", "FIFO"], "Subset Construction"),
            ("Is NFA more powerful than DFA?", ["No, same power", "Yes", "No, less"], "No, same power"),
            ("NFA acceptance?", ["At least 1 path", "All paths", "No paths"], "At least 1 path"),
            ("Can NFA have 0 transitions for a symbol?", ["Yes", "No", "Never"], "Yes"),
            ("NFA is a 5-tuple?", ["Yes", "No", "6-tuple"], "Yes"),
            ("ε-closure includes?", ["Self + ε paths", "Only ε paths", "Only self"], "Self + ε paths"),
            ("NFA is easier to design?", ["Yes", "No", "Same"], "Yes"),
            ("DFA is a subset of NFA?", ["Yes", "No", "Equal"], "Yes"),
            ("NFA recognizes?", ["Regular Languages", "CFG", "CSL"], "Regular Languages")
        ]
        n_score = 0
        for i, (q, opts, ans) in enumerate(nfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"nq_{i}")
            if u_ans == ans: n_score += 1
        if st.button("Submit NFA Quiz"): st.success(f"Your Score: {n_score}/10")

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 Pushdown Automata (PDA)")
    tab_info, tab_q = st.tabs(["📖 PDA Info", "📝 Quiz (10 Qs)"])
    with tab_info:
        st.markdown("""<div class="learning-card"><h3>PDA = FA + Stack</h3><p>Uses LIFO memory. Recognizes Context-Free Languages.</p></div>""", unsafe_allow_html=True)
    with tab_q:
        pda_qs = [("Memory?", ["Stack", "Queue", "None"], "Stack"), ("Language?", ["CFL", "Regular", "CSL"], "CFL"), ("Tuple count?", ["7", "5", "6"], "7"), ("LIFO means?", ["Last In First Out", "First In First Out", "None"], "Last In First Out"), ("Acceptance?", ["Final State/Empty Stack", "Only Final", "Only Empty"], "Final State/Empty Stack"), ("Stack top?", ["Z0", "ε", "X"], "Z0"), ("Push adds?", ["To top", "To bottom", "Middle"], "To top"), ("Pop removes?", ["From top", "From bottom", "Middle"], "From top"), ("NPDA vs DPDA?", ["NPDA more powerful", "Same", "DPDA more"], "NPDA more powerful"), ("PDA recognizes a^n b^n?", ["Yes", "No", "Maybe"], "Yes")]
        p_score = 0
        for i, (q, opts, ans) in enumerate(pda_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"pq_{i}")
            if u_ans == ans: p_score += 1
        if st.button("Submit PDA Quiz"): st.success(f"Your Score: {p_score}/10")

elif subject == "Theory of Computation (Simulator)":
    st.markdown("### 🤖 PDA Simulator (a^n b^n)")
    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph(); dot.attr(rankdir='LR', size='8,5', bgcolor='transparent')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
        dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
        dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')
        dot.edge('S', 'q0'); dot.edge('q0', 'q0', label='a, Z0 / AZ0\\na, A / AA'); dot.edge('q0', 'q1', label='b, A / ε'); dot.edge('q1', 'q1', label='b, A / ε'); dot.edge('q1', 'f', label='ε, Z0 / Z0')
        return dot
    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        diagram_placeholder = st.empty(); diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))
    with col_input:
        test_string = st.text_input("Enter Input String (e.g., aabb):", "aabb", key="pda_in")
        sim_speed = st.slider("Speed:", 0.5, 2.0, 1.0, key="pda_sp")
        if st.button("Run PDA Simulation 🚀"):
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
    st.markdown("### 💬 Feedback Board")
    with st.form("feedback_form"):
        name = st.text_input("Name:"); msg = st.text_area("Feedback:")
        if st.form_submit_button("Post"):
            if name and msg: save_comment(name, msg); st.success("Comment saved!")
    st.markdown("---")
    for c in reversed(load_comments()):
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small>  
{c['m']}</div>""", unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
        </p>
    </div>
    """, unsafe_allow_html=True)