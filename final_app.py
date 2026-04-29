import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE - Ultimate Edition v9",
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
    .comment-box {
            background-color: #f8fafc; padding: 15px; border-radius: 10px; 
            border: 1px solid #e2e8f0; margin-bottom: 15px; line-height: 1.5;
        }
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
    ["Home Page", "Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Contact Developer", "Community Feedback"]
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
    tab_intro, tab_alphabets, tab_strings, tab_languages, tab_sets, tab_functions, tab_boolean, tab_q = st.tabs(["📖 Introduction", "🔤 Alphabets", "🧵 Strings", "🗣️ Languages", "📊 Sets", "⚙️ Functions", "🧠 Boolean Logic", "📝 Comprehensive Quiz"])
    
    with tab_intro:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.0</div>
        <h3>What is Theory of Computation?</h3>
        <p><b>Theory of Computation (TOC)</b> is a branch of computer science and mathematics that deals with whether and how efficiently problems can be solved on a model of computation, using an algorithm. The field is divided into three major branches: Automata Theory, Computability Theory, and Complexity Theory.</p>
        <h4>1. Automata Theory</h4>
        <p>This branch studies abstract machines (or more abstractly, mathematical models of machines) and the computational problems that can be solved using these machines. It is the study of self-operating virtual machines that follow a predetermined sequence of operations automatically. Key concepts include Finite Automata (DFA, NFA), Pushdown Automata (PDA), and Turing Machines.</p>
        <h4>2. Computability Theory</h4>
        <p>This branch deals with the fundamental question of what problems can be solved algorithmically. It explores the limits of computation, identifying problems that are 'computable' (can be solved by an algorithm) and those that are 'uncomputable' (cannot be solved by any algorithm). The Turing Machine is a central concept here, serving as a universal model of computation.</p>
        <h4>3. Complexity Theory</h4>
        <p>This branch focuses on the resources (time and space) required to solve computational problems. It classifies problems based on their inherent difficulty, distinguishing between problems that can be solved efficiently (e.g., in polynomial time) and those that are inherently difficult (e.g., NP-hard problems). It helps in understanding the practical feasibility of solving problems.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_alphabets:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.1</div>
        <h3>What is an Alphabet (Σ)?</h3>
        <p>In the context of Theory of Computation, an <b>Alphabet (Σ)</b> is a finite, non-empty set of symbols. These symbols are the basic building blocks from which all strings and languages are constructed. Think of it as the set of characters you can use to write words in a particular language.</p>
        <h4>Key Characteristics of an Alphabet:</h4>
        <ul>
            <li><b>Finite:</b> The number of symbols in an alphabet must be countable and limited.</li>
            <li><b>Non-empty:</b> An alphabet must contain at least one symbol.</li>
            <li><b>Symbols:</b> These can be letters, numbers, special characters, or any distinct entities.</li>
        </ul>
        <h4>Examples of Alphabets:</h4>
        <ul>
            <li><b>Binary Alphabet:</b> Σ = {0, 1} (Used in digital computers)</li>
            <li><b>English Alphabet (lowercase):</b> Σ = {a, b, c, ..., z}</li>
            <li><b>Decimal Digits:</b> Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_strings:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.2</div>
        <h3>What is a String (Word)?</h3>
        <p>A <b>String</b> (also known as a <b>Word</b>) is a finite sequence of symbols chosen from an alphabet (Σ). Strings are the fundamental units that form languages in Theory of Computation. For example, if Σ = {a, b}, then "ababa", "b", and "aa" are all strings over Σ.</p>
        <h4>Key Properties and Operations of Strings:</h4>
        <ul>
            <li><b>Length (|w|):</b> The number of symbols in a string <i>w</i>. For example, if <i>w</i> = "0110", then |<i>w</i>| = 4.</li>
            <li><b>Empty String (ε or λ):</b> A unique string with length 0. It is the only string that contains no symbols. The empty string is a member of every Σ*.</li>
            <li><b>Concatenation:</b> Joining two strings together. If <i>x</i> = "cat" and <i>y</i> = "dog", then <i>xy</i> = "catdog". Concatenation is associative but not commutative.</li>
            <li><b>Reverse (w<sup>R</sup>):</b> The string obtained by writing the symbols of <i>w</i> in reverse order. If <i>w</i> = "abc", then <i>w<sup>R</sup></i> = "cba".</li>
            <li><b>Substring:</b> A sequence of consecutive symbols within a string. "aba" is a substring of "ababa".</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_languages:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.3</div>
        <h3>What is a Language (L)?</h3>
        <p>A <b>Language (L)</b> over an alphabet Σ is a subset of Σ*. In other words, a language is a set of strings, where each string is formed using symbols from Σ. Languages can be finite or infinite.</p>
        <h4>Key Concepts of Languages:</h4>
        <ul>
            <li><b>Σ* (Kleene Closure):</b> The set of all possible strings that can be formed over Σ, including the empty string ε. It is an infinite set.</li>
            <li><b>Σ<sup>+</sup> (Positive Closure):</b> The set of all possible strings over Σ, excluding the empty string ε. (Σ<sup>+</sup> = Σ* - {ε}).</li>
            <li><b>Empty Language (∅):</b> A language that contains no strings. Note that ∅ ≠ {ε}.</li>
            <li><b>Language Operations:</b> Since languages are sets, we can perform set operations like Union (L₁ ∪ L₂), Intersection (L₁ ∩ L₂), and Difference (L₁ - L₂).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sets:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.4</div>
        <h3>Set Theory: The Mathematical Framework</h3>
        <p>Sets are collections of distinct objects. In TOC, we use sets to define states, alphabets, and languages. Understanding set operations is crucial for formalizing computational models.</p>
        <div class="info-grid">
            <div class="info-item"><b>Union (A ∪ B):</b> The set of all elements that are in A, or in B, or in both.</div>
            <div class="info-item"><b>Intersection (A ∩ B):</b> The set of all elements that are in both A and B.</div>
            <div class="info-item"><b>Difference (A - B):</b> The set of all elements that are in A but not in B.</div>
            <div class="info-item"><b>Complement (Ā):</b> The set of all elements in the universal set that are not in A.</div>
        </div>
        <h4>Advanced Set Concepts:</h4>
        <ul>
            <li><b>Power Set P(S):</b> The set of all subsets of S. If a set S has <i>n</i> elements, its power set P(S) has 2<sup>n</sup> elements. This is a key concept in converting NFAs to DFAs.</li>
            <li><b>Cartesian Product (A × B):</b> The set of all ordered pairs (a, b) where a ∈ A and b ∈ B. This is used to define transition functions in automata.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_functions:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.5</div>
        <h3>Functions and Relations</h3>
        <p>A <b>Function (f: A → B)</b> is a rule that assigns each element in set A (the Domain) to exactly one element in set B (the Codomain). Functions are used to define how automata transition between states.</p>
        <h4>Key Types of Functions:</h4>
        <ul>
            <li><b>Transition Function (δ):</b> The core of any automaton. It defines the next state based on the current state and the input symbol. For a DFA, δ: Q × Σ → Q.</li>
            <li><b>Total Function:</b> A function that is defined for every element in its domain. DFAs require total transition functions.</li>
            <li><b>Partial Function:</b> A function that is not necessarily defined for all elements in its domain. NFAs can be thought of as having partial transition functions.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_boolean:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.6</div>
        <h3>Boolean Logic: The Logic of Computation</h3>
        <p>Boolean logic deals with variables that have only two possible values: <b>True (1)</b> and <b>False (0)</b>. It forms the basis of digital circuit design and the logical transitions in automata.</p>
        <div class="info-grid">
            <div class="info-item"><b>AND (∧):</b> True only if both inputs are True. (1 ∧ 1 = 1, else 0)</div>
            <div class="info-item"><b>OR (∨):</b> True if at least one input is True. (0 ∨ 0 = 0, else 1)</div>
            <div class="info-item"><b>NOT (¬):</b> Inverts the input value. (¬1 = 0, ¬0 = 1)</div>
            <div class="info-item"><b>XOR (⊕):</b> True if the inputs are different. (1 ⊕ 0 = 1, 0 ⊕ 1 = 1, else 0)</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 Foundations Quiz (10 Questions)")
        f_qs = [
            ("What is Σ in Theory of Computation?", ["Alphabet", "Number", "Function"], "Alphabet"),
            ("What is the length of the empty string ε?", ["0", "1", "Undefined"], "0"),
            ("Does Σ* include the empty string ε?", ["Yes", "No", "Sometimes"], "Yes"),
            ("What does the intersection of two sets (A ∩ B) represent?", ["Common elements", "All elements", "Difference"], "Common elements"),
            ("If a set S has 2 elements, what is the size of its power set P(S)?", ["4", "2", "3"], "4"),
            ("In a function f: A → B, what is set A called?", ["Domain", "Codomain", "Range"], "Domain"),
            ("What is the result of NOT True in Boolean logic?", ["False", "True", "Null"], "False"),
            ("What is the union of two sets (A ∪ B)?", ["All elements in A or B", "Only common elements", "Elements in A but not B"], "All elements in A or B"),
            ("What is Σ+ equal to?", ["Σ* - {ε}", "Σ* + {ε}", "Σ*"], "Σ* - {ε}"),
            ("According to De Morgan's Laws, ¬(A ∨ B) is equal to:", ["¬A ∧ ¬B", "¬A ∨ ¬B", "A ∧ B"], "¬A ∧ ¬B")
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
        <p>A <b>Deterministic Finite Automata (DFA)</b> is the simplest model of computation. It has no memory other than its current state. For every state and input symbol, there is exactly one transition to a next state.</p>
        <h4>The 5-Tuple Definition of a DFA:</h4>
        <p>A DFA is formally defined as a 5-tuple (Q, Σ, δ, q₀, F), where:</p>
        <ul>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (the alphabet).</li>
            <li><b>δ:</b> The transition function, δ: Q × Σ → Q. It defines the next state for every state-symbol pair.</li>
            <li><b>q₀:</b> The unique start state (q₀ ∈ Q).</li>
            <li><b>F:</b> A set of accept (or final) states (F ⊆ Q).</li>
        </ul>
        <div class="step-box">
        <b>💡 How to determine Acceptance? (The Process)</b>  

        1. The machine starts at the start state <b>q₀</b>.  

        2. It reads the first symbol of the input string <i>w</i>.  

        3. It moves to the next state according to the transition function <b>δ</b>.  

        4. It repeats this process for every symbol in the string <i>w</i>.  

        5. <b>Crucial Step:</b> After the last symbol is read, the machine checks its current state. If the state is in the set of accept states <b>F</b>, the string is <b>Accepted</b>. If not, it is <b>Rejected</b>.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_viz:
        st.markdown("### 🎨 Visual Examples of DFAs")
        st.markdown("""
        <div class="learning-card">
        <p>Visualizing DFAs using state transition diagrams makes it easier to understand how they process strings. Here are two common examples.</p>
        <h4>Example 1: DFA accepting strings with an even number of '0's</h4>
        """, unsafe_allow_html=True)
        
        dfa1 = graphviz.Digraph(comment='Even 0s', graph_attr={'rankdir': 'LR'})
        dfa1.node('S', '', shape='none')
        dfa1.node('q_even', 'Even (q0)', shape='doublecircle', color='green')
        dfa1.node('q_odd', 'Odd (q1)', shape='circle')
        dfa1.edge('S', 'q_even')
        dfa1.edge('q_even', 'q_odd', label='0')
        dfa1.edge('q_odd', 'q_even', label='0')
        dfa1.edge('q_even', 'q_even', label='1')
        dfa1.edge('q_odd', 'q_odd', label='1')
        st.graphviz_chart(dfa1)

        st.markdown("""
        <h4>Example 2: DFA accepting strings that start with 'a'</h4>
        """, unsafe_allow_html=True)
        
        dfa2 = graphviz.Digraph(comment='Starts with a', graph_attr={'rankdir': 'LR'})
        dfa2.node('S', '', shape='none')
        dfa2.node('q0', 'Start', shape='circle')
        dfa2.node('q1', 'Accept', shape='doublecircle', color='green')
        dfa2.node('q2', 'Trap', shape='circle', color='red')
        dfa2.edge('S', 'q0')
        dfa2.edge('q0', 'q1', label='a')
        dfa2.edge('q0', 'q2', label='b')
        dfa2.edge('q1', 'q1', label='a, b')
        dfa2.edge('q2', 'q2', label='a, b')
        st.graphviz_chart(dfa2)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_sim:
        st.markdown("### 🚀 Interactive DFA Simulator (Pattern '101')")
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
            ("What does 'D' in DFA stand for?", ["Double", "Deterministic", "Direct"], "Deterministic"),
            ("A DFA can have multiple start states.", ["True", "False"], "False"),
            ("Which of these is NOT a component of a DFA's formal definition?", ["States", "Stack", "Alphabet"], "Stack"),
            ("If a DFA is in an accept state after processing an input string, the string is:", ["Rejected", "Accepted", "Ignored"], "Accepted"),
            ("DFAs have finite memory.", ["True", "False"], "True"),
            ("The transition function in a DFA maps (state, input symbol) to:", ["A set of states", "A single next state", "An output symbol"], "A single next state"),
            ("Can a DFA have ε-transitions?", ["Yes", "No", "Sometimes"], "No"),
            ("Which of the following languages can a DFA recognize?", ["All languages", "Regular languages", "Context-free languages"], "Regular languages"),
            ("If a DFA has 3 states and an alphabet of 2 symbols, how many transitions must be defined?", ["3", "6", "9"], "6"),
            ("What is the shape of an accept state in a Graphviz DFA diagram?", ["Circle", "Square", "Double Circle"], "Double Circle")
        ]
        dfa_score = 0
        for i, (q, opts, ans) in enumerate(dfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dfaq_u_{i}")
            if u_ans == ans: dfa_score += 1
        if st.button("Submit DFA Quiz"): st.success(f"Your Score: {dfa_score}/10")

elif subject == "NFA Masterclass":
    st.markdown("## 🧠 Non-Deterministic Finite Automata (NFA)")
    tab_info, tab_viz, tab_sim, tab_q = st.tabs(["📖 Deep Dive Definition", "🎨 Visual Examples", "🚀 Interactive Simulator", "📝 NFA Quiz (10 Qs)"])

    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Formal Theory</div>
        <h3>The Flexibility of NFA</h3>
        <p>A <b>Non-Deterministic Finite Automata (NFA)</b> is a finite automaton where for each state and input symbol, there can be zero, one, or more than one next state. NFAs also allow transitions on the empty string (ε-transitions).</p>
        <h4>Formal Definition of an NFA:</h4>
        <p>An NFA is formally defined as a 5-tuple (Q, Σ, δ, q₀, F), where:</p>
        <ul>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (the alphabet).</li>
            <li><b>δ:</b> The transition function, δ: Q × (Σ ∪ {ε}) → P(Q).</li>
            <li><b>q₀:</b> The start state (q₀ ∈ Q).</li>
            <li><b>F:</b> A set of accept (or final) states (F ⊆ Q).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_viz:
        st.markdown("### 🎨 Visual Examples of NFAs")
        st.markdown("""
        <div class="learning-card">
        <h4>Example 1: NFA accepting strings containing '101'</h4>
        """, unsafe_allow_html=True)

        graph_nfa1 = graphviz.Digraph(comment='NFA containing 101', graph_attr={'rankdir': 'LR'})
        graph_nfa1.node('A', 'q0', shape='circle'); graph_nfa1.node('B', 'q1', shape='circle'); graph_nfa1.node('C', 'q2', shape='circle'); graph_nfa1.node('D', 'q3', shape='doublecircle')
        graph_nfa1.edge('A', 'A', label='0,1'); graph_nfa1.edge('A', 'B', label='1'); graph_nfa1.edge('B', 'C', label='0'); graph_nfa1.edge('C', 'D', label='1'); graph_nfa1.edge('D', 'D', label='0,1')
        st.graphviz_chart(graph_nfa1)

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
            ("What does 'N' in NFA stand for?", ["Natural", "Non-deterministic", "Negative"], "Non-deterministic"),
            ("An NFA can have multiple transitions for the same input symbol from a single state.", ["True", "False"], "True"),
            ("NFAs allow ε-transitions.", ["True", "False"], "True"),
            ("Are NFAs more powerful than DFAs in terms of the languages they can recognize?", ["Yes", "No", "Sometimes"], "No"),
            ("If an NFA has multiple paths for an input string, and at least one path leads to an accept state, the string is:", ["Rejected", "Accepted", "Ignored"], "Accepted"),
            ("The transition function in an NFA maps (state, input symbol or ε) to:", ["A single next state", "A set of possible next states", "An output symbol"], "A set of possible next states"),
            ("Which of the following is a key characteristic of NFAs?", ["Deterministic transitions", "Finite memory", "No ε-transitions"], "Finite memory"),
            ("NFA to DFA conversion is always possible.", ["True", "False"], "True"),
            ("The power set of states is used in the construction of an equivalent DFA from an NFA.", ["True", "False"], "True"),
            ("Which symbol represents an empty string transition in an NFA?", ["0", "1", "ε"], "ε")
        ]
        nfa_score = 0
        for i, (q, opts, ans) in enumerate(nfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"nfaq_u_{i}")
            if u_ans == ans: nfa_score += 1
        if st.button("Submit NFA Quiz"): st.success(f"Your Score: {nfa_score}/10")

