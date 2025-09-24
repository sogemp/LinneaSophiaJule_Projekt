import streamlit as st

def change_room(new_room):
    st.session_state.room = new_room

def aufzug_fahren2():
    if st.session_state.room != 'Aufzug':
        change_room('Aufzug')

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    col1.button("erster Stock", on_click=change_room, args=["erster Stock"], key="ersterStock")

    col2.button("zweiter Stock", on_click=change_room, args=["zweiter Stock"], key="zweiterStock")

    col3.button("dritter Stock", on_click=change_room, args=["dritter Stock"], key="dritterStock")

    col4.button("vierter Stock", on_click=change_room, args=["vierter Stock"], key="vierterStock")

    col5.button("fünfter Stock", on_click=change_room, args=["fünfter Stock"], key="fünfterStock")

    col6.button("sechster Stock", on_click=change_room, args=["sechster Stock"], key="sechsterStock")

    col7.button("siebter Stock", on_click=change_room, args=["siebter Stock"], key="siebterStock")

    col8.button("achter Stock", on_click=change_room, args=["achter Stock"], key="achterStock")
