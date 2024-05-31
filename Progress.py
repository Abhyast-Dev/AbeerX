import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


def disp_distributionChart(df):
    
    col1,col2,col3 = st.columns([50,10,40])
    with col1:

        st.caption(":blue[Weightage of Units]")

        labels = list(df['Unit'])
        size = list(df['Unit_Weightage'])
        unit=[]
        weight=[]
        opts = list(set(df['Unit']))
        for i in opts:
        
            count=1
            for j in range(len(labels)):
                if count ==1 and i == labels[j]:
                    unit.append(labels[j])
                    weight.append(size[j])
                    count+=1
            

        fig1, ax1 = plt.subplots()
        ax1.pie(weight,labels=unit,autopct="%.1f",startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

    with col2:
        pass
    with col3:
        st.dataframe(df,column_order=['Unit','Chapter'],hide_index=True) 



def eng_Display():
    df= pd.read_csv("English.csv",usecols=['Unit_Weightage','Unit','Chapter'])
    disp_distributionChart(df)
    


def maths_Display():
    df= pd.read_csv("Maths.csv",usecols=['Unit_Weightage','Unit','Chapter'])
    disp_distributionChart(df)

def science_Display():
    df= pd.read_csv("Science.csv",usecols=['Unit','Chapter','Unit_Weightage'])
    disp_distributionChart(df)

def sst_Display():
    df= pd.read_csv("SST.csv",usecols=['Unit','Chapter','Unit_Weightage'])
    disp_distributionChart(df)


def subject():
   option = st.selectbox(
   "Choose Subject",
   ('English','Maths','Science','SSt'),
   placeholder="Select subject...")
  
   if option =='English':
        eng_Display()
       
   elif option =='Maths':
        maths_Display()
   elif option == "Science":
        science_Display()
   elif option == "SSt":
        sst_Display()
    



def revision():
    option = st.selectbox("Choose Subject",('English','Maths','Science','SSt'),
    placeholder="Select subject...",key='revSubj')
    filename = str(option)+".csv"
    df= pd.read_csv(filename)
    ch = st.selectbox("Choose Chapter",df['Chapter'])    
    with st.form("rev"):
        """updated = df['Chapter'] == ch
        st.write(updated)
        testcount = df[updated,['Test_count']]
        cnt = testcount+1"""
        df.loc[df["Chapter"] == ch, "Test_count"] = df['Test_count']+1
        #df.loc[updated,'Test_count']=cnt
        tdate= st.date_input("Choose Date")
        by= st.selectbox('Conducted by:',['School','YTTB','Self'])
        tot_qs = st.number_input("Total no of Questions",min_value=0)
        tot_correct = st.number_input("Total no of correct questions",min_value=0)
        max_marks = st.number_input("Maximum Marks",min_value=1)
        score = st.number_input("Your Score")
        per= (score/max_marks)*100           
        mydict= {'Date':[tdate],'Subject':[option],'Chapter covered':[ch],'Total Questions':[tot_qs],'No of Correct Answers':[tot_correct],'Max Marks':[max_marks],'Marks Scored':[score],'By':[by],'Percentage':[per]}
        mydf = pd.DataFrame(mydict)
        submitted = st.form_submit_button("Click to Save!")
        if submitted:
            mydf.to_csv('revisiontest.csv',mode='a',header=False,index=False)
            df.to_csv(filename,index=False)

            

def testRec():
    exam = st.selectbox("Choose assessment",('PT1','PT2','Half yearly','PreBoard I','PreBoard II','BOARD'),
    placeholder="Select subject...",key='testassess')
    if exam=='BOARD':
        exam = 'PreBoard II'
    option = st.selectbox("Choose Subject",('English','Maths','Science','SSt'),
    placeholder="Select subject...",key='testsubj')
    filename = str(option)+".csv"
    df= pd.read_csv(filename,usecols=['Chapter',exam,'Test_count'])
    #ch_list = list(df['Chapter'])
    #ch_list.append('All')
    
    #ch = st.selectbox("Choose Chapter",ch_list,key='testch')
    
    #if ch == 'All':
     #   st.write(df)
    #else:
    rslt = df.loc[df[exam] == True]
    st.write(rslt)
    st.subheader('Test count - Exam wise')

    st.bar_chart(rslt, x='Chapter',y= 'Test_count', color=['#FEE42D'])

        

def ready():
    st.write(":blue[Note: This tab gives you an idea of preparedness with respect to Practice tests you have given]")
    exam = st.selectbox("Choose assessment",('PT1','PT2','Half yearly','PreBoard I','PreBoard II','BOARD'),
    placeholder="Select subject...",key='assess')
    option = st.selectbox("Choose Subject",('English','Maths','Science','SSt'),
    placeholder="Select subject...",key='subj')
    filename = str(option)+".csv"
    if exam=='BOARD':
        exam = 'PreBoard II'
    df= pd.read_csv(filename, usecols =['Chapter',exam])
    rdf = df[df[exam] == True]  
    #st.write(rdf['Chapter'])
    lst_ch = list(rdf['Chapter'])
    df1= pd.read_csv("Revisiontest.csv")
    #x = df1['Chapter covered']
    #check=st.write(df1[df1['Chapter covered'].isin(lst_ch)])
    x1= df1.loc[df1['Chapter covered'].isin(lst_ch)]
    rows = len(x1.axes[0])
    st.write("Total No .of tests attempted",rows)
    st.write("Average score",x1['Percentage'].mean())
    st.write("Deviation from mean",x1['Percentage'].std())
    grouped = x1.groupby('Chapter covered')
    permean=grouped['Percentage'].agg([np.mean,np.std])
    
    st.write(permean)
   
    
    st.subheader(exam +' Analysis - Percentage Scored')

    st.bar_chart(x1, x='Chapter covered',y= 'Percentage', color=['#FEE42D'])
    
    st.subheader(exam +' Analysis - Mean and Standard Deviation')
    st.write('Note: Mean indicates the average marks scored in revision tests of a chapter. A standard deviation close to zero indicates that data points are very close to the mean, whereas a larger standard deviation indicates data points are spread further away from the mean (average marks you scored for a chapter)')
    
    st.scatter_chart(permean, x=None,y= ['mean','std'], color=['#272B6A','#FEE42D'])
    
    #st.bar_chart(permean,x='Chapter covered',y= 'std', color=['#272B6A'])
    
    st.subheader(exam +' Analysis - Box Plot')
    fig = px.box(x1, x='Chapter covered', y='Percentage')
    st.plotly_chart(fig)


   
   
def prepared():
    pass
