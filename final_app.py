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
    .quiz-section {
        background-color: #ffffff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 15px;
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
    ["Home Page", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 6. MODULES ---
if subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    هذه المنصة هي **مبادرة طلابية تعليمية** تهدف إلى تحويل المفاهيم النظرية في علوم الحاسب إلى نماذج تفاعلية ملموسة.
    **المصدر العلمي (Academic Source):**
    جميع الدروس والأمثلة البرمجية المقدمة في هذه المنصة مستمدة من المناهج الأكاديمية المعتمدة في **جامعة تبوك**، ويتم تقديمها هنا لغرض الشرح والتوضيح وتسهيل الفهم.
    """)

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
        st.markdown("## 📘 Additional Lessons")
      st.markdown("## 📘 Theory of Computation - Additional Lessons")

# =========================
# LESSON 1: Alphabets, Strings, Languages
# =========================
st.markdown("""
<div class="learning-card">
<h3>Alphabets, Strings, and Languages</h3>
<p>An alphabet (Σ) is a finite set of symbols. Strings are sequences. Languages are sets of strings.</p>

<ul>
<li>Σ = symbols set</li>
<li>String = sequence</li>
<li>ε = empty string</li>
<li>Σ* = all possible strings</li>
<li>Σ+ = non-empty strings</li>
<li>Concatenation</li>
<li>Substring</li>
<li>Lexicographic order</li>
</ul>
</div>
""", unsafe_allow_html=True)

dot1 = graphviz.Digraph()
dot1.node("Σ")
dot1.node("Strings")
dot1.node("Language")
dot1.edge("Σ", "Strings")
dot1.edge("Strings", "Language")
st.graphviz_chart(dot1)

q1 = st.radio("What does Σ represent?", ["Alphabet (symbols)", "Numbers", "Operations"], key="q1")
if st.button("Check L1"):
    st.success("Correct!" if q1 == "Alphabet (symbols)" else "Incorrect")


# =========================
# LESSON 2: Sets
# =========================
st.markdown("""
<div class="learning-card">
<h3>Sets</h3>
<ul>
<li>Union (A ∪ B)</li>
<li>Intersection (A ∩ B)</li>
<li>Difference</li>
<li>Complement</li>
<li>Power Set</li>
<li>Cartesian Product</li>
<li>Cardinality</li>
</ul>
</div>
""", unsafe_allow_html=True)

dot2 = graphviz.Digraph()
dot2.node("A")
dot2.node("B")
dot2.node("A ∪ B")
dot2.node("A ∩ B")
dot2.edge("A", "A ∪ B")
dot2.edge("B", "A ∪ B")
dot2.edge("A", "A ∩ B")
dot2.edge("B", "A ∩ B")
st.graphviz_chart(dot2)

q2 = st.radio("Intersection means:", ["Common elements", "All elements", "None"], key="q2")
if st.button("Check L2"):
    st.success("Correct!" if q2 == "Common elements" else "Incorrect")


# =========================
# LESSON 3: Functions
# =========================
st.markdown("""
<div class="learning-card">
<h3>Functions and Operations</h3>
<ul>
<li>Domain</li>
<li>Codomain</li>
<li>Range</li>
<li>Sequences</li>
<li>Tuples</li>
<li>Closed operations</li>
</ul>
</div>
""", unsafe_allow_html=True)

dot3 = graphviz.Digraph()
dot3.node("A")
dot3.node("B")
dot3.node("f(x)")
dot3.edge("A", "f(x)")
dot3.edge("f(x)", "B")
st.graphviz_chart(dot3)

q3 = st.radio("Function maps:", ["Set to set", "Numbers only", "Random"], key="q3")
if st.button("Check L3"):
    st.success("Correct!" if q3 == "Set to set" else "Incorrect")


# =========================
# LESSON 4: Boolean Logic
# =========================
st.markdown("""
<div class="learning-card">
<h3>Boolean Logic</h3>
<ul>
<li>AND</li>
<li>OR</li>
<li>NOT</li>
<li>De Morgan's Laws</li>
<li>Commutative / Associative Laws</li>
</ul>
</div>
""", unsafe_allow_html=True)

dot4 = graphviz.Digraph()
dot4.node("True")
dot4.node("False")
dot4.edge("True", "False", label="NOT")
st.graphviz_chart(dot4)

q4 = st.radio("AND means:", ["Both true", "One true", "None"], key="q4")
if st.button("Check L4"):
    st.success("Correct!" if q4 == "Both true" else "Incorrect")  
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
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small><br>{c['m']}</div>""", unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
            © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
            <br> Reuse or redistribution without permission is not allowed.
        </p>
    </div>
    """, unsafe_allow_html=True)