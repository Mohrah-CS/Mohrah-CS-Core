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
    ["Home Page", "Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "PDA Explorer", "Contact Developer", "Community Feedback"]
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
        <h4>Why Study TOC?</h4>
        <ul>
            <li><b>Understanding Limits:</b> It helps us understand the fundamental limits of what computers can and cannot do.</li>
            <li><b>Foundation for AI:</b> Concepts from TOC, especially computability and complexity, are crucial for understanding the theoretical underpinnings of Artificial Intelligence.</li>
            <li><b>Algorithm Design:</b> Provides a theoretical framework for designing and analyzing efficient algorithms.</li>
            <li><b>Compiler Design:</b> Automata theory is directly applied in the design of compilers and parsers.</li>
        </ul>
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
            <li><b>Alphanumeric Characters:</b> Σ = {a-z, A-Z, 0-9}</li>
        </ul>
        <h4>Importance in TOC:</h4>
        <p>Alphabets are fundamental because they define the set of valid inputs for automata and the characters that can form strings in a formal language. Without a clearly defined alphabet, it's impossible to define what constitutes a valid 'word' or 'sentence' in a computational context.</p>
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
            <li><b>Prefix:</b> A substring that occurs at the beginning of a string. "ab" is a prefix of "ababa".</li>
            <li><b>Suffix:</b> A substring that occurs at the end of a string. "aba" is a suffix of "ababa".</li>
        </ul>
        <h4>Powers of an Alphabet (Σ<sup>k</sup>):</h4>
        <p>The notation Σ<sup>k</sup> represents the set of all strings of length <i>k</i> over the alphabet Σ.
        <ul>
            <li>Σ<sup>0</sup> = {ε} (The set containing only the empty string)</li>
            <li>Σ<sup>1</sup> = Σ (The set of all strings of length 1)</li>
            <li>Σ<sup>2</sup> = {xy | x, y ∈ Σ} (The set of all strings of length 2)</li>
        </ul>
        </p>
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
            <li><b>Concatenation of Languages (L₁L₂):</b> The set of all strings formed by concatenating a string from L₁ with a string from L₂. L₁L₂ = {xy | x ∈ L₁, y ∈ L₂}.</li>
            <li><b>Kleene Star of a Language (L*):</b> The set of all strings formed by concatenating zero or more strings from L.</li>
        </ul>
        <h4>Examples of Languages:</h4>
        <ul>
            <li>L = {0, 00, 000, ...} over Σ = {0} (Infinite language)</li>
            <li>L = {ε, 01, 10, 0011, 1100, ...} (Strings with equal number of 0s and 1s)</li>
            <li>L = {w | w starts with 'a'} over Σ = {a, b}</li>
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
            <li><b>Cardinality (|S|):</b> The number of elements in a set S.</li>
            <li><b>Subset (A ⊆ B):</b> Every element of A is also an element of B.</li>
            <li><b>Proper Subset (A ⊂ B):</b> A is a subset of B, but A is not equal to B.</li>
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
            <li><b>Partial Function:</b> A function that is not necessarily defined for all elements in its domain. NFAs can be thought of as having partial transition functions (or mapping to a set of states).</li>
            <li><b>One-to-One (Injective):</b> Each element in the codomain is mapped to by at most one element in the domain.</li>
            <li><b>Onto (Surjective):</b> Each element in the codomain is mapped to by at least one element in the domain.</li>
            <li><b>Bijection:</b> A function that is both one-to-one and onto.</li>
        </ul>
        <div class="step-box">
        <b>Relations:</b> A relation is a subset of the Cartesian product A × B. While every function is a relation, not every relation is a function (a relation can map one input to multiple outputs).
        </div>
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
        <h4>Logical Laws and Identities:</h4>
        <ul>
            <li><b>Commutative Laws:</b> A ∧ B = B ∧ A; A ∨ B = B ∨ A</li>
            <li><b>Associative Laws:</b> (A ∧ B) ∧ C = A ∧ (B ∧ C); (A ∨ B) ∨ C = A ∨ (B ∨ C)</li>
            <li><b>Distributive Laws:</b> A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C); A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)</li>
            <li><b>De Morgan's Laws:</b>
                <ul>
                    <li>¬(A ∨ B) = ¬A ∧ ¬B</li>
                    <li>¬(A ∧ B) = ¬A ∨ ¬B</li>
                </ul>
            </li>
        </ul>
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
        <h4>Key Characteristics of DFAs:</h4>
        <ul>
            <li><b>Deterministic:</b> For any state and input symbol, there is exactly one transition. No ambiguity.</li>
            <li><b>Total Function:</b> The transition function must be defined for every possible state and input symbol.</li>
            <li><b>Finite Memory:</b> The machine's memory is limited to its finite number of states.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_viz:
        st.markdown("### 🎨 Visual Examples of DFAs")
        st.markdown("""
        <div class="learning-card">
        <p>Visualizing DFAs using state transition diagrams makes it easier to understand how they process strings. Here are two common examples.</p>
        <h4>Example 1: DFA accepting strings with an even number of '0's</h4>
        <p>This DFA tracks whether it has seen an even or odd number of '0's. It stays in the same state when it sees a '1'.</p>
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
        <p>This DFA over Σ = {a, b} immediately goes to a 'Trap' state if the first symbol is 'b'. If it starts with 'a', it stays in an accept state.</p>
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
        <p>A <b>Non-Deterministic Finite Automata (NFA)</b> is a finite automaton where for each state and input symbol, there can be zero, one, or more than one next state. NFAs also allow transitions on the empty string (ε-transitions). Despite their non-deterministic nature, NFAs are equivalent in power to DFAs; any language recognized by an NFA can also be recognized by a DFA.</p>
        <h4>Formal Definition of an NFA:</h4>
        <p>An NFA is formally defined as a 5-tuple (Q, Σ, δ, q₀, F), where:</p>
        <ul>
            <li><b>Q:</b> A finite set of states.</li>
            <li><b>Σ:</b> A finite set of input symbols (the alphabet).</li>
            <li><b>δ:</b> The transition function, δ: Q × (Σ ∪ {ε}) → P(Q). It takes a state and an input symbol (or ε) as arguments and returns a set of possible next states. P(Q) denotes the power set of Q.</li>
            <li><b>q₀:</b> The start state (q₀ ∈ Q).</li>
            <li><b>F:</b> A set of accept (or final) states (F ⊆ Q).</li>
        </ul>
        <h4>How an NFA Works:</h4>
        <p>An NFA processes an input string by exploring all possible paths simultaneously. If at least one of these paths leads to an accept state after processing the entire input string, the string is accepted. The presence of ε-transitions allows the NFA to change states without consuming an input symbol.</p>
        <h4>Key Characteristics of NFAs:</h4>
        <ul>
            <li><b>Non-Deterministic:</b> For a given state and input symbol, there can be multiple next states.</li>
            <li><b>ε-transitions:</b> Allowed transitions on the empty string.</li>
            <li><b>Equivalent to DFAs:</b> Despite non-determinism, NFAs recognize the same class of languages as DFAs (regular languages).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_viz:
        st.markdown("### 🎨 Visual Examples of NFAs")
        st.markdown("""
        <div class="learning-card">
        <p>Here are some visual examples of NFAs and how they recognize different languages.</p>
        <h4>Example 1: NFA accepting strings containing '101'</h4>
        <p>This NFA accepts all binary strings that contain the substring '101'. Notice the simplicity compared to the DFA for the same language.</p>
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
        <p>In Theory of Computation, <b>Regular Operations</b> are used to build complex languages from simpler ones. These operations are fundamental to defining regular languages.</p>
        <div class="info-grid">
            <div class="info-item">
                <b>1. Union (L₁ ∪ L₂):</b>  

                The set of all strings that are in either L₁ or L₂.  

                <i>Example:</i> If L₁={a} and L₂={b}, then L₁ ∪ L₂ = {a, b}.
            </div>
            <div class="info-item">
                <b>2. Concatenation (L₁ ∘ L₂):</b>  

                The set of all strings formed by taking a string from L₁ and appending a string from L₂.  

                <i>Example:</i> If L₁={a} and L₂={b}, then L₁ ∘ L₂ = {ab}.
            </div>
            <div class="info-item">
                <b>3. Star (L*):</b>  

                The set of all strings formed by concatenating zero or more strings from L. This is also called the Kleene Star.  

                <i>Example:</i> If L={a}, then L* = {ε, a, aa, aaa, ...}.
            </div>
        </div>
        <h4>Visualizing Operations:</h4>
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Union (L1 ∪ L2)**")
            dot_u = graphviz.Digraph(); dot_u.attr(rankdir='LR', bgcolor='transparent')
            dot_u.node('S', 'Start', shape='circle'); dot_u.node('q1', 'L1', shape='circle'); dot_u.node('q2', 'L2', shape='circle')
            dot_u.edge('S', 'q1', label='ε'); dot_u.edge('S', 'q2', label='ε')
            st.graphviz_chart(dot_u)
        with col2:
            st.write("**Concatenation (L1 ∘ L2)**")
            dot_c = graphviz.Digraph(); dot_c.attr(rankdir='LR', bgcolor='transparent')
            dot_c.node('q1', 'L1', shape='circle'); dot_c.node('q2', 'L2', shape='circle')
            dot_c.edge('q1', 'q2', label='ε')
            st.graphviz_chart(dot_c)
        with col3:
            st.write("**Star (L*)**")
            dot_s = graphviz.Digraph(); dot_s.attr(rankdir='LR', bgcolor='transparent')
            dot_s.node('q', 'L', shape='circle')
            dot_s.edge('q', 'q', label='ε')
            st.graphviz_chart(dot_s)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_re:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.2</div>
        <h3>Regular Expressions (REs)</h3>
        <p>A <b>Regular Expression</b> is a concise way to describe a regular language using symbols and operators. It is a formal algebraic notation.</p>
        <h4>Formal Definition:</h4>
        <p>R is a regular expression if R is:</p>
        <ul>
            <li><b>a</b> for some <i>a</i> in the alphabet Σ.</li>
            <li><b>ε</b> (the empty string).</li>
            <li><b>∅</b> (the empty language).</li>
            <li><b>(R₁ ∪ R₂)</b> where R₁ and R₂ are REs.</li>
            <li><b>(R₁ ∘ R₂)</b> where R₁ and R₂ are REs.</li>
            <li><b>(R₁*)</b> where R₁ is an RE.</li>
        </ul>
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
        <p>A class of languages is <b>closed</b> under an operation if applying that operation to languages in the class always results in a language that is also in the same class.</p>
        <h4>Regular Languages are closed under:</h4>
        <div class="info-grid">
            <div class="info-item">✅ <b>Union:</b> If L₁ and L₂ are regular, L₁ ∪ L₂ is regular.</div>
            <div class="info-item">✅ <b>Concatenation:</b> If L₁ and L₂ are regular, L₁ ∘ L₂ is regular.</div>
            <div class="info-item">✅ <b>Star:</b> If L is regular, L* is regular.</div>
            <div class="info-item">✅ <b>Complement:</b> If L is regular, L' is regular.</div>
            <div class="info-item">✅ <b>Intersection:</b> If L₁ and L₂ are regular, L₁ ∩ L₂ is regular.</div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_conv:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.4</div>
        <h3>Conversion: RE to NFA (Thompson's Construction)</h3>
        <p>Every Regular Expression can be converted into an equivalent NFA. This is done by building small NFAs for basic parts and combining them.</p>
        <div class="step-box">
        <b>Steps for Conversion:</b>  

        1. <b>Base Cases:</b> Create NFAs for single symbols (a), ε, and ∅.  

        2. <b>Union (R₁ ∪ R₂):</b> Create a new start state with ε-transitions to the start states of R₁ and R₂.  

        3. <b>Concatenation (R₁ ∘ R₂):</b> Connect the final states of R₁ to the start state of R₂ with ε-transitions.  

        4. <b>Star (R*):</b> Add ε-transitions from final states back to the start state, and a new start/final state to handle ε.
        </div>
        """)
        st.markdown("#### Visualizing RE to NFA (Example: a ∪ b)")
        dot_conv = graphviz.Digraph(); dot_conv.attr(rankdir='LR', bgcolor='transparent')
        dot_conv.node('S', 'New Start', shape='circle'); dot_conv.node('q1', 'Start a', shape='circle'); dot_conv.node('q2', 'End a', shape='doublecircle')
        dot_conv.node('q3', 'Start b', shape='circle'); dot_conv.node('q4', 'End b', shape='doublecircle')
        dot_conv.edge('S', 'q1', label='ε'); dot_conv.edge('S', 'q3', label='ε'); dot_conv.edge('q1', 'q2', label='a'); dot_conv.edge('q3', 'q4', label='b')
        st.graphviz_chart(dot_conv)
        st.markdown("</div>", unsafe_allow_html=True)

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

elif subject == "PDA Explorer":
    st.markdown("## 📚 Pushdown Automata (PDA) Explorer")
    tab_info, tab_sim, tab_q = st.tabs(["📖 Deep Dive Definition", "🚀 Interactive Simulator (a^n b^n)", "📝 PDA Quiz (10 Qs)"])

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

    with tab_sim:
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