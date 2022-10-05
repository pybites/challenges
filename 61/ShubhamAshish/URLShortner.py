import streamlit as st
import pyperclip
import pyshorteners



st.title("URL Shortner")
st.write("Enter the URL to shorten")
url = st.text_input("URL")
if st.button("Shorten"):
    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(url)
    st.write(x)
    pyperclip.copy(x)
    st.success('Copied to clipboard')
