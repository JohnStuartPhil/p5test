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

    # hard copied from churned customer study notebook
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

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* A churned customer typically has a month-to-month contract \n"
        f"* A churned customer typically has fibre optic. \n"
        f"* A churned customer typically doesn't have tech support. \n"
        f"* A churned customer doesn't have online security. \n"
        f"* A churned customer typically has low tenure levels. \n"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price Levels per Variable"):
        sale_price_level_per_variable(df_eda)


# function created using "02 - Churned Customer Study" notebook code - "Variables Distribution by Churn" section
def sale_price_level_per_variable(df_eda):
    target_var = 'SalePrice'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot(df_eda, col, target_var)




# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
def plot(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()




