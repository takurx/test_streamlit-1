# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

number = '0'
number = st.text_input('Please decimal number', number)

hex_number = '0x0'
hex_number = st.text_input('Please hexadecimal number', hex_number)

if number.isnumeric():
    st.write('Hexadecimal is your input number is', hex(int(number)))
    hex_number = hex(int(number))
elif hex_number.startswith('0x') and hex_number[2:].isalnum():
    decimal_number = int(hex_number, 16)
    st.write('Decimal of your input number is', str(decimal_number))
    number = str(decimal_number)
else:
    st.write('Please input number or Please input hexadecimal number')

