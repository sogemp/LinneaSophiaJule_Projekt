import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2

def vierter_stock_seite():
#if st.session_state.room == 'vierter Stock':
    st.header("vierter Stock")
    st.write("Angekommen im vierten Stock siehst du, dass der Hausmeister gerade da ist.")


    col1, col2, col3 = st.columns(3)

    if col1.button("Hausmeister nach der Kakaomaschine fragen"):
        change_room('SP_4')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('dritter Stock')
        st.rerun()

    elif col3.button("Treppe hoch"):
        change_room('fünfter Stock')
        st.rerun()

def sp_4():
#if st.session_state.room == 'SP_4':
    st.header("Hausmeister")
    st.write("Entscheid dich zwischen den beiden Fragen:")

    col1, col2, = st.columns(2)

    if col1.button("Hast du die Kakaomaschine gesehen?"):
        change_room('K_4')
        st.rerun()

    if col2.button("Zurück gehen"):
        change_room('dritter Stock')
        st.rerun()

def k_4():
#if st.session_state.room == 'K_4':
    st.header("Hausmeister")
    st.write("Nein, ich suche sie ebenfalls. In diesem Stockwerk habe ich schon alles abgesucht, versuch es im nächsten Stockwerk.")

    if st.button("Beende das Gespräch."):
        change_room('SP_4')
        st.rerun()