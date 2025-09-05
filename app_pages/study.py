import plotly.express as px
import numpy as np
import pandas as pd
from feature_engine.discretisation import ArbitraryDiscretiser
import streamlit as st
from src.data_management import load_house_price_records_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def study_body():

    # load data
    df = load_house_price_records_data()


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




