import streamlit as st
import pandas as pd
import numpy as np
from datetime import date


st.set_page_config(
    page_title="Joshua Noel Lo's Portfolio",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Home", "Autobiography", "Portfolio", "Skills Dashboard", "Contact"]
)

st.sidebar.markdown("---")
theme = st.sidebar.selectbox("Theme Mood", ["Light", "Dark", "Minimal"])


if section == "Home":
    st.title("Hi, I'm Joshua Noel D. Lo")
    st.subheader("Aspiring Backend Developer")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Welcome!
        This is my **autobiography and portfolio**.
        
        Explore my:
        - Personal story  
        - Projects  
        - Skills  
        - Contact info  
        """)

    with col2:
        st.image(
            r"C:\Users\PC\streamlit_Lo\images\Lo.png",
            caption="Joshua Noel Lo",
            width=350
        )

    st.success("Use the sidebar to navigate!")

# -------------------- AUTOBIOGRAPHY --------------------
elif section == "Autobiography":
    st.header("My Story")

    with st.expander("Early Life"):
        st.write("""
        I grew up curious about how things work.  
        Technology quickly became my favorite playground.  
        I started my tech journey later in college, with my first degree unrelated to technology.
        """)

    with st.expander("Education"):
        st.write("""
        - Degree: BSIT  
        - University: Cebu Institute of Technology - University  
        - Graduation Year: 2022–2026
        """)

    with st.expander("Interests"):
        st.write("""
        - Programming  
        - Cybersecurity  
        - Games (MOBA & Desktop)  
        - UI/UX Design  
        """)

    st.markdown("### Learning Progress")
    st.progress(80)


elif section == "Portfolio":
    st.header("Projects")

    tab1, tab2, tab3 = st.tabs(["GitHub Projects", "Fun"])

    with tab1:
        st.subheader("GitHub Repositories")

        st.markdown("""
        ### My Projects

        - **Streamlit Portfolio Website**  
          👉 https://github.com/juswangs12  

        - **Python Practice & Mini Projects**  
          👉 https://github.com/juswangs12  

        - **Web Development Projects**  
          👉 https://github.com/juswangs12  
        """)

        st.info("All projects are hosted and version-controlled on GitHub.")

    with tab2:
        st.subheader("Fun & Experiments")

        st.markdown("""
        - Exploring Streamlit components  
        - Practicing Python syntax  
        - Learning interactive UI design  
        """)

        st.code(
            "print('Hello, Streamlit!')",
            language="python"
        )

# -------------------- SKILLS DASHBOARD --------------------
elif section == "Skills Dashboard":
    st.header("Skills Overview")

    skills = {
        "Python": 90,
        "Streamlit": 30,
        "SQL": 75,
        "JavaScript": 65,
        "Java Spring Boot": 70,
        "HTML": 50,
        "C": 50
    }

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Skill Levels")
        for skill, level in skills.items():
            st.write(skill)
            st.progress(level)

    with col2:
        st.markdown("### Skill Chart")
        chart_data = pd.DataFrame.from_dict(
            skills, orient="index", columns=["Proficiency"]
        )
        st.bar_chart(chart_data)

    st.metric("Projects Completed", 5, delta=3)
    st.metric("Years of Coding", 3)

# -------------------- CONTACT --------------------
elif section == "Contact":
    st.header("Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            st.success(f"Thanks {name}! I'll get back to you soon.")

    st.markdown("---")
    st.markdown("""
    **Links**
    - GitHub: https://github.com/juswangs12  
    - LinkedIn: https://www.linkedin.com/in/joshua-noel-lo-66963b3a7  
    """)


st.markdown("---")
st.caption(f"© {date.today().year} | Built with Streamlit 🚀")