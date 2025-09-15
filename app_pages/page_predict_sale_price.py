import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_price_records_data, load_pkl_file
# from src.machine_learning.evaluate_clf import clf_performance


def page_predict_sale_price_body():
    """ Predict Sale Price contents"""

    # load tenure pipeline files
    # version = 'v1'
    # tenure_pipe = load_pkl_file(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/clf_pipeline.pkl")
    # tenure_labels_map = load_pkl_file(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/label_map.pkl")
    # tenure_feat_importance = plt.imread(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/features_importance.png")
    # X_train = pd.read_csv(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/X_train.csv")
    # X_test = pd.read_csv(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/X_test.csv")
    # y_train = pd.read_csv(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/y_train.csv")
    # y_test = pd.read_csv(
    #     f"outputs/ml_pipeline/predict_tenure/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Sale Price")
    # display pipeline training summary conclusions
    st.info(
        f"* TBC "
        f"TBC**: "
        f"TBC. "
        f"TBC. \n"
        f"* TBC, "
        f"TBC. "
        f"TBC.\n"
        f"* TBC "
        f"TBC.")
    st.write("---")

    # # show pipeline steps
    # st.write("* ML pipeline to predict tenure when prospect is expected to churn.")
    # st.write(tenure_pipe)
    # st.write("---")

    # show best features
    st.write("* The features the model was trained and their importance.")
    #st.write(X_train.columns.to_list())
    st.image(sale_price_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    # st.write("### Pipeline Performance")
    # clf_performance(X_train=X_train, y_train=y_train,
    #                 X_test=X_test, y_test=y_test,
    #                 pipeline=tenure_pipe,
    #                 label_map=tenure_labels_map)
