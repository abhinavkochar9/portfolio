# app.py
import streamlit as st
from datetime import date

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Abhinav Kochar — Portfolio",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- THEME TOGGLE ----------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# ---------- GLOBAL STYLE ----------
DARK = """
:root{
  --bg: #0b1020; --panel: #0f162f; --text: #ecf2ff; --muted:#9bb0ff;
  --accent:#7c5cff; --accent2:#00e6a8; --card:#0d1430;
  --border: rgba(255,255,255,0.08); --shadow: 0 10px 30px rgba(0,0,0,.45);
}
"""
LIGHT = """
:root{
  --bg: #f6f8ff; --panel: #ffffff; --text: #16213e; --muted:#5763a7;
  --accent:#5b43ff; --accent2:#00b894; --card:#ffffff;
  --border: rgba(0,0,0,0.06); --shadow: 0 10px 30px rgba(0,0,0,.08);
}
"""
st.markdown(
    f"""
<style>
{DARK if st.session_state.theme=='dark' else LIGHT}

html, body, [data-testid="stAppViewContainer"] {{
  background: radial-gradient(1200px 800px at 10% -10%, var(--panel), var(--bg));
  color: var(--text);
}}
h1,h2,h3,h4,h5,h6 {{ color: var(--text); letter-spacing:.2px; }}
.small {{ color: var(--muted); font-size:.92rem; }}
a {{ color: var(--accent2); text-decoration:none; }}
hr {{ border: 0; height:1px; background: var(--border); }}
.kbd {{
  font: 500 .8rem/1.2 ui-monospace, SFMono-Regular, Menlo, monospace;
  padding:.25rem .45rem; border:1px solid var(--border); border-radius:.5rem; background:var(--panel);
}}
.panel {{
  background: linear-gradient(180deg, var(--panel), color-mix(in oklab, var(--panel), var(--bg) 30%));
  border:1px solid var(--border); border-radius: 20px; padding: 24px; box-shadow: var(--shadow);
}}
.hero {{
  padding: 28px 32px; border-radius: 24px;
  background:
    radial-gradient(1200px 400px at 80% -20%, color-mix(in oklab, var(--accent), transparent 70%), transparent),
    linear-gradient(180deg, color-mix(in oklab, var(--card), var(--bg) 10%), var(--card));
  border: 1px solid var(--border); box-shadow: var(--shadow);
}}
.badge {{
  display:inline-block; padding:.35rem .6rem; border-radius:999px;
  background: color-mix(in oklab, var(--accent), transparent 85%); color: var(--text);
  border: 1px solid var(--border); margin-right:.4rem; margin-bottom:.4rem;
}}
.card {{
  border-radius: 18px; padding:18px; border:1px solid var(--border); background: var(--card);
  transition: transform .15s ease-out, box-shadow .15s ease-out;
}}
.card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow); }}
.grid {{ display:grid; gap:16px; }}
.grid.cols-2 {{ grid-template-columns: repeat(2, minmax(0,1fr)); }}
.grid.cols-3 {{ grid-template-columns: repeat(3, minmax(0,1fr)); }}
@media (max-width: 1200px) {{ .grid.cols-3 {{ grid-template-columns: repeat(2,1fr); }} }}
@media (max-width: 900px)  {{ .grid.cols-2, .grid.cols-3 {{ grid-template-columns: 1fr; }} }}
.footer {{
  text-align:center; color: var(--muted); padding: 16px 0 4px;
}}
.button-row a {{
  display:inline-block; padding:.6rem .9rem; border-radius:12px; margin-right:.5rem; margin-bottom:.5rem;
  border:1px solid var(--border); background: var(--panel);
}}
.kpi {{
  text-align:center; padding:14px 10px; border-radius:14px; border:1px dashed var(--border);
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image(
        "https://avatars.githubusercontent.com/u/9919?s=200&v=4",
        caption="(Replace with your photo/logo URL)", width=110,
    )
    st.title("Abhinav Kochar")
    st.caption("Data Scientist · AI/ML Engineer · CV Researcher")

    nav = st.radio(
        "Navigate",
        ["🏠 Home", "🧠 Research", "🔬 Projects", "🛠 Skills", "🏅 Awards", "📬 Contact"],
        index=0,
    )
    st.write("---")
    c1, c2 = st.columns(2)
    with c1:
        st.button(("☀️ Light" if st.session_state.theme == "dark" else "🌙 Dark"),
                  on_click=toggle_theme, use_container_width=True)
    with c2:
        st.link_button("📄 Resume (PDF)", "https://your-link-to-resume.pdf", use_container_width=True)

    st.write("---")
    st.caption("Quick Links")
    st.markdown(
        """
- 🌐 [Website](https://your-website.com)
- 💼 [LinkedIn](https://linkedin.com/in/abhinavkochar)
- 🐙 [GitHub](https://github.com/abhinavkochar9)
- ✉️ [Email](mailto:abhihk02@gmail.com)
"""
    )

# ---------- DATA (edit here, no code changes needed) ----------
ABOUT = """
I'm a results-driven **Data Scientist & AI/ML Engineer** focused on **Computer Vision, LLMs, Multimodal AI,** and **Quantum ML**.
I build **real-time intelligent systems** end-to-end—from research and modeling to deployment and delightful UX.
"""

HERO_TAGS = [
    "Computer Vision", "LLMs & RAG", "Agentic AI", "Time Series",
    "Quantum ML", "Knowledge Graphs", "AWS", "Streamlit"
]

KPIS = [
    ("2+ yrs", "Data Analytics"),
    ("1+ yr", "Advanced AI Research"),
    ("3", "Tech Awards"),
    ("4+", "Production Projects"),
]

PROJECTS = [
    {
        "title": "Spectra — Stock Forecasting with Quantum ML",
        "year": "2025",
        "blurb": "Quantum-enhanced transformer for NIFTY50 forecasting (79% accuracy, RMSE 0.21). 30-min forward predictions for options.",
        "stack": ["Qiskit", "PyTorch", "Transformers", "Time Series"],
        "links": {"GitHub": "https://github.com/your/spectra", "Demo": "https://your-demo-link"},
    },
    {
        "title": "PoseCorrect — AI-Powered Rehabilitation",
        "year": "2025",
        "blurb": "Real-time pose tracking + RAG-grounded LLM feedback for generalized exercises. Streamlit UI with overlays.",
        "stack": ["MediaPipe", "PyTorch", "LangChain", "FAISS", "Streamlit"],
        "links": {"GitHub": "https://github.com/your/posecorrect"},
    },
    {
        "title": "FluidCloud — Decentralized Personal Cloud",
        "year": "2024",
        "blurb": "Erasure-coded, encrypted shards distributed over user devices via libp2p/IPFS. Privacy-first, self-healing.",
        "stack": ["Rust", "libp2p", "IPFS", "Reed-Solomon"],
        "links": {"GitHub": "https://github.com/your/fluidcloud"},
    },
    {
        "title": "CloudExpense — Serverless Expense Manager",
        "year": "2024",
        "blurb": "AWS Textract OCR → parsing → real-time split with taxes/tips. Streamlit dashboard.",
        "stack": ["AWS", "Textract", "Lambda", "Streamlit", "Flask"],
        "links": {"GitHub": "https://github.com/your/cloudexpense"},
    },
]

RESEARCH = [
    {
        "role": "Graduate Research Assistant",
        "org": "UMKC — Dr. Mei Fu's Lymphedema Research Lab",
        "when": "2024 — Present",
        "bullets": [
            "Real-time CV pose tracking and LLM voice guidance for rehabilitation.",
            "Exercise Knowledge Graph + Graph-RAG for precise instruction delivery.",
            "MCP integration for EMG forecasting and next-posture prediction.",
        ],
    }
]

SKILLS = {
    "AI/ML": ["PyTorch", "Transformers", "scikit-learn", "LLMs", "RAG", "Knowledge Graphs"],
    "Vision": ["OpenCV", "MediaPipe", "YOLO", "Pose Estimation"],
    "Cloud/Dev": ["AWS", "Docker", "GitHub Actions", "FastAPI", "Flask", "Streamlit"],
    "Data": ["Pandas", "NumPy", "Plotly", "SQL", "Tableau", "Power BI"],
    "Quantum": ["Qiskit", "Hybrid Models", "QEC"],
    "Langs": ["Python", "R", "Java", "C", "Rust", "SQL"],
}

AWARDS = [
    ("2nd Prize — Quantum Computing Track", "UMKC Researchathon", "Spring 2025"),
    ("Honorable Mention — Doctoral AI Track", "UMKC Researchathon", "Spring 2025"),
    ("Exemplary Performance Award", "Cloud Computing Course", "2024"),
    ("International Student Ambassador (Selective)", "UMKC", "2024"),
]

# ---------- COMPOSABLE UI HELPERS ----------
def badges(items):
    return " ".join([f"<span class='badge'>{i}</span>" for i in items])

def link_buttons(link_dict):
    html = "<div class='button-row'>"
    for k, v in (link_dict or {}).items():
        html += f"<a href='{v}' target='_blank'>{k} ↗</a>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

# ---------- PAGES ----------
def page_home():
    st.markdown(
        f"""
<div class="hero">
  <h1>👋 Hi, I'm Abhinav.</h1>
  <p class="small">{ABOUT}</p>
  <div style="margin:.5rem 0 1rem 0;">{badges(HERO_TAGS)}</div>
  <div class="grid cols-4" style="margin-top:10px;">
    {"".join([f"<div class='kpi'><div style='font-size:1.2rem;font-weight:700'>{v}</div><div class='small'>{k}</div></div>" for v,k in KPIS])}
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.subheader("Highlights")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
<div class="card">
  <h4>🧠 Multimodal & Agentic AI</h4>
  <p class="small">Vision + LLMs + Signals with RAG and knowledge graphs to deliver intelligent, real-time feedback.</p>
</div>
""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
<div class="card">
  <h4>🔬 Research → Product</h4>
  <p class="small">End-to-end ownership: problem framing, modeling, MLOps, UX, and launch.</p>
</div>
""",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
<div class="card">
  <h4>⚡ Fast, Delightful UX</h4>
  <p class="small">Streamlit apps that feel premium: clean layout, micro-interactions, and accessible defaults.</p>
</div>
""",
            unsafe_allow_html=True,
        )

def page_research():
    st.header("Research")
    for r in RESEARCH:
        with st.container():
            st.markdown(
                f"""
<div class="panel">
  <div style="display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;">
    <div>
      <h3>🧪 {r['role']}</h3>
      <div class="small">{r['org']}</div>
    </div>
    <div class="small">{r['when']}</div>
  </div>
  <ul>
    {''.join([f"<li>{b}</li>" for b in r['bullets']])}
  </ul>
</div>
""",
                unsafe_allow_html=True,
            )

def page_projects():
    st.header("Projects")
    st.markdown('<div class="grid cols-3">', unsafe_allow_html=True)
    for p in PROJECTS:
        stack = badges(p["stack"])
        st.markdown(
            f"""
<div class="card">
  <div style="display:flex;justify-content:space-between;align-items:center;gap:12px;">
    <h4 style="margin:0;">{p['title']}</h4>
    <span class="small">{p['year']}</span>
  </div>
  <p class="small" style="margin-top:.4rem;">{p['blurb']}</p>
  <div style="margin:.4rem 0 .6rem 0;">{stack}</div>
</div>
""",
            unsafe_allow_html=True,
        )
        link_buttons(p.get("links"))
    st.markdown("</div>", unsafe_allow_html=True)

def page_skills():
    st.header("Skills")
    cols = st.columns(3)
    groups = list(SKILLS.items())
    for i, (k, v) in enumerate(groups):
        with cols[i % 3]:
            st.markdown(f"<div class='card'><h4>{k}</h4>{badges(v)}</div>", unsafe_allow_html=True)

def page_awards():
    st.header("Awards & Honors")
    for title, org, when in AWARDS:
        st.markdown(
            f"""
<div class="panel" style="margin-bottom:10px;">
  <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;">
    <div><strong>{title}</strong> — <span class="small">{org}</span></div>
    <div class="small">{when}</div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

def page_contact():
    st.header("Contact")
    st.markdown(
        """
<div class="panel">
  <p class="small">Want to collaborate, discuss research, or hire me? Drop a note below or email me directly.</p>
</div>
""",
        unsafe_allow_html=True,
    )
    with st.form("contact"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your name")
        with c2:
            email = st.text_input("Your email")
        msg = st.text_area("Message", height=140, placeholder="Tell me about your project, role, or idea…")
        submitted = st.form_submit_button("Send ✉️")
        if submitted:
            if name and email and msg:
                # Mailto fallback (replace with your backend/API if desired)
                st.success("Thanks! Opening your email client…")
                st.markdown(
                    f"[Click here if it didn't open](mailto:abhihk02@gmail.com?subject=Portfolio%20Contact%20from%20{name}&body={msg.replace(' ', '%20')})"
                )
            else:
                st.error("Please fill your name, email, and message.")

# ---------- ROUTER ----------
if nav == "🏠 Home":
    page_home()
elif nav == "🧠 Research":
    page_research()
elif nav == "🔬 Projects":
    page_projects()
elif nav == "🛠 Skills":
    page_skills()
elif nav == "🏅 Awards":
    page_awards()
else:
    page_contact()

# ---------- FOOTER ----------
st.write("")
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown(
    f"""
<div class="footer">
  © {date.today().year} Abhinav Kochar · Built with Streamlit · Press <span class="kbd">R</span> to rerun
</div>
""",
    unsafe_allow_html=True,
)