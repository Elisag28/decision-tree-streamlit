# your code here
import streamlit as st 

def main():
    st.title("My first streamlit")

    # Slider
    name = st.slider("What's your name?", 0, 100, 25)

    # Botón
    if st.button("Hi"):
        st.write(f"Hello {name}!")

if __name__ == "__main__":
    main()