import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

from changeRoom import change_room
from changeRoom import aufzug_fahren2

from erster_Stock import erster_stock_seite, sp_1r, sp_1l, k_1
from zweiter_Stock import zweiter_stock_seite, sp_2, k_2
from dritter_Stock import dritter_stock_seite, sp_3, k_3
from vierter_Stock import vierter_stock_seite, sp_4, k_4
from fünfter_Stock import fünfter_stock_seite, sp_5, k_5
from sechster_Stock import sechster_stock_seite, sp_6, k_6
from siebter_Stock import siebter_stock_seite, sp_7, k_7
from achter_Stock import achter_stock_seite, sp_8, k_8
#from Aufzug import aufzug_seite


if 'room' not in st.session_state:
    st.session_state.room = 'start'


# Logik für die Räume

if st.session_state.room == 'start':
    st.header("Haupteingang")
    st.write("Es ist 9 Uhr. Dein Arbeitstag hat begonnen, aber das dringende Verlangen nach einem warmen Kakao überkommt dich. Du machst dich auf den Weg in den ersten Stock, um die geliebte Kakaomaschine zu besuchen. ")
    st.write("Du bist beim Haupteingang. Vor dir ist eine Treppe.")

    if st.button("Treppe Hochgehen"):
        change_room('erster Stock')
        st.rerun()

#erster Stock

elif st.session_state.room == 'erster Stock':
    erster_stock_seite()

elif st.session_state.room == 'SP_1R':
    sp_1r()
elif st.session_state.room == 'SP_1L':
    sp_1l()
elif st.session_state.room == 'K_1':
    k_1()
#elif st.session_state.room == 'Aufzug':
    #aufzug_seite()


#zweiter Stock

elif st.session_state.room == 'zweiter Stock':
    zweiter_stock_seite()

elif st.session_state.room == 'SP_2':
    sp_2()

elif st.session_state.room == 'K_2':
    k_2()

#dritter Stock

elif st.session_state.room == 'dritter Stock':
    dritter_stock_seite()

elif st.session_state.room == 'SP_3':
    sp_3()

elif st.session_state.room == 'K_3':
    k_3()

#vierter Stock

elif st.session_state.room == 'vierter Stock':
    vierter_stock_seite()

elif st.session_state.room == 'SP_4':
    sp_4()

elif st.session_state.room == 'K_4':
    k_4()

#fünfter stock

elif st.session_state.room == 'fünfter Stock':
    fünfter_stock_seite()

elif st.session_state.room == 'SP_5':
    sp_5()

elif st.session_state.room == 'K_5':
    k_5()

#sechster Stock

elif st.session_state.room == 'sechster Stock':
    sechster_stock_seite()

elif st.session_state.room == 'SP_6':
    sp_6()

elif st.session_state.room == 'K_6':
    k_6()

#siebter Stock

elif st.session_state.room == 'siebter Stock':
    siebter_stock_seite()

elif st.session_state.room == 'SP_7':
    sp_7()

elif st.session_state.room == 'K_7':
    k_7()

#achter Stock

elif st.session_state.room == 'achter Stock':
    achter_stock_seite()

elif st.session_state.room == 'SP_8':
    sp_8()

elif st.session_state.room == 'K_8':
    k_8()







