import streamlit as st
import time
from PIL import Image

img = Image.open("MSE.png.png")
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
  st.markdown("### Click start exam to start the exam ")
  st.markdown("### Correct answer :  +4 points  :heavy_check_mark:")
  st.markdown("### Wrong answer :  -1 points" :x:)
  st.markdown("### Time: 35:00")
  start = st.button("start exam" ,on_click = start_exam)
else:
  with place.container():
    scince = st.markdown("### Science")
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
    maths = st.markdown("### Maths")
    q11 = st.radio("**Q11)What is 15% of 80?**", ["A) 10","B) 12","C) 15","D) 8"], index = None, key = "q11")    
    st.markdown("---")
    q12 = st.radio("**Q12)If x+7=20, what is the value of 3x?**", ["A) 13","B) 39","C) 60","D) 45"], index = None, key = "q12")    
    st.markdown("---")
    q13 = st.radio("**Q13)Which of the following is a prime number?**", ["A) 9","B) 21","C) 37","D) 51"], index = None, key = "q13")    
    st.markdown("---")
    q14 = st.radio("**Q14)A rectangle has a length of 10 cm and a width of 5 cm. What is its perimeter?**", ["A) 15 cm","B) 50 cm2","C) 30 cm","D) 25 cm"], index = None, key = "q14")    
    st.markdown("---")
    q15 = st.radio("**Q15)What is the measure of the third angle in a triangle if the other two angles measure 45∘ and 65∘ ?**", ["A) 70∘","B) 80∘","C) 90∘","D) 110∘"], index = None, key = "q15")    
    st.markdown("---")
    q16 = st.radio("**Q16)The diameter of a circle is 14 meters. What is its radius?**", ["A) 7 meters","B) 14 meters","C) 28 meters","D) 3.5 meters"], index = None, key = "q16")    
    st.markdown("---")
    q17 = st.radio("**Q17)Simplify the expression: 2(x−3)+5x**", ["A) 7x−3","B) 7x−6","C) 3x−6","D) 7x+6"], index = None, key = "q17")    
    st.markdown("---")
    q18 = st.radio("**Q18)Evaluate the expression 4 ^3 − square root of 49**",["A) 60","B) 57","C) 38","D) 71"], index = None, key = "q18")    
    st.markdown("---")
    q19 = st.radio("**Q19)What is the median of the following set of numbers: 5,2,8,1,4?**",["A) 4","B) 5","C) 20","D) 8"], index = None, key = "q19")    
    st.markdown("---")
    q20 = st.radio("**Q20)A bag contains 3 red marbles and 7 blue marbles. If one marble is drawn at random, what is the probability that it is a red marble?**",["A) 3/7","B) 7/10","C) 3/10","D) 1/3"], index = None, key = "q20")    
    st.markdown("---")
    st.markdown("### Logical")
    st.write("**Q21)In a room, there are three people: Alice, Bob, and Carol. One of them is a truth-teller (always tells the truth), and the other two are liars (always lie).**")
    st.write("**They make the following statements:**")
    st.write("**Alice: Bob is a liar.**")
    st.write("**Bob: Carol is a liar.**")
    st.write("**Carol: I am the truth-teller.**")
    q21 = st.radio("**Who is the truth-teller?**",["A) Alice", "B) Bob", "C) Carol", "D) Cannot be determined"], index = None, key = "q21")    
    st.markdown("---")
    q22 = st.radio("**Q22)Mary have 4 Daughers and all the daughtes have 1 brother.how many children does Mary have?**",["A) 1", "B) 4", "C) 5", "D) 8"], index = None, key = "q22")    
    st.markdown("---")
    q23 = st.radio("**Q23)A farmer has 17 sheep.All but 9 of them run away.How many sheep does the farmer have left?**",["A) 17", "B) 8", "C) 9", "D) 0"], index = None, key = "q23")    
    st.markdown("---")
    q24 = st.radio("**Q24)A plane crashes on the border of India and Pakistan.Where do you bury the survivors**",["A) In India", "B) In Pakistan", "C) In a neutral country", "D) Dont Bury them"], index = None, key = "q24")    
    st.markdown("---")
    q25 = st.radio("**Q25)A pond has flowers that double in number every day.if the pond is compeletey full on the 14th day, on which day was it half full**",["A) 15", "B) 7", "C) 28", "D) 13"], index = None, key = "q25")    
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
  if q11 == "B) 12":
    points += 4
  elif q11 == None:
    points += 0
  else:
    points -= 1
  if q12 == "B) 39":
    points += 4
  elif q12 == None:
    points += 0
  else:
    points -= 1
  if q13 == "C) 37":
    points += 4
  elif q13 == None:
    points += 0
  else:
    points -= 1
  if q14 == "C) 30 cm":
    points += 4
  elif q14 == None:
    points += 0
  else:
    points -= 1
  if q15 == "A) 70∘":
    points += 4
  elif q15 == None:
    points += 0
  else:
    points -= 1
  if q16 == "A) 7 meters":
    points += 4
  elif q16 == None:
    points += 0
  else:
    points -= 1
  if q17 == "B) 7x−6":
    points += 4
  elif q17 == None:
    points += 0
  else:
    points -= 1
  if q18 == "B) 57":
    points += 4
  elif q18 == None:
    points += 0
  else:
    points -= 1
  if q19 == "A) 4":
    points += 4
  elif q19 == None:
    points += 0
  else:
    points -= 1
  if q20 == "C) 3/10":
    points += 4
  elif q20 == None:
    points += 0
  else:
    points -= 1
  if q21 == "B) Bob":
    points += 4
  elif q21 == None:
    points += 0
  else:
    points -= 1
  if q22 == "C) 5":
    points += 4
  elif q22 == None:
    points += 0
  else:
    points -= 1
  if q23 == "C) 9":
    points += 4
  elif q23 == None:
    points += 0
  else:
    points -= 1
  if q24 == "D) Dont Bury them":
    points += 4
  elif q24 == None:
    points += 0
  else:
    points -= 1
  if q25 == "D) 13":
    points += 4
  elif q25 == None:
    points += 0
  else:
    points -= 1
  
  total = points
  with hold.container():
    if hold.button("submit"):
        place.empty()
        hold.empty()
        hold.markdown(f"### you got {total} points")

tmer = st.empty()

timer = 3100
while True:
  with tmer.container():
    time.sleep(1)
    timer -= 1
    st.markdown(timer)
    
  
























