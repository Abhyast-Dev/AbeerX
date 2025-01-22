import pandas as pd
import streamlit as st
from datetime import date


def color_status(val):
    color = 'red' if val=='Done with' else 'lightgreen'
    return f'background-color: {color}'

exam_det= pd.read_csv("Examdatesandmarks.csv",usecols=['Examination','Starting date'])
exam_marks= pd.read_csv("Examdatesandmarks.csv",usecols=['Examination','English','Hindi', 'Maths','Science','SSt','AI','Percentage'])
def exam_tab1():
    lst_date=[]
    status=[]
    exam_det['Starting date'] = pd.to_datetime(exam_det['Starting date'] ).dt.date
    for i in exam_det['Starting date']:
        lst_date.append(i- date.today() )
    exam_det['Days left']=lst_date
    exam_det['Days left']=exam_det['Days left'].dt.days
    updated = exam_det['Days left'] <0
    
    exam_det.loc[updated, 'Days left'] = 0
    dateid = exam_det['Days left']>0
    messagedays = exam_det.loc[dateid]
   
    
    for i in exam_det['Days left']:
        
         if i>0:
              status.append('Upcoming')
         else:
              status.append('Done with')
    exam_det['Status'] = status
    
    
    st.caption(":green[**Exam dates**]")
    st.dataframe(exam_det.style.applymap(color_status, subset=['Status']),hide_index = True)  
    st.write("Hey Abeer!")
    st.write(":red["+str(messagedays['Examination'].values[0])+"] are approaching. We have :red[",str(messagedays['Days left'].values[0]),"] days to prepare! Go on :red[SET TARGETS], give your BEST!")      
    

def exam_tab2():
     
    st.caption(":green[**Syllabus**]")
    exams = exam_marks['Examination']
    option = st.selectbox("Choose Examination",exams)
    if option == "PT1":
        st.image("PT1_syllabus.png")
    elif option == "PT2":
            st.image("PT2_syllabus.png")
    elif option == "PT2":
            st.image("PT2_syllabus.png")
    elif option == "Half Yearly":
            st.image("Halfyearly_English.png")
            st.image("Halfyearly_Hindi.png")
            st.image("Halfyearly_math,science,ssc.png")
            st.image("Halfyearly_AI.png")
    elif option in ["PreBoard I", "PreBoard II","Board Exams"]:
        tab1,tab2 = st.tabs(["Syllabus","Board Datesheet"])
        with tab1:
            st.image("Pb1and2_English.png")
            st.image("Pb1and2_Hindi.png")
            st.image("Pb1and2_Maths.png")
            st.image("Pb1and2_Science.png")
            st.image("Pb1and2_SscandAI.png")
        with tab2:
            st.image("Boarddatesheet.png")

            
            

            
 
    
def set_Targets():
    st.write("I am In Targets")
def update_Status():
    st.write("I am In status")
def view_Analytics():
    st.write("I am In analytics")





    
    
    
