#import streamlit as st
#from changeRoom import change_room

#def aufzug_fahren2():

    #col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    #col1.button("erster Stock", on_click=change_room, args=["erster Stock"], key="ersterStock")

    #col2.button("zweiter Stock", on_click=change_room, args=["zweiter Stock"], key="zweiterStock")

    #col3.button("dritter Stock", on_click=change_room, args=["dritter Stock"], key="dritterStock")

    #col4.button("vierter Stock", on_click=change_room, args=["vierter Stock"], key="vierterStock")

   #col5.button("fünfter Stock", on_click=change_room, args=["fünfter Stock"], key="fünfterStock")

    #col6.button("sechster Stock", on_click=change_room, args=["sechster Stock"], key="sechsterStock")

    #col7.button("siebter Stock", on_click=change_room, args=["siebter Stock"], key="siebterStock")

    #col8.button("achter Stock", on_click=change_room, args=["achter Stock"], key="achterStock")

#def aufzug_seite():
    #st.header("Aufzug")
    #password = st.number_input("Bitte Passwort eingeben:", min_value=100, max_value=999, step=1)
    #if st.button("Passwort bestätigen"):
        #if password == 811:
            #st.write("Passwort korrekt!")
            #aufzug_fahren2()
       # else:
           # st.write("Falsches Passwort!")