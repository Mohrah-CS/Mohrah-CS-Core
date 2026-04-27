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

# --- 3. ADVANCED STYLING (The Royal Theme) ---
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
    ["Home Page", "Foundations of TOC", "DFA Explorer", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
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
    st.info("💡 استكشف المفاهيم الرياضية الأساسية التي تبنى عليها نظرية الحوسبة.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔤 Alphabets & Strings", "📊 Set Theory", "⚙️ Functions", "🧠 Boolean Logic"])
    
    with tab1:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Lesson 1</div>
        <h3>Alphabets, Strings, and Languages</h3>
        <p>In TOC, we build everything from the ground up, starting with symbols.</p>
        <ul>
            <li><b>Alphabet (Σ):</b> A <span class="highlight">finite, non-empty set</span> of symbols. Example: Σ = {0, 1} for binary.</li>
            <li><b>String (w):</b> A finite sequence of symbols from an alphabet. Example: '0110' is a string over Σ = {0, 1}.</li>
            <li><b>Empty String (ε):</b> A string with <span class="highlight">zero length</span>. It is a member of Σ* but not Σ.</li>
            <li><b>Length |w|:</b> The number of symbol positions in the string. |0110| = 4.</li>
            <li><b>Powers of Alphabet:</b>
                <ul>
                    <li><b>Σ*:</b> The set of ALL possible strings over Σ, including ε (Kleene Closure).</li>
                    <li><b>Σ+:</b> The set of all non-empty strings (Σ+ = Σ* - {ε}).</li>
                </ul>
            </li>
            <li><b>Language (L):</b> A set of strings chosen from Σ*. If Σ = {0,1}, then L = {00, 01, 10, 11} is a language.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        dot1 = graphviz.Digraph()
        dot1.attr(bgcolor='transparent')
        dot1.node("Σ", "Alphabet\\n{a, b}", shape="ellipse", color="#1e3a8a")
        dot1.node("S", "Strings\\n{a, b, aa, ab...}", shape="box", color="#3b82f6")
        dot1.node("L", "Language\\n{aa, bb}", shape="doublecircle", color="#10b981")
        dot1.edge("Σ", "S", label="Combine")
        dot1.edge("S", "L", label="Subset")
        st.graphviz_chart(dot1)
        
        st.markdown("#### 📝 Quick Check")
        q_f1 = st.radio("If Σ = {a, b}, which of the following is NOT in Σ*?", ["ε", "ab", "c", "aaa"], key="q_f1")
        if st.button("Verify Answer", key="b_f1"):
            if q_f1 == "c": st.success("Correct! 'c' is not in the alphabet {a, b}.")
            else: st.error("Try again! Remember Σ* only contains symbols from Σ.")

    with tab2:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Lesson 2</div>
        <h3>Set Theory in Computation</h3>
        <p>Sets are the collection of distinct objects, used to define languages and states.</p>
        <ul>
            <li><b>Union (A ∪ B):</b> Elements in A, or B, or both.</li>
            <li><b>Intersection (A ∩ B):</b> Elements <span class="highlight">common</span> to both A and B.</li>
            <li><b>Complement (Ā):</b> Elements in the Universal set NOT in A.</li>
            <li><b>Power Set P(S):</b> The set of all subsets of S. If |S| = n, then |P(S)| = 2ⁿ.</li>
            <li><b>Cartesian Product (A × B):</b> Set of all ordered pairs (a, b).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        dot2 = graphviz.Digraph()
        dot2.attr(bgcolor='transparent')
        dot2.node("A", "Set A", color="#1e3a8a")
        dot2.node("B", "Set B", color="#1e3a8a")
        dot2.node("U", "Union", shape="hexagon", style="filled", fillcolor="#dbeafe")
        dot2.node("I", "Intersection", shape="hexagon", style="filled", fillcolor="#bfdbfe")
        dot2.edge("A", "U"); dot2.edge("B", "U")
        dot2.edge("A", "I"); dot2.edge("B", "I")
        st.graphviz_chart(dot2)
        
        st.markdown("#### 📝 Quick Check")
        q_f2 = st.radio("If A = {1, 2} and B = {2, 3}, what is A ∩ B?", ["{1, 2, 3}", "{2}", "{1, 3}"], key="q_f2")
        if st.button("Verify Answer", key="b_f2"):
            if q_f2 == "{2}": st.success("Correct! 2 is the only common element.")
            else: st.error("Incorrect. Intersection looks for common elements.")

    with tab3:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Lesson 3</div>
        <h3>Functions and Relations</h3>
        <p>Functions map inputs to outputs, essential for defining transition functions (δ).</p>
        <ul>
            <li><b>Domain:</b> The set of all possible inputs.</li>
            <li><b>Codomain:</b> The set of potential outputs.</li>
            <li><b>Range:</b> The actual set of outputs produced.</li>
            <li><b>Onto (Surjective):</b> Every element in codomain is mapped.</li>
            <li><b>One-to-One (Injective):</b> Each input has a unique output.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        dot3 = graphviz.Digraph()
        dot3.attr(rankdir='LR', bgcolor='transparent')
        dot3.node("In", "Input (Domain)", shape="circle")
        dot3.node("F", "Function (f)", shape="box", style="filled", fillcolor="#1e3a8a", fontcolor="white")
        dot3.node("Out", "Output (Range)", shape="circle")
        dot3.edge("In", "F"); dot3.edge("F", "Out")
        st.graphviz_chart(dot3)
        
        st.markdown("#### 📝 Quick Check")
        q_f3 = st.radio("In a transition function δ: Q × Σ → Q, what is the domain?", ["Q", "Σ", "Q × Σ"], key="q_f3")
        if st.button("Verify Answer", key="b_f3"):
            if q_f3 == "Q × Σ": st.success("Correct! It takes a state and a symbol as input.")
            else: st.error("Incorrect. Look at the part before the arrow.")

    with tab4:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Lesson 4</div>
        <h3>Boolean Logic</h3>
        <p>The logic of True (1) and False (0) that governs all digital computation.</p>
        <ul>
            <li><b>AND (∧):</b> True only if BOTH are true.</li>
            <li><b>OR (∨):</b> True if AT LEAST one is true.</li>
            <li><b>NOT (¬):</b> Inverts the value.</li>
            <li><b>XOR (⊕):</b> True if EXACTLY one is true.</li>
            <li><b>De Morgan's Law:</b> ¬(A ∨ B) = ¬A ∧ ¬B.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📝 Quick Check")
        q_f4 = st.radio("What is (True AND False) OR True?", ["True", "False"], key="q_f4")
        if st.button("Verify Answer", key="b_f4"):
            if q_f4 == "True": st.success("Correct! (F) OR T = True.")
            else: st.error("Incorrect. Remember the order of operations.")

