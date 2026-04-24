import streamlit as st
import time
import graphviz

# إعدادات الصفحة الرسمية
st.set_page_config(page_title="MOHRAH CS CORE", layout="wide", page_icon="💎")

# تصميم الواجهة الأكاديمية الفاخرة
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .header-box {
        text-align: center;
        padding: 30px;
        background: linear-gradient(to right, #1e3a8a, #3b82f6);
        color: white;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .jewel-title { font-family: 'Times New Roman', serif; font-size: 48px; font-weight: bold; letter-spacing: 2px; }
    .author-name { font-size: 24px; font-weight: 300; margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.3); display: inline-block; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# الجزء العلوي الفاخر
st.markdown(f"""
    <div class="header-box">
        <div class="jewel-title">THE JEWEL OF COMPUTER SCIENCE</div>
        <div class="author-name">MOHRAH ATIAH ALMAHYAWI</div>
    </div>
    """, unsafe_allow_html=True)

# القائمة الجانبية
selected_subject = st.sidebar.selectbox(
    "Select Academic Discipline:",
    ["Home Page", "Theory of Computation", "Mobile App Development"]
)

# وظيفة لرسم مخطط الحالات (State Diagram)
def draw_pda_diagram(current_state):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', size='8,5')
    
    # تعريف الحالات
    dot.node('start', '', shape='none')
    dot.node('q0', 'q0', shape='circle', color='blue' if current_state == 'q0' else 'black', penwidth='3' if current_state == 'q0' else '1')
    dot.node('q1', 'q1', shape='circle', color='blue' if current_state == 'q1' else 'black', penwidth='3' if current_state == 'q1' else '1')
    dot.node('q_accept', 'Accept', shape='doublecircle', color='green' if current_state == 'accepted' else 'black')

    # تعريف الانتقالات
    dot.edge('start', 'q0')
    dot.edge('q0', 'q0', label='a, Z0 / AZ0\na, A / AA')
    dot.edge('q0', 'q1', label='b, A / ε')
    dot.edge('q1', 'q1', label='b, A / ε')
    dot.edge('q1', 'q_accept', label='ε, Z0 / Z0')
    
    return dot

# --- مادة نظرية الحوسبة ---
if selected_subject == "Theory of Computation":
    st.markdown("### 🤖 PDA Simulation & State Diagram")
    
    # عرض الرسمة في الأعلى
    st.markdown("#### 📊 State Transition Diagram")
    diagram_placeholder = st.empty()
    diagram_placeholder.graphviz_chart(draw_pda_diagram('q0'))

    st.write("---")
    user_input = st.text_input("Enter Input String:", "aabb")
    
    if st.button("Execute Simulation"):
        stack = ["Z0"]
        state = "q0"
        is_rejected = False
        
        col1, col2 = st.columns([2, 1])
        with col1: step_info = st.empty(); progress_bar = st.progress(0)
        with col2: st.markdown("#### 📥 Stack Status"); stack_display = st.empty()

        for i, char in enumerate(user_input):
            progress_bar.progress((i + 1) / len(user_input))
            step_info.info(f"Processing: '{char}'")
            
            # تحديث الرسمة لتوضيح الحالة الحالية
            diagram_placeholder.graphviz_chart(draw_pda_diagram(state))
            
            if state == "q0":
                if char == 'a': stack.append('A')
                elif char == 'b':
                    if len(stack) > 0 and stack[-1] == 'A': stack.pop(); state = "q1"
                    else: is_rejected = True; break
                else: is_rejected = True; break
            elif state == "q1":
                if char == 'b':
                    if len(stack) > 0 and stack[-1] == 'A': stack.pop()
                    else: is_rejected = True; break
                else: is_rejected = True; break
            
            stack_display.write(stack[::-1])
            time.sleep(0.5)
        
        if not is_rejected and state == "q1" and stack == ["Z0"]:
            diagram_placeholder.graphviz_chart(draw_pda_diagram('accepted'))
            st.success("✅ Formal Result: String Accepted")
        else:
            st.error("❌ Formal Result: String Rejected")

# --- الصفحات الأخرى تبقى كما هي ---
elif selected_subject == "Home Page":
    st.markdown("### 🏛️ Welcome to the CS Core Research Portal")
    st.info("💡 استخدم القائمة الجانبية للتنقل بين المختبرات العلمية.")

elif selected_subject == "Mobile App Development":
    st.markdown("### 📱 Mobile Systems Engineering Laboratory")
    st.warning("🚧 This module is currently under academic development.")