import streamlit as st

base = "dark"


st.title('Gym Planner')

tab1, tab2 = st.tabs(["Day 1", "Day 2"])
tab2.write("this is tab 2")


tab1.checkbox("Cardio")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Scale", 0, 15,key = "cardio_k")
col2_tab1.number_input("Speed", 0, 10,key = "cardio_2")

tab1.checkbox("Core warmup")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Time [mins]", 0, 15)

tab1.checkbox("Rack pulls")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Rack_Pulls")
col2_tab1.number_input("Reps", 0, 10,key = "Rack_Pulls2")

tab1.checkbox("Barbell Rows")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Barbell")
col2_tab1.number_input("Reps", 0, 10,key = "Barbell2")

tab1.checkbox("Bent over cable row")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Bo_Cable_rows")
col2_tab1.number_input("Reps", 0, 10,key = "Bo_Cable_rows2")

tab1.checkbox("Seated cable row")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Se_Cable_rows")
col2_tab1.number_input("Reps", 0, 10,key = "Se_Cable_rows2")

tab1.checkbox("Biceps Curls")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Bicep_Curls")
col2_tab1.number_input("Reps", 0, 10,key = "Bicep_Curls2")

tab1.checkbox("Side lateral Raise")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Sides")
col2_tab1.number_input("Reps", 0, 10,key = "Sides2")

tab1.checkbox("Back Extensions")
col1_tab1, col2_tab1 = tab1.columns(2)
col1_tab1.number_input("Sets", 0, 15,key = "Back")
col2_tab1.number_input("Reps", 0, 10,key = "Back2")

tab1.button("Store")
