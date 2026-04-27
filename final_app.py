import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE - Ultimate Edition",
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
    .highlight { color: #2563eb; font-weight: bold; background: #eff6ff; padding: 2px 6px; border-radius: 4px; }
    .footer {
        text-align: center; padding: 40px; margin-top: 80px;
        border-top: 3px solid #1e3a8a; background-color: #f1f5f9; color: #0f172a;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: clamp(28px, 6vw, 56px); font-weight: 900; letter-spacing: 3px;">THE JEWEL OF COMPUTER SCIENCE</div>
        <div style="font-size: clamp(18px, 3vw, 28px); font-weight: 300; margin-top: 20px; border-top: 2px solid rgba(255,255,255,0.4); display: inline-block; padding-top: 15px;">
            MOHRAH ATIAH AL-JUHANI | مهره عطيه الجهني
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
st.sidebar.title("💎 Academic Navigation")
st.sidebar.write("---")
subject = st.sidebar.selectbox(
    "Select Academic Module:",
    ["Home Page", "Foundations of TOC", "DFA Explorer", "NFA Masterclass", "PDA Learning Hub", "Theory of Computation (Simulator)", "Contact Developer", "Community Feedback"]
)

# --- 6. MODULES ---

if subject == "Home Page":
    st.markdown("## 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    <div class="learning-card">
    <h3>عن المنصة / About the Platform</h3>
    <p>هذه المنصة هي <b>مبادرة طلابية تعليمية متقدمة</b> تهدف إلى سد الفجوة بين المفاهيم الرياضية المجردة والتطبيقات البرمجية التفاعلية في مجال نظرية الحوسبة (Theory of Computation).</p>
    <p><b>المصدر العلمي (Academic Source):</b>  

    تم استقاء كافة المعلومات العلمية، التعريفات الرياضية، والنماذج التوضيحية من المناهج الأكاديمية المعتمدة في <b>جامعة تبوك</b>. تم تصميم المحتوى ليكون مرجعاً شاملاً يساعد الطلاب على فهم تعقيدات الأوتوماتا واللغات الرسمية.</p>
    <div class="info-grid">
        <div class="info-item"><b>🎯 الهدف:</b> تبسيط المفاهيم المعقدة مثل DFA, NFA, و PDA.</div>
        <div class="info-item"><b>🛠️ الأدوات:</b> محاكيات تفاعلية، رسومات بيانية حية، واختبارات تقييمية.</div>
        <div class="info-item"><b>📚 المحتوى:</b> يغطي من الأساسيات الرياضية إلى نماذج الحوسبة المتقدمة.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif subject == "Foundations of TOC":
    st.markdown("## 📘 Foundations of Theory of Computation")
    tab1, tab2, tab3, tab4, tab_q = st.tabs(["🔤 Alphabets & Strings", "📊 Set Theory", "⚙️ Functions", "🧠 Boolean Logic", "📝 Comprehensive Quiz"])
    
    with tab1:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.1</div>
        <h3>Alphabets, Strings, and Languages: The Building Blocks</h3>
        <p>In the world of computation, everything begins with an <b>Alphabet (Σ)</b>. An alphabet is a finite, non-empty set of symbols. For example, the binary alphabet is Σ = {0, 1}.</p>
        <h4>1. Strings (Words)</h4>
        <p>A <b>String</b> is a finite sequence of symbols chosen from Σ. 
        <ul>
            <li><b>Length |w|:</b> The number of symbols in string w. Example: |1011| = 4.</li>
            <li><b>Empty String (ε):</b> A unique string with length 0. It exists in every Σ*.</li>
            <li><b>Reverse (wᴿ):</b> If w = abc, then wᴿ = cba.</li>
            <li><b>Concatenation:</b> Joining two strings. If x = "ab" and y = "cd", then xy = "abcd".</li>
        </ul>
        </p>
        <h4>2. Powers of Alphabet</h4>
        <p>
            - <b>Σ⁰:</b> The set {ε}.  

            - <b>Σ*: (Kleene Closure)</b> The set of all possible strings over Σ, including ε. It is an infinite set.  

            - <b>Σ+: (Positive Closure)</b> Σ* excluding the empty string (Σ+ = Σ* - {ε}).
        </p>
        <h4>3. Languages</h4>
        <p>A <b>Language (L)</b> is a subset of Σ*. A language can be finite (L = {01, 11}) or infinite (L = {all strings starting with 0}).</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.2</div>
        <h3>Set Theory: The Mathematical Framework</h3>
        <p>Sets are collections of distinct objects. In TOC, we use sets to define states, alphabets, and languages.</p>
        <div class="info-grid">
            <div class="info-item"><b>Union (A ∪ B):</b> All elements in A or B.</div>
            <div class="info-item"><b>Intersection (A ∩ B):</b> Only elements common to both.</div>
            <div class="info-item"><b>Difference (A - B):</b> Elements in A but not in B.</div>
            <div class="info-item"><b>Complement (Ā):</b> Elements in the Universal set not in A.</div>
        </div>
        <h4>Advanced Concepts:</h4>
        <ul>
            <li><b>Power Set P(S):</b> The set of all subsets of S. If S has <i>n</i> elements, P(S) has 2ⁿ elements. This is crucial for NFA to DFA conversion.</li>
            <li><b>Cartesian Product (A × B):</b> The set of all ordered pairs (a, b). Used to define transition functions.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.3</div>
        <h3>Functions and Relations</h3>
        <p>A <b>Function (f: A → B)</b> is a rule that assigns each element in set A (Domain) to exactly one element in set B (Codomain).</p>
        <h4>Types of Functions in TOC:</h4>
        <ul>
            <li><b>Transition Function (δ):</b> The most important function in Automata. It maps (Current State × Input Symbol) → Next State.</li>
            <li><b>Total Function:</b> Defined for every possible input in the domain (Required for DFA).</li>
            <li><b>Partial Function:</b> Not defined for all inputs (Common in NFA).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.4</div>
        <h3>Boolean Logic: The Logic of Computation</h3>
        <p>Boolean logic deals with variables that have two values: <b>True (1)</b> and <b>False (0)</b>.</p>
        <div class="info-grid">
            <div class="info-item"><b>AND (∧):</b> Output is 1 only if both inputs are 1.</div>
            <div class="info-item"><b>OR (∨):</b> Output is 1 if at least one input is 1.</div>
            <div class="info-item"><b>NOT (¬):</b> Inverts the input.</div>
            <div class="info-item"><b>XOR (⊕):</b> Output is 1 if inputs are different.</div>
        </div>
        <h4>De Morgan's Laws:</h4>
        <p>1. ¬(A ∨ B) = ¬A ∧ ¬B  
2. ¬(A ∧ B) = ¬A ∨ ¬B</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 Foundations Quiz (10 Questions)")
        f_qs = [
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
        f_score = 0
        for i, (q, opts, ans) in enumerate(f_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"fq_u_{i}")
            if u_ans == ans: f_score += 1
        if st.button("Submit Foundations Quiz"): st.success(f"Your Score: {f_score}/10")

elif subject == "DFA Explorer":
    st.markdown("## ⚙️ Deterministic Finite Automata (DFA)")
    tab_info, tab_viz, tab_sim, tab_q = st.tabs(["📖 Deep Dive Definition", "🎨 Visual Examples", "🚀 Interactive Simulator", "📝 DFA Quiz (10 Qs)"])
    
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Formal Theory</div>
        <h3>The Architecture of DFA</h3>
        <p>A <b>Deterministic Finite Automata (DFA)</b> is the simplest model of computation. It has no memory other than its current state.</p>
        <h4>The 5-Tuple Definition:</h4>
        <ul>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (Alphabet).</li>
            <li><b>δ: (Transition Function)</b> δ: Q × Σ → Q. It defines the next state for every state-symbol pair.</li>
            <li><b>q0:</b> The unique start state (q0 ∈ Q).</li>
            <li><b>F:</b> The set of final or accepting states (F ⊆ Q).</li>
        </ul>
        <div class="step-box">
        <b>💡 How to determine Acceptance? (The Process)</b>  

        1. The machine starts at <b>q0</b>.  

        2. It reads the first symbol of the input string <i>w</i>.  

        3. It moves to the next state according to <b>δ</b>.  

        4. It repeats this for every symbol in <i>w</i>.  

        5. <b>Crucial Step:</b> After the last symbol is read, the machine checks its current state. If the state is in <b>F</b>, the string is <b>Accepted</b>. If not, it is <b>Rejected</b>.
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
        st.markdown("### 🚀 DFA Interactive Simulator (Pattern '101')")
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
            dfa_input_str = st.text_input("Enter Binary String:", "11010", key="dfa_in_u")
            dfa_speed = st.slider("Simulation Speed:", 0.5, 3.0, 1.5, key="dfa_sp_u")
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
        st.markdown("### 📝 DFA Quiz (10 Questions)")
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
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dq_u_{i}")
            if u_ans == ans: d_score += 1
        if st.button("Submit DFA Quiz"): st.success(f"Your Score: {d_score}/10")

elif subject == "NFA Masterclass":
    st.markdown("## 🌀 NFA Masterclass & Conversions")
    tab_nfa, tab_diff, tab_conv, tab_sim, tab_q = st.tabs(["📖 Comprehensive NFA Info", "⚖️ DFA vs NFA", "🔄 Conversion Steps", "🚀 NFA Simulator", "📝 NFA Quiz (10 Qs)"])
    
    with tab_nfa:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Advanced Theory</div>
        <h3>Non-deterministic Finite Automata (NFA)</h3>
        <p>An <b>NFA</b> is a more flexible model of computation. Unlike DFA, an NFA can be in multiple states at once, effectively "guessing" the correct path.</p>
        <h4>Why use NFA?</h4>
        <p>NFA is often much easier to design than DFA for complex languages. It allows for <b>ε-transitions</b> (moving without input) and <b>multiple choices</b> for the same symbol.</p>
        <h4>Formal Definition:</h4>
        <p>Like DFA, it's a 5-tuple (Q, Σ, δ, q0, F), but the transition function is different:  

        <span class="highlight">δ: Q × (Σ ∪ {ε}) → P(Q)</span>  

        This means it maps to the <b>Power Set</b> of states, allowing for zero or more next states.</p>
        <h4>Acceptance in NFA:</h4>
        <p>A string is accepted if there exists <b>at least one path</b> from the start state to any final state. If the machine can "find a way" to accept, it will.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab_diff:
        st.markdown("### ⚖️ Comparison: DFA vs NFA")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**DFA (Deterministic)**")
            st.write("- Exactly one transition per symbol.")
            st.write("- No ε-transitions allowed.")
            st.write("- Implementation is straightforward.")
        with col2:
            st.success("**NFA (Non-deterministic)**")
            st.write("- Zero, one, or many transitions per symbol.")
            st.write("- ε-transitions are allowed.")
            st.write("- Easier to design for humans.")

    with tab_conv:
        st.markdown("### 🔄 Conversion: NFA to DFA (Subset Construction)")
        col_text, col_graph = st.columns([1, 1])
        with col_text:
            st.markdown("""
            <div class="step-box">
            <b>The Step-by-Step Algorithm:</b>  

            1. <b>ε-closure:</b> For every state, find all states reachable using only ε-transitions.  

            2. <b>Start State:</b> The DFA start state is the ε-closure of the NFA start state.  

            3. <b>Transitions:</b> For each DFA state (which is a set of NFA states) and each symbol:  

               - Find all NFA states reachable from this set.  

               - Take the ε-closure of that result.  

               - This set becomes the next DFA state.  

            4. <b>Final States:</b> Any DFA state (set) that contains at least one NFA final state is marked as a Final State in the DFA.
            </div>
            """, unsafe_allow_html=True)
        with col_graph:
            g = graphviz.Digraph(); g.attr(rankdir='LR', bgcolor='transparent')
            g.node("NFA", "{q0, q1}", shape="circle")
            g.node("DFA", "[q0, q1]", shape="box", color="blue")
            g.edge("NFA", "DFA", label="Subset Construction")
            st.graphviz_chart(g)

    with tab_sim:
        st.markdown("### 🚀 NFA Interactive Simulator (Ends with '01')")
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
            n_input = st.text_input("Enter String (0/1):", "101", key="n_in_u")
            n_speed = st.slider("Speed:", 0.5, 3.0, 1.5, key="n_sp_u")
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
        st.markdown("### 📝 NFA Quiz (10 Questions)")
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
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"nq_u_{i}")
            if u_ans == ans: n_score += 1
        if st.button("Submit NFA Quiz"): st.success(f"Your Score: {n_score}/10")

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 Pushdown Automata (PDA)")
    tab_info, tab_q = st.tabs(["📖 Comprehensive PDA Info", "📝 PDA Quiz (10 Qs)"])
    
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Context-Free Theory</div>
        <h3>Pushdown Automata: Adding Memory</h3>
        <p>A <b>Pushdown Automata (PDA)</b> is essentially a Finite Automata with an added <b>Stack</b>. This stack provides infinite memory, but it can only be accessed in a <b>LIFO (Last-In, First-Out)</b> manner.</p>
        <h4>The 7-Tuple Definition:</h4>
        <p>PDA = (Q, Σ, Γ, δ, q0, Z0, F)</p>
        <ul>
            <li><b>Q:</b> States.</li>
            <li><b>Σ:</b> Input Alphabet.</li>
            <li><b>Γ:</b> Stack Alphabet (symbols that can be pushed).</li>
            <li><b>δ:</b> Transition Function (Q × (Σ ∪ {ε}) × Γ → P(Q × Γ*)).</li>
            <li><b>q0:</b> Start State.</li>
            <li><b>Z0:</b> Initial Stack Symbol.</li>
            <li><b>F:</b> Final States.</li>
        </ul>
        <div class="step-box">
        <b>Acceptance Criteria:</b>  

        - <b>Acceptance by Final State:</b> The machine ends in a state q ∈ F.  

        - <b>Acceptance by Empty Stack:</b> The machine finishes the input and the stack is completely empty.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 PDA Quiz (10 Questions)")
        pda_qs = [
            ("Memory structure in PDA?", ["Stack", "Queue", "Tape"], "Stack"),
            ("PDA recognizes which languages?", ["Context-Free", "Regular", "Recursive"], "Context-Free"),
            ("LIFO stands for?", ["Last In First Out", "Lead In Fast Out", "None"], "Last In First Out"),
            ("PDA is a 7-tuple?", ["Yes", "No", "5-tuple"], "Yes"),
            ("Initial stack symbol?", ["Z0", "S0", "ε"], "Z0"),
            ("Can PDA accept by empty stack?", ["Yes", "No", "Only DPDA"], "Yes"),
            ("Push adds to?", ["Top", "Bottom", "Middle"], "Top"),
            ("Is NPDA more powerful than DPDA?", ["Yes", "No", "Same"], "Yes"),
            ("Can PDA recognize a^n b^n?", ["Yes", "No", "Only DFA"], "Yes"),
            ("Γ represents?", ["Stack Alphabet", "Input Alphabet", "States"], "Stack Alphabet")
        ]
        p_score = 0
        for i, (q, opts, ans) in enumerate(pda_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"pq_u_{i}")
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
        test_string = st.text_input("Enter Input String (e.g., aabb):", "aabb", key="pda_in_u")
        sim_speed = st.slider("Speed:", 0.5, 2.0, 1.0, key="pda_sp_u")
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