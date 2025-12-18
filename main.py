import streamlit as st
import pandas as pd
from supabase import create_client

#//supabase configuration

supabase_url="https://supabase.co/"
supabase_key="sb_publishable_m9Tal4APplFeDu2kh5gQ5A_jtz9vKJI "

supabase=create_client(supabase_url,supabase_key)

#//streamlit UI

st.title("HDFC BANK(Supabase)")

menu=("REGISTER","VIEW")
choice=st.sidebar.selectbox("Menu",menu)


#//REGISTER

if choice=="REGISTER":
    name=st.text_input("enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("SAVE"):
        supabase.table("users").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":bal}).execute()
        st.success("user added successfully")

#// view student        
if choice == "view":
    st.subheader(" view user")
    data= supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
