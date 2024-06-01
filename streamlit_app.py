import streamlit as st

st.set_page_config(
    page_title="Thinking about Thinking",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
    st.subheader('Hi, Abeer!:i_love_you_hand_sign:')
    diff = str(daysleft())
    
    ndays = diff.split(',')
    st.title(':blue['+ndays[0]+' to go!] :maple_leaf:')
    st.caption(":green[Remember,]:rainbow[ Exams are not about who's the best, but about who can handle pressure the best]" )
    st.caption(":green[**Let's :red[DO IT] together!**] :sunglasses:")
    choice = st.radio( "***What are you thinking about?***",["***Dates and Syllabus***", "***Your marks***", "***Your Progress***","***Self monitoring***"])
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
          marks.update_marks()
    with tab3:
            marks.exam_Analysis()
    with tab4:
            marks.subj_Analysis()
    
elif choice=="***Your Progress***":
    tab1,tab2,tab3,tab4=st.tabs(["Subjectwise Info","Practice Tests Marks Entry","Practice Tests Report","Check Preparedness"])
    with tab1:
          pr.subject()
    with tab2:
          pr.revision()
    with tab3:
          pr.testRec()
    with tab4:
          pr.ready()

elif choice=="***Self monitoring***":
    tab1,tab2,tab3,tab4=st.tabs(["Plan for Tomorrow","Today's achievement","To do","Self Reflection"])
    with tab1:
        My.Plan()
    with tab2:
        My.achieve()
    with tab3:
        My.ToDo()
    with tab4:
        My.share()




    


