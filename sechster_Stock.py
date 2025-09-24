import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2

def sechster_stock_seite():
#st.session_state.room == 'sechster Stock':
    st.header("sechster Stock")
    st.write("sechster Stock")


    col1, col2, col3 = st.columns(3)

    if col1.button("Betrete Social-Space"):
        change_room('SP_6')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('fünfter Stock')
        st.rerun()

    elif col3.button("Treppe hoch"):
        change_room('siebter Stock')
        st.rerun()

def sp_6():
#if st.session_state.room == 'SP_6':
    st.header("Social Space")
    st.write("social space")

    col1, col2, = st.columns(2)

    if col1.button("öffne Kühlschrank"):
        change_room('K_6')
        st.rerun()

    if col2.button("Zurück gehen"):
        change_room('sechster Stock')
        st.rerun()

def k_6():
#st.session_state.room == 'K_6':
    st.header("Kühlschrank")
    st.write("KÜhlschrank")

    if st.button("Schließe Kühlschrank"):
        change_room('SP_6')
        st.rerun()