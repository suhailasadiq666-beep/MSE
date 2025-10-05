import streamlit as st

if "head" not in st.session_state:
  st.session_state.head = True

def start_exam():
  st.session_state.head = False

st.title("MSE Maths and Scince Exam")
if st.session_state.head:
  st.write("click start exam to start the exam")
else:
  st.write("scince")
  st.radio("what is 2", ["VX","WFD","VFC",]

start = st.button("start exam" ,on_click = start_exam)



