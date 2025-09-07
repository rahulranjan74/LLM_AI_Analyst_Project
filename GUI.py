import streamlit as st
import downlaod_10k_filings
import LLM_inferencing

st.header("LLM based Financial Analyst")
input_ticker = st.chat_input("Enter company ticker as listed on the US stock exchange.")
if input_ticker:
    st.write(f"Company : {input_ticker}")
    downlaod_10k_filings.sec_filling_downloader(input_ticker)
    st.write(LLM_inferencing.run_inferencing(input_ticker))