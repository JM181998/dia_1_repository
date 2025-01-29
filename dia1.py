import pandas as pd
import streamlit as st

def main():
    st.write("hola")
    st.write("adios")
    df=pd.read_csv("https://raw.githubusercontent.com/R43ed/Data_Visualization/refs/heads/main/summer.csv")
    st.dataframe(df.head())
     
if __name__=="__main__":
    main()
 