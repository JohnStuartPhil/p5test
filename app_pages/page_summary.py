import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* TBC.\n"
        f"* TBC.\n"
        f"* TBC.\n "
        f"* TBC. \n\n" 
        f"**Project Dataset**\n"
        f"* The dataset represents a **House Prices in Iowa** "
        f"containing data about each house "
        f"(such as area size of floors, basement, gargae), "
        f"Years (such as the year that the house was built,) "
        f"and profile (like gender, partner, dependents).")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/JohnStuartPhil/p5test).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price. "
        f"Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.\n "
        f"* 2 - The client is interested in predicting house sales price in Ames, Iowa. "
        )