elif subject == "DFA Explorer":
    st.markdown("## ⚙️ Deterministic Finite Automata (DFA)")
    st.info("💡 الـ DFA هو أبسط نموذج للحوسبة، حيث ينتقل بين حالات محددة بناءً على المدخلات.")
    
    tab_info, tab_viz, tab_sim, tab_quiz = st.tabs(["📖 DFA Definition", "🎨 Visual Examples", "🚀 DFA Simulator", "🧠 DFA Quiz"])
    
    with tab_info:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Formal Definition</div>
        <h3>What is a DFA?</h3>
        <p>A <b>Deterministic Finite Automata (DFA)</b> is a theoretical model of a machine that has a finite number of states and transitions between them based on input symbols.</p>
        <p>It is formally defined as a <b>5-tuple (Q, Σ, δ, q0, F)</b>:</p>
        <ul>
            <li><b>Q:</b> A finite set of <span class="highlight">States</span>.</li>
            <li><b>Σ:</b> A finite set of <span class="highlight">Input Symbols</span> (Alphabet).</li>
            <li><b>δ:</b> The <span class="highlight">Transition Function</span> (δ: Q × Σ → Q).</li>
            <li><b>q0:</b> The <span class="highlight">Start State</span> (q0 ∈ Q).</li>
            <li><b>F:</b> The set of <span class="highlight">Accepting (Final) States</span> (F ⊆ Q).</li>
        </ul>
        <p><b>Why "Deterministic"?</b> Because for every state and every input symbol, there is <b>exactly one</b> transition to a next state.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_viz:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 1. Even Number of '0's")
            st.write("This DFA accepts binary strings with an even count of zeros.")
            dfa1 = graphviz.Digraph()
            dfa1.attr(rankdir='LR', bgcolor='transparent')
            dfa1.node('S', '', shape='none')
            dfa1.node('q_even', 'Even (q0)', shape='doublecircle', color='green')
            dfa1.node('q_odd', 'Odd (q1)', shape='circle')
            dfa1.edge('S', 'q_even')
            dfa1.edge('q_even', 'q_odd', label='0')
            dfa1.edge('q_odd', 'q_even', label='0')
            dfa1.edge('q_even', 'q_even', label='1')
            dfa1.edge('q_odd', 'q_odd', label='1')
            st.graphviz_chart(dfa1)
            
        with col2:
            st.markdown("#### 2. Starts with 'a'")
            st.write("This DFA accepts strings that begin with the letter 'a'.")
            dfa2 = graphviz.Digraph()
            dfa2.attr(rankdir='LR', bgcolor='transparent')
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

    with tab_sim:
        st.markdown("### 🚀 DFA Interactive Simulator")
        st.write("Test a DFA that accepts strings containing the pattern **'101'**.")
        
        def generate_dfa_sim_diagram(active_state):
            dot = graphviz.Digraph()
            dot.attr(rankdir='LR', size='8,5', bgcolor='transparent')
            dot.node('S', '', shape='none')
            
            # Define states with highlighting
            states = {
                'q0': {'label': 'Start', 'shape': 'circle'},
                'q1': {'label': 'Got 1', 'shape': 'circle'},
                'q2': {'label': 'Got 10', 'shape': 'circle'},
                'q3': {'label': 'Got 101 (Accept)', 'shape': 'doublecircle'}
            }
            
            for node, attr in states.items():
                color = '#3b82f6' if active_state == node else 'black'
                penwidth = '4' if active_state == node else '1'
                dot.node(node, attr['label'], shape=attr['shape'], color=color, penwidth=penwidth)
            
            dot.edge('S', 'q0')
            dot.edge('q0', 'q0', label='0')
            dot.edge('q0', 'q1', label='1')
            dot.edge('q1', 'q1', label='1')
            dot.edge('q1', 'q2', label='0')
            dot.edge('q2', 'q0', label='0')
            dot.edge('q2', 'q3', label='1')
            dot.edge('q3', 'q3', label='0, 1')
            return dot

        col_sim_graph, col_sim_input = st.columns([2, 1])
        
        with col_sim_graph:
            dfa_placeholder = st.empty()
            dfa_placeholder.graphviz_chart(generate_dfa_sim_diagram('q0'))
            
        with col_sim_input:
            dfa_input_str = st.text_input("Enter Binary String (0s and 1s):", "11010")
            dfa_speed = st.slider("Simulation Speed:", 0.5, 3.0, 1.5, key="dfa_speed")
            run_dfa = st.button("Start DFA Simulation ⚡")
            
        if run_dfa:
            current_state = 'q0'
            dfa_history = []
            dfa_table_placeholder = st.empty()
            
            # DFA Transition Logic for '101'
            transitions = {
                'q0': {'0': 'q0', '1': 'q1'},
                'q1': {'0': 'q2', '1': 'q1'},
                'q2': {'0': 'q0', '1': 'q3'},
                'q3': {'0': 'q3', '1': 'q3'}
            }
            
            valid_input = True
            for i, char in enumerate(dfa_input_str):
                if char not in ['0', '1']:
                    st.error(f"Invalid character '{char}'! Please use only 0 and 1.")
                    valid_input = False
                    break
                
                prev_state = current_state
                current_state = transitions[prev_state][char]
                
                dfa_history.append({
                    "Step": i + 1,
                    "Input": char,
                    "From": prev_state,
                    "To": current_state
                })
                
                dfa_placeholder.graphviz_chart(generate_dfa_sim_diagram(current_state))
                dfa_table_placeholder.table(pd.DataFrame(dfa_history))
                time.sleep(dfa_speed)
            
            if valid_input:
                if current_state == 'q3':
                    st.success("✅ String Accepted! It contains '101'.")
                else:
                    st.error("❌ String Rejected! It does not contain '101'.")

    with tab_quiz:
        st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
        dq1 = st.radio("1. How many transitions must exist for EACH state in a DFA with alphabet Σ={0,1}?", ["One", "Two", "Unlimited"])
        if st.button("Check DFA Q1"):
            if dq1 == "Two": st.success("Correct! One for '0' and one for '1'.")
            else: st.error("Incorrect. In DFA, every symbol must have exactly one transition.")
        
        st.write("---")
        dq2 = st.radio("2. What happens if a DFA ends in a non-final state?", ["String is Accepted", "String is Rejected", "Machine Crashes"])
        if st.button("Check DFA Q2"):
            if dq2 == "String is Rejected": st.success("Correct!")
            else: st.error("Incorrect. Only final states lead to acceptance.")
        st.markdown('</div>', unsafe_allow_html=True)

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 Pushdown Automata (PDA) - Comprehensive Study Guide")
    tab1, tab2 = st.tabs(["📖 Comprehensive Summary", "🧠 Interactive Quiz"])
    with tab1:
        st.markdown("""
        <div class="learning-card">
        <h3>1. Introduction to PDA</h3>
        <p>A <b>Pushdown Automata (PDA)</b> is a way to implement a <b>Context-Free Grammar</b>. It is essentially a Finite Automata with an extra component: a <b>Stack</b>.</p>
        <h3>2. The Formal Definition (7-Tuple)</h3>
        <p>A PDA is formally defined as (Q, Σ, Γ, δ, q0, Z0, F):</p>
        <ul>
            <li><b>Q:</b> Finite set of States.</li>
            <li><b>Σ:</b> Input Alphabet.</li>
            <li><b>Γ:</b> Stack Alphabet.</li>
            <li><b>δ:</b> Transition Function.</li>
            <li><b>q0:</b> Start State.</li>
            <li><b>Z0:</b> Initial Stack Symbol.</li>
            <li><b>F:</b> Set of Accepting States.</li>
        </ul>
        <h3>3. Core Operations (Stack Logic)</h3>
        <p>PDA follows the <b>LIFO (Last In, First Out)</b> principle:</p>
        <ul>
            <li><b>Push:</b> Adds a symbol to the top of the stack.</li>
            <li><b>Pop:</b> Removes the top symbol from the stack.</li>
        </ul>
        <h3>4. Acceptance Criteria</h3>
        <p>A PDA can accept by <b>Final State</b> or by <b>Empty Stack</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("### Test Your Knowledge")
        with st.container():
            st.markdown('<div class="quiz-section">', unsafe_allow_html=True)
            q1 = st.radio("1. Which type of language does a PDA recognize?", ["Regular Languages", "Context-Free Languages", "Context-Sensitive Languages"])
            if st.button("Check Q1"):
                if q1 == "Context-Free Languages": st.success("Correct!")
                else: st.error("Incorrect.")
            st.write("---")
            q2 = st.radio("2. What is the memory structure used in PDA?", ["Queue", "Linked List", "Stack"])
            if st.button("Check Q2"):
                if q2 == "Stack": st.success("Correct!")
                else: st.error("Incorrect.")
            st.write("---")
            q3 = st.radio("3. What does 'ε' represent in a transition?", ["Empty String", "Final State", "Stack Overflow"])
            if st.button("Check Q3"):
                if q3 == "Empty String": st.success("Correct!")
                else: st.error("Incorrect.")
            st.write("---")
            q4 = st.radio("4. How many elements are in the PDA formal definition?", ["5", "6", "7"])
            if st.button("Check Q4"):
                if q4 == "7": st.success("Correct!")
                else: st.error("Incorrect.")
            st.write("---")
            q5 = st.radio("5. Acceptance by 'Empty Stack' means:", ["Only Z0 remains", "The stack is completely empty", "The input is finished"])
            if st.button("Check Q5"):
                if q5 == "The stack is completely empty": st.success("Correct!")
                else: st.error("Incorrect.")
            st.write("---")
            q6 = st.radio("6. Can a PDA be Non-Deterministic (NPDA)?", ["Yes, and it's more powerful", "No", "Yes, but same power as DPDA"])
            if st.button("Check Q6"):
                if q6 == "Yes, and it's more powerful": st.success("Correct!")
                else: st.error("Incorrect.")
            st.markdown('</div>', unsafe_allow_html=True)

elif subject == "Theory of Computation":
    st.markdown("### 🤖 Theory of Computation: PDA Simulator")
    st.info("💡 هذا المحاكي يتيح لك تتبع حركة الآلة (States) وتغير الـ Stack خطوة بخطوة.")
    
    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
        dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
        dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')
        dot.edge('S', 'q0'); dot.edge('q0', 'q0', label='a, Z0 / AZ0\\na, A / AA'); dot.edge('q0', 'q1', label='b, A / ε'); dot.edge('q1', 'q1', label='b, A / ε'); dot.edge('q1', 'f', label='ε, Z0 / Z0')
        return dot

    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        diagram_placeholder = st.empty()
        diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))
    with col_input:
        test_string = st.text_input("Enter Input String (e.g., aabb):", "aabb")
        sim_speed = st.slider("Speed:", 0.5, 2.0, 1.0)
        if st.button("Run Simulation 🚀"):
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
        name = st.text_input("Name:")
        msg = st.text_area("Feedback:")
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
              
 Reuse or redistribution without permission is not allowed.
        </p>
    </div>
    """, unsafe_allow_html=True)