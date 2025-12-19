import streamlit as st
import pandas as pd
from supabase import create_client

# Supabase configuration
supabase_url = "https://hzfsuubrxnammebwaotm.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imh6ZnN1dWJyeG5hbW1lYndhb3RtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDMzODEsImV4cCI6MjA4MTYxOTM4MX0.BGVb89liDXpQ_ZC-DWHrA4SPyQ3V4YZwZWRgP2huclk"

supabase = create_client(supabase_url, supabase_key)

# Streamlit UI
st.title("HDFC BANK (Supabase)")

menu = ("REGISTER", "VIEW")
choice = st.sidebar.selectbox("Menu", menu)

# REGISTER
if choice == "REGISTER":
    name = st.text_input("Enter name")
    age = st.number_input("AGE", min_value=18)
    account = int(st.number_input("ACCOUNT NUMBER"))
    bal = st.number_input("BALANCE", min_value=500)
    if st.button("SAVE"):
        try:
            supabase.table("users").insert({
                "name": name,
                "age": age,
                "account": account,
                "balance": bal
            }).execute()
            st.success("User added successfully")
        except Exception as e:
            st.error(f"Error adding user: {e}")

# VIEW - Fixed case sensitivity and added display
if choice == "VIEW":  # Changed from "view" to "VIEW"
    st.subheader("View Users")
    try:
        response = supabase.table("users").select("*").execute()
        
        # Check if data exists
        if response.data:
            df = pd.DataFrame(response.data)
            st.dataframe(df)  # Display the DataFrame
            st.info(f"Total records: {len(df)}")
        else:
            st.warning("No data found. Check if Row Level Security (RLS) is enabled without proper policies [web:26].")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
