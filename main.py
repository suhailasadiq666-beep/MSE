import streamlit as st

if "head" not in st.session_state:
  st.session_state.head = True

def start_exam():
  st.session_state.head = False

st.title("MSE Maths and Science Exam")
if st.session_state.head:
  st.write("click start exam to start the exam")
  start = st.button("start exam" ,on_click = start_exam)
else:
  st.markdown("#### science")
  st.radio("What fundamental force is responsible for the attraction between objects with mass?", ["A) Electromagnetic Force","B) Strong Nuclear Force","C) Gravitational Force","D) Weak Nuclear Force"])    






