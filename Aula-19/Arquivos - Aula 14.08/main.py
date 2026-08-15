import streamlit as st




st.title('CALCULADORA')
# st.header('teste')


n1 =  st.number_input('nº', value=0.1 )
n2 =  st.number_input('nº', value=0.0)


if st.button('Calcular...') :   
   if n1 and n2:
      soma  =  n1 + n2


      st.info( soma)
   else:
      print('Digite algo ')    