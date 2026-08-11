import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd
import google.generativeai as genai

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MOHRAH CS CORE - Ultimate Edition v13",
    layout="wide",
    page_icon="💎",
    initial_sidebar_state="expanded"
)

# --- LANGUAGE TRANSLATIONS ---
LANGUAGES = {
    "English": {
        "nav_title": "💎 Academic Navigation",
        "select_lang": "Choose Language:",
        "search_placeholder": "Search Platform...",
        "course_select": "Select Course:",
        "lesson_select": "Select Lesson:",
        "contact": "Contact Me",
        "feedback": "Feedback",
        "home": "Home Page",
        "ai_asst": "🤖 Mohrah AI Assistant",
        "toc": "Theory of Computation",
        "os": "Operating Systems",
        "db": "Database Systems",
        "exam_prep": "🚀 Smart Exam Prep",
        "res_hub": "📚 Resource Hub",
        "ach_hall": "🏆 Achievement Hall",
        "community": "👥 Community Corner",
        "dash_title": "🏛️ CS Portal Dashboard",
        "total_lessons": "Total Lessons",
        "students": "Students Benefited",
        "success_rate": "Quiz Success Rate",
        "analytics": "📊 Platform Analytics",
        "why_title": "🎯 Why CS Portal?",
        "source_disp": "Source Dispersion",
        "concept_diff": "Concept Difficulty",
        "instant_eval": "Instant Evaluation"
    },
    "العربية": {
        "nav_title": "💎 التنقل الأكاديمي",
        "select_lang": "اختر اللغة:",
        "search_placeholder": "ابحث في المنصة...",
        "course_select": "اختر المادة:",
        "lesson_select": "اختر الدرس:",
        "contact": "تواصل معي",
        "feedback": "الآراء والملاحظات",
        "home": "الصفحة الرئيسية",
        "ai_asst": "🤖 مساعد مهرة الذكي",
        "toc": "نظرية الحوسبة",
        "os": "نظم التشغيل",
        "db": "نظم قواعد البيانات",
        "exam_prep": "🚀 الاستعداد الذكي للاختبارات",
        "res_hub": "📚 مركز المصادر",
        "ach_hall": "🏆 قاعة الإنجازات",
        "community": "👥 ركن المجتمع",
        "dash_title": "🏛️ COMPUTER SCIENCE PORTAL Dashboard",
        "total_lessons": "إجمالي الدروس",
        "students": "الطلاب المستفيدون",
        "success_rate": "نسبة النجاح",
        "analytics": "📊 تحليلات المنصة",
        "why_title": "🎯 لماذا هذه المنصة؟",
        "source_disp": "تشتت المصادر",
        "concept_diff": "صعوبة المفاهيم",
        "instant_eval": "تقييم فوري"
    },
    "中文": {
        "nav_title": "💎 学术导航",
        "select_lang": "选择语言:",
        "search_placeholder": "搜索平台...",
        "course_select": "选择课程:",
        "lesson_select": "选择课程:",
        "contact": "联系我",
        "feedback": "反馈",
        "home": "主页",
        "ai_asst": "🤖 Mohrah AI 助手",
        "toc": "计算理论",
        "os": "操作系统",
        "db": "数据库系统",
        "exam_prep": "🚀 智能备考",
        "res_hub": "📚 资源中心",
        "ach_hall": "🏆 成就大厅",
        "community": "👥 社区角落",
        "dash_title": "🏛️ 计算机科学门户仪表板",
        "total_lessons": "总课程",
        "students": "受益学生",
        "success_rate": "测验成功率",
        "analytics": "📊 平台分析",
        "why_title": "🎯 为什么选择 CS 门户？",
        "source_disp": "资源分散",
        "concept_diff": "概念难度",
        "instant_eval": "即时评估",
        "about_title": "关于平台",
        "about_desc": "本平台是一项先进的学生教育倡议，旨在简化复杂的计算机科学概念。目前全面涵盖了计算理论 (TOC) 和操作系统 (OS)。",
        "academic_source": "学术来源：所有科学信息、数学定义和说明模型均取自塔布克大学批准的学术课程。内容旨在成为帮助学生理解自动机和正式语言复杂性的综合参考。",
        "goal_target": "🎯 目标：简化 DFA、NFA 和 PDA 等复杂概念。",
        "tool_desc": "🛠️ 工具：交互式模拟器、实时图形和评估测试。",
        "content_desc": "📚 内容：涵盖从数学基础到高级计算模型和图灵机的完整课程。",
        "announcement": "🎊 新成就：操作系统 (OS) 的所有章节已成功添加！🎓✨"
    }
}

if 'lang' not in st.session_state:
    st.session_state.lang = "English"

def t(key):
    return LANGUAGES[st.session_state.lang].get(key, key)

# --- 2. PERSISTENT STORAGE FUNCTIONS ---
COMMENTS_FILE = os.path.join(os.getcwd(), "comments.json")
QUESTIONS_FILE = os.path.join(os.getcwd(), "community_qs.json")

def load_questions():
    initial_qs = [
        {"id": 1, "u": "أحمد", "q": "كيف أفرق بين الـ Paging والـ Segmentation؟", "r": [{"u": "سارة", "m": "الـ Paging تقسيم ثابت، الـ Segmentation منطقي.", "t": "10:05 AM"}], "t": "10:00 AM", "likes": 5},
        {"id": 2, "u": "سارة", "q": "هل الـ DFA يقبل الـ Epsilon؟", "r": [], "t": "11:30 AM", "likes": 3}
    ]
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return initial_qs
    return initial_qs

def save_qs(qs):
    try:
        with open(QUESTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(qs, f, ensure_ascii=False, indent=4)
    except Exception as e:
        st.error(f"Error saving: {e}")

def post_question(name, question, attachment=None):
    qs = load_questions()
    new_id = len(qs) + 1
    att_name = attachment.name if attachment else None
    qs.append({
        "id": new_id, 
        "u": name, 
        "q": question, 
        "r": [], 
        "t": time.strftime("%I:%M %p"),
        "img_name": att_name,
        "likes": 0
    })
    save_qs(qs)

def add_reply(q_id, name, reply):
    qs = load_questions()
    for q in qs:
        if q['id'] == q_id:
            q['r'].append({"u": name, "m": reply, "t": time.strftime("%I:%M %p")})
            break
    save_qs(qs)

def add_like(q_id):
    qs = load_questions()
    for q in qs:
        if q['id'] == q_id:
            q['likes'] += 1
            break
    save_qs(qs)

def load_comments():
    initial_data = [
        {"u": "Academic Support", "m": "Welcome to Mohrah's Lab! Your feedback is valued.", "t": "09:00 AM"},
        {"u": "مهره الجهني", "m": "أهلاً بكم في منصتي التعليمية، أتمنى أن تجدوا الفائدة والمتعة في تعلم علوم الحاسب.", "t": "10:30 AM"},
        {"u": "شعاع", "m": "المشروع رائع جداً ومفيد، شكراً لكِ يا مهره على هذا المجهود المتميز.", "t": "11:15 AM"}
    ]
    if os.path.exists(COMMENTS_FILE):
        try:
            with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return initial_data
    return initial_data

def detect_subject_from_comment(msg):
    """Smart routing: detect if comment is about OS or TOC"""
    msg_lower = msg.lower()
    
    os_keywords = ['operating system', 'نظم التشغيل', 'os', 'process', 'thread', 'scheduling', 'memory', 'deadlock', 'synchronization', 'file system', 'mass storage', 'cpu', 'جدولة', 'عملية', 'خيط', 'ذاكرة', 'تزامن', 'ملف']
    toc_keywords = ['theory of computation', 'نظرية الحوسبة', 'toc', 'dfa', 'nfa', 'automata', 'regular', 'context free', 'turing', 'language', 'grammar', 'أوتوماتا', 'لغة', 'قواعد']
    
    os_score = sum(1 for keyword in os_keywords if keyword in msg_lower)
    toc_score = sum(1 for keyword in toc_keywords if keyword in msg_lower)
    
    if os_score > toc_score and os_score > 0:
        return "Operating Systems"
    elif toc_score > os_score and toc_score > 0:
        return "Theory of Computation"
    return None

def rate_comment(msg):
    """Rate comment quality (1-5 stars)"""
    length = len(msg.split())
    has_question = '?' in msg
    has_code = '`' in msg or 'code' in msg.lower()
    has_reference = 'chapter' in msg.lower() or 'page' in msg.lower()
    
    rating = 1
    if length > 10: rating += 1
    if has_question: rating += 1
    if has_code or has_reference: rating += 1
    if length > 50: rating += 1
    
    return min(rating, 5)

def save_comment(name, msg):
    try:
        if os.path.exists(COMMENTS_FILE):
            with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
                comments = json.load(f)
        else:
            comments = []
        
        rating = rate_comment(msg)
        detected_subject = detect_subject_from_comment(msg)
        
        new_comment = {
            "u": name, 
            "m": msg, 
            "t": time.strftime("%I:%M %p"),
            "rating": rating,
            "subject": detected_subject
        }
        
        comments.append(new_comment)
        
        with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
            json.dump(comments, f, ensure_ascii=False, indent=4)
        
        st.session_state.comment_refresh = time.time()
        return True, detected_subject
    except Exception as e:
        st.error(f"Error saving comment: {e}")
        return False, None

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

    <style>
    /* Ensure main background is white */
    .main { background-color: #ffffff !important; }
    
    /* Sidebar matching the Header Box color exactly */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    }
    
    /* Ensure sidebar text is white */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: white !important;
    }

    /* Input fields and selectboxes inside sidebar */
    [data-testid="stSidebar"] .stTextInput input, 
    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
        color: #0f172a !important;
        border-radius: 8px !important;
    }
    
    /* Circular Logo at the top of sidebar */
    .logo-container {
        display: flex;
        justify-content: center;
        padding: 10px 0;
        margin-bottom: 10px;
    }
    .logo-container img {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        border: 2px solid #fbbf24;
        object-fit: cover;
        background-color: white;
    }
    </style>
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


# --- 5. SIDEBAR NAVIGATION ---
# Language Selector

# --- LOGO ---
st.sidebar.markdown(f'''
    <div class="logo-container">
        <img src="data:image/jpeg;base64,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">
    </div>
''', unsafe_allow_html=True)
st.session_state.lang = st.sidebar.selectbox(t("select_lang"), ["English", "العربية", "中文"], index=0 if st.session_state.lang == "English" else (1 if st.session_state.lang == "العربية" else 2))

st.sidebar.title(t("nav_title"))

# --- SEARCH FEATURE ---
search_query = st.sidebar.text_input(f"🔍 {t('search_placeholder')}", placeholder="e.g. Deadlock, DFA...")
if search_query:
    st.sidebar.info(f"Searching for: {search_query}")

st.sidebar.write("---")

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home Page"

# Navigation mapping
nav_map = {
    t("home"): "Home Page",
    t("ai_asst"): "🤖 Mohrah AI Assistant",
    t("toc"): "Theory of Computation",
    t("os"): "Operating Systems",
    t("db"): "Database Systems",
    t("exam_prep"): "🚀 Smart Exam Prep",
    t("res_hub"): "📚 Resource Hub",
    t("ach_hall"): "🏆 Achievement Hall",
    t("community"): "👥 Community Corner"
}

# Main category selection
main_subject_label = st.sidebar.selectbox(
    t("course_select"),
    list(nav_map.keys()),
    key="main_nav_select"
)
main_subject = nav_map[main_subject_label]

# Handle sub-navigation or direct page assignment
if main_subject == "Theory of Computation":
    subject = st.sidebar.selectbox(
        t("lesson_select"),
        ["Foundations of TOC", "DFA Explorer", "NFA Masterclass", "Regular Expressions", "DFA to RE & Pumping Lemma", "CFG & Chomsky Form", "PDA & CFL Theory", "Turing Machines & Algorithms", "🎓 Course Completion"]
    )
    st.session_state.current_page = subject
elif main_subject == "Operating Systems":
    subject = st.sidebar.selectbox(
        t("lesson_select"),
        ["Operating Systems: Chapter 1 - Introduction", "Operating Systems: Chapter 2 - Structure & Services", "Operating Systems: Chapter 3 - Process Management", "Operating Systems: Chapter 4 - Threads", "Operating Systems: Chapter 5 - CPU Scheduling", "Operating Systems: Chapter 6 - Synchronization", "Operating Systems: Chapter 7 - Deadlocks", "Operating Systems: Chapter 8 - Main Memory", "Operating Systems: Chapter 9 - Virtual Memory", "Operating Systems: Chapter 10 - Mass-Storage Structure", "Operating Systems: Chapter 11 - I/O Systems", "Operating Systems: Chapter 12 - File-System Interface", "Operating Systems: Chapter 13 - File-System Implementation", "🎓 Course Completion"]
    )
    st.session_state.current_page = subject

