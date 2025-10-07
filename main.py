import streamlit as st
from PIL import Image

img = Image.open("MSE.png")
st.set_page_config(
  page_title = "MSE Math and Science Exam",
  page_icon = img,
  layout = "wide"
)

if "head" not in st.session_state:
  st.session_state.head = True
if "rev_ans" not in st.session_state:
  st.session_state.rev_ans = False

points = 0
st.title("MSE Maths and Science Exam")


def start_exam():
  st.session_state.head = False

place = st.empty()
hold = st.empty()

  


if st.session_state.head:
  st.write("click start exam to start the exam ")
  st.write("correct answer :  +4 points")
  st.write("wrong answer :  -1 points")
  start = st.button("start exam" ,on_click = start_exam)
else:
  with place.container():
    scince = st.markdown("#### Science")
    q1 = st.radio("**Q1)What fundamental force is responsible for the attraction between objects with mass?**", ["A) Electromagnetic Force","B) Strong Nuclear Force","C) Gravitational Force","D) Weak Nuclear Force"], index = None, key = "q1")
    st.markdown("---")
    q2 = st.radio("**Q2)Which organelle is often referred to as the 'powerhouse' of the cell because it generates most of the cell's supply of ATP (Adenosine Triphosphate)?**", ["A) Nucleus","B) Mitochondrion","C) Endoplasmic Reticulum","D) Golgi Apparatus"], index = None, key = "q2")  
    st.markdown("---")
    q3 = st.radio("**Q3)What is the chemical symbol for the element Gold?**", ["A) Ag","B) Fe","C) Pt","D) Au"], index = None, key = "q3")    
    st.markdown("---")
    q4 = st.radio("**Q4)What process involves the movement of water from the Earth's surface into the atmosphere, primarily as water vapor?**", ["A) Condensation","B) Precipitation","C) Infiltration","D) Evaporation"], index = None, key = "q4")
    st.markdown("---")
    q5 = st.radio("**Q5)Which of the following is the name given to a small, rocky body orbiting the Sun, typically found in the region between Mars and Jupiter?**", ["A) Comet","B) Meteoroid","C) Asteroid","D) Planetoid"], index = None, key = "q5")
    st.markdown("---")
    q6 = st.radio("**Q6)Which particle orbits the nucleus of an atom and has a negative electrical charge?**", ["A) Proton","B) Neutron","C) Electron","D) Photon"], index = None, key = "q6")    
    st.markdown("---")
    q7 = st.radio("**Q7)The Richter scale is used to measure the intensity of which natural event?**", ["A) Tornadoes","B) Hurricanes","C) Volcanic eruptions","D) Earthquakes"], index = None, key = "q7")    
    st.markdown("---")
    q8 = st.radio("**Q8)What is the primary purpose of the ozone layer in the Earth's atmosphere?**", ["A) To regulate the planet's temperature","B) To absorb harmful ultraviolet (UV) radiation","C) To produce water vapor","D) To generate wind currents"], index = None, key = "q8")    
    st.markdown("---")
    q9 = st.radio("**Q9)In biology, what term describes the process by which a plant turns towards a light source?**", ["A) Hydrotropism","B) Thigmotropism","C) Phototropism","D) Gravitropism"], index = None, key = "q9")    
    st.markdown("---")
    q10 = st.radio("**Q10)Which state of matter has a definite volume but no definite shape?**", ["A) Solid","B) Liquid","C) Gas","D) Plasma"], index = None, key = "q10")    
    st.markdown("---")
    
  if q1 == "C) Gravitational Force":
    points += 4
  elif q1 == None:
    points += 0
  else:
    points -= 1
  if q2 == "B) Mitochondrion":
    points += 4
  elif q2 == None:
    points += 0
  else:
    points -= 1
  if q3 == "D) Au":
    points += 4
  elif q3 == None:
    points += 0
  else:
    points -= 1
  if q4 == "D) Evaporation":
    points += 4
  elif q4 == None:
    points += 0
  else:
    points -= 1
  if q5 == "C) Asteroid":
    points += 4
  elif q5 == None:
    points += 0
  else:
    points -= 1
  if q6 == "C) Electron":
    points += 4
  elif q6 == None:
    points += 0
  else:
    points -= 1
  if q7 == "D) Earthquakes":
    points += 4
  elif q7 == None:
    points += 0
  else:
    points -= 1
  if q8 == "B) To absorb harmful ultraviolet (UV) radiation":
    points += 4
  elif q8 == None:
    points += 0
  else:
    points -= 1
  if q9 == "C) Phototropism":
    points += 4
  elif q9 == None:
    points += 0
  else:
    points -= 1
  if q10 == "B) Liquid":
    points += 4
  elif q10 == None:
    points += 0
  else:
    points -= 1
    
  total = points
  with hold.container():
    if hold.button("submit"):
        place.empty()
        hold.empty()
        hold.markdown(f"### you got {total} points")
  
  


  
  
  
    
  



