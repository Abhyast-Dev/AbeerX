import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import time


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
    


"""
def revision():
    option = st.selectbox("Choose Subject",('English','Maths','Science','SST'),
    placeholder="Select subject...",key='revSubj')
    filename = str(option)+".csv"
    df= pd.read_csv(filename)
    ch = st.selectbox("Choose Chapter",df['Chapter'])    
    with st.form("rev",clear_on_submit=True):
        
        #df.loc[updated,'Test_count']=cnt
        tdate= st.date_input("Choose Date")
        by= st.selectbox('Conducted by:',['School','YTTB','Self'])
        tot_qs = st.number_input("Total no of Questions",min_value=0)
        tot_correct = st.number_input("Total no of correct questions",min_value=0)
        max_marks = st.number_input("Maximum Marks",min_value=1)
        score = st.number_input("Your Score")
        per= round((score/max_marks)*100 ,1)         
        mydict= {'Date':[tdate],'Subject':[option],'Chapter covered':[ch],'Total Questions':[tot_qs],'No of Correct Answers':[tot_correct],'Max Marks':[max_marks],'Marks Scored':[score],'By':[by],'Percentage':[per]}
        mydf = pd.DataFrame(mydict)
        updated= df["Chapter"] == ch
        df.loc[updated, "Test_count"] = df['Test_count']+1
        submitted = st.form_submit_button("Click to Save!")
        
        if submitted:
            with st.spinner('Saving data...'):
                time.sleep(5)
            mydf.to_csv('Revisiontest.csv',mode='a',header=False,index=False)
            df.to_csv(filename,index =False)
            st.success("Done")
            

   """         

def testRec():
    exam = st.selectbox("Choose assessment",('PT1','PT2','Half Yearly','PreBoard I','PreBoard II','BOARD'),
    placeholder="Select subject...",key='testassess')
    if exam=='BOARD':
        exam = 'PreBoard II'
    option = st.selectbox("Choose Subject",('English','Maths','Science','SST'),
    placeholder="Select subject...",key='testsubj')
    filename = str(option)+".csv"
    df= pd.read_csv(filename,usecols=['Chapter',exam,'Test_count'])
    ch_list = list(df['Chapter'])
    #ch_list.append('All')
    
    #ch = st.selectbox("Choose Chapter",ch_list,key='testch')
    
    #if ch == 'All':
     #   st.write(df)
    #else:
    rslt = df.loc[df[exam] == True]
    #st.write(rslt)
    st.subheader('Test count - Exam wise')
    
    fig1 = px.bar(rslt, x='Chapter',y= 'Test_count', color='Test_count',text_auto=True)
    st.plotly_chart(fig1)
    figp = px.pie(rslt, values='Test_count', names= 'Chapter', color='Test_count',title='Number of practice tests taken- Percentage Analysis')
    figp.update_traces(textposition='inside', textinfo='percent+label')

    st.plotly_chart(figp)
    


    testdf= pd.read_csv('Revisiontest.csv',usecols=['Date','Chapter covered','Percentage'])
    myres = testdf[testdf['Chapter covered'].isin(ch_list)]
    st.subheader("Precentage of marks scored for each chapter")
    #st.write(myres)
       
    figh = px.histogram(myres, x="Chapter covered", y="Percentage",
             color='Percentage', barmode='group',
             height=400,text_auto=True)
    st.plotly_chart(figh)    

    
        
    

        

def ready():
    st.write(":blue[Note: This tab gives you an idea of preparedness with respect to Practice tests you have given]")
    exam = st.selectbox("Choose assessment",('PT1','PT2','Half Yearly','PreBoard I','PreBoard II','BOARD'),
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

    st.bar_chart(x1, x='Chapter covered',y= 'Percentage', color= 'Percentage')
    
    
    
    
    
    #st.scatter_chart(permean, x=None,y= ['mean','std'], color=['#272B6A','#FEE42D'])
    
    #st.bar_chart(permean,x='Chapter covered',y= 'std', color=['#272B6A'])
    
    st.subheader(exam +' Analysis - Box Plot')
    fig = px.box(x1, x="Chapter covered", y="Percentage", points="all",color= 'Percentage')
    
    st.plotly_chart(fig)


   
   
def examadministered():
    df1= pd.read_csv("Revisiontest.csv")
    subj1 = set(df1['Subject'])
    option = st.selectbox("Choose Subject",subj1,
    placeholder="Select subject...",key='subj1')
    df = df1[df1['Subject'] == option]
    
    x = st.toggle("Show chapter wise")
    
    if x == True:
      ch =  set(df['Chapter covered'])
      optionch = st.selectbox("Choose Chapter",ch,
      placeholder="Select subject...",key='chap')

      
      dfch = df[df['Chapter covered'] == optionch]
      st.dataframe(dfch,hide_index=True)  
    else:
        st.dataframe(df,hide_index=True)    




