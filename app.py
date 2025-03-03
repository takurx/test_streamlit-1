# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Covnert to 16->10 and 10->16, V1.0')

number = st.text_input('Please input decimal number (10 base number)', value='0')

if number.isnumeric():
    st.write('Hexadecimal is your input number is', hex(int(number)))
else:
    st.write('Please input number')

hex_number = st.text_input('Please input hexadecimal number (16 base number)', value='0x0')

if hex_number.startswith('0x') and hex_number[2:].isalnum():
    decimal_number = int(hex_number, 16)
    st.write('Decimal of your input number is', str(decimal_number))
else:
    st.write('Please input hexadecimal number')

