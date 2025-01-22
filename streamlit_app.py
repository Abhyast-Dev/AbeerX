import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Thinking about Thinking",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

code = """
<style>
    p {
        color: #000000;
    }
</style>
"""
st.html(code)


from datetime import datetime 
from datetime import date
import impdates as imp
import marks
import My
import Progress as pr

def daysleft():
    str_board = '2025/02/15'
    board_date = datetime.strptime(str_board, "%Y/%m/%d").date()
    today = date.today()
    delta = board_date - today
    return(delta)
st.caption(":orange[Today is: "+str(date.today(). strftime("%d/%m/%y"))+"]")
st.header(":blue[Abeer's Dashboard]")
st.subheader("")



    



with st.sidebar:
    st.logo('logo/logosmall.png', icon_image='logo/Abhyast full.png')
    st.subheader('Hi, Abeer!:i_love_you_hand_sign:')
    diff = str(daysleft())
    
    ndays = diff.split(',')
    st.title(':blue['+ndays[0]+' to go!] :maple_leaf:')
    st.caption(":green[Remember,]:rainbow[ Exams are not about who's the best, but about who can handle pressure the best]" )
    st.caption(":green[**Let's :red[DO IT] together!**] :sunglasses:")
    choice = st.radio( "***What are you thinking about?***",["***Dates and Syllabus***", "***Your marks***", "***Your Progress***", "***Run up to Board Exams***"])
if choice=="***Dates and Syllabus***":
    tab1,tab2=st.tabs(["Exam","Syllabus"])
    with tab1:
            imp.exam_tab1()
    with tab2:
            imp.exam_tab2()
            
elif choice=="***Your marks***":
    tab1,tab2,tab3,tab4=st.tabs(["View Marks","Update Marks","Exam wise analysis","Subject wise Analysis"])
    with tab1:
            marks.score()
    with tab2:
          st.subheader("Hey Abeer! The marks need to be directly updated to CSV. Sorry for the inconvenience")
          #marks.update_marks()
    with tab3:
            marks.exam_Analysis()
    with tab4:
            marks.subj_Analysis()

elif choice == "***Run up to Board Exams***":
    df= pd.read_csv("Boardprep.csv")
    tab1,tab2 = st.tabs(["Today's Target","Complete plan"])
    with tab1:
        st.caption(" My dear Abeer")
        st.caption(":blue[Setting targets is the key to unlocking your true potential. Scoring well is not just about the marks but about giving your best with discipline, focus, and effort. When you perform to your full potential, you leave no room for regrets—only the satisfaction of knowing you gave it your all.]")
        today = date.today()
        st.write(today)
        x = pd.to_datetime(df['Date'] ).dt.date
        rslt_df = df[(x == today)]
        st.write(rslt_df)
    with tab2:
        st.dataframe(df)
    

    

#elif choice=="***Your Progress***":
#   tab1,tab2,tab3,tab4,tab5=st.tabs(["Subjectwise Info","Practice Tests Marks Entry","Practice Tests Report","Check Preparedness", "Practice Test details"])
#    with tab1:
#          pr.subject()
#    with tab2:
#          st.subheader("Hey Abeer! The marks need to be directly updated to CSV. Sorry for the inconvenience")
#          #pr.revision()
#    with tab3:
#          pr.testRec()
#   with tab4:
#         pr.ready()
#   with tab5:
#         pr.examadministered()
          


    


