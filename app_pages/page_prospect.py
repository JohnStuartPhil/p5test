import streamlit as st
import pandas as pd
from src.data_management import load_house_price_records_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (predict_sale_price)


def page_prospect_body():

    # # load predict churn files
    # version = 'v1'
    # churn_pipe_dc_fe = load_pkl_file(
    #     f'outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    # churn_pipe_model = load_pkl_file(
    #     f"outputs/ml_pipeline/predict_churn/{version}/clf_pipeline_model.pkl")
    # churn_features = (pd.read_csv(f"outputs/ml_pipeline/predict_churn/{version}/X_train.csv")
    #                   .columns
    #                   .to_list()
    #                   )

    # load predict sale price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/clf_pipeline.pkl")
    sale_price_labels_map = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/label_map.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    # # load cluster analysis files
    # version = 'v1'
    # cluster_pipe = load_pkl_file(
    #     f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    # cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
    #                     .columns
    #                     .to_list()
    #                     )
    # cluster_profile = pd.read_csv(
    #     f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    # st.write("### Prospect Churnometer Interface")
    # st.info(
    #     f"* The client is interested in determining whether or not a given prospect will churn. "
    #     f"If so, the client is interested to know when. In addition, the client is "
    #     f"interested in learning from which cluster this prospect will belong in the customer base. "
    #     f"Based on that, present potential factors that could maintain and/or bring  "
    #     f"the prospect to a non-churnable cluster."
    # )
    st.write("---")

    # Generate Live Data
    # check_variables_for_UI(tenure_features, churn_features, cluster_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_sale_price(X_live, sale_price_features,
                           sale_price_pipe, sale_price_labels_map)


def check_variables_for_UI(sale_price_features):
    import itertools

    # The widgets inputs are the features used in all pipelines (sale_price)
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
    df = load_house_price_records_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 6 features
    col1, col2, col3, col4 = st.columns(4)
    
    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "GrLivAreat"
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

    # st.write(X_live)

    return X_live
