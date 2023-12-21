import streamlit as st

st.set_page_config(page_title="Legal Background", page_icon="📝")

st.markdown("# 📝 Legal Background")
st.sidebar.header("Legal Background")

def main():
    st.write("""
        The institution of bayt al-ta’ ah (the house of obedience) was an institution that enabled a husband to obtain a judge's order to forcibly return a wife who had left home without his permission. Such a wife would be legally defined as nashizah (disobedient/rebellious) and lose her eligibility to obtain a judicial divorce. This law has severe consequences considering the dire circumstances under which a woman with little financial independence would have escaped a likely abusive husband, only to lose her only legal pathway to divorcing said husband. In Egypt, the Egyptian Feminist Union (EFU) fought for this institution to be abolished in 1929, but it was not abolished until 38 years later in 1967.
    """)

    st.write("""
Bayt al-ta’ ah, historically practiced in parts of the SWANA region, is a vivid illustration of the systemic challenges women faced and continue to face, which increase the risk and harm from intimate partner violence.
The prolonged existence of such an institution highlights the resistance to women’s emancipation and the glacial pace of reform in the face of embedded gender inequalities. At the same time, the struggle of the EFU and the eventual removal of bayt al-ta’ ah is emblematic of the broader fight and progress toward women's liberation.
In the context of this project, visualizing the data on current laws and attitudes governing women's lives as well as the prevalence of IPV underlines the urgency of ongoing legal reform, social support structures, and educational efforts to mitigate and ultimately eradicate intimate partner violence, leading us to a future where women's rights and safety are unassailable.""")



    # Replace 'URL_TO_CONTEXT_PAGE' with the actual URL path you want to link to
    st.markdown("""
        For more context on factors relevant to female victims of Intimate Partner Violence, click on this link to [visualize context of Intimate Partner Violence in the SWANA region](pages/1_Contextualizing_IPV.py).
    """)

    # Use the actual path to the image, and ensure the image is stored in your app's directory or is hosted online.
    EFU_IMAGE = "assets/EFU.jpg"
    st.image(EFU_IMAGE, caption="Huda Sha‘rawi from the Egyptian Feminist Union, who fought for the abolition of the institution of bayt al-ta’ ah (the house of obedience), meeting with women from various Arab countries.")

if __name__ == "__main__":
    main()