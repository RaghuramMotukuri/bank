import streamlit as st
import pandas as pd
from supabase import create_client

# Supabase configuration
supabase_url="https://hzfsuubrxnammebwaotm.supabase.co"
supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh6ZnN1dWJyeG5hbW1lYndhb3RtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDMzODEsImV4cCI6MjA4MTYxOTM4MX0.BGVb89liDXpQ_ZC-DWHrA4SPyQ3V4YZwZWRgP2huclk"
supabase = create_client(supabase_url, supabase_key)

# Streamlit UI
st.title("HDFC BANK (Supabase)")

menu = ("REGISTER", "VIEW")
choice = st.sidebar.selectbox("Menu", menu)

# REGISTER
if choice == "REGISTER":
    person_name = st.text_input("Enter Name")
    bank_name = st.text_input("Bank Name")
    account_number = st.text_input("Account Number")
    ifsc_code = st.text_input("IFSC Code")

    if st.button("SAVE"):
        supabase.table("ban").insert({
            "person_name": person_name,
            "bank_name": bank_name,
            "account_number": account_number,
            "ifsc_code": ifsc_code
        }).execute()

        st.success("User added successfully")

# VIEW
if choice == "VIEW":
    st.subheader("View Users")
    data = supabase.table("ban").select("*").execute()
    df = pd.DataFrame(data.data)
    st.dataframe(df)
