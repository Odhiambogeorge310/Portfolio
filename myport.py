import streamlit as st
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide", page_icon="⭐")

def web_portfolio():
    # --- SIDEBAR CONTENT ---
    st.sidebar.image("pic3.png", width=100, caption="DASHBOARDS")
    st.sidebar.image("gp.png", caption="School Analysis")
    st.sidebar.image("p1.png", caption="CocaCola_Stock_Analysis")
    st.sidebar.image("p6.png")
    st.sidebar.image("p5.png")
    st.sidebar.image("p3.png")
    st.sidebar.image("p4.png")
    st.sidebar.image("p8.png")
    st.sidebar.image("p7.png")


    # --- PAGE HEADER -
    st.markdown(
        """
        <h1 style='text-align:center;'>GEORGE ODHIAMBO 👋</h1>
        """,
        unsafe_allow_html=True
    )

    # --- TWO COLUMN LAYOUT ---
    c1, c2 = st.columns(2, gap="small")

    with c1:
        st.image("pic3.png", width=150, caption="GEORGE ODHIAMBO")
        st.divider()

    with c2:
        st.write("I am a **Data Scientist, ICT Technician, and Technical Mentor**")

    #NAVIGATION MENU (HORIZONTAL) 
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Dashboards", "Project Links"],
        icons=["person", "bar-chart", "link"],
        orientation="horizontal",
        default_index=0
    )

    # --- PAGE CONTENT ---
    st.write("Coding Classes for Kids – Ongoing. Contact us for more information:  **odhigjoe@gmail.com**,  ☎ +2547 0280 1953")
    if selected == "About Me":
        #st.subheader("💈 About Me")
        st.markdown("""
        - 🧑‍💻 🧑‍💻 I am a Data Scientist, ICT Technician, and Technical Mentor with skills in Python, SQL, data analysis, data visualization, and interactive dashboard development. I enjoy transforming data into meaningful insights and building practical technology solutions. I am currently working on data analytics and dashboard projects.
        - 🚀💼 Project links: | [Cluster Dash](https://cluster-dash.streamlit.app/) | [School Dashboard](https://analysis-nmeet9epqso2u8t2jwjygx.streamlit.app/) |
        - ❤️ Passionate about *Data Science, Data Analytics, Data Engineering, Machine Learning/Deep Learning, Software Engineering, 
          Computer Vision, and Automation*.
        - 🤖 Also a Senior Instructor offering bootcamps on ScratchJr, Scratch, Python, Artificial Intelligence for kids, HTML, and gamified coding projects.
        - 🏂 I enjoy sports such as football and cycling.
        - 🪧 Contact me at **odhigjoe@gmail.com**,   ☎ +2547 0280 1953
        - 🏠 Based in **Nairobi, Kenya**.
        """)
        st.divider()

    elif selected == "Dashboards":
        #st.subheader("📊 School Dashboard")
        #st.write("Coding Class for Kids ongoing contact for more info:☎")
        c1, c2,c3,c4 = st.columns(4, gap="small")
        with c1:
            st.image("gp.png", width=200, caption="")
            st.divider()

        with c2:
            st.image("p1.png", width=200, caption="")
            st.divider()

        with c3:
            st.image("p6.png", width=200, caption="")
            st.divider()
        
        with c4:
            st.image("p7.png", width=200, caption="")
            st.divider()

        c1, c2,c3,c4 = st.columns(4, gap="small")
        with c1:
            st.image("S1.png", width=200, caption="Scratch Code for Kids")
            

        with c2:
            st.image("S2.png", width=200, caption="")
            st.divider()

        with c3:
            st.image("p3.png", width=200, caption="")
            st.divider()
        
        with c4:
            st.image("p9.png", width=200, caption="")
            st.divider()
    
    
    elif selected == "Project Links":
        st.subheader("🚀 Project Links")
        st.markdown("""
        Here are some of my deployed Streamlit dashboards and data projects:
        - 📈 **Adidas_Business_Analytics Dashboard:** (https://adidasanalytics.streamlit.app/)emoji
        - 🥤 **CocaCola_Stock_Analysis Dashboard:** (https://cocacola-stock-dashboard.streamlit.app/)
        - 📈 **Cluster Dashboard:** [cluster-dash.streamlit.app](https://cluster-dash.streamlit.app/)
        - 📊 **School Performance Analytics:** [analysis-nmeet9epqso2u8t2jwjygx.streamlit.app](https://analysis-nmeet9epqso2u8t2jwjygx.streamlit.app/)
        - 💻 **GitHub Portfolio:** [github.com/odhigjoe](https://github.com/odhigjoe)
        - 🧠 **Data Science Projects:** Coming soon...
        """)
        st.info("Click on the links above to explore my live projects!")
        st.divider()

# --- Calling Function ---
web_portfolio()
