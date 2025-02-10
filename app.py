# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

number = st.text_input('Please input number', '0')

square_number = number * number

st.write('Square of your input number is', square_number)

