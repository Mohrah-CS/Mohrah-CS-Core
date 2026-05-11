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
    initial_data = [
        {"u": "Academic Support", "m": "Welcome to Mohrah's Lab! Your feedback is valued.", "t": "09:00 AM"},
        {"u": "مهره الجهني", "m": "أهلاً بكم في منصتي التعليمية، أتمنى أن تجدوا الفائدة والمتعة في تعلم علوم الحاسب.", "t": "10:30 AM"},
        {"u": "شعاع", "m": "المشروع رائع جداً ومفيد، شكراً لكِ يا مهره على هذا المجهود المتميز.", "t": "11:15 AM"}
    ]
    if 'persistent_comments' not in st.session_state:
        if os.path.exists("comments.json"):
            try:
                with open("comments.json", "r", encoding="utf-8") as f:
                    st.session_state.persistent_comments = json.load(f)
            except:
                st.session_state.persistent_comments = initial_data
        else:
            st.session_state.persistent_comments = initial_data
            try:
                with open("comments.json", "w", encoding="utf-8") as f:
                    json.dump(initial_data, f, ensure_ascii=False, indent=4)
            except: pass
    return st.session_state.persistent_comments

def save_comment(name, msg):
    comments = load_comments()
    comments.append({"u": name, "m": msg, "t": time.strftime("%I:%M %p")})
    st.session_state.persistent_comments = comments
    try:
        with open("comments.json", "w", encoding="utf-8") as f:
            json.dump(comments, f, ensure_ascii=False, indent=4)
    except: pass
    st.rerun()

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
    .announcement-banner {
        background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 100%);
        color: #0f172a; padding: 12px; border-radius: 12px;
        text-align: center; font-weight: bold; margin-bottom: 20px;
        border: 2px solid #d97706; direction: rtl;
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
            direction: rtl; text-align: right;
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

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home Page"

main_subject = st.sidebar.selectbox(
    "Select Course / اختر المادة:",
    ["Home Page", "Theory of Computation", "Operating Systems"],
    index=0 if st.session_state.current_page == "Home Page" else (1 if st.session_state.current_page in ["Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Turing Machines & Algorithms", "🎓 Course Completion"] else 2)
)

if main_subject == "Theory of Computation":
    subject = st.sidebar.selectbox(
        "Select Lesson / اختر الدرس:",
        ["Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Turing Machines & Algorithms", "🎓 Course Completion"]
    )
    if st.session_state.current_page not in ["Community Feedback", "Contact Developer"]:
     st.session_state.current_page = subject
elif main_subject == "Operating Systems":
    subject = st.sidebar.selectbox(
        "Select Lesson / اختر الدرس:",
        ["Introduction to OS", "What Operating Systems Do", "Operating System Types", "Computer-System Organization", "Computer-System Architecture", "Computer-System Operations", "Resource Management", "Virtualization", "Kernel Data Structures", "Free/Libre and Open-Source Operating Systems", "Process Management", "Memory Management", "Storage & I/O"]
    )
    st.session_state.current_page = subject
else:
    st.session_state.current_page = "Home Page"

st.sidebar.write("---")
st.sidebar.write("### 📞 تواصل معي / Contact Me")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("📧 Contact", key="contact_btn"):
        st.session_state.current_page = "Contact Developer"
with col2:
    if st.button("💬 Feedback", key="feedback_btn"):
        st.session_state.current_page = "Community Feedback"

display_page = st.session_state.current_page

# --- 6. MODULES ---

