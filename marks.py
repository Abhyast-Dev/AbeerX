import math
import pandas as pd
import streamlit as st
import plotly.express as px


exam_marks= pd.read_csv("Examdatesandmarks.csv",usecols=['Examination','English','Hindi', 'Maths','Science','SSt','AI','Percentage'])
exams = exam_marks.query("Percentage.notnull()")["Examination"]
perc = exam_marks.query("Percentage.notnull()")["Percentage"]

"""
def writetofile(df):
    
        df.to_csv("Examdatesandmarks.csv",index=False)
 """       

def drawchart(exam,df):
     
    col1,col2,col3 = st.columns([0.4,0.2,0.4])
    with col1:
         st.subheader(exam +' Subjectwise Marks')
         figh = px.histogram(df,x='Subject',y= exam, color='Subject',text_auto=True)
         st.plotly_chart(figh)    

    with col2:
         pass
    with col3:
        st.subheader('Distance from Maximum Score')
        if exam in ['PT1','PT2']:
            st.scatter_chart(df,x='Subject',y=['Max_PT',exam],color='Subject')
        else:
            st.line_chart(df,x='Subject',y=['MAX_Finals',exam],color='Subject')
        

         
 
   
def score():
   
    options=[]
    options = st.multiselect("Choose Exam",exams)
    
    if len(options)>1:
        rslt_df = exam_marks[(exam_marks['Examination'].isin(options))]
    elif len(options)==1:
        rslt_df = exam_marks[(exam_marks['Examination'] == options[0])]
        st.dataframe(rslt_df,hide_index=True)
        # html = build_table(rslt_df, 'blue_light')
        #components.html(html)
    else:
         pass
       
"""def update_marks():
    exam_marks= pd.read_csv("examdatesandmarks.csv")
    df = pd.read_csv("Result.csv")
    exams = exam_marks.query("Percentage.isnull()")["Examination"]
    option = st.selectbox("Choose Examination",exams)
    st.write(option)
    with st.form('marksentry'):
        Eng = st.number_input("English marks")
        Hindi = st.number_input("Hindi marks")
        Maths = st.number_input("Math marks")
        Science = st.number_input("Science marks")
        SST = st.number_input("SSt marks")
        AI = st.number_input("AI marks")
        if option in['PT1','PT2']:
            per = (Eng+Hindi+Maths+Science+SST+AI)/((25*5)+10)*100
        else:
            per = (Eng+Hindi+Maths+Science+SST+AI)/((80*5)+50)*100
        Per = round(per,2)
        updated = exam_marks['Examination'] == option
        exam_marks.loc[updated, 'English'] = Eng
        exam_marks.loc[updated, 'Hindi'] = Hindi
        exam_marks.loc[updated, 'Maths'] = Maths
        exam_marks.loc[updated, 'Science'] = Science
        exam_marks.loc[updated, 'SSt'] = SST
        exam_marks.loc[updated, 'AI'] = AI
        exam_marks.loc[updated, 'Percentage'] = Per
       
        
        submitted = st.form_submit_button("Submit")
        if submitted:
             writetofile(exam_marks)
             st.success("Done")
        st.caption(':blue[Report Card]')
        st.dataframe(exam_marks,hide_index=True)
        #html = build_table(exam_marks, 'blue_light')
        #components.html(html)
   """        
def exam_Analysis():
   df = pd.read_csv('Result.csv')
   #st.bar_chart(exam_marks,x='Examination' ,y= 'Percentage', color='Percentage')
   figh = px.histogram(exam_marks,x='Examination',y= 'Percentage', color='Examination',text_auto=True)
   st.plotly_chart(figh)    
   #figh = px.histogram(exam_marks,x='Examination',y= ['English','Hindi','Maths','Science',"Sst"], color='Examination',text_auto=True)
   #st.plotly_chart(figh)    

   option = st.selectbox("Choose Examination",exams)
   
   drawchart(option,df)
        


def subj_Analysis():
     df = pd.read_csv('Result.csv')
     lstsubj = df['Subject']
     finalsubj=[]
     option = st.selectbox('Choose Subject',lstsubj)
     lsubj=[]
     subj = (exam_marks[option]/25)*100

     for i in range(len(exam_marks[option])):
        if math.isnan(exam_marks[option][i]):
            break
        elif i in [0,1]:
                
                if option == "AI":
                    lsubj.append(((exam_marks[option][i])/10)*100)
                else:
                    lsubj.append(((exam_marks[option][i])/25)*100)
        else:
                if option == "AI":
                    lsubj.append(((exam_marks[option][i])/50)*100)
                else:
                    lsubj.append(((exam_marks[option][i])/80)*100)

         
         
     st.subheader("Analysis of "+ option)
     #st.bar_chart(exam_marks,x='Examination',y= option, color='Examination')
     figh = px.histogram(x=exams,y=lsubj,text_auto=True)
     st.plotly_chart(figh)    
