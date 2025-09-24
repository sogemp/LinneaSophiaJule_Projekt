import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2

def achter_stock_seite():
#st.session_state.room == 'achter Stock':
    st.header("achter Stock")
    st.write("achter Stock")


    col1, col2, = st.columns(2)

    if col1.button("Betrete Social-Space"):
        change_room('SP_8')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('siebter Stock')
        st.rerun()

def sp_8():
#st.session_state.room == 'SP_8':
    st.header("Social Space")
    st.write("social space")

    col1, col2, = st.columns(2)

    if col1.button("öffne Kühlschrank"):
        change_room('K_8')
        st.rerun()

    if col2.button("Zurück gehen"):
        change_room('achter Stock')
        st.rerun()

def k_8():
#st.session_state.room == 'K_8':
    st.header("Kühlschrank")
    st.write("KÜhlschrank")

    if st.button("Schließe Kühlschrank"):
        change_room('SP_8')
        st.rerun()
