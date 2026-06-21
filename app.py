import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)
if st.button("Calculate"):
    if operation == "Addition":
        st.success(num1 + num2)

    elif operation == "Subtraction":
        st.success(num1 - num2)

    elif operation == "Multiplication":
        st.success(num1 * num2)

    elif operation == "Division":
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Cannot divide by zero!")