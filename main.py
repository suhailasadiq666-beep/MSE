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
  st.radio("What fundamental force is responsible for the attraction between objects with mass?", ["A) Electromagnetic Force","B) Strong Nuclear Force","C) Gravitational Force","D) Weak Nuclear Force"], index = None)
  st.radio("Which organelle is often referred to as the 'powerhouse' of the cell because it generates most of the cell's supply of ATP (Adenosine Triphosphate)?", ["A) Nucleus","B) Mitochondrion","C) Endoplasmic Reticulum","D) Golgi Apparatus"], index = None)    
  





