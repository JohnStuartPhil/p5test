import streamlit as st
import pandas as pd
from src.data_management import load_telco_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_sale_price)


def page_prospect_body():

    # load predict Sale Price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    sale_price_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    st.write("---")

    
 # Generate Live Data
    # check_variables_for_UI(tenure_features, churn_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    st.button("Run Predictive Sale Price"): sale_price_preciction = predict_sale_price(X_live, sale_price_features, sale_price_pipe, sale_price_labels_map)


def check_variables_for_UI(sale_price_features):
    import itertools

    # The widgets inputs are the features used in all pipelines (tenure, churn, cluster)
    # We combine them only with unique values
    combined_features = set(
        list(
            itertools.chain(sale_price_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # load dataset
    df = load_telco_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 6 features
    col1, col2, col3, col4 = st.columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.selectbox(
            label=feature,
             min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.selectbox(
            label=feature,
             min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
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
             min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    # st.write(X_live)

    return X_live
