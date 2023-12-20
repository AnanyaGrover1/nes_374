import streamlit as st

st.set_page_config(
    page_title="Introduction",
    page_icon="🧕🏼",)

IMAGE_URL = "assets/Cairo.jpg"

st.sidebar.success("Explore the project by clicking through the pages above")

def main():

    st.write("# NES374 Final Project 🧕🏼")
    st.write(" ### A Data-driven Exploration of Intimate Partner Violence in the SWANA region")
    st.write(" ##### By Yi Jin Toh and Ananya Grover")

    st.write("""
        Our project is an interactive website taking a digital humanities approach to exploring issues related to intimate partner violence (IPV) in the Southwest Asia and North Africa (SWANA) region. The aim of this project is to provide an accessible, visual representation of the historical changes in factors influencing womens' domestic safety and independence in the SWANA region. We chose to visualize issues related to intimate partner violence because the reading on the institution of bayt al-ta’ ah (the house of obedience) was very eye-opening and close to our hearts. However, this method of interactive data visualization can be extended to any feminist issues. Thus, we also hope our project could serve as a template for future work on feminist data visualization.
    """)

    st.markdown("**Website description:**")
    st.write("""
        For ease of user navigation, this website is broken down into multiple pages. We created a homepage (this page), a page for visualizing the data on intimate partner violence, a page for visualizing contextual data that may increase the risk of intimate partner violence (broken down into the sub-categories of 'Laws and legislations', 'Women's experiences', 'Women's beliefs', and 'Women's decision making freedom'), a page explaining the institution of bayt al-ta’ ah (the house of obedience), as well as a page for all of our sources.
    """)

    st.markdown("**Acknowledgements:**")
    st.write("""
        We are very grateful for NES374 and the various thought-provoking and heartfelt class discussions we had surrounding feminist issues in the SWANA region. We would like to express our deepest thanks to Professor Satyel Larson for hosting a wonderful, well-thought-out, and inclusive experience for us.
    """)

    st.image(IMAGE_URL, caption="Egyptian feminists and prominent activists Nabawiyya Musa, Huda Shaarawi, and Saiza Nabrawi revealing their faces at a Cairo railway station in 1923.")

if __name__ == "__main__":
    main()