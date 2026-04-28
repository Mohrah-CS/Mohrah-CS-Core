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
    tab_intro, tab_alphabets, tab_strings, tab_languages, tab_sets, tab_functions, tab_boolean, tab_q = st.tabs(["📖 Introduction", "🔤 Alphabets", "🧵 Strings", "🗣️ Languages", "📊 Sets", "⚙️ Functions", "🧠 Boolean Logic", "📝 Comprehensive Quiz"])
    
    with tab_intro:
        st.markdown("""
        ### 📖 Introduction to Theory of Computation

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
        ### 📖 Alphabets: The Foundation of Formal Languages

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
        ### 📖 Strings: Sequences of Symbols

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
        <p>The notation Σ<sup>k</sup> represents the set of all strings of length <i>k</i> that can be formed using symbols from the alphabet Σ.</p>
        <ul>
            <li><b>Σ<sup>0</sup>:</b> The set containing only the empty string, {ε}.</li>
            <li><b>Σ<sup>1</sup>:</b> The set of all strings of length 1, which is equivalent to the alphabet Σ itself.</li>
            <li><b>Σ<sup>k</sup>:</b> The set of all strings of length <i>k</i>.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_languages:
        st.markdown("""
        ### 📖 Languages: Collections of Strings

        <div class="learning-card">
        <div class="concept-badge">Module 1.3</div>
        <h3>What is a Language (L)?</h3>
        <p>In Theory of Computation, a <b>Language (L)</b> is defined as a set of strings over a given alphabet (Σ). Since an alphabet can generate an infinite number of strings (Σ*), a language is essentially a subset of Σ*. Languages can be finite or infinite.</p>

        <h4>Key Concepts Related to Languages:</h4>
        <ul>
            <li><b>Formal Language:</b> A language defined by precise mathematical or logical rules, often used in computer science for programming languages, data formats, and communication protocols.</li>
            <li><b>Natural Language:</b> Human languages like English or Arabic, which are often ambiguous and not strictly defined by formal rules. TOC primarily deals with formal languages.</li>
            <li><b>Finite Language:</b> A language that contains a finite number of strings. For example, L = {"cat", "dog", "bird"} over Σ = {a-z}.</li>
            <li><b>Infinite Language:</b> A language that contains an infinite number of strings. For example, L = {all binary strings starting with '0'} over Σ = {0, 1}.</li>
        </ul>

        <h4>Operations on Languages:</h4>
        <p>Just like sets, languages can undergo various operations:</p>
        <ul>
            <li><b>Union (L<sub>1</sub> ∪ L<sub>2</sub>):</b> The set of all strings that are in L<sub>1</sub> or in L<sub>2</sub> (or both).</li>
            <li><b>Intersection (L<sub>1</sub> ∩ L<sub>2</sub>):</b> The set of all strings that are in both L<sub>1</sub> and L<sub>2</sub>.</li>
            <li><b>Concatenation (L<sub>1</sub>L<sub>2</sub>):</b> The set of all strings formed by concatenating a string from L<sub>1</sub> with a string from L<sub>2</sub>. For example, if L<sub>1</sub> = {"a"} and L<sub>2</sub> = {"b"}, then L<sub>1</sub>L<sub>2</sub> = {"ab"}.</li>
            <li><b>Kleene Star (L*):</b> The set of all possible strings formed by concatenating zero or more strings from L. This includes the empty string (ε).</li>
            <li><b>Positive Closure (L<sup>+</sup>):</b> Similar to Kleene Star, but excludes the empty string. It's the set of all possible strings formed by concatenating one or more strings from L.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sets:
        st.markdown("""
        ### 📖 Sets: The Fundamental Mathematical Concept

        <div class="learning-card">
        <div class="concept-badge">Module 1.4</div>
        <h3>What is a Set?</h3>
        <p>In mathematics and computer science, a <b>Set</b> is a well-defined collection of distinct objects, considered as an object in its own right. These objects are called the elements or members of the set. Sets are fundamental to Theory of Computation as they are used to define alphabets, states, languages, and many other abstract concepts.</p>

        <h4>Key Properties of Sets:</h4>
        <ul>
            <li><b>Well-defined:</b> It must be clear whether an object is a member of the set or not.</li>
            <li><b>Distinct Elements:</b> Each element in a set must be unique; duplicates are not allowed.</li>
            <li><b>Order Does Not Matter:</b> The order in which elements are listed does not change the set (e.g., {1, 2, 3} is the same as {3, 1, 2}).</li>
        </ul>

        <h4>Common Set Notations:</h4>
        <ul>
            <li><b>Roster Method:</b> Listing all elements, e.g., A = {1, 2, 3, 4}.</li>
            <li><b>Set-Builder Notation:</b> Describing the properties of the elements, e.g., B = {x | x is an even integer and 0 < x < 10}.</li>
            <li><b>Empty Set (∅ or {}):</b> A set containing no elements.</li>
            <li><b>Universal Set (U):</b> The set of all possible elements under consideration.</li>
        </ul>

        <h4>Basic Set Operations:</h4>
        <ul>
            <li><b>Union (A ∪ B):</b> The set of all elements that are in A, or in B, or in both.</li>
            <li><b>Intersection (A ∩ B):</b> The set of all elements that are common to both A and B.</li>
            <li><b>Difference (A - B):</b> The set of all elements that are in A but not in B.</li>
            <li><b>Complement (A<sup>c</sup> or Ā):</b> The set of all elements in the universal set U that are not in A.</li>
            <li><b>Subset (A ⊆ B):</b> Every element of A is also an element of B.</li>
            <li><b>Proper Subset (A ⊂ B):</b> A is a subset of B, and A is not equal to B.</li>
        </ul>

        <h4>Advanced Set Concepts:</h4>
        <ul>
            <li><b>Power Set P(S):</b> The set of all possible subsets of a set S, including the empty set and S itself. If a set S has <i>n</i> elements, its power set P(S) will have 2<sup>n</sup> elements. This concept is crucial for understanding NFA to DFA conversion.</li>
            <li><b>Cartesian Product (A × B):</b> The set of all possible ordered pairs (a, b) where 'a' is an element of A and 'b' is an element of B. This is used to define transition functions.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_functions:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.5</div>
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

    with tab_boolean:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.6</div>
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
            # Introduction Quiz
            ("Which branch of TOC studies abstract machines and their computational problems?", ["Computability Theory", "Complexity Theory", "Automata Theory", "Algorithm Theory"], "Automata Theory"),
            ("What is the primary focus of Computability Theory?", ["The efficiency of algorithms", "Whether problems can be solved algorithmically", "The design of programming languages", "The physical construction of computers"], "Whether problems can be solved algorithmically"),
            ("Which machine is a central concept in Computability Theory and serves as a universal model of computation?", ["Finite Automata", "Pushdown Automata", "Turing Machine", "Von Neumann Machine"], "Turing Machine"),
            ("Complexity Theory classifies problems based on what?", ["Their historical significance", "The programming language used to solve them", "The resources (time and space) required to solve them", "The number of developers working on them"], "The resources (time and space) required to solve them"),
            ("Understanding the fundamental limits of what computers can and cannot do is a benefit of studying which field?", ["Data Structures", "Operating Systems", "Theory of Computation", "Computer Architecture"], "Theory of Computation"),
            # Alphabets Quiz
            ("What is the definition of an Alphabet (Σ) in Theory of Computation?", ["An infinite set of symbols", "A finite, non-empty set of symbols", "A set of all possible strings", "A set of numbers only"], "A finite, non-empty set of symbols"),
            ("Which of the following is NOT a characteristic of an alphabet?", ["It must be finite", "It must be non-empty", "Its symbols must be letters only", "Its symbols must be distinct"], "Its symbols must be letters only"),
            ("What is the binary alphabet?", ["Σ = {a, b}", "Σ = {0, 1}", "Σ = {True, False}", "Σ = {+, -}"], "Σ = {0, 1}"),
            ("If an alphabet Σ = {x, y, z}, how many symbols does it contain?", ["0", "1", "3", "Infinite"], "3"),
            ("Why are alphabets important in Theory of Computation?", ["They define the speed of computation", "They define the set of valid inputs for automata", "They determine the hardware requirements", "They are used for encryption only"], "They define the set of valid inputs for automata"),
            # Strings Quiz
            ("What is the length of the empty string (ε)?", ["1", "0", "Undefined", "Depends on the alphabet"], "0"),
            ("If Σ = {0, 1}, which of the following is NOT a string over Σ?", ["0101", "111", "021", "ε"], "021"),
            ("Given strings <i>x</i> = \"apple\" and <i>y</i> = \"pie\", what is the result of <i>xy</i> concatenation?", ["pieapple", "applepie", "apple pie", "aplepi"], "applepie"),
            ("What is the reverse of the string <i>w</i> = \"racecar\"?", ["racecar", "raccar", "ecarcar", "caracer"], "racecar"),
            ("The set Σ<sup>0</sup> contains which of the following?", ["All strings of length 0", "All strings of length 1", "The alphabet itself", "An infinite number of strings"], "All strings of length 0"),
            # Languages Quiz
            ("In Theory of Computation, what is a Language (L) defined as?", ["An infinite set of symbols", "A set of strings over a given alphabet", "A collection of all possible alphabets", "A set of numbers and operations"], "A set of strings over a given alphabet"),
            ("Which of the following is an example of an infinite language over Σ = {a, b}?", ["L = {\"a\", \"b\", \"ab\"}", "L = {all strings with an even number of 'a's}", "L = {\"aa\", \"bb\"}", "L = {ε}"], "L = {all strings with an even number of 'a's}"),
            ("If L<sub>1</sub> = {\"0\"} and L<sub>2</sub> = {\"1\"}, what is L<sub>1</sub>L<sub>2</sub> (concatenation)?", ["{\"0\", \"1\"}", "{\"01\"}", "{\"10\"}", "{\"0\", \"1\", \"01\"}"], "{\"01\"}"),
            ("What does the Kleene Star operation (L*) on a language L include that Positive Closure (L<sup>+</sup>) does not?", ["All strings of length one", "All strings of infinite length", "The empty string (ε)", "All possible symbols"], "The empty string (ε)"),
            ("Which type of language is primarily studied in Theory of Computation?", ["Natural Language", "Programming Language", "Formal Language", "Spoken Language"], "Formal Language"),
            # Sets Quiz
            ("Which of the following best describes a set?", ["An unordered collection of non-distinct objects", "A well-defined collection of distinct objects", "A list of elements in a specific order", "A collection that can contain duplicate elements"], "A well-defined collection of distinct objects"),
            ("If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∪ B?", ["{3}", "{1, 2, 3, 4, 5}", "{1, 2, 4, 5}", "{1, 2}"], "{1, 2, 3, 4, 5}"),
            ("What is the intersection of A = {a, b, c} and B = {b, d, e}?", ["{a, b, c, d, e}", "{a, c, d, e}", "{b}", "{}"], "{b}"),
            ("If a set S has 3 elements, how many elements does its Power Set P(S) have?", ["3", "6", "8", "9"], "8"),
            ("The Cartesian Product A × B results in a set of what?", ["Single elements", "Ordered pairs", "Disjoint sets", "Subsets"], "Ordered pairs"),
            # Original Foundations Quiz Questions (re-indexed)
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