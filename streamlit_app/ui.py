from pathlib import Path
import streamlit as st

def page(title, subtitle, tag):
    st.set_page_config(page_title=title + " | Naga Anweesh Reddy", page_icon="✦", layout="wide")
    st.markdown("""<style>
    .stApp {background:#f6f8fc;}
    .block-container {max-width:1180px;padding-top:2.2rem;padding-bottom:3rem;}
    [data-testid="stSidebar"] {background:#fff;border-right:1px solid #e8ecf4;}
    h1,h2,h3 {letter-spacing:-.035em;}
    .hero {background:linear-gradient(120deg,#101c3e,#343c8c);padding:2.3rem;border-radius:22px;color:white;margin-bottom:1.8rem;}
    .hero h1 {color:white;font-size:2.8rem;margin:.45rem 0;}
    .hero p {color:#d9e1ff;max-width:780px;font-size:1.05rem;}
    .eyebrow {font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:#b8c7ff;}
    [data-testid="stMetric"] {background:white;border:1px solid #e4e9f3;padding:1rem;border-radius:14px;}
    .stButton>button[kind="primary"] {background:#4f46e5;border-color:#4f46e5;}
    </style>""", unsafe_allow_html=True)
    # These values are application constants, never user-provided HTML.
    st.markdown(f'<div class="hero"><div class="eyebrow">{tag} · PROJECT LAB</div><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)
    with st.sidebar:
        st.markdown("### Naga Anweesh Reddy")
        st.caption("AI Developer & Technical Trainer")
        st.markdown("[GitHub portfolio](https://github.com/Arjun1443/Naga-Anweesh-Reddy)")
        st.divider()
    st.caption("Interactive portfolio application · inspect the methodology alongside the result.")

def data_path(filename):
    root = Path(__file__).resolve().parents[1]
    original = root / filename
    return original if original.exists() else root / "data" / filename

def secret(name, default=""):
    import os
    try:
        return st.secrets.get(name, os.getenv(name, default))
    except st.errors.StreamlitSecretNotFoundError:
        return os.getenv(name, default)
