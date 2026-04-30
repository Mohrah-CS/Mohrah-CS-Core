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
    .highlight { color: #2563eb; font-weight: bold; background: #eff6ff; padding: 2px 6px; border-radius: 4px; }
    .comment-box {
            background-color: #f8fafc; padding: 15px; border-radius: 10px; 
            border: 1px solid #e2e8f0; margin-bottom: 15px; line-height: 1.5;
        }
    .footer {
        text-align: center; padding: 40px; margin-top: 80px;
        border-top: 3px solid #1e3a8a; background-color: #f1f5f9; color: #0f172a;
    }
    .summary-table {
        width: 100%; border-collapse: collapse; margin-top: 20px;
    }
    .summary-table th, .summary-table td {
        border: 1px solid #e2e8f0; padding: 12px; text-align: left;
    }
    .summary-table th {
        background-color: #1e3a8a; color: white;
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

# --- 5. SIDEBAR NAVIGATION (NESTED) ---
st.sidebar.title("💎 Academic Navigation")
st.sidebar.write("---")

# Initialize session state for navigation if not exists
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home Page"

# First Level: Select Subject/Course
main_subject = st.sidebar.selectbox(
    "Select Course / اختر المادة:",
    ["Home Page", "Theory of Computation", "Operating Systems"],
    index=0 if st.session_state.current_page == "Home Page" else (1 if st.session_state.current_page in ["Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Turing Machines & Algorithms", "🎓 Course Completion"] else 2)
)

# Second Level: Select Lesson based on Subject
if main_subject == "Theory of Computation":
    subject = st.sidebar.selectbox(
        "Select Lesson / اختر الدرس:",
        ["Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Turing Machines & Algorithms", "🎓 Course Completion"]
    )
    st.session_state.current_page = subject
elif main_subject == "Operating Systems":
    subject = st.sidebar.selectbox(
        "Select Lesson / اختر الدرس:",
        ["Introduction to OS",
            "What Operating Systems Do",
            "Operating System Types",
            "Computer-System Organization",
            "Computer-System Architecture",
            "Computer-System Operations",
            "Resource Management",
            "Virtualization",
            "Kernel Data Structures",
            "Free/Libre and Open-Source Operating Systems",
            "Process Management",
            "Memory Management",
            "Storage & I/O"
        ]
    )
    st.session_state.current_page = subject
else:
    subject = "Home Page"
    st.session_state.current_page = "Home Page"

# Always show Contact and Feedback buttons in sidebar (Fixed Position)
st.sidebar.write("---")
st.sidebar.write("### 📞 تواصل معي / Contact Me")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("📧 Contact", key="contact_btn"):
        st.session_state.current_page = "Contact Developer"
with col2:
    if st.button("💬 Feedback", key="feedback_btn"):
        st.session_state.current_page = "Community Feedback"

# Use the session state to determine what to display
display_page = st.session_state.current_page

# --- 6. MODULES ---

if display_page == "Home Page":
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
        <div class="info-item"><b>📚 المحتوى:</b> يغطي المنهج الكامل من الأساسيات الرياضية إلى نماذج الحوسبة المتقدمة وآلات تورينج.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Foundations of TOC":
    st.markdown("## 📘 Foundations of Theory of Computation")
    tab_intro, tab_alphabets, tab_strings, tab_languages, tab_sets, tab_functions, tab_boolean, tab_q = st.tabs(["📖 Introduction", "🔤 Alphabets", "🧵 Strings", "🗣️ Languages", "📊 Sets", "⚙️ Functions", "🧠 Boolean Logic", "📝 Comprehensive Quiz"])
    
    with tab_intro:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.0</div>
        <h3>What is Theory of Computation?</h3>
        <p><b>Theory of Computation (TOC)</b> is a branch of computer science and mathematics that deals with whether and how efficiently problems can be solved on a model of computation, using an algorithm. The field is divided into three major branches: Automata Theory, Computability Theory, and Complexity Theory.</p>
        <h4>1. Automata Theory</h4>
        <p>This branch studies abstract machines (or more abstractly, mathematical models of machines) and the computational problems that can be solved using these machines. Key concepts include Finite Automata (DFA, NFA), Pushdown Automata (PDA), and Turing Machines.</p>
        <h4>2. Computability Theory</h4>
        <p>This branch deals with the fundamental question of what problems can be solved algorithmically. It explores the limits of computation, identifying problems that are 'computable' (can be solved by an algorithm) and those that are 'uncomputable' (cannot be solved by any algorithm). The Turing Machine is a central concept here, serving as a universal model of computation.</p>
        <h4>3. Complexity Theory</h4>
        <p>This branch focuses on the resources (time and space) required to solve computational problems. It classifies problems based on their inherent difficulty, distinguishing between problems that can be solved efficiently (e.g., in polynomial time) and those that are inherently difficult (e.g., NP-hard problems).</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_alphabets:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.1</div>
        <h3>What is an Alphabet (Σ)?</h3>
        <p>In the context of Theory of Computation, an <b>Alphabet (Σ)</b> is a finite, non-empty set of symbols. These symbols are the basic building blocks from which all strings and languages are constructed.</p>
        <h4>Key Characteristics:</h4>
        <ul>
            <li><b>Finite:</b> The number of symbols must be countable and limited.</li>
            <li><b>Non-empty:</b> Must contain at least one symbol.</li>
        </ul>
        <h4>Examples:</h4>
        <ul>
            <li><b>Binary Alphabet:</b> Σ = {0, 1}</li>
            <li><b>English Alphabet:</b> Σ = {a, b, c, ..., z}</li>
            <li><b>Numeric Alphabet:</b> Σ = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_strings:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.2</div>
        <h3>What is a String (Word)?</h3>
        <p>A <b>String</b> is a finite sequence of symbols chosen from an alphabet (Σ).</p>
        <h4>Key Properties and Operations:</h4>
        <ul>
            <li><b>Length (|w|):</b> The number of symbols in a string. For example, if w = "abc", then |w| = 3.</li>
            <li><b>Empty String (ε):</b> A unique string with length 0. It contains no symbols.</li>
            <li><b>Concatenation:</b> Joining two strings together. If u = "cat" and v = "dog", then uv = "catdog".</li>
            <li><b>Reverse (w<sup>R</sup>):</b> Writing symbols in reverse order. If w = "abc", then w<sup>R</sup> = "cba".</li>
            <li><b>Substring:</b> A sequence of symbols that appears within a string.</li>
            <li><b>Prefix and Suffix:</b> A prefix is a substring at the beginning; a suffix is a substring at the end.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_languages:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.3</div>
        <h3>What is a Language (L)?</h3>
        <p>A <b>Language (L)</b> over an alphabet Σ is a subset of Σ*. It is a set of strings chosen from Σ*.</p>
        <h4>Key Concepts:</h4>
        <ul>
            <li><b>Σ* (Kleene Closure):</b> The set of all possible strings over Σ, including the empty string ε. It is an infinite set if Σ is non-empty.</li>
            <li><b>Σ<sup>+</sup> (Positive Closure):</b> The set of all possible strings over Σ, excluding the empty string ε. Σ<sup>+</sup> = Σ* - {ε}.</li>
            <li><b>Empty Language (∅):</b> A language that contains no strings. Note that ∅ ≠ {ε}.</li>
            <li><b>Language Operations:</b> Union, Intersection, Complement, and Concatenation of languages.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sets:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.4</div>
        <h3>Set Theory Foundations</h3>
        <p>Set theory is the mathematical language used to define languages and automata.</p>
        <div class="info-grid">
            <div class="info-item"><b>Union (A ∪ B):</b> The set of elements that are in A, in B, or in both.</div>
            <div class="info-item"><b>Intersection (A ∩ B):</b> The set of elements that are in both A and B.</div>
            <div class="info-item"><b>Difference (A - B):</b> The set of elements that are in A but not in B.</div>
            <div class="info-item"><b>Complement (A'):</b> The set of elements in the universal set that are not in A.</div>
            <div class="info-item"><b>Power Set P(S):</b> The set of all possible subsets of S. If |S| = n, then |P(S)| = 2ⁿ.</div>
            <div class="info-item"><b>Cartesian Product (A × B):</b> The set of all ordered pairs (a, b) where a ∈ A and b ∈ B.</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_functions:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.5</div>
        <h3>Functions and Relations</h3>
        <p>Functions define how an automaton moves from one state to another based on input.</p>
        <ul>
            <li><b>Domain:</b> The set of all possible inputs.</li>
            <li><b>Codomain:</b> The set of all possible outputs.</li>
            <li><b>Range:</b> The set of actual outputs produced by the function.</li>
            <li><b>Transition Function (δ):</b> In automata, δ: Q × Σ → Q (for DFA) or δ: Q × Σ → P(Q) (for NFA).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_boolean:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.6</div>
        <h3>Boolean Logic</h3>
        <p>Boolean logic is essential for understanding state transitions and decision-making in automata.</p>
        <div class="info-grid">
            <div class="info-item"><b>AND (∧):</b> True only if both inputs are true.</div>
            <div class="info-item"><b>OR (∨):</b> True if at least one input is true.</div>
            <div class="info-item"><b>NOT (¬):</b> Inverts the input value.</div>
            <div class="info-item"><b>XOR (⊕):</b> True if exactly one input is true.</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 Foundations Quiz (10 Questions)")
        f_qs = [
            ("What is Σ?", ["Alphabet (Set of symbols)", "Number", "Operation"], "Alphabet (Set of symbols)"),
            ("Length of ε?", ["0", "1", "Undefined"], "0"),
            ("Σ* includes ε?", ["Yes", "No", "Sometimes"], "Yes"),
            ("A ∩ B is?", ["Common elements", "All elements", "Difference"], "Common elements"),
            ("P(S) for 2 elements?", ["4", "2", "8"], "4"),
            ("Set A in f: A→B?", ["Domain", "Range", "Codomain"], "Domain"),
            ("NOT True?", ["False", "True", "None"], "False"),
            ("A ∪ B?", ["All elements", "Common elements", "None"], "All elements"),
            ("Σ+ is?", ["Σ* - {ε}", "Σ*", "{ε}"], "Σ* - {ε}"),
            ("¬(A ∨ B)?", ["¬A ∧ ¬B", "A ∧ B", "¬A ∨ ¬B"], "¬A ∧ ¬B")
        ]
        f_score = 0
        for i, (q, opts, ans) in enumerate(f_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"fq_u_{i}")
            if u_ans == ans: f_score += 1
        if st.button("Submit Foundations Quiz"):
            st.success(f"Your Score: {f_score}/10")

elif display_page == "DFA Explorer":
    st.markdown("## ⚙️ Deterministic Finite Automata (DFA)")
    tab_info, tab_viz, tab_sim, tab_q = st.tabs(["📖 Definition", "🎨 Visuals", "🚀 Simulator", "📝 Quiz"])
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.0</div>
        <h3>DFA 5-Tuple Definition</h3>
        <p>A <b>Deterministic Finite Automaton (DFA)</b> is a 5-tuple (Q, Σ, δ, q₀, F):</p>
        <ul>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (alphabet).</li>
            <li><b>δ:</b> The transition function (δ: Q × Σ → Q).</li>
            <li><b>q₀:</b> The start state (q₀ ∈ Q).</li>
            <li><b>F:</b> The set of accept states (F ⊆ Q).</li>
        </ul>
        <p><b>Deterministic</b> means that for every state and every input symbol, there is exactly one transition to a next state.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_viz:
        st.markdown("### Example: DFA for Even Number of 0s")
        dfa1 = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
        dfa1.node('S', '', shape='none')
        dfa1.node('q0', 'Even (q0)', shape='doublecircle')
        dfa1.node('q1', 'Odd (q1)', shape='circle')
        dfa1.edge('S', 'q0')
        dfa1.edge('q0', 'q1', label='0')
        dfa1.edge('q1', 'q0', label='0')
        dfa1.edge('q0', 'q0', label='1')
        dfa1.edge('q1', 'q1', label='1')
        st.graphviz_chart(dfa1)
    with tab_sim:
        st.markdown("### DFA Simulator (Pattern '101')")
        def gen_dfa_diag(active_state):
            dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
            states = {'q0': 'Start', 'q1': 'Saw 1', 'q2': 'Saw 10', 'q3': 'Accept 101'}
            for s, label in states.items():
                shape = 'doublecircle' if s == 'q3' else 'circle'
                color = 'blue' if s == active_state else 'black'
                penwidth = '3' if s == active_state else '1'
                dot.node(s, f"{label}\n({s})", shape=shape, color=color, penwidth=penwidth)
            dot.edge('q0', 'q1', label='1'); dot.edge('q0', 'q0', label='0')
            dot.edge('q1', 'q1', label='1'); dot.edge('q1', 'q2', label='0')
            dot.edge('q2', 'q3', label='1'); dot.edge('q2', 'q0', label='0')
            dot.edge('q3', 'q1', label='1'); dot.edge('q3', 'q0', label='0')
            return dot
        
        input_str = st.text_input("Enter binary string (e.g., 110101):", "101")
        speed = st.slider("Simulation Speed (seconds):", 0.5, 3.0, 1.0)
        if st.button("Start DFA Simulation"):
            curr = 'q0'
            history = []
            diag_placeholder = st.empty()
            for i, char in enumerate(input_str):
                diag_placeholder.graphviz_chart(gen_dfa_diag(curr))
                prev = curr
                if curr == 'q0': curr = 'q1' if char == '1' else 'q0'
                elif curr == 'q1': curr = 'q2' if char == '0' else 'q1'
                elif curr == 'q2': curr = 'q3' if char == '1' else 'q0'
                elif curr == 'q3': curr = 'q1' if char == '1' else 'q0'
                history.append({"Step": i+1, "Input": char, "From": prev, "To": curr})
                time.sleep(speed)
            diag_placeholder.graphviz_chart(gen_dfa_diag(curr))
            st.table(pd.DataFrame(history))
            if curr == 'q3': st.success("✅ String Accepted!")
            else: st.error("❌ String Rejected")
    with tab_q:
        dfa_qs = [
            ("What does 'D' in DFA stand for?", ["Deterministic", "Direct", "Dynamic"], "Deterministic"),
            ("Can a DFA have multiple start states?", ["No", "Yes", "Only if it's empty"], "No"),
            ("Does a DFA have a stack?", ["No", "Yes", "Optional"], "No"),
            ("If a string ends in an accept state, it is:", ["Accepted", "Rejected", "Undefined"], "Accepted"),
            ("DFA has finite memory?", ["True", "False", "Infinite"], "True"),
            ("The transition function δ maps to:", ["A single state", "A set of states", "Empty set"], "A single state"),
            ("Are ε-transitions allowed in DFA?", ["No", "Yes", "Only at the start"], "No"),
            ("DFA recognizes which languages?", ["Regular", "Context-Free", "Recursive"], "Regular"),
            ("For 3 states and 2 symbols, how many transitions?", ["6", "3", "9"], "6"),
            ("Accept state shape in diagrams?", ["Double Circle", "Single Circle", "Square"], "Double Circle")
        ]
        d_score = 0
        for i, (q, opts, ans) in enumerate(dfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dq_u_{i}")
            if u_ans == ans: d_score += 1
        if st.button("Submit DFA Quiz"):
            st.success(f"Your Score: {d_score}/10")

elif display_page == "NFA Masterclass":
    st.markdown("## 🧠 Non-Deterministic Finite Automata (NFA)")
    tab_info, tab_viz, tab_sim, tab_q = st.tabs(["📖 Definition", "🎨 Visuals", "🚀 Simulator", "📝 Quiz"])
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.0</div>
        <h3>NFA Definition & Power</h3>
        <p>A <b>Non-deterministic Finite Automaton (NFA)</b> is a 5-tuple (Q, Σ, δ, q₀, F) where the transition function δ maps to the <b>Power Set</b> of states: δ: Q × (Σ ∪ {ε}) → P(Q).</p>
        <h4>Key Differences from DFA:</h4>
        <ul>
            <li><b>Multiple Choices:</b> For a given state and symbol, there can be zero, one, or many next states.</li>
            <li><b>ε-Transitions:</b> Can move to a new state without reading any input symbol.</li>
            <li><b>Acceptance:</b> A string is accepted if <i>at least one</i> possible path leads to an accept state.</li>
        </ul>
        <p><b>Equivalence:</b> Every NFA can be converted to an equivalent DFA (Subset Construction), meaning they have the same computational power.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_viz:
        st.markdown("### DFA vs NFA Comparison (Ends with '01')")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("NFA (Simpler)")
            nfa_v = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
            nfa_v.node('S', '', shape='none'); nfa_v.node('q0', 'q0'); nfa_v.node('q1', 'q1'); nfa_v.node('q2', 'q2', shape='doublecircle')
            nfa_v.edge('S', 'q0'); nfa_v.edge('q0', 'q0', label='0,1'); nfa_v.edge('q0', 'q1', label='0'); nfa_v.edge('q1', 'q2', label='1')
            st.graphviz_chart(nfa_v)
        with col2:
            st.subheader("DFA (More Complex)")
            dfa_v = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
            dfa_v.node('S', '', shape='none'); dfa_v.node('q0', 'q0'); dfa_v.node('q1', 'q1'); dfa_v.node('q2', 'q2', shape='doublecircle')
            dfa_v.edge('S', 'q0'); dfa_v.edge('q0', 'q1', label='0'); dfa_v.edge('q0', 'q0', label='1')
            dfa_v.edge('q1', 'q1', label='0'); dfa_v.edge('q1', 'q2', label='1')
            dfa_v.edge('q2', 'q1', label='0'); dfa_v.edge('q2', 'q0', label='1')
            st.graphviz_chart(dfa_v)
    with tab_sim:
        st.markdown("### NFA Simulator (Contains '01')")
        def gen_nfa_diag(active_states):
            dot = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
            states = {'q0': 'Start', 'q1': 'Saw 0', 'q2': 'Accept 01'}
            for s, label in states.items():
                shape = 'doublecircle' if s == 'q2' else 'circle'
                color = 'blue' if s in active_states else 'black'
                penwidth = '3' if s in active_states else '1'
                dot.node(s, f"{label}\n({s})", shape=shape, color=color, penwidth=penwidth)
            dot.edge('q0', 'q0', label='0,1'); dot.edge('q0', 'q1', label='0'); dot.edge('q1', 'q2', label='1')
            return dot
        
        n_input = st.text_input("Enter binary string for NFA:", "001")
        n_speed = st.slider("NFA Speed:", 0.5, 3.0, 1.0)
        if st.button("Start NFA Simulation"):
            current_states = {'q0'}
            n_history = []
            nfa_placeholder = st.empty()
            for i, char in enumerate(n_input):
                nfa_placeholder.graphviz_chart(gen_nfa_diag(current_states))
                next_states = set()
                for s in current_states:
                    next_states.add('q0')
                    if s == 'q0' and char == '0': next_states.add('q1')
                    elif s == 'q1' and char == '1': next_states.add('q2')
                    elif s == 'q2': pass
                n_history.append({"Step": i+1, "Input": char, "Active States": str(list(next_states))})
                current_states = next_states
                time.sleep(n_speed)
            nfa_placeholder.graphviz_chart(gen_nfa_diag(current_states))
            st.table(pd.DataFrame(n_history))
            if 'q2' in current_states: st.success("✅ Accepted!")
            else: st.error("❌ Rejected")
    with tab_q:
        nfa_qs = [
            ("What does 'N' in NFA stand for?", ["Non-deterministic", "Network", "Null"], "Non-deterministic"),
            ("Can an NFA have multiple transitions for one symbol?", ["Yes", "No", "Only for ε"], "Yes"),
            ("Are ε-transitions allowed in NFA?", ["Yes", "No", "Only in DFA"], "Yes"),
            ("Is NFA more powerful than DFA?", ["No (Equally powerful)", "Yes", "Only for long strings"], "No (Equally powerful)"),
            ("In NFA, a string is accepted if:", ["At least one path accepts", "All paths accept", "No paths loop"], "At least one path accepts"),
            ("The transition function δ maps to:", ["A set of states", "A single state", "Empty set"], "A set of states"),
            ("NFA has finite memory?", ["True", "False", "Infinite"], "True"),
            ("Can every NFA be converted to a DFA?", ["Yes", "No", "Only if it has no ε"], "Yes"),
            ("What construction is used for NFA to DFA?", ["Subset Construction", "State Elimination", "Pumping"], "Subset Construction"),
            ("What is the symbol for empty transition?", ["ε (Epsilon)", "∅ (Empty set)", "Σ"], "ε (Epsilon)")
        ]
        n_score = 0
        for i, (q, opts, ans) in enumerate(nfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"nq_u_{i}")
            if u_ans == ans: n_score += 1
        if st.button("Submit NFA Quiz"):
            st.success(f"Your Score: {n_score}/10")

elif display_page == "Regular Expressions":
    st.markdown("## 🧩 Regular Expressions & Operations")
    tab_ops, tab_re, tab_conv, tab_q = st.tabs(["⚙️ Operations", "📝 REs", "🔄 RE to NFA", "📝 Quiz"])
    with tab_ops:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.1</div>
        <h3>Regular Operations</h3>
        <p>The three fundamental operations that define regular languages are:</p>
        <ul>
            <li><b>Union (L₁ ∪ L₂):</b> {w | w ∈ L₁ or w ∈ L₂}</li>
            <li><b>Concatenation (L₁ ∘ L₂):</b> {xy | x ∈ L₁ and y ∈ L₂}</li>
            <li><b>Star (L*):</b> {x₁x₂...xₖ | k ≥ 0 and each xᵢ ∈ L}. This includes the empty string ε.</li>
        </ul>
        <h4>Closure Properties:</h4>
        <p>Regular languages are <b>closed</b> under these operations, meaning applying them to regular languages always results in a regular language.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_re:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.2</div>
        <h3>Regular Expressions (RE)</h3>
        <p>A <b>Regular Expression</b> is a concise way to describe a regular language using symbols and operations.</p>
        <ul>
            <li><b>a:</b> Represents the language {a}.</li>
            <li><b>ε:</b> Represents the language {ε}.</li>
            <li><b>∅:</b> Represents the empty language.</li>
            <li><b>(R₁ ∪ R₂):</b> Union of two REs.</li>
            <li><b>(R₁ ∘ R₂):</b> Concatenation of two REs.</li>
            <li><b>(R*):</b> Kleene Star of an RE.</li>
        </ul>
        <p><b>Example:</b> (0 ∪ 1)* 00 (0 ∪ 1)* describes all binary strings containing '00'.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_conv:
        st.markdown("### RE to NFA (Thompson's Construction)")
        st.write("Each RE operation has a corresponding NFA structure:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Union (R1 ∪ R2)**")
            u_diag = graphviz.Digraph()
            u_diag.node('S', 'Start'); u_diag.node('R1', 'NFA R1'); u_diag.node('R2', 'NFA R2'); u_diag.node('E', 'End')
            u_diag.edge('S', 'R1', label='ε'); u_diag.edge('S', 'R2', label='ε'); u_diag.edge('R1', 'E', label='ε'); u_diag.edge('R2', 'E', label='ε')
            st.graphviz_chart(u_diag)
        with col2:
            st.write("**Concatenation (R1 ∘ R2)**")
            c_diag = graphviz.Digraph()
            c_diag.node('R1', 'NFA R1'); c_diag.node('R2', 'NFA R2')
            c_diag.edge('R1', 'R2', label='ε')
            st.graphviz_chart(c_diag)
        with col3:
            st.write("**Star (R*)**")
            s_diag = graphviz.Digraph()
            s_diag.node('S', 'Start'); s_diag.node('R', 'NFA R'); s_diag.node('E', 'End')
            s_diag.edge('S', 'R', label='ε'); s_diag.edge('R', 'E', label='ε'); s_diag.edge('E', 'S', label='ε'); s_diag.edge('S', 'E', label='ε')
            st.graphviz_chart(s_diag)
    with tab_q:
        re_qs = [
            ("What does L* represent?", ["Kleene Star (0 or more)", "Union", "Concatenation"], "Kleene Star (0 or more)"),
            ("Are regular languages closed under intersection?", ["Yes", "No", "Only if finite"], "Yes"),
            ("What does (0 ∪ 1)* represent?", ["All binary strings", "Only 0s and 1s", "Empty string only"], "All binary strings"),
            ("Thompson's construction handles Union using:", ["ε-transitions", "Sequential states", "Stack"], "ε-transitions"),
            ("The empty language is represented by:", ["∅", "ε", "Σ"], "∅"),
            ("Is (ab)* the same as a*b*?", ["No", "Yes", "Only for ε"], "No"),
            ("What is {a} ∘ {b}?", ["{ab}", "{a, b}", "{a, b, ab}"], "{ab}"),
            ("Can a regular expression describe a non-regular language?", ["No", "Yes", "Sometimes"], "No"),
            ("Does R* always include the empty string ε?", ["Yes", "No", "Only if R has ε"], "Yes"),
            ("Closure property means the result is also regular?", ["True", "False", "Maybe"], "True")
        ]
        r_score = 0
        for i, (q, opts, ans) in enumerate(re_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"rq_u_{i}")
            if u_ans == ans: r_score += 1
        if st.button("Submit RE Quiz"):
            st.success(f"Your Score: {r_score}/10")

elif display_page == "DFA to RE & Pumping Lemma":
    st.markdown("## 🔄 DFA to RE & Pumping Lemma")
    tab_conv, tab_pump, tab_q = st.tabs(["🔄 Conversion", "🧪 Pumping Lemma", "📝 Quiz"])
    with tab_conv:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.1</div>
        <h3>DFA to Regular Expression</h3>
        <p>The standard method to convert a DFA to an RE is the <b>State Elimination Method</b>. We transform the DFA into a <b>Generalized NFA (GNFA)</b> and eliminate states one by one until only the start and accept states remain.</p>
        <h4>The Formula:</h4>
        <p>When eliminating state <i>q_rip</i>, the new transition between <i>q_i</i> and <i>q_j</i> becomes:</p>
        <div class="step-box">R_new = R_ij ∪ (R_ir ∘ (R_rr)* ∘ R_rj)</div>
        <ul>
            <li><b>R_ij:</b> Direct transition from i to j.</li>
            <li><b>R_ir:</b> Transition from i to the state being eliminated.</li>
            <li><b>R_rr:</b> Self-loop on the state being eliminated.</li>
            <li><b>R_rj:</b> Transition from the eliminated state to j.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("### Visual: State Elimination Step")
        elim_diag = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
        elim_diag.node('qi', 'qi'); elim_diag.node('qj', 'qj'); elim_diag.node('qr', 'q_rip', color='red')
        elim_diag.edge('qi', 'qr', label='R_ir'); elim_diag.edge('qr', 'qr', label='R_rr'); elim_diag.edge('qr', 'qj', label='R_rj'); elim_diag.edge('qi', 'qj', label='R_ij')
        st.graphviz_chart(elim_diag)
    with tab_pump:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.2</div>
        <h3>Pumping Lemma for Regular Languages</h3>
        <p>The <b>Pumping Lemma</b> is a tool used to prove that a language is <b>NOT</b> regular. It states that if a language L is regular, there exists a pumping length <i>p</i> such that any string <i>s</i> in L with |s| ≥ p can be split into three parts <i>s = xyz</i> satisfying:</p>
        <ol>
            <li><b>|y| > 0</b> (The pumped part is not empty).</li>
            <li><b>|xy| ≤ p</b> (The pumping happens within the first p symbols).</li>
            <li><b>xyⁱz ∈ L</b> for all i ≥ 0 (Pumping y any number of times stays in the language).</li>
        </ol>
        <h4>How to use it (Proof by Contradiction):</h4>
        <ol>
            <li>Assume L is regular.</li>
            <li>There must be a pumping length <i>p</i>.</li>
            <li>Choose a specific string <i>s</i> ∈ L such that |s| ≥ p.</li>
            <li>Show that for <i>all</i> possible splits <i>s = xyz</i>, there is an <i>i</i> such that <i>xyⁱz</i> ∉ L.</li>
            <li>This contradicts the lemma, so L is not regular.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    with tab_q:
        dp_qs = [
            ("What is the method to convert DFA to RE?", ["State Elimination", "Subset Construction", "Pumping"], "State Elimination"),
            ("Pumping Lemma is used to prove a language is regular?", ["False", "True", "Only for finite"], "False"),
            ("In s = xyz, which part is pumped?", ["y", "x", "z"], "y"),
            ("What is the condition for |y|?", ["> 0", "= 0", "< p"], "> 0"),
            ("What is the condition for |xy|?", ["≤ p", "> p", "= p"], "≤ p"),
            ("Is the language {aⁿbⁿ | n ≥ 0} regular?", ["No", "Yes", "Only for n < 10"], "No"),
            ("A GNFA has how many states after elimination?", ["2 (Start & Accept)", "1", "0"], "2 (Start & Accept)"),
            ("Can a DFA recognize balanced parentheses?", ["No", "Yes", "Only if nested"], "No"),
            ("The pumping length p depends on the language?", ["True", "False", "It's always 5"], "True"),
            ("If i = 0 in xyⁱz, it means:", ["y is removed", "y stays the same", "y is doubled"], "y is removed")
        ]
        dp_score = 0
        for i, (q, opts, ans) in enumerate(dp_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dpq_u_{i}")
            if u_ans == ans: dp_score += 1
        if st.button("Submit Module 5 Quiz"):
            st.success(f"Your Score: {dp_score}/10")

elif display_page == "CFG & Chomsky Form":
    st.markdown("## 📜 Context-Free Grammars & Chomsky Form")
    tab_cfg, tab_cnf, tab_q = st.tabs(["📝 CFG", "📐 CNF", "📝 Quiz"])
    with tab_cfg:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.1</div>
        <h3>Context-Free Grammar (CFG)</h3>
        <p>A <b>CFG</b> is a 4-tuple (V, Σ, R, S):</p>
        <ul>
            <li><b>V:</b> Finite set of variables (non-terminals).</li>
            <li><b>Σ:</b> Finite set of terminals (alphabet).</li>
            <li><b>R:</b> Finite set of rules (e.g., A → 0A1 | ε).</li>
            <li><b>S:</b> Start variable (S ∈ V).</li>
        </ul>
        <p>CFGs are more powerful than regular expressions and can describe languages like {aⁿbⁿ}.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("### Visual: Derivation Tree for '0011'")
        tree = graphviz.Digraph()
        tree.node('S1', 'S'); tree.node('01', '0'); tree.node('S2', 'S'); tree.node('11', '1')
        tree.node('02', '0'); tree.node('S3', 'ε'); tree.node('12', '1')
        tree.edge('S1', '01'); tree.edge('S1', 'S2'); tree.edge('S1', '11')
        tree.edge('S2', '02'); tree.edge('S2', 'S3'); tree.edge('S2', '12')
        st.graphviz_chart(tree)
    with tab_cnf:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.2</div>
        <h3>Chomsky Normal Form (CNF)</h3>
        <p>A CFG is in <b>CNF</b> if every rule is of the form:</p>
        <div class="step-box">A → BC  OR  A → a</div>
        <p>Where A, B, C are variables (B, C not the start variable) and 'a' is a terminal.</p>
        <h4>Steps to convert CFG to CNF:</h4>
        <ol>
            <li><b>New Start State:</b> Add S₀ → S.</li>
            <li><b>Eliminate ε-rules:</b> Remove A → ε and update other rules.</li>
            <li><b>Eliminate Unit rules:</b> Remove A → B.</li>
            <li><b>Eliminate Long rules:</b> Break A → BCD into A → BC₁ and C₁ → D.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    with tab_q:
        cfg_qs = [
            ("What does CFG stand for?", ["Context-Free Grammar", "Computer Finite Grammar", "Central Form"], "Context-Free Grammar"),
            ("In (V, Σ, R, S), Σ represents:", ["Terminals", "Variables", "Rules"], "Terminals"),
            ("Is A → BC allowed in CNF?", ["True", "False", "Only if A is start"], "True"),
            ("Is A → aB allowed in CNF?", ["False", "True", "Only if B is terminal"], "False"),
            ("What is the first step in CNF conversion?", ["Add new start variable", "Eliminate ε", "Eliminate unit"], "Add new start variable"),
            ("Are CFGs more powerful than DFAs?", ["True", "False", "Equally powerful"], "True"),
            ("The start variable is usually denoted by:", ["S", "V", "Σ"], "S"),
            ("Can CFG recognize {aⁿbⁿ}?", ["Yes", "No", "Only for small n"], "Yes"),
            ("In CNF, how many variables on the RHS?", ["Exactly 2", "At least 2", "Exactly 1"], "Exactly 2"),
            ("A rule A → B is called a:", ["Unit rule", "ε-rule", "Terminal rule"], "Unit rule")
        ]
        c_score = 0
        for i, (q, opts, ans) in enumerate(cfg_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"cq_u_{i}")
            if u_ans == ans: c_score += 1
        if st.button("Submit CFG Quiz"):
            st.success(f"Your Score: {c_score}/10")

elif display_page == "PDA & CFL Theory":
    st.markdown("## ⚙️ Pushdown Automata & CFL Theory")
    tab_pda, tab_theory, tab_q = st.tabs(["🤖 PDA", "🧪 CFL Theory", "📝 Quiz"])
    with tab_pda:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.1</div>
        <h3>Pushdown Automata (PDA)</h3>
        <p>A <b>PDA</b> is essentially a Finite Automaton with an added <b>Stack</b> (Infinite memory, LIFO). It is defined by a 6-tuple (Q, Σ, Γ, δ, q₀, F):</p>
        <ul>
            <li><b>Γ:</b> Stack alphabet.</li>
            <li><b>δ:</b> Transition function (Q × (Σ ∪ {ε}) × (Γ ∪ {ε}) → P(Q × (Γ ∪ {ε}))).</li>
        </ul>
        <p><b>Equivalence:</b> A language is Context-Free if and only if some PDA recognizes it.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_theory:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.2</div>
        <h3>Pumping Lemma for CFLs</h3>
        <p>If L is a CFL, any string <i>s</i> with |s| ≥ p can be split into <i>s = uvxyz</i> such that:</p>
        <ol>
            <li><b>|vxy| ≤ p</b></li>
            <li><b>|vy| > 0</b></li>
            <li><b>uvⁱxyⁱz ∈ L</b> for all i ≥ 0.</li>
        </ol>
        <p><b>Example:</b> {aⁿbⁿcⁿ} is NOT a CFL (proved by this lemma).</p>
        </div>
        """, unsafe_allow_html=True)
    with tab_q:
        pc_qs = [
            ("PDA is equivalent to which grammar?", ["CFG", "Regular", "Unrestricted"], "CFG"),
            ("How many parts in CFL Pumping Lemma?", ["5 (uvxyz)", "3 (xyz)", "2"], "5 (uvxyz)"),
            ("Is {aⁿbⁿcⁿ} a Context-Free Language?", ["No", "Yes", "Only if n is even"], "No"),
            ("Which parts are pumped in CFL lemma?", ["v and y", "u and z", "x only"], "v and y"),
            ("What memory structure does a PDA use?", ["Stack", "Queue", "Random Access"], "Stack"),
            ("Is every regular language a CFL?", ["True", "False", "Only if finite"], "True"),
            ("Is NPDA more powerful than DPDA?", ["True", "False", "Equally powerful"], "True"),
            ("Condition for pumped parts in CFL?", ["|vy| > 0", "|v| > 0", "|y| > 0"], "|vy| > 0"),
            ("Can a PDA recognize {ww^R}?", ["Yes", "No", "Only if w is short"], "Yes"),
            ("Condition for length in CFL lemma?", ["|vxy| ≤ p", "|uvx| ≤ p", "|xyz| ≤ p"], "|vxy| ≤ p")
        ]
        pc_score = 0
        for i, (q, opts, ans) in enumerate(pc_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"pcq_u_{i}")
            if u_ans == ans: pc_score += 1
        if st.button("Submit Module 7 Quiz"):
            st.success(f"Your Score: {pc_score}/10")

elif display_page == "Turing Machines & Algorithms":
    st.markdown("## 📟 Turing Machines & Algorithms")
    tab_tm, tab_dec, tab_var, tab_alg, tab_q = st.tabs(["📟 TM Definition", "🛑 Decidability", "🔄 Variants", "⚙️ Algorithms & Encoding", "📝 Quiz"])
    
    with tab_tm:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.1</div>
        <h3>The Turing Machine (TM)</h3>
        <p>A <b>Turing Machine</b> is the most powerful model of computation, capable of simulating any computer algorithm. It was proposed by Alan Turing in 1936.</p>
        <h4>The 7-Tuple Definition:</h4>
        <p>M = (Q, Σ, Γ, δ, q₀, q_acc, q_rej)</p>
        <ul>
            <li><b>Q:</b> Finite set of states.</li>
            <li><b>Σ:</b> Input alphabet (not containing the blank symbol ␣).</li>
            <li><b>Γ:</b> Tape alphabet (contains Σ and ␣).</li>
            <li><b>δ:</b> Transition function (δ: Q × Γ → Q × Γ × {L, R}).</li>
            <li><b>q₀:</b> Start state.</li>
            <li><b>q_acc:</b> Accept state.</li>
            <li><b>q_rej:</b> Reject state.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("### Visual: Turing Machine Components")
        tm_diag = graphviz.Digraph(graph_attr={'rankdir': 'LR'})
        tm_diag.node('Tape', 'Infinite Tape\n[a][b][c][␣][␣]...', shape='square')
        tm_diag.node('Head', 'Read/Write Head', shape='invhouse')
        tm_diag.node('Control', 'Finite Control\n(States & Rules)', shape='circle')
        tm_diag.edge('Control', 'Head', label='Move L/R')
        tm_diag.edge('Head', 'Tape', label='Read/Write')
        st.graphviz_chart(tm_diag)

    with tab_dec:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.2</div>
        <h3>Decidability vs. Recognizability</h3>
        <p>A Turing Machine can behave in three ways on an input:</p>
        <ol>
            <li><b>Accept:</b> The TM reaches q_acc.</li>
            <li><b>Reject:</b> The TM reaches q_rej.</li>
            <li><b>Loop:</b> The TM never halts (runs forever).</li>
        </ol>
        <div class="info-grid">
            <div class="info-item">
                <h4>Turing-Decidable (Recursive)</h4>
                <p>A language is <b>decidable</b> if there exists a TM (called a <b>Decider</b>) that halts on ALL inputs (either accepts or rejects).</p>
            </div>
            <div class="info-item">
                <h4>Turing-Recognizable (Recursively Enumerable)</h4>
                <p>A language is <b>recognizable</b> if there exists a TM that accepts all strings in the language. For strings NOT in the language, it may reject or loop forever.</p>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_var:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.3</div>
        <h3>Variants of Turing Machines</h3>
        <p>Surprisingly, many "enhanced" versions of TMs have the <b>same power</b> as the standard TM:</p>
        <ul>
            <li><b>Multi-tape TM:</b> Has multiple tapes and heads. Can be simulated by a single-tape TM.</li>
            <li><b>Non-deterministic TM (NTM):</b> Can have multiple possible transitions. Can be simulated by a deterministic TM.</li>
            <li><b>Enumerators:</b> A TM with a printer that lists all strings in a language.</li>
        </ul>
        <p><b>Church-Turing Thesis:</b> Any algorithmic process can be simulated by a Turing Machine.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_alg:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.4</div>
        <h3>Algorithms & Encoding</h3>
        <p>To process complex objects (graphs, grammars, other TMs), we must <b>encode</b> them into a string format that a TM can read.</p>
        <div class="step-box">
            <b>Notation:</b> ⟨O⟩ represents the encoding of object O.
        </div>
        <h4>High-Level Description of Algorithms:</h4>
        <p>Instead of writing δ functions, we describe TM behavior in stages:</p>
        <ol>
            <li>"On input ⟨G⟩ where G is a graph..."</li>
            <li>"Mark the first node..."</li>
            <li>"Repeat until no more nodes can be marked..."</li>
            <li>"If all nodes are marked, Accept; else, Reject."</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    with tab_q:
        st.markdown("### 📝 Turing Machine Quiz (10 Questions)")
        tm_qs = [
            ("How many elements in a TM tuple?", ["7", "5", "6"], "7"),
            ("A TM that halts on all inputs is called a:", ["Decider", "Recognizer", "Enumerator"], "Decider"),
            ("The tape alphabet Γ must contain:", ["Blank symbol (␣)", "ε", "Only 0 and 1"], "Blank symbol (␣)"),
            ("Can a TM move its head to the left?", ["Yes", "No", "Only at the start"], "Yes"),
            ("The Church-Turing Thesis states that TMs can simulate any:", ["Algorithm", "DFA", "Human"], "Algorithm"),
            ("Is every decidable language also recognizable?", ["True", "False", "Only if finite"], "True"),
            ("Does a Multi-tape TM have more power than a single-tape TM?", ["No (Same power)", "Yes", "Only for speed"], "No (Same power)"),
            ("If a TM reaches q_reject, it:", ["Halts and rejects", "Loops forever", "Restarts"], "Halts and rejects"),
            ("What does ⟨M⟩ represent?", ["Encoding of TM M", "Size of TM M", "States of TM M"], "Encoding of TM M"),
            ("An Enumerator is equivalent in power to a TM?", ["True", "False", "Only for regular languages"], "True")
        ]
        t_score = 0
        for i, (q, opts, ans) in enumerate(tm_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"tq_u_{i}")
            if u_ans == ans: t_score += 1
        if st.button("Submit TM Quiz"):
            st.success(f"Your Score: {t_score}/10")

elif display_page == "🎓 Course Completion":
    st.balloons()
    st.markdown("## 🎓 تهانينا! تم إتمام مقرر نظرية الحوسبة")
    st.markdown("""
    <div class="learning-card" style="text-align: center; border: 5px solid #1e3a8a;">
        <h1 style="color: #1e3a8a;">🎉 CONGRATULATIONS 🎉</h1>
        <p style="font-size: 24px;">لقد أتممت بنجاح رحلتك التعليمية في مقرر <b>نظرية الحوسبة (Theory of Computation)</b>.</p>
        <p>من خلال هذه المنصة، استعرضت المفاهيم من أبسط قواعد الأبجدية وصولاً إلى أعقد نماذج الحوسبة العالمية.</p>
        <hr>
        <h3>📊 ملخص المنهج الشامل / Executive Summary</h3>
        <table class="summary-table">
            <tr>
                <th>الموضوع (Module)</th>
                <th>المفهوم الأساسي (Key Concept)</th>
                <th>نموذج الآلة (Machine Model)</th>
            </tr>
            <tr>
                <td>Foundations</td>
                <td>Alphabets, Strings, Languages, Logic</td>
                <td>Mathematical Sets</td>
            </tr>
            <tr>
                <td>Regular Languages</td>
                <td>DFA, NFA, Regular Expressions</td>
                <td>Finite Automata (FA)</td>
            </tr>
            <tr>
                <td>Context-Free Languages</td>
                <td>CFG, Chomsky Normal Form (CNF)</td>
                <td>Pushdown Automata (PDA)</td>
            </tr>
            <tr>
                <td>Computability Theory</td>
                <td>Decidability, Algorithms, Encoding</td>
                <td>Turing Machines (TM)</td>
            </tr>
        </table>
        <br>
        <p><i>"The power of computation is not just in the machines we build, but in the theories that define them."</i></p>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Introduction to OS":
    st.markdown("## ⚙️ Operating Systems: Introduction")
    st.markdown("""
    <div class="learning-card">
    <div class="concept-badge">Module 1.1</div>
    <h3>What is an Operating System?</h3>
    <p>An <b>Operating System (OS)</b> is a software that acts as an intermediary between a computer user and the computer hardware. The purpose of an OS is to provide an environment in which a user can execute programs in a convenient and efficient manner.</p>
    <h4>Main Functions of an OS:</h4>
    <ul>
        <li><b>Resource Management:</b> Manages hardware resources like CPU, memory, and I/O devices.</li>
        <li><b>Process Management:</b> Scheduling, creation, and deletion of processes.</li>
        <li><b>Memory Management:</b> Allocating and deallocating memory space as needed.</li>
        <li><b>Storage Management:</b> Managing files and directories on secondary storage.</li>
        <li><b>Security & Protection:</b> Protecting data and resources from unauthorized access.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
elif display_page == "Introduction to OS":
    st.markdown("## ⚙️ Operating Systems: Introduction")

    st.markdown("""
    <div class="learning-card">
    <div class="concept-badge">Module 1.1</div>

    <h3>What is an Operating System?</h3>

    <p>An <b>Operating System (OS)</b> is a software that acts as an intermediary between a computer user and the computer hardware.</p>

    <h4>Main Functions of an OS:</h4>
    <ul>
        <li><b>Resource Management:</b> Manages hardware resources like CPU, memory, and I/O devices.</li>
        <li><b>Process Management:</b> Scheduling, creation, and deletion of processes.</li>
        <li><b>Memory Management:</b> Allocating and deallocating memory space as needed.</li>
        <li><b>Storage & I/O:</b> Managing files and devices on secondary storage.</li>
        <li><b>Security & Protection:</b> Protecting data and system resources from unauthorized access.</li>
    </ul>

    <h4>📚 What Operating Systems Do (Added Content):</h4>
    <ul>
        <li>Handle system resources efficiently</li>
        <li>Provide user interface (GUI / CLI)</li>
        <li>Run applications and processes</li>
        <li>Control hardware and software interaction</li>
    </ul>

    <h4>📌 Operating System Types:</h4>
    <ul>
        <li>Batch Operating Systems</li>
        <li>Time-Sharing Systems</li>
        <li>Distributed Operating Systems</li>
        <li>Real-Time Operating Systems</li>
    </ul>

    <h4>🏗️ Computer-System Organization:</h4>
    <ul>
        <li>CPU, Memory, I/O Devices</li>
        <li>Bus structure connects components</li>
        <li>Interrupt-based communication</li>
    </ul>

    <h4>🧠 Computer-System Architecture:</h4>
    <ul>
        <li>Single Processor Systems</li>
        <li>Multiprocessor Systems</li>
        <li>Clustered Systems</li>
    </ul>

    <h4>⚙️ Resource Management:</h4>
    <ul>
        <li>CPU Scheduling</li>
        <li>Memory Allocation</li>
        <li>Disk & File Management</li>
    </ul>

    <h4>🧩 Virtualization:</h4>
    <ul>
        <li>Running multiple OS on one machine</li>
        <li>Virtual Machines (VMs)</li>
        <li>Hypervisors</li>
    </ul>

    <h4>🧱 Kernel Data Structures:</h4>
    <ul>
        <li>Process Control Block (PCB)</li>
        <li>Queues (Ready, Waiting)</li>
        <li>Page Tables</li>
    </ul>

    <h4>💡 Open Source Operating Systems:</h4>
    <ul>
        <li>Linux</li>
        <li>Ubuntu</li>
        <li>FreeBSD</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

elif display_page == "Process Management":
    st.info("Process Management module is under development. Stay tuned!")
elif display_page == "Memory Management":
    st.info("Memory Management module is under development. Stay tuned!")
elif display_page == "Storage & I/O":
    st.info("Storage & I/O module is under development. Stay tuned!")

elif display_page == "Contact Developer":
    st.markdown("### 📧 Contact the Developer / تواصل مع المبرمجة")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🏛️ **Academic Email**")
        st.code("451000518@stu.ut.edu.sa")
    with col2:
        st.success("📩 **Personal Email**")
        st.code("mohrah.atiiah@icloud.com")

elif display_page == "Community Feedback":
    st.markdown("### 💬 Feedback Board")
    with st.form("feedback_form"):
        name = st.text_input("Name:"); msg = st.text_area("Feedback:")
        if st.form_submit_button("Post"):
            if name and msg: save_comment(name, msg); st.success("Comment saved!")
    st.markdown("---")
    for c in reversed(load_comments()):
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small><br>{c['m']}</div>""", unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
        </p>
    </div>
    """, unsafe_allow_html=True)