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
        background-color: #f8fafc; padding: 25px; border-radius: 15px;
        border-left: 6px solid #1e3a8a; margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .quiz-section {
        background-color: #ffffff; padding: 20px; border: 1px solid #e2e8f0;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. HEADER ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: clamp(24px, 5vw, 48px); font-weight: bold; letter-spacing: 2px;">
            THE JEWEL OF COMPUTER SCIENCE
        </div>
        <div style="font-size: clamp(16px, 3vw, 24px); font-weight: 300; margin-top: 15px;
        border-top: 1px solid rgba(255,255,255,0.3); display: inline-block; padding-top: 10px;">
            MOHRAH ATIAH AL-JUHANI | مهره عطيه الجهني
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. SIDEBAR ---
subject = st.sidebar.selectbox(
    "Choose a Module:",
    ["Home Page", "PDA Learning Hub", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 6. MODULES ---
if subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")

elif subject == "PDA Learning Hub":
    st.markdown("## 📚 Pushdown Automata (PDA) - Comprehensive Study Guide")

elif subject == "Theory of Computation":

    st.markdown("### 🤖 Theory of Computation: PDA Simulator")
    st.info("💡 هذا المحاكي يتيح لك تتبع حركة الآلة (States) وتغير الـ Stack خطوة بخطوة.")

    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle')
        dot.node('q1', 'q1', shape='circle')
        dot.node('f', 'Accept', shape='doublecircle')
        dot.edge('S', 'q0')
        dot.edge('q0', 'q1')
        dot.edge('q1', 'f')
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

                history.append({
                    "Step": i+1,
                    "Input": char,
                    "State": current_state,
                    "Stack": str(stack[::-1]),
                    "Action": action
                })

                diagram_placeholder.graphviz_chart(generate_pda_diagram(current_state))
                table_placeholder.table(pd.DataFrame(history))

                if current_state == "q0":
                    if char == 'a':
                        stack.append('A')
                    elif char == 'b' and len(stack) > 1:
                        stack.pop()
                        current_state = "q1"
                    else:
                        failed = True
                        break

                elif current_state == "q1":
                    if char == 'b' and len(stack) > 1:
                        stack.pop()
                    else:
                        failed = True
                        break

                time.sleep(sim_speed)

            if not failed and current_state == "q1" and len(stack) == 1:
                diagram_placeholder.graphviz_chart(generate_pda_diagram('accepted'))
                st.success("✅ Result: String Accepted")
            else:
                st.error("❌ Result: String Rejected")

    # =========================
    # 📘 ADDED LESSON (ONLY INSERTION)
    # =========================

    st.markdown("## 📘 Lesson 1: Alphabets, Strings, and Languages")

    st.markdown("""
    <div class="learning-card">
        <h3>Definition</h3>
        Alphabet (Σ) is a finite set of symbols.<br>
        String is a finite sequence of symbols.<br>
        Language is a set of strings over an alphabet.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card">
        <h3>Key Concepts</h3>
        Σ = Alphabet<br>
        ε = Empty string<br>
        Σ* = All possible strings<br>
        Σ+ = Non-empty strings
    </div>
    """, unsafe_allow_html=True)

    dot1 = graphviz.Digraph()
    dot1.edge("Σ", "Strings")
    dot1.edge("Strings", "Language")
    st.graphviz_chart(dot1)

    st.markdown("### 🧠 Quiz")

    q1 = st.radio("What is Σ?", ["Alphabet", "Number", "Stack"], key="q1")
    if st.button("Check Answer"):
        if q1 == "Alphabet":
            st.success("Correct!")
        else:
            st.error("Wrong")

elif subject == "Contact Developer":
    st.markdown("### 📧 Contact")

elif subject == "Community Feedback":
    st.markdown("### 💬 Feedback")