# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

st.session_state.number = '0'
number = st.text_input('Please decimal number', value=st.session_state.number)

st.session_state.hex_number = '0x0'
hex_number = st.text_input('Please hexadecimal number', value=st.session_state.hex_number)

btn = st.button('Convert')

if btn:
    if number.isnumeric():
        st.write('Hexadecimal is your input number is', hex(int(number)))
        st.session_state.hex_number = hex(int(number))
    elif hex_number.startswith('0x') and hex_number[2:].isalnum():
        decimal_number = int(hex_number, 16)
        st.write('Decimal of your input number is', str(decimal_number))
        st.session_state.number = str(decimal_number)
    else:
        st.write('Please input number or Please input hexadecimal number')
    #None
# None

