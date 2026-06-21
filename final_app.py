import streamlit as st
import time
import graphviz
import os
import json
import pandas as pd
import google.generativeai as genai
from fpdf import FPDF
import base64

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
        "exam_prep": "🚀 الاستعداد الذكي للاختبارات",
        "res_hub": "📚 مركز المصادر",
        "ach_hall": "🏆 قاعة الإنجازات",
        "community": "👥 ركن المجتمع",
        "dash_title": "🏛️ لوحة تحكم بوابة علوم الحاسب",
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

def create_pdf(title, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, txt=line, align='L')
    return pdf.output(dest='S').encode('latin-1')

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
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; }
    ::-webkit-scrollbar-thumb { background: #1e3a8a; border-radius: 10px; }
    
    /* Dashboard Cards */
    .metric-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-top: 5px solid #1e3a8a; text-align: center;
    }
    
    /* Why Cards */
    .why-card {
        background: #f8fafc; padding: 25px; border-radius: 15px;
        border: 1px solid #e2e8f0; transition: transform 0.3s;
    }
    .why-card:hover { transform: translateY(-5px); border-color: #1e3a8a; }
    
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
        ["Operating Systems: Chapter 1 - Introduction", "Operating Systems: Chapter 2 - Structure & Services", "Operating Systems: Chapter 3 - Process Management", "Operating Systems: Chapter 4 - Threads", "Operating Systems: Chapter 5 - CPU Scheduling", "Operating Systems: Chapter 6 - Synchronization", "Operating Systems: Chapter 7 - Deadlocks", "Operating Systems: Chapter 8 - Memory Management", "Operating Systems: Chapter 9 - Mass-Storage", "Operating Systems: Chapter 10 - File Systems", "🎓 OS Course Completion"]
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
    
    # Dashboard Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>25+</h3><p>{t("total_lessons")}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3>1,200+</h3><p>{t("students")}</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h3>94%</h3><p>{t("success_rate")}</p></div>', unsafe_allow_html=True)

    st.write("---")
    
    # Why Cards Section
    st.markdown(f"<h2 style='text-align: center;'>{t('why_title')}</h2>", unsafe_allow_html=True)
    wcol1, wcol2, wcol3 = st.columns(3)
    with wcol1:
        st.markdown(f"""<div class="why-card"><h3>🧩 {t('source_disp')}</h3>
        <p>نجمع لك كل المصادر الأكاديمية المعتمدة في مكان واحد لتوفير وقتك وجهدك.</p></div>""", unsafe_allow_html=True)
    with wcol2:
        st.markdown(f"""<div class="why-card"><h3>🧠 {t('concept_diff')}</h3>
        <p>تبسيط المفاهيم المعقدة مثل DFA و OS Scheduling باستخدام رسوم تفاعلية وذكاء اصطناعي.</p></div>""", unsafe_allow_html=True)
    with wcol3:
        st.markdown(f"""<div class="why-card"><h3>⚡ {t('instant_eval')}</h3>
        <p>اختبارات ذكية تعطيك تقييماً فورياً وشرحاً مفصلاً لكل إجابة لتعزيز فهمك.</p></div>""", unsafe_allow_html=True)
    
    st.write("---")

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
    
    # Suggestion Chips
    st.markdown("##### 💡 اقتراحات سريعة:")
    cols = st.columns(3)
    suggestions = ["اشرح لي خوارزمية Banker's بالتفصيل", "ما الفرق بين DFA و NFA؟", "كيف يعمل الـ Paging في الذاكرة؟"]
    for i, sug in enumerate(suggestions):
        if cols[i%3].button(sug, key=f"sug_{i}"):
            st.session_state.temp_prompt = sug
            st.rerun()

    st.info("اسألني أي شيء عن نظم التشغيل أو نظرية الحوسبة!")
    
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

            # Handle suggestion click
            prompt = st.chat_input("How can I help you today?")
            if 'temp_prompt' in st.session_state:
                prompt = st.session_state.temp_prompt
                del st.session_state.temp_prompt

            if prompt:
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    
                    system_prompt = """أنت مساعد أكاديمي ذكي لمنصة "مهرة لعلوم الحاسب". 
                    مهمتك هي الإجابة على أسئلة الطلاب في مادتي (نظم التشغيل) و (نظرية الحوسبة) بأسلوب أكاديمي، دقيق، ومنظم. 
                    استخدم مصطلحات علمية واضحة، وإذا لزم الأمر، قدم أمثلة توضيحية أو خطوات برمجية. 
                    اجعل ردودك ملهمة وتشجع الطالب على التعلم."""
                    
                    full_prompt = f"{system_prompt}\n\nسؤال الطالب: {prompt}"
                    
                    try:
                        response = model.generate_content(full_prompt, stream=True)
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
        progress = st.progress(0)
        for i, (q, opts, ans) in enumerate(f_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"fq_u_{i}")
            if u_ans == ans: 
                f_score += 1
                st.success("إجابة صحيحة! 🎉")
            elif u_ans:
                st.error(f"إجابة خاطئة. الإجابة الصحيحة هي: {ans}")
            progress.progress((i + 1) / len(f_qs))
        
        if st.button("Submit Foundations Quiz"):
            st.balloons()
            st.success(f"النتيجة النهائية: {f_score}/10")
        
        st.write("---")
        if st.button("📥 تحميل ملخص الدرس (PDF)"):
            summary = "Theory of Computation Foundations Summary\n\n1. Alphabet: Finite set of symbols.\n2. String: Finite sequence of symbols.\n3. Language: Set of strings.\n4. DFA: Deterministic Finite Automata.\n5. NFA: Non-deterministic Finite Automata."
            pdf_data = create_pdf("Foundations of TOC", summary)
            st.download_button(label="Click to Download PDF", data=pdf_data, file_name="TOC_Foundations.pdf", mime="application/pdf")

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
        progress = st.progress(0)
        for i, (q, opts, ans) in enumerate(dfa_qs):
            u_ans = st.radio(f"{i+1}. {q}", opts, key=f"dq_u_{i}")
            if u_ans == ans: 
                d_score += 1
                st.success("ممتاز! إجابة صحيحة.")
            elif u_ans:
                st.error(f"خطأ. الصحيح هو: {ans}")
            progress.progress((i + 1) / len(dfa_qs))
            
        if st.button("Submit DFA Quiz"):
            st.balloons()
            st.success(f"نتيجتك النهائية: {d_score}/10")
            
        st.write("---")
        if st.button("📥 تحميل ملخص درس DFA (PDF)"):
            summary = "DFA (Deterministic Finite Automata) Summary\n\n1. 5-Tuple: (Q, Sigma, delta, q0, F)\n2. Deterministic: One transition per input symbol.\n3. Recognizes: Regular Languages.\n4. Visual: Double circle for accept states."
            pdf_data = create_pdf("DFA Explorer Summary", summary)
            st.download_button(label="Click to Download PDF", data=pdf_data, file_name="DFA_Summary.pdf", mime="application/pdf")

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