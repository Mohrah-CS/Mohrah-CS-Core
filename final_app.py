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

# --- 2. PERSISTENT STORAGE (Visitor & Comments) ---
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 150  # Starting count
else:
    st.session_state.visitor_count += 1

if 'db_comments' not in st.session_state:
    st.session_state.db_comments = [
        {"u": "Academic Support", "m": "Welcome to Mohrah's Lab! Share your feedback here.", "t": "09:00 AM"}
    ]

# --- 3. ADVANCED STYLING ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-box {
        text-align: center; padding: 40px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white; border-radius: 20px; margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .visitor-badge {
        padding: 10px; background-color: #f1f5f9; border-radius: 10px;
        text-align: center; border: 1px solid #1e3a8a; color: #1e3a8a; font-weight: bold;
    }
    .comment-box {
        padding: 15px; border-radius: 10px; background-color: #f8f9fa;
        border-left: 5px solid #1e3a8a; margin-bottom: 10px; color: #1e3a8a;
    }
    .footer {
        text-align: center; padding: 30px; margin-top: 60px;
        border-top: 3px solid #1e3a8a; background-color: #f1f5f9; color: #1e3a8a;
    }
    .legal-warning { color: #b91c1c; font-weight: bold; font-size: 14px; }
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
st.sidebar.markdown(f"""<div class="visitor-badge">👁️ Visitors: {st.session_state.visitor_count}</div>""", unsafe_allow_html=True)
st.sidebar.write("---")

subject = st.sidebar.selectbox(
    "Choose a Module:",
    ["Home Page", "Theory of Computation", "Contact Developer", "Community Feedback"]
)

# --- 6. MODULE: CONTACT DEVELOPER (With Your Real Emails) ---
if subject == "Contact Developer":
    st.markdown("### 📧 Contact the Developer / تواصل مع المبرمجة")
    st.write("يسعدني استقبال استفساراتكم الأكاديمية أو المهنية عبر القنوات الرسمية التالية:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🏛️ **Academic Email (University)**")
        st.code("451000518@stu.ut.edu.sa")
    with col2:
        st.success("📩 **Personal Professional Email**")
        st.code("mohrah.atiiah@icloud.com")

# --- 7. MODULE: COMMUNITY FEEDBACK ---
elif subject == "Community Feedback":
    st.markdown("### 💬 Community Discussion Board")
    with st.form("feedback_form"):
        name = st.text_input("Name / الاسم:")
        msg = st.text_area("Feedback / التعليق:")
        if st.form_submit_button("Post / إرسال"):
            if name and msg:
                st.session_state.db_comments.append({"u": name, "m": msg, "t": time.strftime("%H:%M")})
                st.success("Sent Successfully!")
    
    st.markdown("---")
    for i, c in enumerate(reversed(st.session_state.db_comments)):
        st.markdown(f"""<div class="comment-box"><b>👤 {c['u']}</b> <small>({c['t']})</small><br>{c['m']}</div>""", unsafe_allow_html=True)
        if st.button(f"Translate / ترجمة", key=f"trans_{i}"):
            st.info("Translation service is currently being optimized for this module.")

# --- 8. MODULE: THEORY OF COMPUTATION ---
elif subject == "Theory of Computation":
    st.markdown("### 🤖 Theory of Computation: PDA Simulator")
    st.info("💡 المحتوى العلمي مبني على مناهج جامعة تبوك لتبسيط الفهم.")
    
    def generate_pda_diagram(active_state):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.node('S', '', shape='none')
        dot.node('q0', 'q0', shape='circle', color='#3b82f6' if active_state == 'q0' else 'black', penwidth='3' if active_state == 'q0' else '1')
        dot.node('q1', 'q1', shape='circle', color='#3b82f6' if active_state == 'q1' else 'black', penwidth='3' if active_state == 'q1' else '1')
        dot.node('f', 'Accept', shape='doublecircle', color='green' if active_state == 'accepted' else 'black')
        dot.edge('S', 'q0')
        dot.edge('q0', 'q0', label='a, Z0 / AZ0\\na, A / AA')
        dot.edge('q0', 'q1', label='b, A / ε')
        dot.edge('q1', 'q1', label='b, A / ε')
        dot.edge('q1', 'f', label='ε, Z0 / Z0')
        return dot

    col_graph, col_input = st.columns([2, 1])
    with col_graph:
        diagram_placeholder = st.empty()
        diagram_placeholder.graphviz_chart(generate_pda_diagram('q0'))
    with col_input:
        test_string = st.text_input("Enter Input String:", "aabb")
        if st.button("Run Simulation"):
            stack, current_state, failed = ["Z0"], "q0", False
            for char in test_string:
                diagram_placeholder.graphviz_chart(generate_pda_diagram(current_state))
                if current_state == "q0":
                    if char == 'a': stack.append('A')
                    elif char == 'b' and len(stack) > 0 and stack[-1] == 'A': stack.pop(); current_state = "q1"
                    else: failed = True; break
                elif current_state == "q1":
                    if char == 'b' and len(stack) > 0 and stack[-1] == 'A': stack.pop()
                    else: failed = True; break
                time.sleep(0.6)
            if not failed and current_state == "q1" and stack == ["Z0"]:
                diagram_placeholder.graphviz_chart(generate_pda_diagram('accepted'))
                st.success("✅ Result: String Accepted")
            else: st.error("❌ Result: String Rejected")

# --- 9. HOME PAGE ---
elif subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Portal")
    st.markdown("""
    هذه المنصة هي **مبادرة طلابية تعليمية** تهدف إلى تحويل المفاهيم النظرية في علوم الحاسب إلى نماذج تفاعلية ملموسة.

    **المصدر العلمي (Academic Source):**
    جميع الدروس والأمثلة البرمجية المقدمة في هذه المنصة مستمدة من المناهج الأكاديمية المعتمدة في **جامعة تبوك**، ويتم تقديمها هنا لغرض الشرح والتوضيح وتسهيل الفهم.
    """)

# --- 10. LEGAL FOOTER ---
st.markdown(f"""
    <div class="footer">
        <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
        <p style="font-size: 14px;">📖 المحتوى العلمي مستمد من مناهج جامعة تبوك (جميع الحقوق محفوظة للجامعة).</p>
        <p class="legal-warning">⚠️ WARNING: Any unauthorized copying or reproduction of this framework will lead to legal action under Intellectual Property Laws.</p>
    </div>
    """, unsafe_allow_html=True)