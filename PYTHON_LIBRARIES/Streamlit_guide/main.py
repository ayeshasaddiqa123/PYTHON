import streamlit as st
import pandas as pd
import time as ts
from datetime import time
st.title("Hye I am boldcase title")
st.subheader("Hye i am sub header")
st.header("I am not in boldcase")
st.text("Hye i am here to write simple text") # print anything
st.markdown("*Hye* ""**Everyone**" )# hye in itatlics and Everyone in boldcase
st.markdown("> Their is no need to have college dgree" )
st.markdown("---" ) #prints line
st.markdown("[Google](https://www.google.com)") #  google's url
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")# for mathematical functions
js={"1":"12,3,4","2":"4,5,6"}
st.json(js) # prints data in json format
code ="""
print(f"{"Enter your daily routine :" :^40}")"""
st.code(code) # prints code as it is written in trople quotes
st.latex(r"\overbrace{AB}")
st.latex(r"a\raisebox{0.25em}{$b$}c")
st.latex(r"\Lambda")
st.write("## We can use it as a markdown ,latex,json,code as well ")
st.metric(label = "Wind speed",value =" 1.4ms⁻¹",delta = "2ms⁻²")

table = pd.DataFrame(
    {
        "Roll no" : [1,2,3,4,5],
        "Name" : ["Ayesha" ,"Amna" ," usman" ,"Irfan" ,"Lanti"]
    }
)
st.table(table) # prints dataframe in table format
st.dataframe(table) # prints in table format but with multiple options available
st.image("D:/PYTHON/PYTHON_LIBRARIES/Streamlit_guide/bac.jpg",caption = "This is my background",width=680)
st.audio("D:/PYTHON/PYTHON_LIBRARIES/Streamlit_guide/audio.mp3")
st.video("D:/PYTHON/PYTHON_LIBRARIES/Streamlit_guide/video.mp4")

def change():
    print(st.session_state.checker)
state = st.checkbox("Checkbox",value = True,on_change=change,key="checker") # makes checkbox
if state :
    st.write("Hi")
else:
    pass  
radio_btn = st.radio("In which country do yo live?",options=("US","UK")) # radio button with multiple options to select
def btn_click():
    st.text("You are on the way.........")
btn = st.button("Click me",on_click=btn_click)
select = st.selectbox("What is your favourit car?",options=("a","b","c"))
  
multi_select = st.multiselect("What is your favourite Tech brand",options= ("Dell","Microsoft","Apple")) # multi selection

st.header("Uploading files")
st.markdown("---")
images=st.file_uploader("Please upload an image",type=["png","jpg"],accept_multiple_files=True)
 
if images is not None :
    for image in images:
        
       st.image(image) 
    
 
st.slider("This is a slider")
val = st.text_input("Enter your course title")
st.text_area("Course Description")
st.date_input("Enter registeration date")
st.time_input("Enter time",value=time(0,0,0))


bar = st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)
    ts.sleep(1)


