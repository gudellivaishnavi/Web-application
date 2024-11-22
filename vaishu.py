import streamlit as st
import math

st.title("2205A21043_PS7")
st.header("calculate the  resistance (R0) and reactance(X0) of a transformer based on open circuit test measurements like V0, I0, W0")

def Tran_Eff(vo,io,wo):
    NPF=wo/(vo*io)
    Iu=io*(math.sqrt(1-(NPF**2)))
    Iw=io*NPF
    ro=vo/Iw
    xo=vo/Iu
    return ro,xo



col1,col2=st.columns(2)
with col1:
    vo=st.number_input("VO(vlot)",value=100)
    io=st.number_input("IO(amps)",value=100)
    wo=st.number_input("WO(watts)",value=100)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            ro,xo=Tran_Eff(vo,io,wo)
            st.write(f"RO={ro:2f}ohms")    
            st.write(f"XO={xo:2f}ohms") 