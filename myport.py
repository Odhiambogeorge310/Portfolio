import base64
import io
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide", page_icon="⭐")


# --- HELPERS ---
@st.cache_data
def img_to_base64(path, height):
    """Resizes the picture (keeps it light) and returns it as base64 JPEG."""
    img = Image.open(path).convert("RGB")
    new_h = height * 2  # 2x for sharp display
    new_w = int(img.width * new_h / img.height)
    img = img.resize((new_w, new_h))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    return base64.b64encode(buf.getvalue()).decode()


def glide_banner(images, height=120, speed=20, caption=""):
    """Shows ALL images gliding from left to right like an advertisement banner."""
    tags = []
    for p in images:
        try:
            tags.append(
                f'<img src="data:image/jpeg;base64,{img_to_base64(p, height)}" '
                f'style="height:{height}px; margin-right:40px;">'
            )
        except Exception as e:
            st.warning(f"Could not load banner picture '{p}': {e}")
    imgs = "".join(tags)
    html = (
        "<style>"
        ".glide-wrap{overflow:hidden;width:100%;white-space:nowrap;}"
        ".glide-track{display:inline-flex;width:max-content;animation:glide " + str(speed) + "s linear infinite;}"
        ".glide-track:hover{animation-play-state:paused;}"
        "@keyframes glide{from{transform:translateX(-50%);}to{transform:translateX(0);}}"
        "</style>"
        "<div class='glide-wrap'><div class='glide-track'>" + imgs + imgs + "</div></div>"
        "<p style='text-align:center;font-weight:bold;font-size:18px;margin-top:6px;'>"
        + caption + "</p>"
    )
    st.markdown(html, unsafe_allow_html=True)


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

    # --- PAGE HEADER ---
    st.markdown(
        """
        <h1 style='text-align:center;'>GEORGE ODHIAMBO 👋</h1>
        """,
        unsafe_allow_html=True
    )

    # --- TWO COLUMN LAYOUT ---
    c1, c2 = st.columns(2, gap="small")

    with c1:
        st.image("prof.jpeg", width=150, caption="GEORGE ODHIAMBO")
        st.divider()

    with c2:
        st.write("I am a **Data Scientist, ICT Technician, and Technical Mentor**")

    # --- GLIDING BANNER (ADVERT) ---
    glide_banner(
        ["bc.png", "1.jpeg", "2.jpeg", "3.jpeg"],
        height=120,
        speed=30,
        caption="Holiday Teens Coding Bootcamp – Ongoing"
    )

    # --- NAVIGATION MENU (HORIZONTAL) ---
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Dashboards", "Project Links"],
        icons=["person", "bar-chart", "link"],
        orientation="horizontal",
        default_index=0
    )

    # --- PAGE CONTENT ---
    st.write("Coding Classes for Kids – Ongoing. Contact us for more information:  **odhigjoe@gmail.com**,  ☎ +2547 0280 1953  | ☎ +2547 1124 0428")

    if selected == "About Me":
        st.markdown("""
        - 🧑‍💻  I am a Data Scientist, ICT Technician, and Technical Mentor with skills in Python, SQL, Tableau, Power BI, data analysis, data visualization, and interactive dashboard development. I enjoy transforming data into meaningful insights and building practical technology solutions. I am currently working on data analytics and dashboard projects.
        - 🚀💼 Project links: | https://adidasanalytics.streamlit.app/ | https://cocacola-stock-dashboard.streamlit.app/ | https://church-analysis.streamlit.app/ | [Cluster Dash](https://cluster-dash.streamlit.app/) | [School Dashboard](https://analysis-nmeet9epqso2u8t2jwjygx.streamlit.app/) |
        - ❤️ Passionate about *Data Science, Data Analytics, Data Engineering, Machine Learning/Deep Learning, Software Engineering, Computer Vision, and Automation*.
        - 🤖 Also a Senior Instructor offering bootcamps on ScratchJr, Scratch, Python, Artificial Intelligence for kids, HTML, and gamified coding projects.
        - 🏂 I enjoy sports such as football and cycling.
        - 🪧 Contact me at **odhigjoe@gmail.com**,   ☎ +2547 0280 1953
        - 🏠 Based in **Nairobi, Kenya**.
        """)
        st.divider()

    elif selected == "Dashboards":
        c1, c2, c3, c4 = st.columns(4, gap="small")

        with c1:
            st.image("bc.png", width=200, caption="Holiday Teens Coding Bootcamp – Ongoing")
            st.divider()

        with c2:
            st.image("p1.png", width=200)
            st.divider()

        with c3:
            st.image("p6.png", width=200)
            st.divider()

        with c4:
            st.image("p7.png", width=200)
            st.divider()

        c1, c2, c3, c4 = st.columns(4, gap="small")

        with c1:
            st.image("S1.png", width=200, caption="Scratch Code for Kids")
            st.divider()

        with c2:
            st.image("S2.png", width=200)
            st.divider()

        with c3:
            st.image("p3.png", width=200)
            st.divider()

        with c4:
            st.image("p9.png", width=200)
            st.divider()

    elif selected == "Project Links":
        st.subheader("🚀 Project Links")
        st.markdown("""
        Here are some of my deployed Streamlit dashboards and data projects:
        - 📈 **Adidas_Business_Analytics Dashboard:** [adidasanalytics.streamlit.app](https://adidasanalytics.streamlit.app/)
        - 🥤 **CocaCola_Stock_Analysis Dashboard:** [cocacola-stock-dashboard.streamlit.app](https://cocacola-stock-dashboard.streamlit.app/)
        - 📈 **Cluster Dashboard:** [cluster-dash.streamlit.app](https://cluster-dash.streamlit.app/)
        - 📊 **School Performance Analytics:** [analysis-nmeet9epqso2u8t2jwjygx.streamlit.app](https://analysis-nmeet9epqso2u8t2jwjygx.streamlit.app/)
        - 💻 **GitHub Portfolio:** [github.com/odhigjoe](https://github.com/odhigjoe)
        - 🧠 **Data Science Projects:** Coming soon...
        """)
        st.info("Click on the links above to explore my live projects!")
        st.divider()
        st.write("Generated by: George Odhiambo")
        st.divider()


# --- Calling Function ---
web_portfolio()
