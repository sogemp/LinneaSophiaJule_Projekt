import streamlit as st
from changeRoom import change_room
#from changeRoom import aufzug_fahren2


def zweiter_stock_seite():
    st.header("zweiter Stock")
    st.write("Nun bist du in Stockwerk 2 angekommen. Du siehst einen Mitarbeiter, der normalerweise die Kakaomaschnie nachfüllt, in den Social Space gehen. Hat er vielleicht einen Hinweis für dich?")
    col1, col2, col3 = st.columns(3)

    if col1.button("Betrete Social-Space"):
        change_room('SP_2')
        st.rerun()

    elif col2.button("Treppe runter"):
        change_room('erster Stock')
        st.rerun()

    elif col3.button("Treppe hoch"):
        change_room('dritter Stock')
        st.rerun()

def sp_2():
    st.header("Social Space")
    st.write("Du konfrontierst den Mitarbeiter, da du vermutest, dass er in Verbindung zu dem Dieb steht. Er ist bereit, dir den nächsten Hinweis zu verraten, aber nur, wenn du ihm die wichtigsten Bestandteile von Trinkschokolade nach Mengenanteil vom größten zum kleinsten Bestanteil ordnen kannst.")

    #Farbrätsel
    st.write("Wähle die richtige Reihenfolge:")
    farben = ["Zucker", "Vollmilchpulver", "Kakaobutter", "Salz"]
    richtige_reihenfolge = ["Zucker", "Kakaobutter", "Vollmilchpulver", "Salz"]

    auswahl1 = st.selectbox("Nr.1:", farben, key="f1")
    auswahl2 = st.selectbox("Nr.2:", farben, key="f2")
    auswahl3 = st.selectbox("Nr.3:", farben, key="f3")
    auswahl4 = st.selectbox("Nr.4:", farben, key="f4")

    geratene_reihenfolge = [auswahl1, auswahl2, auswahl3, auswahl4]

    if geratene_reihenfolge == richtige_reihenfolge:
        st.write("Richtig! Der Mitarbeiter verrät dir, dass sich der nächste Hinweis im Geschirrschrank befindet.")

        col1, col2, = st.columns(2)

        if col1.button("Öffne den Geschirrrückgaben-Schrank"):
            change_room('K_2')
            st.rerun()

        if col2.button("Zurück gehen"):
            change_room('zweiter Stock')
            st.rerun()
    else:
        st.write("Falsch! Versuche es noch einmal.")
        col1, col2, = st.columns(2)

        if col2.button("Zurück gehen"):
            change_room('zweiter Stock')
            st.rerun()

def k_2():
    st.header("Geschirrrückgabe")
    st.write("Restkakao in den Tassen ist zwar nicht das Ziel, doch hier findest du den nächsten Geschmack deiner Lösung: Gehe in das nächste Stockwerk zu dem Schießfach!")

    if st.button("Schließe den Schrank wieder"):
        change_room('SP_2')
        st.rerun()