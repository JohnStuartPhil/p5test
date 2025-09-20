import plotly.express as px
import numpy as np
import pandas as pd
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_house_price_records_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_house_price_study_body():

    # load data
    df = load_house_price_records_data()

    # hard copied from study notebook
    vars_to_study = ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']


    st.write("### House Price Study")
    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price.\n"
        f"* Therefore, the client expects data visualisations of the correlated variables against the sale price to show that. ")
       

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to Churn levels. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Study notebook"
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* TBC \n"
        f"* TBC. \n"
        f"* TBC. \n"
        f"* TBC. \n"
        f"* TBC. \n"
    )