elif subject == "Regular Expressions":
    st.markdown("## 🧩 Regular Expressions & Operations")
    tab_ops, tab_re, tab_closure, tab_conv, tab_q = st.tabs(["⚙️ Regular Operations", "📝 Regular Expressions", "🔒 Closure Properties", "🔄 RE to NFA", "📝 Quiz (10 Qs)"])

    with tab_ops:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.1</div>
        <h3>Regular Operations: Union, Concatenation, and Star</h3>
        <p>In Theory of Computation, <b>Regular Operations</b> are used to build complex languages from simpler ones.</p>
        <div class="info-grid">
            <div class="info-item"><b>1. Union (L₁ ∪ L₂):</b> The set of all strings that are in either L₁ or L₂.</div>
            <div class="info-item"><b>2. Concatenation (L₁ ∘ L₂):</b> The set of all strings formed by taking a string from L₁ and appending a string from L₂.</div>
            <div class="info-item"><b>3. Star (L*):</b> The set of all strings formed by concatenating zero or more strings from L.</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_re:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.2</div>
        <h3>Regular Expressions (REs)</h3>
        <p>A <b>Regular Expression</b> is a concise way to describe a regular language using symbols and operators.</p>
        <div class="step-box">
        <b>Common Examples:</b>  

        - <b>(0 ∪ 1)*</b> : All binary strings.  

        - <b>01*</b> : A '0' followed by any number of '1's.  

        - <b>(0 ∪ 1)*00</b> : All binary strings ending with '00'.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_closure:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.3</div>
        <h3>Closure Properties for Regular Languages</h3>
        <p>Regular Languages are closed under: Union, Concatenation, Star, Complement, and Intersection.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_conv:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.4</div>
        <h3>Conversion: RE to NFA (Thompson's Construction)</h3>
        <p>Every Regular Expression can be converted into an equivalent NFA by building small NFAs for basic parts and combining them.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 Regular Expressions Quiz (10 Questions)")
        re_qs = [
            ("Which operation represents L*?", ["Star", "Union", "Concatenation"], "Star"),
            ("Regular languages are closed under intersection.", ["True", "False"], "True"),
            ("What does the RE (0 ∪ 1)* represent?", ["All binary strings", "Only 0s", "Only 1s"], "All binary strings"),
            ("In Thompson's construction, how is Union handled?", ["New start with ε-transitions", "Sequential connection", "Looping back"], "New start with ε-transitions"),
            ("Which symbol represents the empty language in RE?", ["∅", "ε", "Σ"], "∅"),
            ("Is (ab)* the same as a*b*?", ["No", "Yes", "Sometimes"], "No"),
            ("Concatenation of {a} and {b} is?", ["{ab}", "{a, b}", "{ba}"], "{ab}"),
            ("Regular expressions can describe non-regular languages.", ["False", "True"], "False"),
            ("The 'Star' operation can produce an empty string.", ["True", "False"], "True"),
            ("Which property means applying an operation stays within the same class?", ["Closure", "Commutative", "Associative"], "Closure")
        ]
        re_score = 0
        for i, (q, opts, ans) in enumerate(re_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"req_u_{i}")
            if u_ans == ans: re_score += 1
        if st.button("Submit RE Quiz"): st.success(f"Your Score: {re_score}/10")

elif subject == "DFA to RE & Pumping Lemma":
    st.markdown("## 🔄 DFA to RE & Pumping Lemma")
    tab_dfa_re, tab_pumping, tab_q = st.tabs(["🔄 DFA to RE Conversion", "🧪 Pumping Lemma", "📝 Quiz (10 Qs)"])

    with tab_dfa_re:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.1</div>
        <h3>Conversion of DFA to Regular Expression (RE)</h3>
        <p>The most common method for this conversion is the <b>State Elimination Method</b>.</p>
        <div class="step-box">
        <b>Steps for State Elimination:</b>  

        1. Add New States (Start and Final).  

        2. Eliminate internal states one by one.  

        3. Update transitions using R_new = R_ij ∪ (R_ir ∘ (R_rr)* ∘ R_rj).
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_pumping:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.2</div>
        <h3>Proving Languages Aren't Regular: Pumping Lemma</h3>
        <p>If <i>L</i> is a regular language, then there exists a number <i>p</i> such that any string <i>s</i> in <i>L</i> with length |<i>s</i>| ≥ <i>p</i> can be split into <b>s = xyz</b>, satisfying:</p>
        <ul>
            <li>1. For each <i>i</i> ≥ 0, <b>xyⁱz ∈ L</b>.</li>
            <li>2. <b>|y| > 0</b>.</li>
            <li>3. <b>|xy| ≤ p</b>.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 DFA to RE & Pumping Lemma Quiz (10 Questions)")
        dp_qs = [
            ("What is the main method to convert DFA to RE?", ["State Elimination", "Subset Construction", "Thompson's"], "State Elimination"),
            ("Pumping Lemma is used to prove a language is regular.", ["False", "True"], "False"),
            ("In s = xyz, which part is 'pumped'?", ["y", "x", "z"], "y"),
            ("What is the condition for the length of y in Pumping Lemma?", ["|y| > 0", "|y| = 0", "|y| < p"], "|y| > 0"),
            ("The condition |xy| ≤ p must hold in Pumping Lemma.", ["True", "False"], "True"),
            ("If L = {aⁿbⁿ | n ≥ 0}, is it regular?", ["No", "Yes", "Only for small n"], "No"),
            ("State elimination results in a GNFA with how many states?", ["2", "1", "3"], "2"),
            ("Can a DFA recognize the language of balanced parentheses?", ["No", "Yes", "Sometimes"], "No"),
            ("The pumping length p depends on the language.", ["True", "False"], "True"),
            ("What happens if we pump y with i=0?", ["y is removed", "y is doubled", "String stays same"], "y is removed")
        ]
        dp_score = 0
        for i, (q, opts, ans) in enumerate(dp_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dpq_u_{i}")
            if u_ans == ans: dp_score += 1
        if st.button("Submit Module 5 Quiz"): st.success(f"Your Score: {dp_score}/10")

elif subject == "CFG & Chomsky Form":
    st.markdown("## 📜 Context-Free Grammars (CFG) & Chomsky Normal Form")
    tab_cfg, tab_cnf, tab_q = st.tabs(["📝 CFG Definition", "📐 Chomsky Normal Form (CNF)", "📝 Quiz (10 Qs)"])

    with tab_cfg:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.1</div>
        <h3>Context-Free Grammar (CFG)</h3>
        <p>A <b>Context-Free Grammar</b> is a formal grammar used to generate all possible strings in a given context-free language. It is more powerful than regular expressions.</p>
        <h4>The 4-Tuple Definition (V, Σ, R, S):</h4>
        <ul>
            <li><b>V:</b> A finite set of variables (non-terminals).</li>
            <li><b>Σ:</b> A finite set of terminals (alphabet).</li>
            <li><b>R:</b> A finite set of rules (productions) of the form A → w, where A ∈ V and w ∈ (V ∪ Σ)*.</li>
            <li><b>S:</b> The start variable (S ∈ V).</li>
        </ul>
        <div class="step-box">
        <b>Example:</b> S → 0S1 | ε (Generates strings like 0011, 01, ε).
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_cnf:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.2</div>
        <h3>Chomsky Normal Form (CNF)</h3>
        <p>A CFG is in <b>Chomsky Normal Form</b> if every production rule is of the form:</p>
        <ul>
            <li><b>A → BC</b> (A variable goes to exactly two variables)</li>
            <li><b>A → a</b> (A variable goes to exactly one terminal)</li>
            <li><b>S → ε</b> (Only if S is the start variable and doesn't appear on the RHS)</li>
        </ul>
        <h4>Steps to convert CFG to CNF:</h4>
        <ol>
            <li>Add a new start variable S₀ → S.</li>
            <li>Eliminate all ε-productions (A → ε).</li>
            <li>Eliminate all unit productions (A → B).</li>
            <li>Eliminate rules with more than two variables or mixed terminals.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 CFG & CNF Quiz (10 Questions)")
        cfg_qs = [
            ("What does CFG stand for?", ["Context-Free Grammar", "Computer-File Graph", "Common-Form Grammar"], "Context-Free Grammar"),
            ("In CFG, Σ represents?", ["Terminals", "Variables", "Rules"], "Terminals"),
            ("A rule A → BC is allowed in CNF.", ["True", "False"], "True"),
            ("A rule A → aB is allowed in CNF.", ["False", "True"], "False"),
            ("Which step comes first in CNF conversion?", ["New start variable", "Eliminate ε", "Eliminate unit"], "New start variable"),
            ("CFGs are more powerful than DFAs.", ["True", "False"], "True"),
            ("The start variable is usually denoted by?", ["S", "V", "T"], "S"),
            ("Can a CFG generate the language {aⁿbⁿ}?", ["Yes", "No", "Only for small n"], "Yes"),
            ("In CNF, a variable can go to how many terminals?", ["1", "2", "Unlimited"], "1"),
            ("What is a production rule with only one variable on RHS called?", ["Unit production", "ε-production", "Terminal rule"], "Unit production")
        ]
        cfg_score = 0
        for i, (q, opts, ans) in enumerate(cfg_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"cfgq_u_{i}")
            if u_ans == ans: cfg_score += 1
        if st.button("Submit CFG Quiz"): st.success(f"Your Score: {cfg_score}/10")

elif subject == "PDA & CFL Theory":
    st.markdown("## ⚙️ PDA & Context-Free Language (CFL) Theory")
    tab_pda, tab_pda_cfg, tab_pumping_cfl, tab_q = st.tabs(["🤖 PDA Recap", "🔄 PDA ↔ CFG", "🧪 Pumping Lemma for CFLs", "📝 Quiz (10 Qs)"])

    with tab_pda:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.1</div>
        <h3>Pushdown Automata (PDA)</h3>
        <p>A PDA is a finite automaton with a <b>Stack</b>. It is the machine model for Context-Free Languages.</p>
        <div class="info-grid">
            <div class="info-item"><b>Deterministic PDA (DPDA):</b> Recognizes a subset of CFLs.</div>
            <div class="info-item"><b>Non-deterministic PDA (NPDA):</b> Recognizes all CFLs.</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_pda_cfg:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.2</div>
        <h3>Equivalence of PDA and CFG</h3>
        <p>A language is context-free if and only if some pushdown automaton recognizes it. This means we can convert any CFG into an equivalent PDA and vice versa.</p>
        <h4>Conversion Highlights:</h4>
        <ul>
            <li><b>CFG to PDA:</b> The PDA simulates the leftmost derivation of the grammar on its stack.</li>
            <li><b>PDA to CFG:</b> More complex, involves creating variables for pairs of states (p, q) representing the stack behavior.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_pumping_cfl:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.3</div>
        <h3>Pumping Lemma for CFLs</h3>
        <p>Used to prove a language is <b>NOT</b> context-free. If L is a CFL, any string <i>s</i> with |s| ≥ p can be split into <b>s = uvxyz</b> such that:</p>
        <ul>
            <li>1. <b>uvⁱxyⁱz ∈ L</b> for all i ≥ 0.</li>
            <li>2. <b>|vy| > 0</b>.</li>
            <li>3. <b>|vxy| ≤ p</b>.</li>
        </ul>
        <div class="step-box">
        <b>Example:</b> L = {aⁿbⁿcⁿ | n ≥ 0} is NOT a CFL.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 PDA & CFL Quiz (10 Questions)")
        pc_qs = [
            ("PDAs are equivalent to which grammars?", ["CFG", "Regular", "Unrestricted"], "CFG"),
            ("Pumping Lemma for CFLs splits string into how many parts?", ["5", "3", "2"], "5"),
            ("Is {aⁿbⁿcⁿ} a Context-Free Language?", ["No", "Yes", "Sometimes"], "No"),
            ("In uvxyz, which parts are pumped?", ["v and y", "u and z", "x only"], "v and y"),
            ("A PDA uses which data structure?", ["Stack", "Queue", "Array"], "Stack"),
            ("Every Regular Language is also a Context-Free Language.", ["True", "False"], "True"),
            ("NPDA is more powerful than DPDA.", ["True", "False"], "True"),
            ("The condition |vy| > 0 means?", ["At least one of v or y is non-empty", "Both must be non-empty", "u must be empty"], "At least one of v or y is non-empty"),
            ("Can a PDA recognize {ww^R}?", ["Yes", "No", "Only DFA"], "Yes"),
            ("The 'vxy' part in Pumping Lemma for CFLs must be ≤ p.", ["True", "False"], "True")
        ]
        pc_score = 0
        for i, (q, opts, ans) in enumerate(pc_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"pcq_u_{i}")
            if u_ans == ans: pc_score += 1
        if st.button("Submit Module 7 Quiz"): st.success(f"Your Score: {pc_score}/10")

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