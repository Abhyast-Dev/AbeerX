import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time
import matplotlib.pyplot as plt
import plotly.express as px


def openfile():
    df = pd.read_csv('activities.csv')
    return(df)



def addtofile(df):
    df.to_csv("activities.csv",mode='a', index=False, header=False)

def writetofile(df):
    df.to_csv("activities.csv",index =False)

d={}
def Plan():
    
     st.write(":blue[A goal without a plan is just a wish.]")
     with st.form('myplan'):
        dt = st.date_input("Plan your day for :", datetime.now().date()+timedelta(days=1),format="YYYY/MM/DD")
        tv = st.number_input('TV : No. of hours',min_value=0)
        imptv = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='tv')
        Guitar = st.number_input("Guitar: No. of hours",min_value=0)
        impguitar = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='guitar')
        music = st.number_input("Music: No. of hours",min_value=0)
        impmusic = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='music')
        playing = st.number_input("Playing: No. of hours",min_value=0)
        impplaying = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='play')
        homework = st.number_input("Homework: No. of hours",min_value=0)
        imphomework = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='hw')
        selfstudy = st.number_input("Self Study No. of hours",min_value=0)
        impselfstudy = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='selfstudy')
        sleep = st.number_input("Sleep: No. of hours",min_value=0)
        impsleep = st.slider("Choose level of importance on a scale of 1 to 10", 0,10,1,key='sleep')
        submitted = st.form_submit_button("Submit")
        d = {'Date': [dt],'TV':[tv],'TV_imp' :[imptv],'Guitar':[Guitar], 'Guitar_imp': [impguitar],'Music':[music],'Music_imp': [impmusic], 'Playing': [playing], 'Playing_imp' : [impplaying],  'Homework' : [homework],'Homework_imp': [imphomework],'Selfstudy': [selfstudy], 'Selfstudy_imp' : [impselfstudy],'Sleep':[sleep],'Sleep_imp':[impsleep]} 
        myact=pd.DataFrame(d)     
        
        if submitted:
                writetofile(myact)
                
                st.markdown('Submitted responses:')
def ToDo():
    df= pd.read_csv("todo.csv")
    tdate= datetime.now().date()-timedelta(days=1)
    mydf = df['Date'] == str(tdate)
    rslt_df = df[df['Date'] == str(tdate)]
    st.write(":blue[The victory of success is half won when one gains the habit of setting goals and achieving them.]")
   
    if not(df.empty):
     
        with st.form('ytodo',clear_on_submit=False):
            st.dataframe(rslt_df,hide_index=True)
            submitted = st.form_submit_button("Submit")
            on = st.toggle("Could you achieve?")
            rem=st.text_area("Remarks",key="Remarks")
            
            if on == True:
                ach = True                
                st.balloons()
            else:
                ach = False                
                st.toast('Imagine!',icon="🏅")
                time.sleep(.5)
                st.toast('Believe!',icon="🤩")
                time.sleep(.5)
                st.toast('Achieve!', icon='🎉')
            df.loc[mydf, 'Achieved'] = ach
            df.loc[mydf, 'Remarks'] = rem
            if submitted:
                    
                    df.to_csv("todo.csv",index =False)
                    st.markdown('Submitted response')
        

                    
         
    with st.form('mytodo',clear_on_submit=True):
        dt = st.date_input("Plan your day for :", datetime.now().date()+timedelta(days=1),format="YYYY/MM/DD")
        todo = st.text_area("Plan for tomorrow",key='todo') 
        num = st.slider("Achieved?,Choose from a scale of 0 to 5. 0 means -> Not at all, 1-> 25%, 2-> 50%, 3->75%, 4-> All Done  ")
        submitted = st.form_submit_button("Submit")
        if num==0:
            desc = " Not at all"
        elif num == 1:
            desc = "25%"
        elif num ==2:
            desc = '50%'
        elif num == 3:
            desc = '75%'
        else:
            desc = 'All Done'
        d = {'Date': [dt],'Todo':[todo],'Achieved':num,'Desc': desc} 
        myact=pd.DataFrame(d)       

        if submitted:
                myact.to_csv("todo.csv",mode='a', index=False, header=False)
                
                st.markdown('Submitted response')
    

    fig = px.pie(values = df['Achieved'],hole = 0.5)
    mydf = df.groupby(['Desc'])['Desc'].count().reset_index(name='count')
    fig = px.pie(mydf, values='count', names='Desc', title='To do Analysis')
    

    st.plotly_chart(fig)
                

            
        
        