elif main_subject == "Database Systems":
    subject = st.sidebar.selectbox(
        t("lesson_select"),
        ['Chapter 1: Introduction to Database Systems', 'Chapter 2: Database Architecture', 'Chapter 3: Entity Relationship Model (ERD)', 'Chapter 4: Enhanced ER Model (EER)', 'Chapter 5: Relational Model', 'Chapter 6: Relational Algebra', 'Chapter 7: SQL Basics', 'Chapter 8: Advanced SQL', 'Chapter 9: Functional Dependencies', 'Chapter 10: Normalization', 'Chapter 11: Transactions and Concurrency Control', 'Chapter 12: Database Recovery and Security']
    )
    st.session_state.current_page = subject
else:
    st.session_state.current_page = main_subject

# Override if contact or feedback buttons are pressed
st.sidebar.write("---")
st.sidebar.write(f"### 📞 {t('contact')}")
col1, col2 = st.sidebar.columns(2)

if col1.button(t("contact"), key="contact_btn"):
    st.session_state.current_page = "Contact Developer"
if col2.button(t("feedback"), key="feedback_btn"):
    st.session_state.current_page = "Community Feedback"

display_page = st.session_state.current_page



# --- 6. MODULES ---
if display_page == "Home Page":
    # Translate Home Page Content
    announcement_text = t("announcement") if st.session_state.lang == "中文" else "🎊 إنجاز جديد: تم بحمد الله الانتهاء من إضافة كافة شباتر مادة نظم التشغيل (OS) كاملة! 🎓✨"
    about_title = t("about_title") if st.session_state.lang == "中文" else "عن المنصة / About the Platform"
    about_desc = t("about_desc") if st.session_state.lang == "中文" else "هذه المنصة هي <b>مبادرة طلابية تعليمية متقدمة</b> تهدف إلى تبسيط المفاهيم المعقدة في علوم الحاسب، وتغطي حالياً وبشكل كامل مادتي <b>نظرية الحوسبة (TOC)</b> و <b>نظم التشغيل (OS)</b>."
    academic_source = t("academic_source") if st.session_state.lang == "中文" else "<b>المصدر العلمي (Academic Source):</b> تم استقاء كافة المعلومات العلمية، التعريفات الرياضية، والنماذج التوضيحية من المناهج الأكاديمية المعتمدة في <b>جامعة تبوك</b>. تم تصميم المحتوى ليكون مرجعاً شاملاً يساعد الطلاب على فهم تعقيدات الأوتوماتا واللغات الرسمية."
    goal_target = t("goal_target") if st.session_state.lang == "中文" else "<b>🎯 الهدف:</b> تبسيط المفاهيم المعقدة مثل DFA, NFA, و PDA."
    tool_desc = t("tool_desc") if st.session_state.lang == "中文" else "<b>🛠️ الأدوات:</b> محاكيات تفاعلية، رسومات بيانية حية، واختبارات تقييمية."
    content_desc = t("content_desc") if st.session_state.lang == "中文" else "<b>📚 المحتوى:</b> يغطي المنهج الكامل من الأساسيات الرياضية إلى نماذج الحوسبة المتقدمة وآلات تورينج."

    st.markdown(f"""<div class="announcement-banner">{announcement_text}</div>""", unsafe_allow_html=True)
    st.markdown(f"## {t('dash_title')}")
    st.markdown(f"""
    <div class="learning-card">
    <h3>{about_title}</h3>
    <p>{about_desc}</p>
    <p>{academic_source}</p>
    <div class="info-grid">
        <div class="info-item">{goal_target}</div>
        <div class="info-item">{tool_desc}</div>
        <div class="info-item">{content_desc}</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "🤖 Mohrah AI Assistant":
    st.markdown(f"## {t('ai_asst')}")
    st.info("Ask me anything about Operating Systems or Theory of Computation!")
    
    # Initialize Gemini
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if not api_key:
            st.warning("⚠️ مفتاح الذكاء الاصطناعي غير موجود. يرجى إضافته في إعدادات Streamlit Cloud (Secrets) تحت اسم GOOGLE_API_KEY.")
        else:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("How can I help you today?"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    context_prompt = f"You are an academic assistant for Mohrah's CS Portal. Answer this question in the context of Computer Science (Operating Systems or Theory of Computation): {prompt}"
                    
                    try:
                        response = model.generate_content(context_prompt, stream=True)
                        for chunk in response:
                            full_response += chunk.text
                            message_placeholder.markdown(full_response + "▌")
                        message_placeholder.markdown(full_response)
                    except Exception as e:
                        st.error(f"Error: {e}")
                        full_response = "Sorry, I encountered an error. Please check your API key."
                        message_placeholder.markdown(full_response)
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
    except Exception as e:
        st.error(f"AI Setup Error: {e}")

# --- REST OF THE CODE (PRESERVED) ---
# [Remaining lines from original file will be appended below]
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


elif display_page == "Operating Systems: Chapter 1 - Introduction":
    st.markdown("## ⚙️ Operating Systems: Chapter 1 - Introduction")
    tab_intro_os, tab_what_os_do, tab_os_types, tab_sys_org, tab_sys_arch, tab_sys_ops, tab_res_mgmt, tab_virt, tab_kernel_ds, tab_foss_os = st.tabs([
        "📖 Introduction to OS",
        "📚 What OS Do",
        "📌 OS Types",
        "🏗️ System Organization",
        "🧠 System Architecture",
        "⚙️ System Operations",
        "📊 Resource Management",
        "🧩 Virtualization",
        "🧱 Kernel Data Structures",
        "💡 FOSS OS"
    ])

    with tab_intro_os:
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
        </div>
        """, unsafe_allow_html=True)

    with tab_what_os_do:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.2</div>
        <h3>What Operating Systems Do</h3>
        <p>An Operating System is responsible for managing hardware and software resources and providing services for computer programs.</p>
        <h4>Key Responsibilities:</h4>
        <ul>
            <li>Handle system resources efficiently</li>
            <li>Provide user interface (GUI / CLI)</li>
            <li>Run applications and processes</li>
            <li>Control hardware and software interaction</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_os_types:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.3</div>
        <h3>Operating System Types</h3>
        <ul>
            <li>Batch Operating Systems</li>
            <li>Time-Sharing Systems</li>
            <li>Distributed Operating Systems</li>
            <li>Real-Time Operating Systems</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sys_org:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.4</div>
        <h3>Computer-System Organization</h3>
        <ul>
            <li>CPU, Memory, I/O Devices</li>
            <li>Bus structure connects components</li>
            <li>Interrupt-based communication</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sys_arch:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.5</div>
        <h3>Computer-System Architecture</h3>
        <ul>
            <li>Single Processor Systems</li>
            <li>Multiprocessor Systems</li>
            <li>Clustered Systems</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sys_ops:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.6</div>
        <h3>Computer-System Operations</h3>
        <p>Details about how computer systems operate, including bootstrapping, interrupt handling, and I/O structure.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_res_mgmt:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.7</div>
        <h3>Resource Management</h3>
        <ul>
            <li>CPU Scheduling</li>
            <li>Memory Allocation</li>
            <li>Disk & File Management</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_virt:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.8</div>
        <h3>Virtualization</h3>
        <ul>
            <li>Running multiple OS on one machine</li>
            <li>Virtual Machines (VMs)</li>
            <li>Hypervisors</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_kernel_ds:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.9</div>
        <h3>Kernel Data Structures</h3>
        <ul>
            <li>Process Control Block (PCB)</li>
            <li>Queues (Ready, Waiting)</li>
            <li>Page Tables</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_foss_os:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 1.10</div>
        <h3>Free/Libre and Open-Source Operating Systems</h3>
        <ul>
            <li>Linux</li>
            <li>Ubuntu</li>
            <li>FreeBSD</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 2 - Structure & Services":
    st.markdown("## 🏗️ Operating Systems: Chapter 2 - Structure & Services")
    tab_services, tab_interface, tab_calls, tab_sys_services, tab_link_load, tab_app_specific, tab_design, tab_structure, tab_boot = st.tabs([
        "🛠️ OS Services",
        "🖥️ OS Interface",
        "📞 System Calls",
        "⚙️ System Services",
        "🔗 Linkers & Loaders",
        "📱 App Specificity",
        "🎨 Design & Impl",
        "🏗️ OS Structure",
        "🚀 Build & Boot"
    ])

    with tab_services:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.1</div>
        <h3>Operating System Services</h3>
        <p>Operating systems provide an environment for execution of programs and services to programs and users.</p>
        <ul>
            <li><b>User Interface:</b> CLI, GUI, or Touch.</li>
            <li><b>Program Execution:</b> Loading and running programs.</li>
            <li><b>I/O Operations:</b> Managing input and output devices.</li>
            <li><b>File-System Manipulation:</b> Reading, writing, and creating files.</li>
            <li><b>Communications:</b> Exchange of information between processes.</li>
            <li><b>Error Detection:</b> Detecting and responding to hardware/software errors.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_interface:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.2</div>
        <h3>User and Operating System Interface</h3>
        <ul>
            <li><b>Command Line Interface (CLI):</b> Allows direct command entry.</li>
            <li><b>Graphical User Interface (GUI):</b> User-friendly desktop metaphor interface.</li>
            <li><b>Touchscreen Interface:</b> Gesture-based interaction.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_calls:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.3</div>
        <h3>System Calls</h3>
        <p>Programming interface to the services provided by the OS. Typically written in C or C++.</p>
        <h4>Types of System Calls:</h4>
        <ul>
            <li>Process Control</li>
            <li>File Management</li>
            <li>Device Management</li>
            <li>Information Maintenance</li>
            <li>Communications</li>
            <li>Protection</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_sys_services:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.4</div>
        <h3>System Services</h3>
        <p>System programs provide a convenient environment for program development and execution.</p>
        <ul>
            <li>File manipulation</li>
            <li>Status information</li>
            <li>Programming language support</li>
            <li>Program loading and execution</li>
            <li>Communications</li>
            <li>Background services</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_link_load:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.5</div>
        <h3>Linkers and Loaders</h3>
        <p><b>Linker:</b> Combines several object files into a single executable binary.</p>
        <p><b>Loader:</b> Loads the executable binary into memory for execution.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_app_specific:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.6</div>
        <h3>Why Applications are OS Specific</h3>
        <p>Apps are often compiled for a specific OS because each OS provides different system calls, binary formats, and instruction sets.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_design:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.7</div>
        <h3>Design and Implementation</h3>
        <p>Design goals can be divided into <b>User Goals</b> (easy to use, reliable) and <b>System Goals</b> (easy to design, implement, and maintain).</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_structure:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.8</div>
        <h3>Operating System Structure</h3>
        <ul>
            <li><b>Monolithic:</b> All OS services run in the kernel.</li>
            <li><b>Layered:</b> OS is divided into a number of layers.</li>
            <li><b>Microkernel:</b> Moves as much from the kernel into user space as possible.</li>
            <li><b>Modules:</b> Uses object-oriented approach to load core components.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_boot:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 2.9</div>
        <h3>Building and Booting an OS</h3>
        <p>The process of starting a computer by loading the kernel. The <b>Bootstrap Loader</b> (stored in ROM or EEPROM) locates the kernel, loads it into memory, and starts it.</p>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 3 - Process Management":
    st.markdown("## 📑 Operating Systems: Chapter 3 - Process Management")
    tab_concept, tab_sched, tab_ops, tab_ipc, tab_shared, tab_msg = st.tabs([
        "🔄 Process Concept",
        "📅 Process Scheduling",
        "🛠️ Process Operations",
        "💬 IPC Concept",
        "🧠 Shared Memory",
        "✉️ Message Passing"
    ])

    with tab_concept:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.1</div>
        <h3>Process Concept</h3>
        <p>A <b>Process</b> is a program in execution. It is the unit of work in a modern time-sharing system.</p>
        <h4>Process State:</h4>
        <ul>
            <li><b>New:</b> The process is being created.</li>
            <li><b>Running:</b> Instructions are being executed.</li>
            <li><b>Waiting:</b> The process is waiting for some event to occur.</li>
            <li><b>Ready:</b> The process is waiting to be assigned to a processor.</li>
            <li><b>Terminated:</b> The process has finished execution.</li>
        </ul>
        <p><b>Process Control Block (PCB):</b> Contains information associated with each process (Process state, Program counter, CPU registers, etc.).</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_sched:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.2</div>
        <h3>Process Scheduling</h3>
        <p>The objective of multi-programming is to have some process running at all times to maximize CPU utilization.</p>
        <h4>Scheduling Queues:</h4>
        <ul>
            <li><b>Job Queue:</b> Set of all processes in the system.</li>
            <li><b>Ready Queue:</b> Set of all processes residing in main memory, ready and waiting to execute.</li>
            <li><b>Device Queues:</b> Set of processes waiting for an I/O device.</li>
        </ul>
        <p><b>Schedulers:</b> Long-term (Job), Short-term (CPU), and Medium-term schedulers.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_ops:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.3</div>
        <h3>Operations on Processes</h3>
        <ul>
            <li><b>Process Creation:</b> Parent process creates children processes, which, in turn create other processes, forming a tree of processes.</li>
            <li><b>Process Termination:</b> Process executes last statement and asks the operating system to delete it (exit).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_ipc:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.4</div>
        <h3>Interprocess Communication (IPC)</h3>
        <p>Processes within a system may be <b>independent</b> or <b>cooperating</b>.</p>
        <h4>Reasons for Cooperating Processes:</h4>
        <ul>
            <li>Information sharing</li>
            <li>Computation speedup</li>
            <li>Modularity</li>
            <li>Convenience</li>
        </ul>
        <p>Two models of IPC: <b>Shared Memory</b> and <b>Message Passing</b>.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_shared:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.5</div>
        <h3>IPC in Shared-Memory Systems</h3>
        <p>Cooperating processes communicate by sharing a region of memory. The communication is under the control of the users processes, not the operating system.</p>
        <p><b>Producer-Consumer Problem:</b> A common paradigm for cooperating processes.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_msg:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 3.6</div>
        <h3>IPC in Message-Passing Systems</h3>
        <p>Mechanism for processes to communicate and synchronize their actions without sharing the same address space.</p>
        <h4>Two operations:</h4>
        <ul>
            <li><b>send(message)</b></li>
            <li><b>receive(message)</b></li>
        </ul>
        <p>Communication link can be: Direct or Indirect, Synchronous or Asynchronous.</p>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 4 - Threads":
    st.markdown("## 🧵 Operating Systems: Chapter 4 - Threads")
    tab_overview, tab_multicore, tab_models, tab_libs, tab_implicit = st.tabs([
        "🔍 Overview",
        "💻 Multicore Programming",
        "🏗️ Multithreading Models",
        "📚 Thread Libraries",
        "⚙️ Implicit Threading"
    ])

    with tab_overview:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.1</div>
        <h3>Threads Overview</h3>
        <p>A <b>Thread</b> is a basic unit of CPU utilization; it comprises a thread ID, a program counter, a register set, and a stack.</p>
        <h4>Benefits:</h4>
        <ul>
            <li><b>Responsiveness:</b> Allows continued execution if part of a process is blocked.</li>
            <li><b>Resource Sharing:</b> Threads share the memory and resources of the process they belong to.</li>
            <li><b>Economy:</b> Creating threads is cheaper than creating processes.</li>
            <li><b>Scalability:</b> Can take advantage of multicore architectures.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_multicore:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.2</div>
        <h3>Multicore Programming</h3>
        <p>Multicore systems put multiple computing cores on a single chip. This provides a mechanism for more efficient concurrency.</p>
        <h4>Challenges for Programmers:</h4>
        <ul>
            <li>Identifying tasks</li>
            <li>Balance</li>
            <li>Data splitting</li>
            <li>Data dependency</li>
            <li>Testing and debugging</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_models:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.3</div>
        <h3>Multithreading Models</h3>
        <p>Support for threads may be provided either at the user level, for <b>User Threads</b>, or by the kernel, for <b>Kernel Threads</b>.</p>
        <h4>Common Models:</h4>
        <ul>
            <li><b>Many-to-One:</b> Many user-level threads mapped to a single kernel thread.</li>
            <li><b>One-to-One:</b> Each user-level thread maps to a kernel thread.</li>
            <li><b>Many-to-Many:</b> Many user-level threads mapped to many kernel threads.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_libs:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.4</div>
        <h3>Thread Libraries</h3>
        <p>Provides the programmer with an API for creating and managing threads.</p>
        <ul>
            <li><b>POSIX Pthreads:</b> May be provided as either a user-level or kernel-level library.</li>
            <li><b>Windows Threads:</b> Kernel-level library available on Windows systems.</li>
            <li><b>Java Threads:</b> Managed by the JVM and typically implemented using the underlying OS thread library.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_implicit:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 4.5</div>
        <h3>Implicit Threading</h3>
        <p>Transferring the creation and management of threads from developers to compilers and run-time libraries.</p>
        <h4>Methods:</h4>
        <ul>
            <li><b>Thread Pools:</b> Create a number of threads at process startup and place them into a pool.</li>
            <li><b>OpenMP:</b> Set of compiler directives and an API for C, C++, FORTRAN.</li>
            <li><b>Grand Central Dispatch (GCD):</b> Apple technology for macOS and iOS.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 5 - CPU Scheduling":
    st.markdown("## ⏱️ Operating Systems: Chapter 5 - CPU Scheduling")
    tab_basic, tab_criteria, tab_algorithms, tab_multiprocessor, tab_summary = st.tabs([
        "📌 Basic Concepts",
        "📊 Scheduling Criteria",
        "⚙️ Scheduling Algorithms",
        "🖥️ Multi-Processor Scheduling",
        "📝 Chapter Summary"
    ])

    with tab_basic:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.1</div>
        <h3>Basic Concepts</h3>
        <p><b>CPU Scheduling</b> is one of the most important operating-system functions. Its main goal is to decide which ready process should get the CPU next, especially in a multiprogramming environment where many processes compete for processor time.</p>
        <p>The operating system keeps the CPU busy by switching it among processes. When one process waits for I/O, another ready process can use the CPU. This improves <b>CPU utilization</b> and overall system performance.</p>
        <h4>CPU-I/O Burst Cycle</h4>
        <p>Process execution usually alternates between <b>CPU bursts</b> and <b>I/O bursts</b>. A CPU-bound process spends more time doing computations, while an I/O-bound process spends more time waiting for input/output operations.</p>
        <div class="info-grid">
            <div class="info-item"><b>CPU Burst:</b> Time during which a process uses the CPU for computation.</div>
            <div class="info-item"><b>I/O Burst:</b> Time during which a process waits for input/output completion.</div>
            <div class="info-item"><b>Ready Queue:</b> The queue that contains processes ready to run on the CPU.</div>
        </div>
        <h4>CPU Scheduler and Dispatcher</h4>
        <p>The <b>CPU Scheduler</b> selects a process from the ready queue. The <b>Dispatcher</b> gives control of the CPU to the selected process by performing a context switch, switching to user mode, and jumping to the correct program location.</p>
        <p><b>Dispatch Latency:</b> The time needed by the dispatcher to stop one process and start another process.</p>
        <h4>Preemptive and Non-Preemptive Scheduling</h4>
        <ul>
            <li><b>Non-Preemptive Scheduling:</b> Once a process gets the CPU, it keeps it until it terminates or waits for I/O.</li>
            <li><b>Preemptive Scheduling:</b> The operating system can interrupt a running process and move it back to the ready queue.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_criteria:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.2</div>
        <h3>Scheduling Criteria</h3>
        <p>Different scheduling algorithms are evaluated using specific criteria. The best algorithm depends on the system goal, such as maximizing performance, improving response time, or supporting fairness among processes.</p>
        <table class="summary-table">
            <tr>
                <th>Criterion</th>
                <th>Meaning</th>
                <th>Goal</th>
            </tr>
            <tr>
                <td><b>CPU Utilization</b></td>
                <td>Percentage of time the CPU is busy doing useful work.</td>
                <td>Maximize</td>
            </tr>
            <tr>
                <td><b>Throughput</b></td>
                <td>Number of processes completed per time unit.</td>
                <td>Maximize</td>
            </tr>
            <tr>
                <td><b>Turnaround Time</b></td>
                <td>Total time from process submission to process completion.</td>
                <td>Minimize</td>
            </tr>
            <tr>
                <td><b>Waiting Time</b></td>
                <td>Total time a process spends waiting in the ready queue.</td>
                <td>Minimize</td>
            </tr>
            <tr>
                <td><b>Response Time</b></td>
                <td>Time from submitting a request until the first response is produced.</td>
                <td>Minimize</td>
            </tr>
        </table>
        <div class="step-box">
        <b>Important Note:</b> In interactive systems, response time is often more important than turnaround time because users care about how fast the system starts responding.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_algorithms:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.3</div>
        <h3>Scheduling Algorithms</h3>
        <p>Scheduling algorithms define the rules used by the operating system to choose the next process that will run on the CPU. Each algorithm has advantages and disadvantages depending on process behavior and system requirements.</p>
        <h4>1. First-Come, First-Served (FCFS)</h4>
        <p><b>FCFS</b> schedules processes in the order they arrive. It is simple and non-preemptive, but it may cause the <b>convoy effect</b>, where short processes wait behind a long process.</p>
        <h4>2. Shortest-Job-First (SJF)</h4>
        <p><b>SJF</b> selects the process with the smallest next CPU burst. It can produce minimum average waiting time, but it requires predicting the length of the next CPU burst.</p>
        <h4>3. Shortest-Remaining-Time First (SRTF)</h4>
        <p><b>SRTF</b> is the preemptive version of SJF. If a new process arrives with a CPU burst shorter than the remaining time of the current process, the current process is preempted.</p>
        <h4>4. Priority Scheduling</h4>
        <p>Each process is assigned a priority, and the CPU is allocated to the process with the highest priority. A problem called <b>starvation</b> may occur when low-priority processes wait for a very long time. <b>Aging</b> can solve this problem by gradually increasing the priority of waiting processes.</p>
        <h4>5. Round Robin (RR)</h4>
        <p><b>Round Robin</b> gives each process a small unit of CPU time called a <b>time quantum</b>. After the quantum expires, the process is preempted and placed at the end of the ready queue. RR is commonly used in time-sharing systems.</p>
        <h4>6. Multilevel Queue Scheduling</h4>
        <p>The ready queue is divided into separate queues, such as foreground and background queues. Each queue may have its own scheduling algorithm.</p>
        <h4>7. Multilevel Feedback Queue Scheduling</h4>
        <p>This algorithm allows processes to move between queues. It is flexible because it can favor interactive processes while still giving CPU time to longer jobs.</p>
        <table class="summary-table">
            <tr>
                <th>Algorithm</th>
                <th>Preemptive?</th>
                <th>Main Advantage</th>
                <th>Main Disadvantage</th>
            </tr>
            <tr>
                <td>FCFS</td>
                <td>No</td>
                <td>Simple and fair by arrival order</td>
                <td>Convoy effect</td>
            </tr>
            <tr>
                <td>SJF</td>
                <td>No</td>
                <td>Low average waiting time</td>
                <td>Difficult burst prediction</td>
            </tr>
            <tr>
                <td>SRTF</td>
                <td>Yes</td>
                <td>Good for short jobs</td>
                <td>More context switching</td>
            </tr>
            <tr>
                <td>Priority</td>
                <td>Both</td>
                <td>Supports process importance</td>
                <td>Starvation</td>
            </tr>
            <tr>
                <td>Round Robin</td>
                <td>Yes</td>
                <td>Good response time</td>
                <td>Performance depends on time quantum</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)

    with tab_multiprocessor:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.4</div>
        <h3>Multi-Processor Scheduling</h3>
        <p><b>Multi-Processor Scheduling</b> becomes more complex because the operating system must schedule processes or threads on more than one CPU. The goal is to keep all processors busy while maintaining load balance and efficient execution.</p>
        <h4>Approaches to Multiprocessor Scheduling</h4>
        <ul>
            <li><b>Asymmetric Multiprocessing:</b> One processor handles scheduling decisions, I/O processing, and system activities, while other processors execute user code.</li>
            <li><b>Symmetric Multiprocessing (SMP):</b> Each processor schedules itself. This is common in modern operating systems.</li>
        </ul>
        <h4>Processor Affinity</h4>
        <p><b>Processor Affinity</b> means keeping a process running on the same processor when possible. This is useful because data may remain in that processor's cache, improving performance.</p>
        <ul>
            <li><b>Soft Affinity:</b> The operating system tries to keep a process on the same processor but does not guarantee it.</li>
            <li><b>Hard Affinity:</b> A process is restricted to run only on a specific processor or set of processors.</li>
        </ul>
        <h4>Load Balancing</h4>
        <p><b>Load Balancing</b> attempts to distribute work evenly among processors so that no processor is overloaded while others are idle.</p>
        <ul>
            <li><b>Push Migration:</b> A task periodically checks processor load and moves processes from overloaded processors to less busy ones.</li>
            <li><b>Pull Migration:</b> An idle processor pulls a waiting process from a busy processor.</li>
        </ul>
        <h4>Multicore Processors</h4>
        <p>In multicore systems, multiple processing cores exist on the same chip. Scheduling should consider cache sharing, memory access, and parallel execution to improve performance.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_summary:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 5.5</div>
        <h3>Chapter 5 Summary</h3>
        <p>This chapter explains how operating systems choose which process should use the CPU. CPU scheduling is essential for multiprogramming because it improves CPU utilization and helps the system respond efficiently to users and applications.</p>
        <table class="summary-table">
            <tr>
                <th>Topic</th>
                <th>Key Idea</th>
            </tr>
            <tr>
                <td>Basic Concepts</td>
                <td>CPU scheduling selects a ready process and assigns the CPU to it.</td>
            </tr>
            <tr>
                <td>Scheduling Criteria</td>
                <td>Algorithms are compared using CPU utilization, throughput, turnaround time, waiting time, and response time.</td>
            </tr>
            <tr>
                <td>Scheduling Algorithms</td>
                <td>Common algorithms include FCFS, SJF, SRTF, Priority, Round Robin, Multilevel Queue, and Multilevel Feedback Queue.</td>
            </tr>
            <tr>
                <td>Multi-Processor Scheduling</td>
                <td>Scheduling on multiple CPUs requires load balancing, processor affinity, and efficient management of parallel execution.</td>
            </tr>
        </table>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 6 - Synchronization":
    st.markdown("## 🔄 Operating Systems: Chapter 6 - Synchronization")
    tab_background, tab_critical, tab_hardware, tab_mutex, tab_semaphores, tab_monitors, tab_liveness = st.tabs([
        "📖 Background",
        "⚠️ Critical-Section",
        "🛠️ Hardware Support",
        "🔒 Mutex Locks",
        "🚥 Semaphores",
        "🖥️ Monitors",
        "⚡ Liveness"
    ])

    with tab_background:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.1</div>
        <h3>Background</h3>
        <p>In a multitasking system, multiple processes or threads often share data. If they access and modify the same data concurrently, the outcome may depend on the specific order in which the access takes place. This situation is called a <b>Race Condition</b>.</p>
        <p>The objective of <b>Process Synchronization</b> is to coordinate the execution of processes that share data to ensure data consistency and integrity.</p>
        <div class="step-box">
        <b>Example:</b> If two threads increment the same counter variable at the same time, the final value might be incorrect if the operations overlap.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_critical:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.2</div>
        <h3>The Critical-Section Problem</h3>
        <p>A <b>Critical Section</b> is a segment of code where a process accesses shared resources (like variables or files). No two processes should execute their critical sections at the same time.</p>
        <h4>Requirements for a Solution:</h4>
        <ul>
            <li><b>Mutual Exclusion:</b> If process P is executing in its critical section, no other processes can be executing in theirs.</li>
            <li><b>Progress:</b> If no process is in its critical section and some processes wish to enter, only those not in their remainder sections can participate in the decision, and the selection cannot be postponed indefinitely.</li>
            <li><b>Bounded Waiting:</b> There must be a limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_hardware:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.3</div>
        <h3>Hardware Support for Synchronization</h3>
        <p>Modern computer systems provide special hardware instructions to help solve the critical-section problem efficiently.</p>
        <ul>
            <li><b>Memory Barriers:</b> Instructions that force any changes in memory to be propagated to all other processors.</li>
            <li><b>Atomic Instructions:</b> Non-interruptible instructions like <b>test-and-set</b> and <b>compare-and-swap (CAS)</b> that allow testing and modifying a variable in one atomic step.</li>
            <li><b>Atomic Variables:</b> High-level tools built on atomic instructions to provide thread-safe operations on single variables.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_mutex:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.4</div>
        <h3>Mutex Locks</h3>
        <p>A <b>Mutex (Mutual Exclusion) Lock</b> is the simplest software tool to solve the critical-section problem. It protects a critical section by first requiring a process to <b>acquire</b> a lock and then <b>release</b> it after finishing.</p>
        <ul>
            <li><b>acquire():</b> Atomically checks if the lock is available.</li>
            <li><b>release():</b> Atomically makes the lock available for others.</li>
        </ul>
        <p><b>Spinlock:</b> A type of mutex where a process "spins" (waits in a loop) while waiting for the lock. This is useful for short waits but wastes CPU cycles for long waits.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_semaphores:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.5</div>
        <h3>Semaphores</h3>
        <p>A <b>Semaphore</b> is a more robust tool than mutex locks. It uses an integer variable that can be accessed only through two atomic operations: <b>wait()</b> (or P) and <b>signal()</b> (or V).</p>
        <h4>Types of Semaphores:</h4>
        <ul>
            <li><b>Binary Semaphore:</b> Can range only between 0 and 1. Behaves similarly to a mutex lock.</li>
            <li><b>Counting Semaphore:</b> Can range over an unrestricted domain. Used to control access to a resource with a finite number of instances.</li>
        </ul>
        <div class="step-box">
        <b>Wait Operation:</b> Decrements the semaphore value. If the value is negative, the process blocks.
        <br><b>Signal Operation:</b> Increments the semaphore value. If there are blocked processes, one is woken up.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_monitors:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.6</div>
        <h3>Monitors</h3>
        <p>A <b>Monitor</b> is a high-level synchronization construct that provides a convenient and effective mechanism for process synchronization. It encapsulates shared data and the procedures that operate on that data.</p>
        <ul>
            <li>Only one process at a time can be active within the monitor.</li>
            <li><b>Condition Variables:</b> Used within monitors to allow processes to wait for specific conditions (e.g., <code>condition.wait()</code> and <code>condition.signal()</code>).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_liveness:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 6.7</div>
        <h3>Liveness</h3>
        <p><b>Liveness</b> refers to a set of properties that a system must satisfy to ensure that processes make progress during their execution.</p>
        <h4>Liveness Failures:</h4>
        <ul>
            <li><b>Deadlock:</b> Two or more processes are waiting indefinitely for an event that can be caused only by one of the waiting processes.</li>
            <li><b>Starvation:</b> A process is indefinitely delayed from receiving service because other processes are preferred.</li>
            <li><b>Priority Inversion:</b> A higher-priority process is delayed by a lower-priority process holding a required resource.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 7 - Deadlocks":
    st.markdown("## 🛑 Operating Systems: Chapter 7 - Deadlocks")
    tab_model, tab_char, tab_handling, tab_prev, tab_avoid, tab_detect, tab_recovery = st.tabs([
        "🏗️ System Model",
        "🔍 Characterization",
        "🛠️ Handling Methods",
        "🛡️ Prevention",
        "⚖️ Avoidance",
        "📡 Detection",
        "🔄 Recovery"
    ])

    with tab_model:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.1</div>
        <h3>System Model</h3>
        <p>A system consists of a finite number of resources to be distributed among several competing processes. Resources are partitioned into several types (CPU cycles, memory space, I/O devices).</p>
        <p>A process must request a resource before using it and release it after using it. The sequence is: <b>Request → Use → Release</b>.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_char:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.2</div>
        <h3>Deadlock Characterization</h3>
        <p>A deadlock situation can arise if the following four conditions hold simultaneously in a system:</p>
        <ul>
            <li><b>Mutual Exclusion:</b> Only one process at a time can use a resource.</li>
            <li><b>Hold and Wait:</b> A process holding at least one resource is waiting to acquire additional resources held by other processes.</li>
            <li><b>No Preemption:</b> Resources cannot be preempted; they are released only voluntarily by the process holding them.</li>
            <li><b>Circular Wait:</b> A set of waiting processes exists such that P0 is waiting for P1, P1 for P2, ..., and Pn for P0.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_handling:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.3</div>
        <h3>Methods for Handling Deadlocks</h3>
        <p>There are three main ways to deal with the deadlock problem:</p>
        <ul>
            <li>Ensure that the system will never enter a deadlock state (Prevention or Avoidance).</li>
            <li>Allow the system to enter a deadlock state, detect it, and then recover.</li>
            <li>Ignore the problem altogether and pretend that deadlocks never occur (used by most operating systems, including UNIX and Windows).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_prev:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.4</div>
        <h3>Deadlock Prevention</h3>
        <p>Prevention provides a set of methods to ensure that at least one of the four necessary conditions for deadlock cannot hold.</p>
        <ul>
            <li><b>Mutual Exclusion:</b> Not required for sharable resources (e.g., read-only files).</li>
            <li><b>Hold and Wait:</b> Must guarantee that whenever a process requests a resource, it does not hold any other resources.</li>
            <li><b>No Preemption:</b> If a process holding resources requests another that cannot be immediately allocated, all currently held resources are released.</li>
            <li><b>Circular Wait:</b> Impose a total ordering of all resource types and require that each process requests resources in an increasing order of enumeration.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_avoid:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.5</div>
        <h3>Deadlock Avoidance</h3>
        <p>Avoidance requires that the system has some additional a priori information available about which resources a process will request and use during its lifetime.</p>
        <p><b>Safe State:</b> A state is safe if the system can allocate resources to each process in some order and still avoid a deadlock.</p>
        <p><b>Banker’s Algorithm:</b> A classic avoidance algorithm used in systems with multiple instances of each resource type.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_detect:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.6</div>
        <h3>Deadlock Detection</h3>
        <p>If a system does not employ deadlock prevention or avoidance, a deadlock situation may occur. In this environment, the system must provide:</p>
        <ul>
            <li>An algorithm that examines the state of the system to determine whether a deadlock has occurred.</li>
            <li>An algorithm to recover from the deadlock.</li>
        </ul>
        <p><b>Wait-for Graph:</b> Used for detection in systems with single instances of resource types.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_recovery:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 7.7</div>
        <h3>Recovery from Deadlock</h3>
        <p>When a detection algorithm determines that a deadlock exists, several alternatives are available:</p>
        <ul>
            <li><b>Process Termination:</b> Abort all deadlocked processes or abort one process at a time until the deadlock cycle is eliminated.</li>
            <li><b>Resource Preemption:</b> Successively preempt some resources from processes and give them to other processes until the deadlock cycle is broken.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 8 - Memory Management":
    st.markdown("## 🧠 Operating Systems: Chapter 8 - Memory Management")
    tab_address, tab_allocation, tab_logical, tab_virtual, tab_cache = st.tabs([
        "📍 Address Space",
        "📦 Allocation",
        "🔀 Logical vs Physical",
        "☁️ Virtual Memory",
        "⚡ Cache & TLB"
    ])

    with tab_address:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.1</div>
        <h3>Memory Address Space</h3>
        <p>The <b>Address Space</b> is the set of all logical addresses generated by a program. Memory management ensures that programs have enough space to run and that they don't interfere with each other.</p>
        <p><b>Binding:</b> The process of mapping program addresses to actual physical memory addresses. This can happen at Compile time, Load time, or Execution time.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_allocation:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.2</div>
        <h3>Memory Allocation Techniques</h3>
        <p>Main memory must provide for both the operating system and various user processes. We need to allocate memory in the most efficient way possible.</p>
        <ul>
            <li><b>Contiguous Allocation:</b> Each process is contained in a single contiguous section of memory.</li>
            <li><b>Paging:</b> A memory-management scheme that permits the physical address space of a process to be non-contiguous.</li>
            <li><b>Segmentation:</b> A memory-management scheme that supports the user view of memory as a collection of segments (code, data, stack).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_logical:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.3</div>
        <h3>Logical vs Physical Address</h3>
        <p><b>Logical Address:</b> Generated by the CPU; also referred to as a virtual address.</p>
        <p><b>Physical Address:</b> Address seen by the memory unit (the actual location in RAM).</p>
        <p><b>Memory-Management Unit (MMU):</b> Hardware device that at run time maps virtual to physical addresses.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_virtual:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.4</div>
        <h3>Virtual Memory vs Physical Memory</h3>
        <p><b>Virtual Memory:</b> A technique that allows the execution of processes that are not completely in memory. It abstracts main memory into an extremely large, uniform array of storage, separating logical memory as viewed by the user from physical memory.</p>
        <p><b>Physical Memory:</b> The actual RAM available in the system.</p>
        <div class="step-box">
        <b>Benefit:</b> Virtual memory allows programs to be larger than physical memory and increases CPU utilization by allowing more processes to run concurrently.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab_cache:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 8.5</div>
        <h3>Cache Line and TLB</h3>
        <p>To speed up memory access, modern systems use specialized hardware buffers.</p>
        <ul>
            <li><b>Cache Line:</b> The smallest unit of data that can be transferred between the main memory and the cache.</li>
            <li><b>Translation Look-aside Buffer (TLB):</b> A small, fast-lookup hardware cache that stores recent transitions from logical to physical addresses. It helps avoid the need to access the page table in main memory for every memory reference.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 9 - Mass-Storage":
    st.markdown("## 💾 Operating Systems: Chapter 9 - Mass-Storage Systems")
    tab_overview, tab_hdd, tab_nvm, tab_error, tab_raid = st.tabs([
        "🏗️ Overview",
        "💿 HDD Scheduling",
        "⚡ NVM Scheduling",
        "🔍 Error Detection",
        "🛡️ RAID Structure"
    ])

    with tab_overview:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 9.1</div>
        <h3>Overview of Mass Storage Structure</h3>
        <p>Mass storage systems are used to store large amounts of data permanently. The most common types are <b>Hard Disk Drives (HDD)</b> and <b>Non-Volatile Memory (NVM)</b> like SSDs.</p>
        <p>The operating system is responsible for using the storage hardware efficiently, providing fast access, and ensuring data reliability.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_hdd:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 9.2</div>
        <h3>HDD Scheduling</h3>
        <p>For HDD, the goal is to minimize <b>Seek Time</b> (the time for the disk arm to move the heads to the cylinder containing the desired sector).</p>
        <h4>Scheduling Algorithms:</h4>
        <ul>
            <li><b>FCFS:</b> First-Come, First-Served. Simple but may cause long movements.</li>
            <li><b>SCAN (Elevator Algorithm):</b> The disk arm moves from one end to the other, servicing requests along the way.</li>
            <li><b>C-SCAN (Circular SCAN):</b> Similar to SCAN but only services requests in one direction, then jumps back to the start.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_nvm:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 9.3</div>
        <h3>NVM Scheduling</h3>
        <p><b>Non-Volatile Memory (NVM)</b> devices, like SSDs, have no moving parts. Therefore, seek time is not an issue. Scheduling for NVM focuses more on reducing latency and managing write endurance.</p>
        <p>Most NVM devices use simple FCFS scheduling because the access time is nearly uniform across the entire device.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_error:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 9.4</div>
        <h3>Error Detection and Correction</h3>
        <p>Storage devices are prone to errors due to physical wear or electromagnetic interference. Systems use <b>Error-Correcting Codes (ECC)</b> to detect and fix small data corruptions automatically.</p>
        <p><b>Checksums:</b> Used to verify the integrity of data blocks by comparing calculated values during read and write operations.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_raid:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 9.5</div>
        <h3>RAID Structure</h3>
        <p><b>RAID (Redundant Array of Independent Disks)</b> is a technology that combines multiple physical disk drives into a single logical unit for data redundancy and performance improvement.</p>
        <ul>
            <li><b>RAID 0:</b> Striping (Performance, no redundancy).</li>
            <li><b>RAID 1:</b> Mirroring (High redundancy).</li>
            <li><b>RAID 5:</b> Striping with distributed parity (Balance of performance and redundancy).</li>
            <li><b>RAID 6:</b> Dual parity (Can survive two disk failures).</li>
            <li><b>RAID 10:</b> A combination of mirroring and striping.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "Operating Systems: Chapter 10 - File Systems":
    st.markdown("## 📂 Operating Systems: Chapter 10 - File Systems")
    tab_concept, tab_access, tab_dir, tab_alloc, tab_free = st.tabs([
        "📄 File Concept",
        "🖱️ Access Methods",
        "📁 Directory Structure",
        "📦 Allocation Methods",
        "🆓 Free Space"
    ])

    with tab_concept:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 10.1</div>
        <h3>File Concept</h3>
        <p>A <b>File</b> is a logical storage unit mapped by the operating system onto physical devices. It is a collection of related information recorded on secondary storage.</p>
        <p><b>Attributes:</b> Name, Identifier, Type, Location, Size, Protection, Time/Date/User ID.</p>
        <p><b>Operations:</b> Create, Write, Read, Reposition (seek), Delete, Truncate.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab_access:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 10.2</div>
        <h3>Access Methods</h3>
        <ul>
            <li><b>Sequential Access:</b> Information in the file is processed in order, one record after the other (like a tape).</li>
            <li><b>Direct Access (Relative Access):</b> A file is made up of fixed-length logical records that allow programs to read and write records rapidly in no particular order.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_dir:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 10.3</div>
        <h3>Directory Structure</h3>
        <p>The <b>Directory</b> is a symbol table that translates file names into their directory entries. It helps organize and provide information about all files in the system.</p>
        <ul>
            <li><b>Single-Level Directory:</b> All files are in the same directory (easy but naming conflicts).</li>
            <li><b>Two-Level Directory:</b> Separate directory for each user.</li>
            <li><b>Tree-Structured Directory:</b> Users can create their own subdirectories and organize files (most common).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_alloc:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 10.4</div>
        <h3>Allocation Methods</h3>
        <p>Refers to how disk blocks are allocated for files:</p>
        <ul>
            <li><b>Contiguous Allocation:</b> Each file occupies a set of contiguous blocks (Fast but fragmentation).</li>
            <li><b>Linked Allocation:</b> Each file is a linked list of disk blocks (No fragmentation but slow).</li>
            <li><b>Indexed Allocation:</b> Brings all pointers together into one location: the index block (Supports direct access without fragmentation).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab_free:
        st.markdown("""
        <div class="learning-card">
        <div class="concept-badge">Module 10.5</div>
        <h3>Free Space Management</h3>
        <p>The system maintains a <b>Free-Space List</b> to keep track of available disk blocks.</p>
        <ul>
            <li><b>Bit Vector:</b> Each block is represented by 1 bit (0=allocated, 1=free).</li>
            <li><b>Linked List:</b> Link together all the free disk blocks.</li>
            <li><b>Grouping:</b> Store the addresses of n free blocks in the first free block.</li>
            <li><b>Counting:</b> Store the address of the first free block and the number of free blocks following it.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif display_page == "🎓 OS Course Completion":
    st.balloons()
    st.markdown("""
    <div class="header-box" style="background: linear-gradient(135deg, #065f46 0%, #059669 100%);">
        <h1 style="color: white; margin: 0;">🎓 Operating Systems: Final Review</h1>
        <p style="color: #d1fae5; font-size: 20px;">Comprehensive Summary & Key Concepts</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="learning-card">
        <h3>🌟 Core Pillars of OS</h3>
        <p>Operating Systems manage the complex interaction between hardware and software. The main areas we covered are:</p>
        <ul>
            <li><b>Process Management:</b> Creation, scheduling, and synchronization of processes and threads.</li>
            <li><b>Memory Management:</b> Paging, segmentation, and virtual memory to optimize RAM usage.</li>
            <li><b>Storage Management:</b> Efficient data placement on HDDs/SSDs and file system organization.</li>
            <li><b>Protection & Security:</b> Ensuring safe access to system resources.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="learning-card">
        <h3>📝 Exam Preparation Tips</h3>
        <ul>
            <li><b>Scheduling:</b> Practice Gantt charts for FCFS, SJF, and Round Robin.</li>
            <li><b>Deadlocks:</b> Understand the 4 conditions and Banker's Algorithm.</li>
            <li><b>Memory:</b> Be able to calculate physical addresses from logical addresses in Paging.</li>
            <li><b>Synchronization:</b> Understand Mutex vs Semaphores and the Critical Section problem.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="learning-card" style="text-align: center;">
        <h3>🏆 Congratulations! / تهانينا!</h3>
        <p>لقد أتممت بنجاح مراجعة منهج <b>نظم التشغيل (Operating Systems)</b>. هذه المنصة صُممت لتكون مرجعك الدائم للفهم والتميز.</p>
        <p><b>"Education is the most powerful weapon which you can use to change the world."</b></p>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Memory Management":
    st.info("Memory Management module is under development. Stay tuned!")
elif display_page == "Storage & I/O":
    st.info("Storage & I/O module is under development. Stay tuned!")



elif display_page == "🚀 Smart Exam Prep":
    st.markdown("## 🚀 The Ultimate Challenge: Professional Quiz Bank")
    st.error("🚨 LEVEL: IMPOSSIBLE | مستوى الصعوبة: مستحيل")
    st.write("هذا القسم مصمم للمحترفين فقط. الأسئلة هنا تحاكي اختبارات الشهادات العالمية والاختبارات النهائية الأكثر تعقيداً.")
    
    quiz_subject = st.selectbox("Choose Your Battlefield / اختر المادة:", ["Operating Systems (OS)", "Theory of Computation (TOC)"])
    
    if quiz_subject == "Operating Systems (OS)":
        st.subheader("🖥️ OS Hardcore Challenge (20 Questions)")
        os_bank = [
            {"q": "1. In a system with 4 resources of the same type, shared by 3 processes, each needing at most 2 resources. The system is:", "o": ["Always deadlock-free", "Prone to deadlock", "In an unsafe state", "Inconsistent"], "a": "Always deadlock-free"},
            {"q": "2. Which of these is NOT a necessary condition for deadlock?", "o": ["Mutual Exclusion", "Hold and Wait", "No Preemption", "Circular Wait", "Preemption"], "a": "Preemption"},
            {"q": "3. If the hit ratio of a TLB is 80%, and it takes 20ns to search TLB and 100ns to access memory, what is the Effective Access Time (EAT)?", "o": ["120ns", "140ns", "100ns", "180ns"], "a": "140ns"},
            {"q": "4. In UNIX, which system call is used to replace the process's memory space with a new program?", "o": ["fork()", "exec()", "wait()", "exit()"], "a": "exec()"},
            {"q": "5. Which scheduling algorithm is optimal in terms of minimizing average waiting time?", "o": ["FCFS", "RR", "SJF (Non-preemptive)", "SRTF (Preemptive SJF)"], "a": "SRTF (Preemptive SJF)"},
            {"q": "6. Belady's Anomaly is a phenomenon where adding more page frames results in:", "o": ["Fewer page faults", "More page faults", "Same page faults", "Faster execution"], "a": "More page faults"},
            {"q": "7. A critical section is a program segment where:", "o": ["The OS kernel runs", "Shared data is accessed", "Deadlock occurs", "Processes are terminated"], "a": "Shared data is accessed"},
            {"q": "8. Which RAID level provides no redundancy and focuses only on performance?", "o": ["RAID 0", "RAID 1", "RAID 5", "RAID 10"], "a": "RAID 0"},
            {"q": "9. In the context of I/O, 'Spooling' stands for:", "o": ["Simultaneous Peripheral Operations On-Line", "Sequential Peripheral Output Line", "System Peripheral Operations Link", "Simple Process Output Line"], "a": "Simultaneous Peripheral Operations On-Line"},
            {"q": "10. What is the main purpose of the 'Dirty Bit' in paging?", "o": ["To mark a page as read-only", "To indicate if a page has been modified", "To prevent page faults", "To speed up TLB search"], "a": "To indicate if a page has been modified"},
            {"q": "11. A thread shares with other threads of the same process its:", "o": ["Stack", "Registers", "Code section", "Thread ID"], "a": "Code section"},
            {"q": "12. In Banker's algorithm, the 'Need' matrix is calculated as:", "o": ["Max + Allocation", "Max - Allocation", "Allocation - Max", "Max * Allocation"], "a": "Max - Allocation"},
            {"q": "13. Which of the following is a solution to the 'External Fragmentation' problem?", "o": ["Paging", "Segmentation", "Fixed Partitioning", "Compaction"], "a": "Compaction"},
            {"q": "14. The 'Thrashing' occurs when:", "o": ["The CPU is idle", "A process is in a safe state", "The system spends more time paging than executing", "The disk is full"], "a": "The system spends more time paging than executing"},
            {"q": "15. Which of the following is NOT a kernel structure?", "o": ["Monolithic", "Microkernel", "Exokernel", "Multithreaded"], "a": "Multithreaded"},
            {"q": "16. A 'Zombie' process is a process that has:", "o": ["Not started yet", "Finished execution but still has an entry in the process table", "Been killed by the user", "No parent"], "a": "Finished execution but still has an entry in the process table"},
            {"q": "17. The 'Wait' operation on a semaphore decreases its value. If the value becomes negative, the process is:", "o": ["Terminated", "Blocked", "Continued", "Restarted"], "a": "Blocked"},
            {"q": "18. In the Buddy System memory allocation, memory is divided into blocks of size:", "o": ["Fixed 4KB", "Powers of 2", "Variable sizes based on process", "Prime numbers"], "a": "Powers of 2"},
            {"q": "19. Which disk scheduling algorithm is also known as the 'Elevator Algorithm'?", "o": ["FCFS", "SSTF", "SCAN", "LOOK"], "a": "SCAN"},
            {"q": "20. What is the purpose of the 'Medium-term Scheduler'?", "o": ["Selects processes from the pool to load into memory", "Selects processes from ready queue to execute", "Swaps processes in and out of memory", "Manages I/O devices"], "a": "Swaps processes in and out of memory"}
        ]
        
        score = 0
        for i, item in enumerate(os_bank):
            choice = st.radio(item["q"], item["o"], key=f"os_huge_{i}")
            if choice == item["a"]:
                score += 1
        
        if st.button("Submit OS Mega Quiz"):
            st.write(f"### Final Result: {score}/{len(os_bank)}")
            if score == len(os_bank):
                st.success("🏆 LEGENDARY! You've conquered the OS Mega Bank!")
                st.balloons()
            elif score >= 15:
                st.info("Excellent! You have a very strong grasp of OS.")
            else:
                st.warning("Keep pushing! These questions are tough for a reason.")

    elif quiz_subject == "Theory of Computation (TOC)":
        st.subheader("🧠 TOC Theoretical Battlefield (20 Questions)")
        toc_bank = [
            {"q": "1. Which of the following is the most powerful machine?", "o": ["DFA", "PDA", "Turing Machine", "LBA"], "a": "Turing Machine"},
            {"q": "2. The language L = {a^n b^n | n >= 0} is:", "o": ["Regular", "Context-Free", "Context-Sensitive", "Unrestricted"], "a": "Context-Free"},
            {"q": "3. A language is 'Recursively Enumerable' if it is recognized by:", "o": ["DFA", "PDA", "Turing Machine", "Finite State Machine"], "a": "Turing Machine"},
            {"q": "4. The 'Pumping Lemma' for Context-Free Languages uses the value:", "o": ["n", "p", "k", "m"], "a": "p"},
            {"q": "5. Which of the following problems is 'Undecidable'?", "o": ["DFA Acceptance", "CFG Emptiness", "The Halting Problem", "NFA to DFA Conversion"], "a": "The Halting Problem"},
            {"q": "6. A grammar is 'Ambiguous' if it produces:", "o": ["No strings", "More than one leftmost derivation for a string", "Only infinite strings", "Only regular languages"], "a": "More than one leftmost derivation for a string"},
            {"q": "7. The intersection of two Regular Languages is always:", "o": ["Regular", "Context-Free", "Non-regular", "Recursive"], "a": "Regular"},
            {"q": "8. Every Regular Language is also a Context-Free Language.", "o": ["True", "False"], "a": "True"},
            {"q": "9. A Turing Machine that always halts is called:", "o": ["Universal TM", "Decider", "Recognizer", "Linear Bounded Automaton"], "a": "Decider"},
            {"q": "10. Chomsky Normal Form (CNF) requires productions to be of the form:", "o": ["A -> BC or A -> a", "A -> aB", "A -> B", "A -> abc"], "a": "A -> BC or A -> a"},
            {"q": "11. The set of all strings over {0,1} is:", "o": ["Finite", "Countably Infinite", "Uncountably Infinite", "Empty"], "a": "Countably Infinite"},
            {"q": "12. Which machine uses two stacks to simulate a Turing Machine?", "o": ["DFA", "PDA", "2-stack PDA", "NFA"], "a": "2-stack PDA"},
            {"q": "13. The 'Rice's Theorem' states that any non-trivial property of the language recognized by a TM is:", "o": ["Decidable", "Undecidable", "Regular", "Context-Free"], "a": "Undecidable"},
            {"q": "14. What is the time complexity of the CYK algorithm for CFG parsing?", "o": ["O(n)", "O(n^2)", "O(n^3)", "O(2^n)"], "a": "O(n^3)"},
            {"q": "15. A language is 'Regular' if and only if it is described by a:", "o": ["Regular Expression", "PDA", "Turing Machine", "Context-Free Grammar"], "a": "Regular Expression"},
            {"q": "16. Greibach Normal Form (GNF) requires productions to start with:", "o": ["A non-terminal", "A terminal", "Two non-terminals", "An epsilon"], "a": "A terminal"},
            {"q": "17. The 'Empty String' is denoted by:", "o": ["Sigma", "Delta", "Epsilon", "Phi"], "a": "Epsilon"},
            {"q": "18. Which of the following is NOT a closure property of Context-Free Languages?", "o": ["Union", "Concatenation", "Kleene Star", "Intersection"], "a": "Intersection"},
            {"q": "19. The 'Universal Turing Machine' (UTM) can simulate:", "o": ["Only DFAs", "Only PDAs", "Any other Turing Machine", "Only itself"], "a": "Any other Turing Machine"},
            {"q": "20. The 'Church-Turing Thesis' states that:", "o": ["Everything is decidable", "Turing Machines define the limit of effective computation", "PDAs are as powerful as TMs", "DFAs are better than NFAs"], "a": "Turing Machines define the limit of effective computation"}
        ]
        
        score = 0
        for i, item in enumerate(toc_bank):
            choice = st.radio(item["q"], item["o"], key=f"toc_huge_{i}")
            if choice == item["a"]:
                score += 1
        
        if st.button("Submit TOC Mega Quiz"):
            st.write(f"### Final Result: {score}/{len(toc_bank)}")
            if score == len(toc_bank):
                st.success("💎 GOD-LIKE! You have mastered the theory of computation!")
                st.balloons()
            elif score >= 15:
                st.info("Great job! You are ready for the final exam.")
            else:
                st.warning("Theory is deep. Re-read the modules and try again!")
elif display_page == "📚 Resource Hub":
    st.markdown("## 📚 Deep-Dive Resource Hub")
    st.write("هنا تجد ملخصات PDF عميقة وشاملة لكل شابتر، تم إعدادها بعناية لتكون مرجعك النهائي.")
    
    tab_os_res, tab_toc_res = st.tabs(["🖥️ Operating Systems Resources", "🧠 Theory of Computation Resources"])
    
    with tab_os_res:
        st.markdown("### 📄 Comprehensive OS Chapter Summaries")
        os_chapters = {
            "Chapter 1: Introduction to OS Concepts": "OS_Ch1.pdf",
            "Chapter 2: OS Structures & System Calls": "OS_Ch2.pdf",
            "Chapter 3: Process Management & IPC": "OS_Ch3.pdf",
            "Chapter 4: Threads & Multicore Programming": "OS_Ch4.pdf",
            "Chapter 5: CPU Scheduling Algorithms (Deep Analysis)": "OS_Ch5.pdf",
            "Chapter 6: Process Synchronization & Mutex": "OS_Ch6.pdf",
            "Chapter 7: Deadlocks: Prevention & Avoidance": "OS_Ch7.pdf",
            "Chapter 8: Memory Management & Paging": "OS_Ch8.pdf",
            "Chapter 9: Mass-Storage & RAID Structures": "OS_Ch9.pdf",
            "Chapter 10: File Systems & Allocation Methods": "OS_Ch10.pdf"
        }
        for ch_name, file_name in os_chapters.items():
            col_a, col_b = st.columns([3, 1])
            col_a.write(f"📂 **{ch_name}**")
            file_path = f"pdfs/{file_name}"
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    col_b.download_button("Download PDF", f, file_name=file_name, key=f"dl_{file_name}")
            else:
                col_b.button("Coming Soon", key=f"soon_{file_name}", disabled=True)

            
    with tab_toc_res:
        st.markdown("### 📄 Advanced TOC Modules")
        toc_modules = {
            "Module 1: Mathematical Foundations": "TOC_Mod1.pdf",
            "Module 2: Finite Automata (DFA/NFA) Masterclass": "TOC_Mod2.pdf",
            "Module 3: Regular Expressions & Pumping Lemma": "TOC_Mod3.pdf",
            "Module 4: Context-Free Grammars & PDA": "TOC_Mod4.pdf",
            "Module 5: Turing Machines & Decidability": "TOC_Mod5.pdf"
        }
        for mod_name, file_name in toc_modules.items():
            col_a, col_b = st.columns([3, 1])
            col_a.write(f"📂 **{mod_name}**")
            file_path = f"pdfs/{file_name}"
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    col_b.download_button("Download PDF", f, file_name=file_name, key=f"dl_{file_name}")
            else:
                col_b.button("Coming Soon", key=f"soon_{file_name}", disabled=True)


    st.markdown("""
    <div class="step-box">
        <b>ملاحظة:</b> جميع هذه المصادر مستقاة من المناهج الأكاديمية المعتمدة ومحدثة لعام 2026.
    </div>
    """, unsafe_allow_html=True)


elif display_page == "🏆 Achievement Hall":
    st.markdown("## 🏆 Achievement Hall: Celebrate Your Academic Journey")
    st.write("كل خطوة تخطوها في هذه المنصة هي لبنة في بناء مستقبلك المهني. هنا نحتفي بإنجازاتك!")
    
    st.markdown("""
    <div class="learning-card">
        <h4>🌟 فلسفة الإنجاز / Achievement Philosophy</h4>
        <p>التعلم ليس مجرد حفظ للمعلومات، بل هو رحلة من التحدي والاستمرار. الحصول على هذه الأوسمة يعني أنك امتلكت الانضباط والشغف اللازمين لفهم أعقد مفاهيم علوم الحاسب.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="learning-card" style="border-top: 5px solid #fbbf24;">
            <h2 style="text-align: center;">🥇 OS Master</h2>
            <p style="color: #d97706; font-weight: bold; text-align: center;">وسام خبير نظم التشغيل</p>
            <p>يُمنح هذا الوسام للطالب الذي استطاع الإبحار في أعماق النواة (Kernel)، وفهم كيف تدار العمليات وتوزع الذاكرة. أنت الآن تدرك كيف يفكر "عقل" الحاسوب، وهذا يجعلك مبرمجاً أكثر كفاءة وقدرة على بناء أنظمة مستقرة.</p>
            <ul style="font-size: 14px;">
                <li>فهم عميق لجدولة العمليات (Scheduling)</li>
                <li>إتقان مفاهيم المزامنة (Synchronization)</li>
                <li>القدرة على تحليل مشاكل الذاكرة والتخزين</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="learning-card" style="border-top: 5px solid #10b981;">
            <h2 style="text-align: center;">💎 Diamond Researcher</h2>
            <p style="color: #059669; font-weight: bold; text-align: center;">وسام الباحث المتميز</p>
            <p>هذا الوسام مخصص لمن لم يكتفِ بالقشور، بل غاص في المصادر الخارجية والملخصات العميقة. البحث هو مفتاح الابتكار، وأنت أثبتّ أنك تمتلك عقلية الباحث الذي لا يتوقف عن التعلم.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="learning-card" style="border-top: 5px solid #3b82f6;">
            <h2 style="text-align: center;">🥈 TOC Expert</h2>
            <p style="color: #2563eb; font-weight: bold; text-align: center;">وسام مهندس الحوسبة النظرية</p>
            <p>التعامل مع اللغات الرسمية والأوتوماتا يتطلب قدرات ذهنية تحليلية عالية. حصولك على هذا الوسام يعني أنك تغلبت على أحد أصعب التحديات الرياضية في علوم الحاسب، وأصبحت قادراً على فهم حدود الحوسبة ومنطق الآلات.</p>
            <ul style="font-size: 14px;">
                <li>تصميم وتحليل آلات DFA و NFA</li>
                <li>فهم قواعد اللغات الحرة (CFG)</li>
                <li>إدراك القوة الحوسبية لآلات تورينج</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="learning-card" style="border-top: 5px solid #8b5cf6;">
            <h2 style="text-align: center;">🚀 Early Adopter</h2>
            <p style="color: #7c3aed; font-weight: bold; text-align: center;">وسام الريادة والسبق</p>
            <p>أنت من أوائل الذين وضعوا ثقتهم في "Mohrah's Lab". هذا الوسام يعبر عن روح المبادرة لديك، واهتمامك بمواكبة الأدوات التعليمية الحديثة والمتطورة.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 نصيحة: قم بتصوير إنجازاتك ومشاركتها مع زملائك لتحفيزهم على التعلم!")


elif display_page == "👥 Community Corner":
    st.markdown("## 👥 Community Corner: Ask & Learn")
    st.write("هذا الركن مخصص لتبادل الخبرات والاستفسارات بين الطلاب. لا تتردد في طرح أي سؤال!")
    
    with st.expander("❓ طرح سؤال جديد / Ask a Question"):
        with st.form("q_form", clear_on_submit=True):
            q_name = st.text_input("الاسم / Name:")
            q_text = st.text_area("سؤالك / Your Question:")
            q_file = st.file_uploader("إرفاق صورة أو ملف / Attach Image or File:", type=["png", "jpg", "jpeg", "pdf", "zip"])
            if st.form_submit_button("نشر السؤال / Post"):
                if q_name and q_text:
                    post_question(q_name, q_text, q_file)
                    st.success("تم نشر سؤالك مع المرفقات! انتظر إجابة زملائك.")
                    st.rerun()
    
    st.markdown("### 💬 الأسئلة الحالية / Current Discussions")
    questions = load_questions() # Load fresh from file
    for q in reversed(questions):
        with st.container():
            st.markdown(f"""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 15px 15px 0 0; border-left: 5px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between;">
                    <b>👤 {q['u']}</b>
                    <span style="font-size: 12px; color: gray;">{q['t']}</span>
                </div>
                <p style="margin-top: 10px; font-size: 18px; color: #1e3a8a;"><b>Q: {q['q']}</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display attachment placeholder
            if "img_name" in q and q["img_name"]:
                st.info(f"📎 Attached: {q['img_name']}")

            # Likes and Reply Button
            col_l, col_r = st.columns([1, 4])
            if col_l.button(f"❤️ {q['likes']}", key=f"like_{q['id']}"):
                add_like(q['id'])
                st.rerun()
            
            with col_r.expander("💬 Replies / الردود"):
                for rep in q['r']:
                    st.markdown(f"""
                    <div style="background-color: #f8fafc; padding: 10px; border-radius: 10px; margin-bottom: 5px; border-right: 3px solid #3b82f6;">
                        <b>{rep['u']}</b>: {rep['m']} <br>
                        <small style="color: gray;">{rep['t']}</small>
                    </div>
                    """, unsafe_allow_html=True)
                
                with st.form(f"reply_form_{q['id']}", clear_on_submit=True):
                    r_name = st.text_input("الاسم:", key=f"rn_{q['id']}")
                    r_msg = st.text_area("ردك:", key=f"rm_{q['id']}")
                    if st.form_submit_button("إرسال الرد"):
                        if r_name and r_msg:
                            add_reply(q['id'], r_name, r_msg)
                            st.success("تم إضافة الرد!")
                            st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)

            
elif display_page == "Contact Developer":
    st.markdown("### 📧 Contact the Developer / تواصل مع المبرمجة")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🏛️ **Academic Email**")
        st.code("451000518@stu.ut.edu.sa")
    with col2:
        st.success("📩 **Personal Email**")
        st.code("mohrah.atiiah@icloud.com")

elif display_page == "📺 Channel Rating":
    st.markdown("### 📺 Rate Our Channel / قيّم قناتنا")
    st.write("شارك رأيك وساعدنا على التحسن!")
    
    with st.form("rating_form", clear_on_submit=True):
        r_name = st.text_input("Name / الاسم:")
        r_stars = st.slider("Rating / التقييم:", 1, 5, 5)
        r_msg = st.text_area("Feedback / تعليقك:")
        if st.form_submit_button("Submit / إرسال"):
            if r_name and r_msg:
                try:
                    rf = "channel_ratings.json"
                    if os.path.exists(rf):
                        with open(rf, "r", encoding="utf-8") as f:
                            ratings = json.load(f)
                    else:
                        ratings = []
                    ratings.append({"u": r_name, "r": r_stars, "m": r_msg, "t": time.strftime("%I:%M %p")})
                    with open(rf, "w", encoding="utf-8") as f:
                        json.dump(ratings, f, ensure_ascii=False, indent=4)
                    st.success("✅ شكراً على تقييمك!")
                    st.rerun()
                except:
                    st.error("Error")
    
    st.markdown("---")
    try:
        if os.path.exists("channel_ratings.json"):
            with open("channel_ratings.json", "r", encoding="utf-8") as f:
                ratings = json.load(f)
            if ratings:
                avg = sum(r["r"] for r in ratings) / len(ratings)
                st.metric("Average Rating", f"{avg:.1f} ⭐")
                for r in reversed(ratings):
                    stars = "⭐" * r["r"] + "☆" * (5 - r["r"])
                    st.markdown(f"**{r['u']}** {stars} ({r['t']})\n\n{r['m']}")
    except:
        pass

elif display_page == "Community Feedback":
    st.markdown("### 💬 Feedback Board / لوحة التعليقات")
    
    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("Name / الاسم:")
        msg = st.text_area("Feedback / التعليق:")
        submit = st.form_submit_button("Post / نشر")
        if submit:
            if name and msg:
                success, subject = save_comment(name, msg)
                if success:
                    st.success("✅ Comment saved! / تم حفظ التعليق بنجاح!")
                    st.session_state.current_page = "Community Feedback"
                    st.rerun()
            else:
                st.error("❌ Please fill in both fields. / يرجى ملء جميع الحقول.")
    
    st.markdown("---")
    st.markdown("### 📊 All Feedback / جميع التعليقات")
    
    comments = load_comments()
    
    if not comments:
        st.info("No feedback yet. Be the first to share your thoughts!")
    else:
        for idx, c in enumerate(reversed(comments)):
            rating = c.get('rating', 0)
            subject = c.get('subject', 'General')
            stars = "⭐" * rating + "☆" * (5 - rating)
            
            st.markdown(f"""
            <div class="comment-box" style="border-left: 5px solid #1e3a8a; background-color: #f0f9ff;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <b>👤 {c['u']}</b> 
                        <span style="font-size: 12px; color: gray;">({c['t']})</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size: 16px;">{stars}</span>
                        <span style="font-size: 12px; color: #7c3aed; font-weight: bold; margin-left: 10px;">📌 {subject if subject else 'General'}</span>
                    </div>
                </div>
                <p style="margin-top: 10px; font-size: 15px; line-height: 1.6;">{c['m']}</p>
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid #e0e0e0;">
                    <small style="color: #666;">Quality Rating: {rating}/5 ⭐</small>
                </div>
            </div>
            """, unsafe_allow_html=True)


elif display_page == "Chapter 1: Introduction to Database Systems":
    st.markdown("## 📚 Chapter 1: Introduction to Database Systems")
    st.info("Comprehensive guide to fundamental database concepts and the DBMS approach.")
    
    # --- 1. Introduction ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">1. Introduction</div>
        <p>A <b>Database</b> is a collection of related data that represents some aspect of the real world (often called the <b>mini-world</b> or Universe of Discourse). A <b>Database Management System (DBMS)</b> is a collection of programs that enables users to create and maintain a database.</p>
        <div class="info-grid">
            <div class="info-item">
                <b>Data:</b> Known facts that can be recorded and have an implicit meaning.
            </div>
            <div class="info-item">
                <b>Database System:</b> The combination of the DBMS software and the data itself.
            </div>
        </div>
        <div class="step-box">
            <b>Core Functionalities:</b>
            <ul>
                <li><b>Defining:</b> Specifying data types, structures, and constraints.</li>
                <li><b>Constructing:</b> Storing the data on some storage medium.</li>
                <li><b>Manipulating:</b> Querying to retrieve data and updating to reflect changes.</li>
                <li><b>Sharing:</b> Allowing multiple users and programs to access the data concurrently.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. An Example ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">2. An Example (UNIVERSITY Database)</div>
        <p>Consider a university environment. The database would store data concerning:</p>
        <table class="summary-table">
            <tr><th>Entities</th><th>Relationships</th></tr>
            <tr><td>STUDENT, COURSE, SECTION, GRADE_REPORT, PREREQUISITE</td><td>Students take sections, Sections are of courses, Courses have prerequisites</td></tr>
        </table>
        <p style="margin-top:15px;">In a traditional <b>File Processing System</b>, each department might have its own files. For example, the Accounting office has student billing files, while the Registrar's office has academic record files. This leads to <b>Data Redundancy</b> and <b>Inconsistency</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- 3. Characteristics of the Database Approach ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">3. Characteristics of the Database Approach</div>
        <p>The database approach differs significantly from traditional file processing:</p>
        <ul>
            <li><b>Self-describing nature:</b> A DBMS catalog stores the description of the database (meta-data), allowing it to work with different databases.</li>
            <li><b>Insulation between programs and data:</b> Also known as <b>Program-Data Independence</b>. Changing data structures doesn't require changing the access programs.</li>
            <li><b>Data Abstraction:</b> A data model hides storage details and provides a conceptual view to users.</li>
            <li><b>Support of multiple views:</b> Different users see different perspectives of the same data.</li>
            <li><b>Sharing and multi-user transaction processing:</b> Allows multiple users to access the database simultaneously while ensuring data integrity via concurrency control.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. Actors on the Scene ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">4. Actors on the Scene</div>
        <p>People whose jobs involve day-to-day use of the database:</p>
        <div class="info-grid">
            <div class="info-item">
                <b>Database Administrators (DBA):</b> Responsible for authorizing access, coordinating use, and acquiring resources.
            </div>
            <div class="info-item">
                <b>Database Designers:</b> Responsible for identifying data to be stored and choosing appropriate structures.
            </div>
            <div class="info-item">
                <b>End Users:</b> People who require access for querying, updating, and reporting (Casual, Naive, Sophisticated, Stand-alone).
            </div>
            <div class="info-item">
                <b>System Analysts & Programmers:</b> Determine requirements and implement canned transactions.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 5. Workers behind the Scene ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">5. Workers behind the Scene</div>
        <p>Those who work to maintain the database system environment but don't use the database itself:</p>
        <ul>
            <li><b>DBMS System Designers and Implementers:</b> Design and implement the DBMS software modules.</li>
            <li><b>Tool Developers:</b> Design and implement tools for modeling, performance monitoring, etc.</li>
            <li><b>Operators and Maintenance Personnel:</b> Responsible for the actual running and maintenance of the hardware and software.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. Advantages of Using the DBMS Approach ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">6. Advantages of Using the DBMS Approach</div>
        <table class="summary-table">
            <tr><th>Advantage</th><th>Description</th></tr>
            <tr><td><b>Controlling Redundancy</b></td><td>Reducing duplication of data to save space and maintain consistency.</td></tr>
            <tr><td><b>Restricting Unauthorized Access</b></td><td>Security and authorization subsystems.</td></tr>
            <tr><td><b>Persistent Storage</b></td><td>Providing storage for program objects.</td></tr>
            <tr><td><b>Inference and Actions</b></td><td>Using rules to trigger actions (Active Databases).</td></tr>
            <tr><td><b>Multiple User Interfaces</b></td><td>GUI, Query Languages, Web interfaces.</td></tr>
            <tr><td><b>Representing Complex Relationships</b></td><td>Linking related data items efficiently.</td></tr>
            <tr><td><b>Enforcing Integrity Constraints</b></td><td>Ensuring data follows business rules.</td></tr>
            <tr><td><b>Backup and Recovery</b></td><td>Ensuring data is not lost after a crash.</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    # --- 7. A Brief History of Database Applications ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">7. A Brief History of Database Applications</div>
        <ul>
            <li><b>Early Days (1960s):</b> Hierarchical and Network models (IMS, IDS).</li>
            <li><b>Relational Revolution (1970s):</b> E.F. Codd introduced the Relational Model; SQL development began.</li>
            <li><b>Object-Oriented Era (1980s-90s):</b> OODBMS for complex data types.</li>
            <li><b>Web & ERP (Late 90s):</b> Databases became the backbone of the internet and enterprise systems.</li>
            <li><b>Big Data & NoSQL (2000s-Present):</b> Handling unstructured data, high velocity, and massive scale (Hadoop, MongoDB).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- 8. When Not to Use a DBMS ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">8. When Not to Use a DBMS</div>
        <p>DBMS involves significant overhead. It may not be appropriate when:</p>
        <div class="step-box">
            <ul>
                <li>High initial investment in hardware, software, and training.</li>
                <li>The overhead of providing security, concurrency control, and recovery is not needed.</li>
                <li>The database and applications are simple and well-defined.</li>
                <li>Real-time requirements cannot be met due to DBMS overhead.</li>
                <li>Multiple-user access is not required.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 2: Database Architecture":
    st.markdown("## 📚 Chapter 2: Database Architecture")
    st.info("Detailed exploration of database system concepts, architectures, and classifications.")
    
    # --- 1. Data Models, Schemas, and Instances ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">1. Data Models, Schemas, and Instances</div>
        <p>Fundamental to the study of database systems is the distinction between the description of the database and the data itself.</p>
        <div class="info-grid">
            <div class="info-item">
                <b>Data Model:</b> A collection of concepts used to describe the structure of a database (data types, relationships, constraints) and operations for manipulating them.
            </div>
            <div class="info-item">
                <b>Database Schema:</b> The description of the database (also called <i>intension</i>). It changes very infrequently.
            </div>
            <div class="info-item">
                <b>Database Instance:</b> The actual data stored at a particular moment (also called <i>state</i> or <i>snapshot</i>). It changes with every update.
            </div>
        </div>
        <div class="step-box">
            <b>Categories of Data Models:</b>
            <ul>
                <li><b>Conceptual (High-level):</b> Close to how users perceive data (e.g., Entity-Relationship Model).</li>
                <li><b>Implementation (Representational):</b> Used by commercial DBMSs (e.g., Relational, Network, Hierarchical).</li>
                <li><b>Physical (Low-level):</b> Describe how data is stored on computer storage media.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. Three-Schema Architecture and Data Independence ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">2. Three-Schema Architecture and Data Independence</div>
        <p>Proposed to separate user applications from the physical database, providing three levels of abstraction:</p>
        <table class="summary-table">
            <tr><th>Level</th><th>Schema</th><th>Description</th></tr>
            <tr><td><b>External</b></td><td>External Schema</td><td>Describes user views; hides the rest of the database from specific user groups.</td></tr>
            <tr><td><b>Conceptual</b></td><td>Conceptual Schema</td><td>Describes the structure of the whole database for all users; hides physical details.</td></tr>
            <tr><td><b>Internal</b></td><td>Internal Schema</td><td>Describes physical storage structure and access paths (e.g., indexes).</td></tr>
        </table>
        <div class="step-box" style="margin-top:20px;">
            <b>Data Independence:</b>
            <ul>
                <li><b>Logical Data Independence:</b> Capacity to change the conceptual schema without changing external schemas or applications.</li>
                <li><b>Physical Data Independence:</b> Capacity to change the internal schema without changing the conceptual schema.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3. Database Languages and Interfaces ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">3. Database Languages and Interfaces</div>
        <div class="info-grid">
            <div class="info-item">
                <b>DDL (Data Definition Language):</b> Used by DBA and designers to define the conceptual and internal schemas.
            </div>
            <div class="info-item">
                <b>DML (Data Manipulation Language):</b> Used for retrievals, insertions, deletions, and updates.
            </div>
        </div>
        <p style="margin-top:15px;"><b>Types of DML:</b></p>
        <ul>
            <li><b>High-level (Non-procedural):</b> Declarative; specifies <i>what</i> data to get (e.g., SQL).</li>
            <li><b>Low-level (Procedural):</b> Record-at-a-time; specifies <i>how</i> to retrieve data (requires loops).</li>
        </ul>
        <div class="step-box">
            <b>DBMS Interfaces:</b>
            <ul>
                <li>Menu-based (for web browsing)</li>
                <li>Forms-based (for naive users like bank tellers)</li>
                <li>Graphical User Interfaces (GUI)</li>
                <li>Natural Language interfaces</li>
                <li>DBA interfaces (for account management and tuning)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. The Database System Environment ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">4. The Database System Environment</div>
        <p>A DBMS is a complex software system. Typical component modules include:</p>
        <ul>
            <li><b>Query Compiler:</b> Parses and optimizes queries.</li>
            <li><b>Runtime Database Processor:</b> Executes the privileged commands.</li>
            <li><b>Data Manager:</b> Handles buffer management and disk I/O.</li>
            <li><b>System Catalog:</b> Stores meta-data (schema descriptions).</li>
        </ul>
        <div class="step-box">
            <b>Database Utilities:</b> Loading, Backup, Reorganization, Performance Monitoring, and Report Generation.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 5. Centralized and Client/Server Architectures ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">5. Centralized and Client/Server Architectures</div>
        <div class="info-grid">
            <div class="info-item">
                <b>Centralized Architecture:</b> DBMS, hardware, and application software all reside on a single machine.
            </div>
            <div class="info-item">
                <b>Client/Server Architecture:</b> Distributes processing between client machines (UI/Apps) and server machines (DBMS).
            </div>
        </div>
        <p style="margin-top:15px;"><b>Multi-tier Architectures:</b></p>
        <ul>
            <li><b>Two-tier:</b> Client (User Interface + Apps) ↔ Server (DBMS).</li>
            <li><b>Three-tier:</b> Client (Web Browser) ↔ Application/Web Server ↔ Database Server (DBMS). Common for web applications.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- 6. Classification of Database Management Systems ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">6. Classification of DBMSs</div>
        <p>DBMSs can be classified based on several criteria:</p>
        <table class="summary-table">
            <tr><th>Criteria</th><th>Categories</th></tr>
            <tr><td><b>Data Model</b></td><td>Relational, Object-oriented, Object-relational, NoSQL (Key-value, Document, Graph), XML.</td></tr>
            <tr><td><b>Number of Users</b></td><td>Single-user vs. Multi-user systems.</td></tr>
            <tr><td><b>Site Distribution</b></td><td>Centralized vs. Distributed (Homogeneous or Heterogeneous).</td></tr>
            <tr><td><b>Cost</b></td><td>Open-source vs. Proprietary commercial systems.</td></tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 3: Entity Relationship Model (ERD)":
    st.markdown("## 📚 Chapter 3: Relational Model Concepts")
    st.info("Comprehensive study of the Relational Model, its notation, constraints, and update operations.")
    
    # --- 1. Relational Model Concepts & Modeling Concepts ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">1. Relational Model Concepts</div>
        <p>The Relational Model was proposed by <b>Dr. E.F. Codd</b> in 1970. It is based on the mathematical concept of a <b>Relation</b> (represented as a table).</p>
        <div class="info-grid">
            <div class="info-item">
                <b>Relation:</b> A table of values. Each row represents a real-world fact (Entity or Relationship).
            </div>
            <div class="info-item">
                <b>Tuple:</b> A row in a relation. Formally, an ordered set of values.
            </div>
            <div class="info-item">
                <b>Attribute:</b> A column header that gives meaning to the data items in that column.
            </div>
            <div class="info-item">
                <b>Domain:</b> A set of atomic values (data types) that an attribute can take.
            </div>
        </div>
        <div class="step-box">
            <b>Formal vs. Informal Terms:</b>
            <table class="summary-table">
                <tr><th>Informal Term</th><th>Formal Term</th></tr>
                <tr><td>Table</td><td>Relation</td></tr>
                <tr><td>Row</td><td>Tuple</td></tr>
                <tr><td>Column Header</td><td>Attribute</td></tr>
                <tr><td>Table Definition</td><td>Relation Schema</td></tr>
                <tr><td>Populated Table</td><td>Relation State</td></tr>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 2. Notation of the Relational Model ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">2. Notation of the Relational Model</div>
        <p>Precise notation is used to define schemas and access data:</p>
        <ul>
            <li><b>Relation Schema:</b> Denoted by <code>R(A1, A2, ..., An)</code>. Example: <code>STUDENT(Name, SSN, Home_phone, Address)</code>.</li>
            <li><b>Tuple Notation:</b> A tuple <i>t</i> is represented as <code>&lt;v1, v2, ..., vn&gt;</code>.</li>
            <li><b>Attribute Access:</b> <code>t[Ai]</code> or <code>t.Ai</code> refers to the value of attribute <i>Ai</i> in tuple <i>t</i>.</li>
            <li><b>Relation State:</b> Denoted by <i>r(R)</i>, representing the set of tuples currently in the relation.</li>
        </ul>
        <div class="step-box">
            <b>Characteristics:</b>
            <ul>
                <li>Tuples in a relation are <b>unordered</b>.</li>
                <li>Values in a tuple are <b>atomic</b> (indivisible).</li>
                <li>A special <b>NULL</b> value represents unknown or inapplicable data.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 3. Relational Constraints ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">3. Relational Constraints</div>
        <p>Constraints are conditions that must hold for all valid relation states. They are crucial for data integrity.</p>
        <div class="info-grid">
            <div class="info-item">
                <b>Key Constraints:</b> A <i>Superkey</i> is a set of attributes that uniquely identifies a tuple. A <i>Key</i> is a minimal superkey. The <i>Primary Key</i> is the chosen key to identify tuples (underlined in schema).
            </div>
            <div class="info-item">
                <b>Entity Integrity:</b> The Primary Key cannot have NULL values. This ensures every tuple can be identified.
            </div>
            <div class="info-item">
                <b>Referential Integrity:</b> Specified between two relations. A <i>Foreign Key</i> in one table must match a Primary Key in another table or be NULL.
            </div>
            <div class="info-item">
                <b>Domain Constraints:</b> Every value in a tuple must be from the domain of its attribute.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. Update Operations & Handling Violations ---
    st.markdown("""
    <div class="learning-card">
        <div class="concept-badge">4. Update Operations & Handling Violations</div>
        <p>There are three basic operations that can change the state of a relation:</p>
        <ol>
            <li><b>INSERT:</b> Adding a new tuple. Can violate any of the four constraints.</li>
            <li><b>DELETE:</b> Removing an existing tuple. Can violate referential integrity (if the deleted tuple is referenced by others).</li>
            <li><b>UPDATE:</b> Changing values in an existing tuple. Can violate any constraint.</li>
        </ol>
        <div class="step-box">
            <b>How Violations are Handled:</b>
            <ul>
                <li><b>Reject:</b> The operation is simply cancelled, and the user is informed of the violation.</li>
                <li><b>Cascade:</b> (For Delete/Update) The change is propagated to all referencing tuples.</li>
                <li><b>Set-NULL / Set-Default:</b> (For Delete/Update) The foreign keys in referencing tuples are set to NULL or a default value.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 4: Enhanced ER Model (EER)":
    st.markdown("## 📚 Chapter 4: Enhanced ER Model (EER)")
    st.info("Content for Chapter 4: Enhanced ER Model (EER) is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>EER Model</h3>
        <ul>
            <li>Specialization</li><li>Generalization</li><li>Aggregation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 5: Relational Model":
    st.markdown("## 📚 Chapter 5: Relational Model")
    st.info("Content for Chapter 5: Relational Model is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Relational Model</h3>
        <ul>
            <li>الجداول (Relations)</li><li>المفاتيح (Keys)</li><li>قيود التكامل (Integrity Constraints)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 6: Relational Algebra":
    st.markdown("## 📚 Chapter 6: Relational Algebra")
    st.info("Content for Chapter 6: Relational Algebra is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Relational Algebra</h3>
        <ul>
            <li>Select (σ)</li><li>Project (π)</li><li>Union</li><li>Difference</li><li>Join</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 7: SQL Basics":
    st.markdown("## 📚 Chapter 7: SQL Basics")
    st.info("Content for Chapter 7: SQL Basics is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>SQL Basics</h3>
        <ul>
            <li>CREATE TABLE</li><li>INSERT</li><li>UPDATE</li><li>DELETE</li><li>SELECT</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 8: Advanced SQL":
    st.markdown("## 📚 Chapter 8: Advanced SQL")
    st.info("Content for Chapter 8: Advanced SQL is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Advanced SQL</h3>
        <ul>
            <li>JOIN</li><li>GROUP BY</li><li>HAVING</li><li>ORDER BY</li><li>Nested Queries</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 9: Functional Dependencies":
    st.markdown("## 📚 Chapter 9: Functional Dependencies")
    st.info("Content for Chapter 9: Functional Dependencies is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Functional Dependencies</h3>
        <ul>
            <li>أنواع الاعتماديات</li><li>Full Dependency</li><li>Partial Dependency</li><li>Transitive Dependency</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 10: Normalization":
    st.markdown("## 📚 Chapter 10: Normalization")
    st.info("Content for Chapter 10: Normalization is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Normalization</h3>
        <ul>
            <li>1NF</li><li>2NF</li><li>3NF</li><li>BCNF</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 11: Transactions and Concurrency Control":
    st.markdown("## 📚 Chapter 11: Transactions and Concurrency Control")
    st.info("Content for Chapter 11: Transactions and Concurrency Control is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Transactions</h3>
        <ul>
            <li>Transaction</li><li>ACID Properties</li><li>Concurrent Execution</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif display_page == "Chapter 12: Database Recovery and Security":
    st.markdown("## 📚 Chapter 12: Database Recovery and Security")
    st.info("Content for Chapter 12: Database Recovery and Security is being loaded...")
    st.markdown("""
    <div class="learning-card">
        <h3>Recovery & Security</h3>
        <ul>
            <li>Recovery</li><li>Backup</li><li>Security and Authorization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
# --- 7. FOOTER ---
st.markdown(f"""
        <div class="footer">
     <p>© 2026 | <b>تطوير وبرمجة: مهره عطيه الجهني</b></p>
    <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">
        © 2026 Mohrah Atiah. All rights reserved. This platform is an original academic project. 
        </p>
    """, unsafe_allow_html=True)
st.sidebar.write("---")
st.sidebar.markdown(f"""
    <div style="background-color: #f0fdf4; padding: 10px; border-radius: 10px; border: 1px solid #bbf7d0; text-align: center;">
        <span style="color: #16a34a; font-weight: bold;">🟢 12 Students Online</span><br>
        <span style="font-size: 12px; color: #16a34a;">Studying right now!</span>
    </div>
""", unsafe_allow_html=True)