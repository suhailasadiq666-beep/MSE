import streamlit as st

if "head" not in st.session_state:
  st.session_state.head = True
if "rev_ans" not in st.session_state:
  st.session_state.rev_ans = False

points = 0
st.title("MSE Maths and Science Exam")

def start_exam():
  st.session_state.head = False

place = st.empty()

  


if st.session_state.head:
  st.write("click start exam to start the exam ")
  st.write("correct answer :  +4 points")
  st.write("wrong answer :  -1 points")
  start = st.button("start exam" ,on_click = start_exam)
else:
  with place.container():
    scince = st.markdown("#### science")
    q1 = st.radio("What fundamental force is responsible for the attraction between objects with mass?", ["A) Electromagnetic Force","B) Strong Nuclear Force","C) Gravitational Force","D) Weak Nuclear Force"], index = None, key = "q1")
    st.markdown("---")
    q2 = st.radio("Which organelle is often referred to as the 'powerhouse' of the cell because it generates most of the cell's supply of ATP (Adenosine Triphosphate)?", ["A) Nucleus","B) Mitochondrion","C) Endoplasmic Reticulum","D) Golgi Apparatus"], index = None, key = "q2")  
    st.markdown("---")
    q3 = st.radio("What is the chemical symbol for the element Gold?", ["A) Ag","B) Fe","C) Pt","D) Au"], index = None, key = "q3")    
    st.markdown("---")
    q4 = st.radio("What process involves the movement of water from the Earth's surface into the atmosphere, primarily as water vapor?", ["A) Condensation","B) Precipitation","C) Infiltration","D) Evaporation"], index = None, key = "q4")
    st.markdown("---")
    q5 = st.radio("Which of the following is the name given to a small, rocky body orbiting the Sun, typically found in the region between Mars and Jupiter?", ["A) Comet","B) Meteoroid","C) Asteroid","D) Planetoid"], index = None, key = "q5")
    st.markdown("---")
  if q1 == "C) Gravitational Force":
    points += 4
  else:
    points -= 1
  if q2 == "B) Mitochondrion":
    points += 4
  else:
    points -= 1
  if q3 == "D) Au":
    points += 4
  else:
    points -= 1
  if q4 == "D) Evaporation":
    points += 4
  else:
    points -= 1
  if q5 == "C) Asteroid":
    points += 4
  else:
    points -= 1
  total = points
  rev = st.button("submit")
  if rev:
    place.empty()
    with place.container():
      st.write(f"your got {total} points")
  


  
  
  
    
  



