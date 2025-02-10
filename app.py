# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

number = st.text_input('Please input number', '0')

if number.isnumeric():
    square_number = int(number) * int(number)
    st.write('Square of your input number is', str(square_number))
else:
    st.write('Please input number')


