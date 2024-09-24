import streamlit as st
import pandas as pd
import numpy as np 


st.title("QR based Attendence Application")

def intro():
    import streamlit as st
    st.write("### Introduction")
    st.write("User Manual For the App.")
    st.sidebar.success("Navigate on the Webapp using Drop Down Menu.")
    st.write("This App leverages Computer Vision & Python Libraries.")
    st.write("Made By - Team PyClub")


def cntrl():
    import streamlit as st
    st.write("### Admin Login")
    st.sidebar.success("Administrator Login")
    st.write("Admin Logins to first initialise the attendence list for students,")
    st.write("Admin will upload the attendence name list, in excel format")
    st.write("the data will be scrapped by python libraries to make database out of it.")
    st.write("the database then can be use to initiate qr scanning process...")

def dashbrd():
    st.write("### Student Dashboard")
    st.sidebar.success(" Find out if Your Attendence Percentage is > 75% ? ")
    st.write("this is student's dashboard, where they can see their attendence.")

def bout():
    st.write("### About The Project")
    st.sidebar.success("Find Information About the Creators...")
    st.write("this is the about page for the projects")
    st.write("and we are the faces behind this project.")


page_names_to_funcs = {
    "Introduction": intro,
    "Admin Control": cntrl,
    "Student Dashboard": dashbrd,
    "About": bout
}

demo_name = st.sidebar.selectbox("# Menu", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()



