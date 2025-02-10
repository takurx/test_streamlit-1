# Ref1, Streamlitを試す（インストールからSreamlitCloudへのデプロイまで）
# https://zenn.dev/mopinfish/articles/try-streamlit

import streamlit as st

st.title('Hello World!')

number = st.text_input('Please input number', '0')

st.write('Square of your input number is', number*number)
