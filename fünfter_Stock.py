import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2

def fünfter_stock_seite():
#if st.session_state.room == 'fünfter Stock':
    st.header("fünfter Stock")
    st.write("Nun bist du im fünften Sock angekommen. Gehe schnell in den Social-Space!")


    col1, col2, col3 = st.columns(3)

    if col1.button("Betrete Social-Space"):
        change_room('SP_5')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('vierter Stock')
        st.rerun()

    elif col3.button("Treppe hoch"):
        change_room('sechster Stock')
        st.rerun()

def sp_5():
#if st.session_state.room == 'SP_5':
    st.header("Social Space")
    st.write("Um weiter zu kommen, musst du unter Zeitdruck die Aufgabe lösen. Ansonsten geht der Hinweis verloren!")

    col1, col2, = st.columns(2)

    if col1.button("Aufgabe"):
        change_room('K_5')
        st.rerun()

    if col2.button("Zurück gehen"):
        change_room('fünfter Stock')
        st.rerun()

def k_5():
#if st.session_state.room == 'K_5':
    st.header("Aufgabe")
    st.write("Wie viele Buchstaben hat das Wort „Kakaomaschine""")

    if st.button("Schließe Kühlschrank"):
        change_room('SP_5')
        st.rerun()