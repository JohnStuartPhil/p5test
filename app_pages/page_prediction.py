import streamlit as st
import pandas as pd
from src.data_management import load_house_price_records_data
from src.machine_learning.predictive_analysis_ui import (predict_sale_price)



def page_prediction_body():
    
    st.write("### Sale Price predictor Interface")
    st.info(
        f"* The client is interested in predicting potential sale prices. "
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_sale_price(X_live, sale_price_features,
                           sale_price_pipe, sale_price_labels_map)



def DrawInputsWidgets():

    # load dataset
    df = load_house_price_records_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 4 features
    col1, col2, col3, col4 = st.columns(4)
    
    # We are using these features to feed the ML pipeline 

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "GarageArea"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
        )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live
