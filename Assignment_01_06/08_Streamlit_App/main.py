import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Admin dashboard")
upload_file = st.file_uploader("upload a CSV file", type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("filter data")
    columns = df.columns.to_list()
    selected_columns = st.selectbox("filder data by",columns)
    unique_values =  df[selected_columns].unique()
    selected_value = st.selectbox("Select value", unique_values)
    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)
    st.subheader("Plot data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column",columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    else:
        st.write("waiting on file upload...")    