if display_page == "Home Page":
    st.markdown("""<div class="announcement-banner">📢 تحديث جديد: تم بحمد الله وضع جميع الشباتر النظرية كمرجع شامل لكم في المنصة! 🎓</div>""", unsafe_allow_html=True)
    st.markdown("## 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    <div class="learning-card">
    <h3>عن المنصة / About the Platform</h3>
    <p>هذه المنصة هي <b>مبادرة طلابية تعليمية متقدمة</b> تهدف إلى سد الفجوة بين المفاهيم الرياضية المجردة والتطبيقات البرمجية التفاعلية في مجال نظرية الحوسبة (Theory of Computation).</p>
    <p><b>المصدر العلمي (Academic Source):</b>  
    تم استقاء كافة المعلومات العلمية، التعريفات الرياضية، والنماذج التوضيحية من المناهج الأكاديمية المعتمدة في <b>جامعة تبوك</b>. تم تصميم المحتوى ليكون مرجعاً شاملاً يساعد الطلاب على فهم تعقيدات الأوتوماتا واللغات الرسمية.</p>
    <div class="info-grid">
        <div class="info-item">
            <h4 style="margin:0; color:#1e3a8a;">🎯 الهدف</h4>
            تبسيط المفاهيم المعقدة مثل DFA, NFA, و PDA من خلال أدوات بصرية تفاعلية تجعل التعلم أكثر عمقاً.
        </div>
        <div class="info-item">
            <h4 style="margin:0; color:#1e3a8a;">🛠️ الأدوات</h4>
            استخدام لغة Python وإطار عمل Streamlit لتوفير محاكيات حية وتقنيات عرض البيانات المتقدمة.
        </div>
        <div class="info-item">
            <h4 style="margin:0; color:#1e3a8a;">📚 المحتوى</h4>
            تغطية شاملة للمادة العلمية ابتداءً من الألفباء والسلاسل وصولاً إلى أعقد نماذج الحوسبة.
        </div>
    </div>
    <div style="margin-top: 30px; padding: 20px; background: #f1f5f9; border-radius: 12px; text-align: center;">
        <b>استخدم القائمة الجانبية ⬅️ للبدء في تصفح الدروس والمحاكيات</b>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Foundations of TOC":
    st.markdown("## 📘 Foundations of Theory of Computation")
    
    tab_intro, tab_alphabets, tab_strings, tab_languages, tab_sets, tab_functions, tab_boolean, tab_q = st.tabs([
        "📖 Introduction", "🔤 Alphabets", "🧵 Strings", "🗣️ Languages", "📊 Sets", "⚙️ Functions", "🧠 Boolean Logic", "📝 Comprehensive Quiz"
    ])
    
    with tab_intro:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.0</div>
        <h3>What is Theory of Computation?</h3>
        <p><b>Theory of Computation (TOC)</b> is a branch of computer science and mathematics that deals with whether and how efficiently problems can be solved on a model of computation, using an algorithm.</p>
        <p>The field is divided into three major branches:</p>
        <ol>
            <li><b>Automata Theory:</b> Deals with different models of devices (abstract machines).</li>
            <li><b>Computability Theory:</b> What can be computed and what cannot.</li>
            <li><b>Complexity Theory:</b> What makes some problems hard and others easy to solve.</li>
        </ol>
        <div class="step-box">
            <b>Why study it?</b> It provides the formal framework for understanding the limitations and capabilities of computers.
        </div>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_alphabets:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Formal Definition</div>
        <h3>1. Alphabets (Σ - Sigma)</h3>
        <p>An <b>alphabet</b> is a finite, non-empty set of symbols.</p>
        <ul>
            <li>Example 1: Binary alphabet Σ = {0, 1}</li>
            <li>Example 2: English alphabet Σ = {a, b, c, ..., z}</li>
            <li>Example 3: Σ = {0, 1, a, b}</li>
        </ul>
        <p>Symbols are the atomic building blocks of the theory.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_strings:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Definition</div>
        <h3>2. Strings (w)</h3>
        <p>A <b>string</b> is a finite sequence of symbols chosen from some alphabet.</p>
        <ul>
            <li>If Σ = {0, 1}, then <span class="highlight">01101</span> is a string.</li>
            <li><b>Empty String (ε - Epsilon):</b> A string with zero symbols. Its length |ε| = 0.</li>
            <li><b>Length (|w|):</b> The number of symbol positions in the string. Example: |011| = 3.</li>
        </ul>
        <h3>Operations on Strings:</h3>
        <p><b>1. Concatenation:</b> If x = dog and y = house, then xy = doghouse.</p>
        <p><b>2. Power of Alphabet (Σⁿ):</b> The set of all strings of length n over Σ.</p>
        <ul>
            <li>Σ⁰ = {ε}</li>
            <li>Σ¹ = {0, 1} (if binary)</li>
            <li>Σ² = {00, 01, 10, 11}</li>
            <li><b>Σ* (Kleene Star):</b> The set of ALL possible strings over Σ, including ε.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_languages:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Logic</div>
        <h3>3. Languages (L)</h3>
        <p>A <b>language</b> is a set of strings all of which are chosen from some Σ*.</p>
        <p>If L ⊆ Σ*, then L is a language over Σ.</p>
        <ul>
            <li>Example: L = {strings of 0s and 1s with an equal number of each}.</li>
            <li>Example: The set of all valid Python programs.</li>
            <li><b>Empty Language (∅):</b> A language with no strings. (Note: ∅ ≠ {ε}).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sets:
        st.markdown("""
        <div class="learning-card">
        <h3>4. Sets Theory in TOC</h3>
        <p>A set is a collection of objects (elements). In TOC, we use sets to define alphabets and languages.</p>
        <ul>
            <li><b>Union (A ∪ B):</b> Elements in A OR B.</li>
            <li><b>Intersection (A ∩ B):</b> Elements in both A AND B.</li>
            <li><b>Complement (Ā):</b> Elements NOT in A (within the universe Σ*).</li>
            <li><b>Power Set (P(S)):</b> The set of all subsets of S.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_functions:
        st.markdown("""
        <div class="learning-card">
        <h3>5. Functions & Relations</h3>
        <p>In TOC, we use functions to describe how an automaton moves from one state to another.</p>
        <ul>
            <li><b>Transition Function (δ):</b> Takes a state and an input symbol, and returns the next state. 
            <br>Format: <span class="highlight">δ: Q × Σ → Q</span></li>
            <li><b>Domain & Range:</b> Essential for defining valid inputs for our machines.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_boolean:
        st.markdown("""
        <div class="learning-card">
        <h3>6. Boolean Logic</h3>
        <p>The foundation of decision problems (Yes/No answers).</p>
        <ul>
            <li><b>AND (∧):</b> True only if both inputs are true.</li>
            <li><b>OR (∨):</b> True if at least one input is true.</li>
            <li><b>NOT (¬):</b> Inverts the value.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        with tab_q:
        st.markdown("### 📝 Foundations Quiz")
        q1 = st.radio("1. What is the length of the empty string ε?", ["0", "1", "Undefined"])
        q2 = st.radio("2. If Σ = {0, 1}, what is Σ⁰?", ["{0, 1}", "{ε}", "∅"])
        if st.button("Check Answers", key="q_foundations"):
            if q1 == "0" and q2 == "{ε}":
                st.success("Correct! You have a solid foundation.")
            else:
                st.error("Some answers are incorrect. Review the Strings tab!")

elif display_page == "DFA Explorer":
    st.markdown("## 🕹️ Deterministic Finite Automata (DFA)")
    
    tab_def, tab_sim, tab_formal = st.tabs(["📖 Definition", "🚀 Live Simulator", "📐 Formal Description"])
    
    with tab_def:
        st.markdown("""
        <div class="learning-card">
        <h3>What is a DFA?</h3>
        <p>A <b>DFA</b> is a theoretical model of a machine that has a finite number of states and moves between them based on input symbols.</p>
        <p><b>Key Characteristics:</b></p>
        <ul>
            <li>For every state and every input symbol, there is <b>exactly one</b> transition.</li>
            <li>It is predictable and deterministic.</li>
            <li>It is used in lexical analysis and pattern matching.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sim:
        st.write("### Interactive DFA Simulator")
        st.info("Goal: Create a DFA that accepts strings ending with '1'.")
        
        test_input = st.text_input("Enter a binary string (e.g., 101, 110):", "101")
        
        if test_input:
            if all(c in '01' for c in test_input):
                current_state = "q0"
                path = ["q0"]
                for char in test_input:
                    if current_state == "q0":
                        current_state = "q1" if char == '1' else "q0"
                    else: # q1
                        current_state = "q1" if char == '1' else "q0"
                    path.append(current_state)
                
                cols = st.columns(len(path))
                for i, s in enumerate(path):
                    cols[i].metric(f"Step {i}", s)
                
                if current_state == "q1":
                    st.success(f"String '{test_input}' is ACCEPTED ✅")
                else:
                    st.error(f"String '{test_input}' is REJECTED ❌")
                
                # Visualizing the DFA
                dot = graphviz.Digraph()
                dot.attr(rankdir='LR')
                dot.node('start', shape='point')
                dot.node('q0', 'q0 (Start)')
                dot.node('q1', 'q1 (Final)', shape='doublecircle')
                dot.edge('start', 'q0')
                dot.edge('q0', 'q0', label='0')
                dot.edge('q0', 'q1', label='1')
                dot.edge('q1', 'q0', label='0')
                dot.edge('q1', 'q1', label='1')
                st.graphviz_chart(dot)
            else:
                st.warning("Please enter only 0s and 1s.")

    with tab_formal:
        st.markdown("""
        <div class="learning-card">
        <h3>The 5-Tuple Definition</h3>
        <p>A DFA is formally defined by 5 components <span class="highlight">M = (Q, Σ, δ, q₀, F)</span>:</p>
        <ol>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (Alphabet).</li>
            <li><b>δ:</b> The transition function (δ: Q × Σ → Q).</li>
            <li><b>q₀:</b> The start state (q₀ ∈ Q).</li>
            <li><b>F:</b> The set of accept/final states (F ⊆ Q).</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "NFA Masterclass":
    st.markdown("## 🌪️ Non-Deterministic Finite Automata (NFA)")
    
    tab_n_def, tab_n_diff, tab_n_sim = st.tabs(["📖 NFA Definition", "⚖️ DFA vs NFA", "🛠️ NFA Visualization"])
    
    with tab_n_def:
        st.markdown("""
        <div class="learning-card">
        <h3>What is an NFA?</h3>
        <p>In an <b>NFA</b>, for a given state and input symbol, the machine can move to <b>multiple</b> states or even <b>none</b>.</p>
        <p><b>ε-Transitions:</b> An NFA can change states without reading any input symbol at all!</p>
        <div class="step-box">
            <b>Power:</b> Even though NFAs seem more powerful, they are actually equivalent to DFAs in terms of the languages they can recognize.
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab_n_diff:
        st.markdown("""
        <table class="summary-table">
            <tr><th>Feature</th><th>DFA</th><th>NFA</th></tr>
            <tr><td>Predictability</td><td>Deterministic (One path)</td><td>Non-deterministic (Multiple paths)</td></tr>
            <tr><td>ε-Transitions</td><td>Not allowed</td><td>Allowed</td></tr>
            <tr><td>Complexity</td><td>Harder to design</td><td>Easier to design</td></tr>
            <tr><td>Implementation</td><td>Directly in code</td><td>Usually converted to DFA</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with tab_n_sim:
        st.write("### NFA Construction Example")
        st.write("An NFA that accepts strings containing '01'.")
        nfa_dot = graphviz.Digraph()
        nfa_dot.attr(rankdir='LR')
        nfa_dot.node('start', shape='point')
        nfa_dot.node('q0', 'q0')
        nfa_dot.node('q1', 'q1')
        nfa_dot.node('q2', 'q2', shape='doublecircle')
        nfa_dot.edge('start', 'q0')
        nfa_dot.edge('q0', 'q0', label='0, 1')
        nfa_dot.edge('q0', 'q1', label='0')
        nfa_dot.edge('q1', 'q2', label='1')
        nfa_dot.edge('q2', 'q2', label='0, 1')
        st.graphviz_chart(nfa_dot)

elif display_page == "Regular Expressions":
    st.markdown("## 🧩 Regular Expressions (RE)")
    
    tab_re_intro, tab_re_ops, tab_re_examples = st.tabs(["📖 Intro", "⚡ Operations", "💡 Examples"])
    
    with tab_re_intro:
        st.markdown("""
        <div class="learning-card">
        <h3>Formal Languages & RE</h3>
        <p><b>Regular Expressions</b> are a compact way to describe Regular Languages. They are the algebraic equivalent of Finite Automata.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with tab_re_ops:
        st.markdown("""
        <div class="learning-card">
        <ul>
            <li><b>Union (+ or |):</b> L ∪ M. Example: (0+1) means {0, 1}.</li>
            <li><b>Concatenation:</b> LM. Example: 01 means {01}.</li>
            <li><b>Kleene Star (*):</b> Zero or more repetitions. Example: 0* means {ε, 0, 00, 000, ...}.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "DFA to RE & Pumping Lemma":
    st.markdown("## 🔄 Conversions & Pumping Lemma")
    
    tab_conv, tab_pumping = st.tabs(["🔄 DFA to RE", "⚓ Pumping Lemma"])
    
    with tab_conv:
        st.markdown("""
        <div class="learning-card">
        <h3>Converting DFA to RE</h3>
        <p>We use the <b>State Elimination Method</b> to convert a DFA into its equivalent Regular Expression.</p>
        <p>Steps:</p>
        <ol>
            <li>Add a new start state with an ε-transition to the old start state.</li>
            <li>Add a new final state with ε-transitions from all old final states.</li>
            <li>Eliminate intermediate states one by one until only start and final remain.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    with tab_pumping:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Crucial Concept</div>
        <h3>The Pumping Lemma for Regular Languages</h3>
        <p>This lemma is used to prove that a language is <b>NOT</b> regular.</p>
        <p>If L is regular, there exists a constant <i>p</i> (pumping length) such that any string <i>s</i> in L with |s| ≥ p can be split into <i>s = xyz</i> satisfying:</p>
        <ol>
            <li>xyⁱz ∈ L for all i ≥ 0</li>
            <li>|y| > 0</li>
            <li>|xy| ≤ p</li>
        </ol>
        <div class="step-box">
            <b>Classic Example:</b> L = {0ⁿ1ⁿ | n ≥ 0} is NOT regular.
        </div>
        </div>
        """, unsafe_allow_html=True)
        elif display_page == "CFG & Chomsky Form":
    st.markdown("## 📜 Context-Free Grammars (CFG)")
    
    tab_cfg_def, tab_chomsky, tab_ambiguity = st.tabs(["📖 CFG Definition", "📐 Chomsky Normal Form", "🔍 Ambiguity"])
    
    with tab_cfg_def:
        st.markdown("""
        <div class="learning-card">
        <h3>What is a CFG?</h3>
        <p>A <b>Context-Free Grammar</b> is a formal grammar used to describe context-free languages. It consists of 4 components (V, Σ, R, S):</p>
        <ul>
            <li><b>V:</b> A finite set of variables (non-terminals).</li>
            <li><b>Σ:</b> A finite set of terminals.</li>
            <li><b>R:</b> A set of production rules (e.g., A → 0A1).</li>
            <li><b>S:</b> The start variable.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_chomsky:
        st.markdown("""
        <div class="learning-card">
        <h3>Chomsky Normal Form (CNF)</h3>
        <p>A grammar is in CNF if all its production rules are of the form:</p>
        <ul>
            <li><span class="highlight">A → BC</span> (Two variables)</li>
            <li><span class="highlight">A → a</span> (One terminal)</li>
        </ul>
        <p>This form is very useful for parsing algorithms like CYK.</p>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "PDA & CFL Theory":
    st.markdown("## 🏗️ Pushdown Automata (PDA)")
    
    tab_pda_intro, tab_pda_stack, tab_cfl = st.tabs(["📖 PDA Intro", "📚 Stack Mechanism", "📉 CFL Properties"])
    
    with tab_pda_intro:
        st.markdown("""
        <div class="learning-card">
        <h3>PDA = DFA + Stack</h3>
        <p>A <b>Pushdown Automaton</b> is essentially an NFA with an infinite memory in the form of a <b>Stack</b>.</p>
        <p>This allows it to recognize Context-Free Languages (CFLs) like {0ⁿ1ⁿ | n ≥ 0}, which a DFA cannot do.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_pda_stack:
        st.markdown("""
        <div class="learning-card">
        <h3>Stack Operations</h3>
        <ul>
            <li><b>Push:</b> Add a symbol to the top of the stack.</li>
            <li><b>Pop:</b> Remove the top symbol from the stack.</li>
            <li><b>No-op:</b> Leave the stack unchanged.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Turing Machines & Algorithms":
    st.markdown("## 📟 Turing Machines & Algorithms")
    
    tab_tm_def, tab_church, tab_decidability = st.tabs(["📖 TM Definition", "⛪ Church-Turing Thesis", "❓ Decidability"])
    
    with tab_tm_def:
        st.markdown("""
        <div class="learning-card">
        <h3>The Ultimate Machine: Turing Machine (TM)</h3>
        <p>A <b>Turing Machine</b> consists of an infinite tape and a read/write head. It is the most powerful model of computation.</p>
        <p><b>Capabilities:</b> It can move left, right, read, and write symbols.</p>
        <div class="step-box">
            <b>Fundamental Fact:</b> Anything that can be computed by any computer can be computed by a Turing Machine.
        </div>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "🎓 Course Completion":
    st.balloons()
    st.markdown("""
    <div style="text-align:center; padding: 100px;">
        <h1 style="font-size: 80px;">🎓</h1>
        <h2>CONGRATULATIONS!</h2>
        <p style="font-size: 24px;">You have successfully navigated through the Core of Computer Science.</p>
        <div class="learning-card">
            "The journey of computation never ends; it only becomes more efficient."
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- OPERATING SYSTEMS MODULES ---
elif display_page == "Introduction to OS":
    st.markdown("## ⚙️ Operating Systems: Introduction")
    st.markdown("""
    <div class="learning-card">
    <h3>What is an Operating System?</h3>
    <p>An <b>Operating System (OS)</b> is software that acts as an intermediary between a computer user and the computer hardware.</p>
    <div class="info-grid">
        <div class="info-item"><b>User View:</b> Convenience, ease of use, and good performance.</div>
        <div class="info-item"><b>System View:</b> Resource allocator and control program.</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "What Operating Systems Do":
    st.markdown("## 🛠️ What Operating Systems Do")
    st.markdown("""
    <div class="learning-card">
    <ul>
        <li><b>Hardware Management:</b> CPU, Memory, I/O devices.</li>
        <li><b>Application Interface:</b> Provides services to programs.</li>
        <li><b>Resource Allocation:</b> Decides how to share resources among users and tasks.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Operating System Types":
    st.markdown("## 💻 Operating System Types")
    st.markdown("""
    <div class="learning-card">
    <ol>
        <li><b>Mainframe Systems:</b> Massive processing power.</li>
        <li><b>Desktop Systems:</b> Focused on user experience.</li>
        <li><b>Multiprocessor Systems:</b> Parallel computing.</li>
        <li><b>Distributed Systems:</b> Multiple computers working together.</li>
        <li><b>Real-Time Systems:</b> Strict time constraints.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Computer-System Organization":
    st.info("Module under development: Focuses on Buses, Controllers, and I/O Structure.")

elif display_page == "Computer-System Architecture":
    st.info("Module under development: Focuses on Single-processor, Multiprocessor, and Clustered Systems.")

elif display_page == "Computer-System Operations":
    st.info("Module under development: Focuses on Interrupts, Storage Structure, and I/O Structure.")

elif display_page == "Resource Management":
    st.info("Module under development: Focuses on Process Management, Memory Management, and File-System Management.")

elif display_page == "Virtualization":
    st.info("Module under development: Focuses on VMs and their architecture.")

elif display_page == "Kernel Data Structures":
    st.info("Module under development: Lists, Stacks, Queues, and Trees in OS Kernels.")

elif display_page == "Free/Libre and Open-Source Operating Systems":
    st.info("Focuses on Linux, BSD, and Open Source Philosophy.")

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
    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("Name / الاسم:")
        msg = st.text_area("Feedback / التعليق:")
        submit = st.form_submit_button("Post / نشر")
        if submit:
            if name and msg:
                save_comment(name, msg)
                st.success("Comment saved! / تم حفظ التعليق بنجاح!")
            else:
                st.error("Please fill in both fields. / يرجى ملء جميع الحقول.")
    st.markdown("---")
    
    # Display comments
    comments_list = load_comments()
    for c in reversed(comments_list):
        st.markdown(f"""
        <div class="comment-box">
            <b>👤 {c['u']}</b> <span style='font-size:12px; color:gray;'>({c['t']})</span><br>
            {c['m']}
        </div>
        """, unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project designed for CS students.
        </p>
        <div style="margin-top: 15px;">
            <span style="margin: 0 10px;">Python</span> • 
            <span style="margin: 0 10px;">Streamlit</span> • 
            <span style="margin: 0 10px;">Theory of Computation</span> • 
            <span style="margin: 0 10px;">Operating Systems</span>
        </div>
    </div>
    """, unsafe_allow_html=True