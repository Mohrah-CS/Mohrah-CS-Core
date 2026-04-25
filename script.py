import streamlit as st
import time
import graphviz

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED STYLING ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-box {
        text-align: center;
        padding: 40px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        padding: 30px;
        margin-top: 60px;
        border-top: 3px solid #1e3a8a;
        background-color: #f1f5f9;
        color: #1e3a8a;
        border-radius: 15px;
    }
    .legal-warning { color: #b91c1c; font-weight: bold; font-size: 16px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC STATE DIAGRAM GENERATOR ---
def generate_pda_diagram(active_state):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', fontname='Arial', fontsize='12')
    
    dot.node('S', '', shape='none')
    dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
    dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
    dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')

    dot.edge('S', 'q0')
    dot.edge('q0', 'q0', label='a, Z0 / AZ0\na, A / AA')
    dot.edge('q0', 'q1', label='b, A / ε')
    dot.edge('q1', 'q1', label='b, A / ε')
    dot.edge('q1', 'f', label='ε, Z0 / Z0')
    
    return dot

# --- 4. HEADER SECTION (With Correct Name) ---
st.markdown(f"""
    <div class="header-box">
        <div style="font-family: 'Georgia', serif; font-size: clamp(24px, 5vw, 48px); font-weight: bold; letter-spacing: 2px;">THE JEWEL OF COMPUTER SCIENCE</div>
        <div style="font-size: clamp(16px, 3vw, 24px); font-weight: 300; margin-top: 15px; border-top: 1px solid rgba(255,255,255,0.3); display: inline-block; padding-top: 10px;">مهره عطيه الجهني</div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR NAVIGATION ---
st.sidebar.title("💎 Navigation Menu")
subject = st.sidebar.selectbox(
    "Choose a Subject:",
    ["Home Page", "Theory of Computation", "Community Feedback"]
)

# --- 6. SUBJECT: THEORY OF COMPUTATION ---
if subject == "Theory of Computation":
    st.markdown("### 🤖 Pushdown Automata (PDA) Laboratory")
    st.info("Language: L = {aⁿbⁿ | n ≥ 1}")
    
    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        st.markdown("#### 📊 Dynamic State Diagram")
        diagram_placeholder = st.empty()
        diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))

    with col_input:
        st.markdown("#### ⚙️ Execution Control")
        test_string = st.text_input("Enter Input String (e.g., aabb):", "aabb")
        run_btn = st.button("Run Simulation")

    if run_btn:
        stack = ["Z0"]
        current_state = "q0"
        failed = False
        for char in test_string:
            diagram_placeholder.graphviz_chart(generate_pda_diagram(current_state))
            if current_state == "q0":
                if char == 'a': stack.append('A')
                elif char == 'b' and stack[-1] == 'A': stack.pop(); current_state = "q1"
                else: failed = True; break
            elif current_state == "q1":
                if char == 'b' and stack[-1] == 'A': stack.pop()
                else: failed = True; break
            time.sleep(0.6)
        
        if not failed and current_state == "q1" and stack == ["Z0"]:
            diagram_placeholder.graphviz_chart(generate_pda_diagram('accepted'))
            st.success("✅ Result: String Accepted")
        else:
            st.error("❌ Result: String Rejected")

# --- 7. SUBJECT: COMMUNITY FEEDBACK ---
elif subject == "Community Feedback":
    st.markdown("### 💬 Community Discussion Board")
    st.write("شاركنا رأيك الأكاديمي حول المنصة.")
    if 'db_comments' not in st.session_state:
        st.session_state.db_comments = []

    bad_words = ["bad", "fake", "سيء", "فاشل", "سرقة"]
    with st.form("feedback"):
        name = st.text_input("Name / الاسم:")
        msg = st.text_area("Feedback / التعليق:")
        if st.form_submit_button("Post / إرسال"):
            if any(w in msg.lower() for w in bad_words):
                st.error("⚠️ محتوى غير ملائم.")
            elif name and msg:
                st.session_state.db_comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
                st.success("Sent!")

    for c in reversed(st.session_state.db_comments):
        st.markdown(f"**👤 {c['u']}** ({c['t']}):  \n{c['m']}")
        st.write("---")

# --- 8. SUBJECT: HOME PAGE ---
elif subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    This portal is a professional academic environment for simulating Computer Science concepts.
    - **Theory of Computation**: Interactive PDA visualization.
    - **Mobile App Dev**: Coming soon.
    """)

# --- 9. LEGAL FOOTER (Correct Name) ---
st.markdown(f"""
    <div class="footer">
        <p>© 2024 <b>مهره عطيه الجهني</b> | All Rights Reserved</p>
        <p>🛡️ <b>Intellectual Property Protected:</b> This project is officially registered and timestamped via <b>GitHub</b>.</p>
        <p class="legal-warning">⚠️ WARNING: Any unauthorized copying, imitation of logic, or reproduction of this framework will lead to legal action under International Intellectual Property Laws. 
        <br> يمنع منعاً باتاً تقليد فكرة المشروع أو نسخ الكود البرمجي، ومن يفعل ذلك يعرض نفسه للمساءلة القانونية.</p>
    </div>
    """, unsafe_allow_html=True)