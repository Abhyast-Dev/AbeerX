import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time


def openfile():
    df = pd.read_csv('activities.csv')
    return(df)



def addtofile(df):
    df.to_csv("activities.csv",mode='a', index=False, header=False)

def writetofile(df):
    df.to_csv("activities.csv",index =False)


def Plan():
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
        
            
        
        
def achieve():

    st.subheader('Hi! Abeer, Hope you had a good day:heart_eyes:')
    df = openfile()
    tdate= datetime.now().date()    
    rslt_df = df[df['Date'] == str(tdate)]
    mydict = rslt_df.to_dict('list')

    Do={}
    Later={}
    Ignore={}
    for i in mydict:
        if (i.find('imp') ==-1):
            x = mydict[i]
        field = str(i)

        if field.find('imp')!=-1:
            res = (str(i).split('_')[0]).strip()
                    
            if mydict[i][0]>=8 and mydict[i][0]<11:
                Do[res]= x
            elif mydict[i][0]>=5 and mydict[i][0]<8:
                Later[res]=x
            else:
                Ignore[res] =x
    with st.form("valueupdate"):

        st.text("Could you achieve your plan?")

        container = st.container(border=True)
        status=False
        with container:
            st.caption("Absolutely necessary, ")
            for i in Do:
                st.success( str(i)+" :->"+str(Do[i][0])+" hours")
            st.caption("Leisure time, can be done later")
            for i in Later:
                st.warning( str(i)+" :->"+str(Later[i][0])+" hours")
            st.caption("Can be ignored")
            for i in Ignore:
                st.info( str(i)+" :->"+str(Ignore[i][0])+" hours")
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
   
          

   
        
    