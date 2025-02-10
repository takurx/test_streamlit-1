# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

number = st.text_input('Please decimal number', '0')

if number.isnumeric():
    square_number = int(number) * int(number)
    #st.write('Square of your input number is', str(square_number))
    st.write('Hexadecimal is your input number is', hex(int(number)))
else:
    st.write('Please input number')

hex_number = st.text_input('Please hexadecimal number', '0x0')

if hex_number.startswith('0x') and hex_number[2:].isalnum():
    decimal_number = int(hex_number, 16)
    st.write('Decimal of your input number is', str(decimal_number))
else:
    st.write('Please input hexadecimal number')