def achieve():
    st.subheader('Hi! Abeer, Hope you had a good day:heart_eyes:')
    st.write(":blue[Time management is not about managing TIME. It's about managing priorities]")
    df = openfile()
    tdate= datetime.now().date() 
    myloc=    df['Date'] == str(tdate)
    rslt_df = df[myloc]
    st.dataframe(rslt_df,hide_index=True)
    Do={}
    Later={}
    Ignore={}
    for i in rslt_df.columns:
        if (str(i).find('imp') ==-1):
            x = rslt_df.loc[myloc][i]
        field = str(i)

        if field.find('imp')!=-1:
            res = rslt_df.loc[myloc][i]
            #st.write(res)
                    
            if int(res)>=8 and int(res)<11:
                Do[i]= x
            elif int(res)>=5 and int(res)<8:
                Later[i]=x
            else:
                Ignore[i] =x
    with st.form("valueupdate"):

        st.text("Could you achieve your plan?")

        container = st.container(border=True)
        status=False
        with container:
            st.caption("Absolutely necessary, ")
            for i in Do:
                st.success( str(i)+" :->"+str(Do[i])+" hours")
            st.caption("Leisure time, can be done later")
            for i in Later:
                st.warning( str(i)+" :->"+str(Later[i])+" hours")
            st.caption("Can be ignored")
            for i in Ignore:
                st.info( str(i)+" :->"+str(Ignore[i])+" hours")
            on = st.toggle("Everything went as planned")
    
            if on:
                st.balloons()
                status=True
            else:
                status = False
                st.toast('Imagine!',icon="🏅")
                time.sleep(.5)
                st.toast('Believe!',icon="🤩")
                time.sleep(.5)
                st.toast('Achieve!', icon='🎉')

        submitted =  st.form_submit_button("Click to update status")
        updated = df['Date'] == tdate
        
        df.loc[updated, 'Achieved?'] = status

        if submitted:
            writetofile(df)

    
def share():
    
    st.write(":blue[From the quiet reflection will come even more effective action.]")
    #feeldf= pd.read_csv("expressself.csv",usecols=['Date','Feelings'])
    
    
    with st.form("feeldata"):
        st.snow()           
        # Create two columns
        col1, col2=st.columns(2)
        
        with col1:
            s = st.text_area("I feel my :blue[**STRENGTH**] is:", max_chars=1000,key="stre")
        with col2:
            w = st.text_area("I feel my :red[**WEAKNESS**] is:", max_chars=1000,key="wea")
        st.divider
        col3,col4 = st.columns(2)
        with col3:
            o=st.text_area("I feel my :blue[**OPPORTUNITY**] is:", max_chars=1000,key="opp")
        with col4:
            t = st.text_area("I feel :red[**THREAT**] is/are:", max_chars=1000,key="thr")
        feelsubmitted =  st.form_submit_button("Click to update status")
        tdate= str(datetime.now().date()) 
        x= {'Date':[tdate],'STRENGTH':[s],'WEAKNESS':[w],'OPPORTUNITY':[o], 'THREAT':[t]}
        feeldf=pd.DataFrame(x)
        
                
        if feelsubmitted:
            
            feeldf.to_csv("expressself.csv",mode='a',header=False, index=False)
   
          

   
        
    
