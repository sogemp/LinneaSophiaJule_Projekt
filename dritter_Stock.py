import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2

def dritter_stock_seite():

    st.header("dritter Stock")
    st.write("Suche den nächsten Hinweis")


    col1, col2, col3 = st.columns(3)

    if col1.button("Schließfächer"):
        change_room('SP_3')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('zweiter Stock')
        st.rerun()

    elif col3.button("Treppe hoch"):
        change_room('vierter Stock')
        st.rerun()

def sp_3():

    st.header("Schließfach")
    st.write("Um deinen nächsten Tipp zu bekommen, musst du die nächsten Aufgaben erfolgreich lösen!")

    col1, col2, = st.columns(2)

    if col1.button("öffne das Schließfach"):
        change_room('K_3')
        st.rerun()

    if col2.button("Zurück gehen"):
        change_room('dritter Stock')
        st.rerun()

#def k_3():

    #st.header("Schließfach")
   #st.write("")

    #if st.button("Schließe Schließfach"):
        #change_room('SP_3')
        #st.rerun()

def k_3():

    st.header("Schließfach")
    st.write("")

    # Lückentext-Implementierung
    text = "Im Schließfach befindet sich ein Zettel mit dem [___1___] für das nächste Rätsel."
    loesung = "Code" # Oder "Hinweis", je nachdem, was besser passt
    eingabe = st.text_input("Was steht auf dem Zettel?")

    if eingabe.lower() == loesung.lower():
        st.success("Richtig! Du hast das Rätsel gelöst und den Code gefunden.")

        if st.button("Öffne das Schließfach und gehe weiter"): # Button wird nur angezeigt, wenn der Lückentext gelöst ist.
            change_room('SP_3')
            st.rerun()

    elif eingabe: # Zeigt die Fehlermeldung nur, wenn der Benutzer etwas eingegeben hat.
        st.error("Leider falsch. Versuche es noch einmal.")

    else: #Vor dem lösen des Rätsels
        st.write("Finde den Code!")