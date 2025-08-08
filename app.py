# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Covnert to 16->10 and 10->16, V1.1')

number = st.text_input('Please input decimal number (10 base number)', value='0')

if number.isnumeric():
    st.markdown("Hexadecimal is your input number is " + f":red[{hex(int(number))}]")
else:
    st.markdown("Please input number")

hex_number = st.text_input('Please input hexadecimal number (16 base number)', value='0x0')

if hex_number.startswith('0x') and hex_number[2:].isalnum():
    decimal_number = int(hex_number, 16)
    st.markdown("Decimal of your input number is " + f":red[{str(decimal_number)}]")
else:
    st.markdown("Please input hexadecimal number")

