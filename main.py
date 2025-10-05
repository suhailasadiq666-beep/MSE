import streamlit as st

if "head" not in st.session_state:
  st.session_state.head = True

def start_exam():
  st.session_state.head = False

start = st.button("start exam" ,on_click = start_exam)

st.title("MSE Maths and Scince Exam")
if st.session_state.head:
  st.header("click start exam to start the exam")



