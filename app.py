import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Sadiya Sajid Portfolio", layout="wide")

# ---------- GLOBAL STYLE ---------- #
st.markdown("""
<style>
.profile-pic img {
    border-radius: 14px;
    border: 2px solid #4f6ef7;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.block-container{
padding-top:1rem;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}


/* ---------- NAVBAR FIX ---------- */

.nav-link {
background: transparent !important;
padding:6px 14px !important;
font-size:15px;
font-weight:500;
color:#333 !important;
}

.nav-link:hover{
background:transparent !important;
color:#4f6ef7 !important;
}

.nav-link.active{
background:transparent !important;
border-bottom:2px solid #4f6ef7;
}

.nav-link i{
display:none !important;
}

.nav-item{
margin-right:12px !important;
}

.nav{
justify-content:flex-end !important;
}


/* ---------- BUTTON STYLE ---------- */

.stButton > button {
background: none;
border: none;
color: #4f6ef7;
font-size: 15px;
font-weight: 500;
padding: 6px 0px;
cursor: pointer;
width: auto;
}

.stButton > button:hover {
color: #2f46c7;
text-decoration: underline;
}


/* ---------- PROJECT CARDS ---------- */

.project-card{
padding:22px;
border-radius:14px;
background-color:#ffffff;
border:1px solid #e6e6e6;
box-shadow:0px 4px 10px rgba(0,0,0,0.08);
transition:all 0.25s ease;
min-height:180px;
}

.project-card:hover{
transform:translateY(-6px);
box-shadow:0px 10px 22px rgba(0,0,0,0.15);
}

.project-title{
font-size:18px;
font-weight:600;
margin-bottom:8px;
}

.project-desc{
font-size:14px;
color:#555;
}


/* ---------- ABOUT CARD ---------- */

.about-card{
padding:25px;
border-radius:12px;
background:#f9fafb;
border:1px solid #e6e6e6;
box-shadow:0 4px 10px rgba(0,0,0,0.05);
}


/* ---------- SKILL TAGS ---------- */

.skill-tag{
display:inline-block;
padding:8px 14px;
margin:6px;
background:#eef2ff;
border-radius:20px;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ---------- #

col1, col2 = st.columns([2,11])

with col1:
    st.markdown("## Sadiya Sajid")

with col2:
    selected = option_menu(
        menu_title=None,
        options=["Home","About","Projects","Education","Experience","Activities","Contact"],
        icons=[None,None,None,None,None,None,None],
        menu_icon=None,
        default_index=0,
        orientation="horizontal"
    )

st.divider()

# ---------- HOME ---------- #

if selected == "Home":

    st.subheader("AI/ML Engineer | Generative AI & NLP | Data Science")

    col1,col2 = st.columns([1,3.5])

    with col1:
        try:
            st.markdown('<div class="profile-pic">', unsafe_allow_html=True)
            st.image("formal.jpeg", width=200)
            st.markdown('</div>', unsafe_allow_html=True)
        except:
            st.warning("Add formals.jpg in project folder")

    with col2:

        st.write("""
<div style="font-size:27px; line-height:1.8;">
MTech Data Science graduate focused on building practical AI systems
that transform data into intelligent applications.

My work combines machine learning, deep learning, and generative AI
to create solutions designed for real-world deployment and decision making.
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.subheader("Portfolio Highlights")

    h1,h2,h3,h4 = st.columns(4)

    h1.metric("Projects","6+")
    h2.metric("ML Models","9+")
    h3.metric("Deployments","3")
    h4.metric("Research Work","2")

    st.divider()

    st.subheader("Selected Work")

    p1,p2,p3 = st.columns(3)

    with p1:
        st.markdown("""
        <div class="project-card">
        <div class="project-title">CommunityOps AI Planner</div>
        <div class="project-desc">
        AI assistant generating structured community event plans automatically.
        </div>
        </div>
        """,unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="project-card">
        <div class="project-title">LeafGuard</div>
        <div class="project-desc">
        Deep learning model detecting potato plant diseases from leaf images.
        </div>
        </div>
        """,unsafe_allow_html=True)

    with p3:
        st.markdown("""
        <div class="project-card">
        <div class="project-title">Insurance Premium Predictor</div>
        <div class="project-desc">
        Machine learning system predicting insurance premium pricing.
        </div>
        </div>
        """,unsafe_allow_html=True)

# ---------- ABOUT ---------- #

if selected == "About":

    st.header("About Me")

    st.markdown("""
<div class="about-card">

Hi, I'm <b>Sadiya Sajid</b>, a data science enthusiast passionate about building intelligent AI systems.

My journey into data science began with curiosity — a fascination with patterns and understanding how data can reveal insights behind complex decisions.

I recently graduated with an <b>MTech in Data Science from Christ University</b>, where my work focused on machine learning, deep learning, and generative AI.

Through my projects and research, I enjoy building intelligent systems that transform raw data into meaningful insights and real-world applications.

</div>
""", unsafe_allow_html=True)

    st.subheader("Key Interests")

    st.markdown("""
<span class="skill-tag">Machine Learning</span>
<span class="skill-tag">Deep Learning</span>
<span class="skill-tag">Generative AI & NLP</span>
<span class="skill-tag">Data-Driven Systems</span>
""",unsafe_allow_html=True)

    st.subheader("Technical Skills")

    st.markdown("**Programming**")

    st.markdown("""
<span class="skill-tag">Python</span>
<span class="skill-tag">SQL</span>
""",unsafe_allow_html=True)

    st.markdown("**Machine Learning**")

    st.markdown("""
<span class="skill-tag">Random Forest</span>
<span class="skill-tag">XGBoost</span>
<span class="skill-tag">KNN</span>
<span class="skill-tag">Logistic Regression</span>
<span class="skill-tag">Decision Trees</span>
""",unsafe_allow_html=True)

    st.markdown("**Data & Visualization**")

    st.markdown("""
<span class="skill-tag">Pandas</span>
<span class="skill-tag">NumPy</span>
<span class="skill-tag">Power BI</span>
<span class="skill-tag">Matplotlib</span>
<span class="skill-tag">Seaborn</span>
""",unsafe_allow_html=True)

    st.markdown("**Tools & Deployment**")

    st.markdown("""
<span class="skill-tag">Streamlit</span>
<span class="skill-tag">FastAPI</span>
<span class="skill-tag">Docker</span>
<span class="skill-tag">Git</span>
""",unsafe_allow_html=True)

# ---------- PROJECTS ---------- #

if selected == "Projects":

    # ---------- SESSION STATE ---------- #
    if "project_view" not in st.session_state:
        st.session_state.project_view = "list"

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = None


    # ---------- CSS ---------- #
    st.markdown("""
<style>
div.stButton > button {
    background: none;
    border: none;
    color: #4f6ef7;
    padding: 0;
    font-size: 14px;
    cursor: pointer;
}

div.stButton > button:hover {
    color: #2c4be0;
}
</style>
""", unsafe_allow_html=True)
    st.markdown("""
    <style>

    .project-card {
        padding:22px;
        border-radius:16px;
        background:#ffffff;
        border:1px solid #e6e6e6;
        box-shadow:0 6px 18px rgba(0,0,0,0.08);
        transition:0.3s;
        margin-bottom:10px;
    }

    .project-card:hover {
        transform: translateY(-6px);
        box-shadow:0 12px 28px rgba(0,0,0,0.15);
    }

    .project-title {
        font-size:18px;
        font-weight:600;
        margin-bottom:6px;
    }

    .project-desc {
        font-size:14px;
        color:#444;
        margin-bottom:8px;
    }

    .project-tech {
        font-size:13px;
        color:#666;
        margin-bottom:14px;
    }

    .project-links a {
        display:inline-block;
        padding:6px 12px;
        margin-right:8px;
        border-radius:8px;
        font-size:13px;
        text-decoration:none;
        color:#4f6ef7;
        border:1px solid #4f6ef7;
        transition:0.2s;
    }

    .project-links a:hover {
        background:#4f6ef7;
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------- PROJECT DATA ---------- #
    projects = {

        "community": {
            "title": "CommunityOps AI Planner",
            "short": "GenAI-powered event planning assistant",
            "tech": "LLM, Groq API, Streamlit",
            "github": "https://github.com/sadiya005/community-event-ai",
            "live": "https://communityio.streamlit.app/",
            "details": """
### 📌 Problem
Community event planning is often unstructured and fragmented, with ideas scattered across chats, documents, and spreadsheets. This leads to poor coordination, missed tasks, and last-minute execution stress.

### 💡 Solution
Developed a Generative AI-powered system that transforms simple event prompts into structured, execution-ready plans, enabling communities to move from idea to action efficiently.

### ⚙️ Approach
• Integrated Groq LLM API for fast and context-aware plan generation  
• Engineered structured prompts to produce consistent, actionable outputs instead of generic text  
• Implemented regeneration logic to support iterative refinement  
• Designed event readiness scoring with visual insights to evaluate execution feasibility  

### 🚀 Key Features
• Automated generation of timelines, logistics, and role assignments  
• Event readiness scoring with visual feedback  
• Exportable structured plans for real-world usage  
• Interactive UI designed for non-technical users  

### 🧠 Tech Stack
Python, Streamlit, Groq LLM API, Matplotlib

### 📊 Impact
Significantly reduced manual planning effort and improved clarity in execution, enabling faster and more organized event coordination.

### 🔮 Future Scope
Role-based collaboration, calendar integration, and advanced analytics
            """
        },

        "leafguard": {
            "title": "LeafGuard",
            "short": "Deep learning potato disease detection",
            "tech": "CNN, FastAPI, Docker",
            "github": "https://github.com/sadiya005/potato_disease_detection_system",
            "live": "https://leafguard-full.onrender.com/",
            "details": """
### 📌 Problem
Farmers often rely on manual inspection to detect plant diseases, which is time-consuming and prone to error. Lack of early detection leads to delayed treatment, increased crop damage, and reduced agricultural yield.

### 💡 Solution
Developed an end-to-end deep learning system that enables real-time detection of potato leaf diseases using image inputs, making disease identification faster and more accessible.

### ⚙️ Approach
• Built a CNN-based classification model to detect Healthy, Early Blight, and Late Blight conditions  
• Designed an image preprocessing pipeline including resizing, normalization, and validation for consistent input quality  
• Developed a FastAPI backend to serve predictions with confidence scores  
• Created a Streamlit interface for real-time interaction via image upload and camera input   

### 🚀 Key Features
• Real-time disease detection using uploaded or captured images  
• Confidence-aware predictions with safer decision handling  
• Interactive and user-friendly interface for non-technical users  
• Fully containerized deployment using Docker for scalability   

### 🧠 Tech Stack
Python, TensorFlow/Keras, FastAPI, Streamlit, Docker, NumPy, Pillow

### 📊 Impact
Provides an accessible AI-powered solution for early disease detection, helping reduce crop loss and enabling faster agricultural decision-making.

### 🔮 Future Scope
Extend support to multiple crops and diseases, improve model robustness with diverse datasets, and integrate environmental factors for enhanced prediction accuracy.
            """
        },

        "insurance": {
            "title": "Insurance Premium Predictor",
            "short": "ML-based decision support system",
            "tech": "XGBoost, FastAPI",
            "github": "https://github.com/sadiya005/medical_insurance",
            "live": "https://insurance-prediction-latest.onrender.com",
            "details": """
### 📌 Problem
Insurance premium calculation is often complex and lacks transparency, making it difficult for customers to understand pricing factors. Manual estimation processes can also be inefficient and inconsistent.

### 💡 Solution
Developed a machine learning-based system that predicts insurance premiums while providing insights into key factors influencing the cost, enabling more transparent and data-driven decision-making.

### ⚙️ Approach
• Conducted exploratory data analysis (EDA) to identify patterns, trends, and outliers in the dataset  
• Performed feature engineering and preprocessing, including encoding and validation of user inputs  
• Trained an XGBoost model with cross-validation and hyperparameter tuning for robust performance  
• Built a FastAPI backend and Streamlit interface for real-time user interaction and prediction  

### 🚀 Key Features
• Real-time premium prediction based on user inputs  
• Input validation to ensure reliable and accurate predictions  
• Visualization of user premium compared to population trends  
• End-to-end deployed system with interactive interface  

### 🧠 Tech Stack
Python, Pandas, NumPy, XGBoost, Scikit-learn, FastAPI, Streamlit, Docker

### 📊 Impact
Enhances transparency in insurance pricing and enables users to understand cost-driving factors, supporting better financial and policy decisions.

### 🔮 Future Scope
Enhances transparency in insurance pricing and enables users to understand cost-driving factors, supporting better financial and policy decisions.            """
        },

        "asteroid": {
            "title": "Hazardous Asteroid Prediction",
            "short": "ML prediction of near-earth object risks",
            "tech": "ML, Ensemble Models",
            "kaggle": "https://www.kaggle.com/code/sadiyasajid/hazardous-neo-prediction",
            "github": "",
            "live": "",
            "details": """
### 📌 Problem
Near-Earth Objects (NEOs), particularly asteroids, pose potential threats to Earth, but identifying hazardous ones among thousands of observations is complex. Traditional monitoring relies heavily on manual analysis and predefined thresholds, which may not scale efficiently.

### 💡 Solution
Developed a machine learning-based classification system to identify potentially hazardous asteroids using historical NASA data, enabling faster and more scalable risk assessment.

### ⚙️ Approach
• Processed a large-scale NASA dataset (1910–2024) containing 338K+ observations and multiple orbital features  
• Performed data preprocessing, normalization, and feature analysis to handle variability and imbalance  
• Implemented multiple models including Logistic Regression, KNN, SVM, and Decision Tree for baseline comparison  
• Applied ensemble techniques (Random Forest, XGBoost, CatBoost, Voting Classifier) to improve predictive performance  
• Evaluated models using precision, recall, and F1-score to ensure balanced classification  

### 🚀 Key Features
• Comparative analysis across multiple machine learning and ensemble models  
• Identification of key factors influencing asteroid hazard classification  
• Improved prediction performance using ensemble learning techniques  
• Application of data science in a real-world space safety context  

### 🧠 Tech Stack
Python, Pandas, Scikit-learn, XGBoost, CatBoost, Matplotlib

### 📊 Impact
Achieved ~92% accuracy using Random Forest, demonstrating the effectiveness of ensemble models in identifying hazardous asteroids and supporting faster risk assessment.

### 🔮 Future Scope
Integrate real-time astronomical data streams, explore deep learning models for improved prediction, and extend the system for continuous monitoring in space research applications.            """
        }

    }

    order = ["community", "leafguard", "insurance", "asteroid"]



    # ---------- LIST VIEW ---------- #
    if st.session_state.project_view == "list":

        st.header("Projects")

        cols = st.columns(2)

        for i, key in enumerate(order):
            p = projects[key]

            with cols[i % 2]:

                links_html = ""

                if p.get("github"):
                    links_html += f'<a href="{p["github"]}" target="_blank">💻 GitHub</a>'

                if p.get("kaggle"):
                    links_html += f'<a href="{p["kaggle"]}" target="_blank">📊 Kaggle</a>'

                if p.get("live"):
                    links_html += f' <a href="{p["live"]}" target="_blank">🔗 Live</a>'

                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{p['title']}</div>
                    <div class="project-desc">{p['short']}</div>
                    <div class="project-tech">Tech: {p['tech']}</div>
                    <div class="project-links">{links_html}</div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("View Details →", key=f"detail_{key}"):
                    st.session_state.project_view = "detail"
                    st.session_state.selected_project = key
                    st.rerun()


    # ---------- DETAIL VIEW ---------- #
    elif st.session_state.project_view == "detail":

        key = st.session_state.selected_project
        p = projects[key]

        if st.button("← View All Projects"):
            st.session_state.project_view = "list"
            st.rerun()

        st.header(p["title"])

        st.markdown(f"**Tech Stack:** {p['tech']}")

        st.markdown(p["details"])

        if key == "asteroid":
            st.info("🔒 Full implementation available upon request (restricted due to academic research work).")

        st.divider()

        col1, col2, col3 = st.columns(3)

        # GitHub
        if p.get("github"):
            col1.link_button("💻 GitHub" ,p["github"])

        # Kaggle
        if p.get("kaggle"):
            col2.link_button("📊 Kaggle", p["kaggle"])

        # Live
        if p.get("live"):
            col3.link_button("🔗 Live App", p["live"])
# ---------- EXPERIENCE ---------- #

if selected == "Experience":

    st.header("Professional Experience")

    st.markdown("""
    <style>

    .timeline{
        border-left:3px solid #4f6ef7;
        margin-left:10px;
        padding-left:25px;
    }

    .exp-card{
        padding:22px;
        border-radius:14px;
        background:#ffffff;
        border:1px solid #e6e6e6;
        box-shadow:0px 4px 10px rgba(0,0,0,0.08);
        margin-bottom:30px;
        position:relative;
    }

    .exp-card:before{
        content:'';
        width:14px;
        height:14px;
        background:#4f6ef7;
        border-radius:50%;
        position:absolute;
        left:-34px;
        top:26px;
    }

    .exp-role{
        font-size:18px;
        font-weight:600;
    }

    .exp-company{
        font-size:14px;
        color:#666;
        margin-bottom:4px;
    }

    .exp-date{
        font-size:13px;
        color:#888;
        margin-bottom:10px;
    }

    .exp-tech{
        font-size:13px;
        color:#4f6ef7;
        margin-bottom:12px;
        font-weight:500;
    }

    .exp-desc{
        font-size:14px;
        color:#444;
        line-height:1.6;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    # -------- SUPERCHAT INTERNSHIP -------- #

    st.markdown("""
    <div class="exp-card">

    <div class="exp-role">Artificial Intelligence Engineer Intern</div>

    <div class="exp-company">Superchat LLC · Remote</div>

    <div class="exp-date">Sep 2024 – Mar 2025</div>

    <div class="exp-tech">
    Tech Stack: Python • BLIP • HuggingFace • FastAPI • Streamlit
    </div>

    <div class="exp-desc">

    • Built an AI-powered <b>image captioning system using the BLIP model</b> to automatically generate descriptive captions for images.<br>

    • Optimized model inference performance, reducing response time from <b>8–12 seconds to 6–8 seconds</b> for improved real-time usability.<br>

    • Integrated and deployed the model into the <b>SuperChat platform</b>, enabling automated caption generation within the application.<br>

    • Improved inference efficiency to support <b>scalable real-time AI systems</b>.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # -------- MENTORNESS INTERNSHIP -------- #

    st.markdown("""
    <div class="exp-card">

    <div class="exp-role">Data Analyst Intern</div>

    <div class="exp-company">Mentorness · Remote</div>

    <div class="exp-date">Jun 2024 – Jul 2024</div>

    <div class="exp-tech">
    Tech Stack: SQL • Python • Power BI • Pandas • Data Visualization
    </div>

    <div class="exp-desc">

    • Performed <b>data extraction, transformation, and analysis</b> using SQL and Python to process structured datasets.<br>

    • Developed <b>interactive Power BI dashboards</b> to visualize business metrics and key performance indicators.<br>

    • Conducted <b>exploratory data analysis (EDA)</b> to identify patterns, trends, and insights within datasets.<br>

    • Presented insights through clear visualizations and <b>data storytelling techniques</b>.

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- EDUCATION ---------- #

if selected == "Education":

    st.header("Education")

    st.markdown("""
    <style>

    .timeline{
        border-left:3px solid #4f6ef7;
        margin-left:10px;
        padding-left:25px;
    }

    .edu-card{
        padding:22px;
        border-radius:14px;
        background:#ffffff;
        border:1px solid #e6e6e6;
        box-shadow:0px 4px 10px rgba(0,0,0,0.08);
        margin-bottom:30px;
        position:relative;
    }

    .edu-card:before{
        content:'';
        width:14px;
        height:14px;
        background:#4f6ef7;
        border-radius:50%;
        position:absolute;
        left:-34px;
        top:26px;
    }

    .edu-degree{
        font-size:18px;
        font-weight:600;
    }

    .edu-school{
        font-size:14px;
        color:#666;
        margin-bottom:4px;
    }

    .edu-date{
        font-size:13px;
        color:#888;
        margin-bottom:10px;
    }

    .edu-cgpa{
        font-size:14px;
        color:#4f6ef7;
        margin-bottom:10px;
        font-weight:500;
    }

    .edu-desc{
        font-size:14px;
        color:#444;
        line-height:1.6;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    # ----- MTECH ----- #

    st.markdown("""
    <div class="edu-card">

    <div class="edu-degree">Master of Technology in Data Science</div>

    <div class="edu-school">Christ University</div>

    <div class="edu-date">2023 – 2025</div>

    <div class="edu-cgpa">CGPA: 9.1</div>

    <div class="edu-desc">

    Focus Areas: Machine Learning, Deep Learning, Data Mining, Statistical Modeling, Artificial Intelligence.  
    <b>Thesis / Final Year Project:</b> Comparative Analysis of Hazardous Near Earth Objects using Machine Learning.

    </div>

    </div>
    """, unsafe_allow_html=True)

    # ----- BACHELORS ----- #

    st.markdown("""
    <div class="edu-card">

    <div class="edu-degree">Bachelor of Engineering in Computer Science and Engineering</div>

    <div class="edu-school">Rajiv Gandhi Institute of Technology</div>

    <div class="edu-date">2019 – 2023</div>

    <div class="edu-cgpa">CGPA: 8.3</div>

    <div class="edu-desc">

    Core Coursework: Data Structures, Algorithms, Database Systems, Operating Systems, Computer Networks.  
    <b>Final Year Project:</b> Movable Smart Road Divider (IoT-based solution for smart traffic management).

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ACTIVITIES ---------- #

if selected == "Activities":

    st.header("Activities & Achievements")

    st.markdown("""
    <style>
    .timeline{
        border-left:3px solid #4f6ef7;
        margin-left:10px;
        padding-left:25px;
    }

    .activity-card{
        padding:20px;
        border-radius:14px;
        background:#ffffff;
        border:1px solid #e6e6e6;
        box-shadow:0 4px 10px rgba(0,0,0,0.08);
        margin-bottom:25px;
        position:relative;
    }

    .activity-card:before{
        content:'';
        width:14px;
        height:14px;
        background:#4f6ef7;
        border-radius:50%;
        position:absolute;
        left:-34px;
        top:20px;
    }

    .activity-title{
        font-size:16px;
        font-weight:600;
        margin-bottom:4px;
    }

    .activity-desc{
        font-size:14px;
        color:#444;
        line-height:1.5;
    }

    .activity-meta{
        font-size:13px;
        color:#666;
        margin-bottom:6px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    # ----- PUBLICATIONS ----- #
    with st.expander("Publications", expanded=True):
        st.markdown("""
        <div class="activity-card">
            <div class="activity-title">Machine Learning & Ensemble Models for Hazardous Asteroids Prediction – Springer (Scopus), IDSCS, July 2025</div>
            <div class="activity-meta">Tech: Python, ML, Ensemble Models</div>
            <div class="activity-desc">
            Developed and evaluated ensemble machine learning models to accurately classify hazardous near-earth objects using real-world NASA data.<br>
            🔗 <a href="https://link.springer.com/chapter/10.1007/978-981-96-4883-2_12" target="_blank">Read Paper</a>
            </div>
        </div>

        <div class="activity-card">
            <div class="activity-title">Movable Smart Road Divider – IJSREM, Apr 2023</div>
            <div class="activity-meta">Tech: IoT, Embedded Systems</div>
            <div class="activity-desc">
            IoT-based smart traffic divider system for dynamic road management.<br>
            🔗 <a href="https://ijsrem.com/download/movable-smart-road-divider/" target="_blank">Read Paper</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ----- HACKATHONS ----- #
    with st.expander("Hackathons / Competitions", expanded=False):
        st.markdown("""
        <div class="activity-card">
            <div class="activity-title">DEV AI Challenge</div>
            <div class="activity-desc">
            Built an AI-powered community planning system that generates optimized solutions based on user needs and real-world constraints.<br>
            🔗 <a href="https://communityio.streamlit.app/" target="_blank">View Submission</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ----- AWARDS ----- #
    with st.expander("Awards & Recognition", expanded=False):
        st.markdown("""
        <div class="activity-card">
            <div class="activity-title">Google Cloud Challenge – Legend Tier</div>
            <div class="activity-desc">
            Achieved <b>Legend Tier</b> and received exclusive swags for outstanding performance in cloud challenges.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Optional image
        try:
            st.image("swags.jpg", width=1000)
        except:
            st.info("Add swag image if available")

    # ----- CERTIFICATIONS ----- #
    with st.expander("Certifications", expanded=False):
        st.markdown("""
        <div class="activity-card">
            <div class="activity-title">British Airways - Data Science Job Simulation</div>
            <div class="activity-desc">
            Completed real-world tasks including web scraping and customer purchase prediction.
            </div>
        </div>

        <div class="activity-card">
            <div class="activity-title">Tata Group - Data Visualization</div>
            <div class="activity-desc">
            Transformed business data into actionable insights using visualization.
            </div>
        </div>

        <div class="activity-card">
            <div class="activity-title">HackerRank - SQL</div>
            <div class="activity-desc">
            Demonstrated proficiency in SQL and database querying.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ----- BLOG ----- #
    with st.expander("Blog / Medium", expanded=False):
        st.markdown("""
        <div class="activity-card">
            <div class="activity-title">Hazardous Asteroid Prediction – Medium</div>
            <div class="activity-desc">
            Detailed explanation of ML models used for predicting hazardous near-earth objects.<br>
            🔗 <a href="https://medium.com/@sadiya.sajid135/can-data-science-help-protect-earth-predicting-hazardous-asteroids-with-machine-learning-%EF%B8%8F-63bf8eb52c88" target="_blank">Read Blog</a>
            </div>
        </div>
                    
        <div class="activity-card">
            <div class="activity-title">CommunityOps AI Planner – DEV</div>
            <div class="activity-desc">
            Detailed breakdown of the Community AI Planner, explaining system design, model logic, and decision-making process.<br>
            🔗 <a href="https://dev.to/sadiya_sajid/communityops-ai-planner-turning-scattered-ideas-into-structured-event-plans-with-genai-2mpa" target="_blank">Read Blog</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONTACT ---------- #

import requests

if selected == "Contact":

    st.header("Contact Me")

    st.markdown("### 📩 Get in Touch")
    st.write("Open to AI/ML, Data Science, and GenAI opportunities.")

    # ----- STREAMLIT FORM ----- #
    st.caption("\\* indicates required fields")
    with st.form("contact_form", clear_on_submit=True):

        name = st.text_input("Name * ")
        email = st.text_input("Your Email * ")
        message = st.text_area("Your Message / How can I help? * ")

        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and message:

                response = requests.post(
                    "https://formspree.io/f/mwvrabza",
                    data={
                        "name": name,
                        "email": email,
                        "message": message
                    }
                )

                if response.status_code == 200:
                    st.success("✅ Message sent successfully!")
                else:
                    st.error("❌ Something went wrong. Try again.")

            else:
                st.warning("⚠️ Please fill all fields.")

    st.divider()

    # ----- SOCIAL LINKS ----- #
    st.subheader("🌐 Connect with Me")

    st.markdown("""
    <style>
    .social-container{
        display:flex;
        gap:20px;
        flex-wrap:wrap;
        margin-top:10px;
    }

    .social-card{
        display:flex;
        align-items:center;
        gap:10px;
        padding:12px 18px;
        border-radius:12px;
        border:1px solid #e6e6e6;
        text-decoration:none;
        color:#333;
        font-size:14px;
        transition:0.3s;
        background:#ffffff;
    }

    .social-card:hover{
        background:#f5f7ff;
        transform:translateY(-3px);
    }

    .social-icon{
        width:30px;
        height:30px;
    }
    </style>

    <div class="social-container">

    <a href="https://www.linkedin.com/in/sadiyasajid/" target="_blank" class="social-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" class="social-icon">
    </a>

    <a href="https://github.com/sadiya005" target="_blank" class="social-card">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" class="social-icon">
    </a>

    <a href="https://www.kaggle.com/sadiyasajid" target="_blank" class="social-card">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/kaggle.svg" class="social-icon">
    </a>

    <a href="https://medium.com/@sadiya.sajid135" target="_blank" class="social-card">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/medium.svg" class="social-icon">
    </a>

    <a href="https://dev.to/sadiya_sajid" target="_blank" class="social-card">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/devdotto.svg" class="social-icon">
    </a>

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr style="margin-top:50px;">

<div style="text-align:center; font-size:13px; color:#777;">
© 2026 Sadiya Sajid • All rights reserved
</div>
""", unsafe_allow_html=True)