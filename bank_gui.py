import streamlit as st
from bank_system import Bank

bank = Bank()

st.set_page_config(page_title="Python Bank", page_icon="🏦")

st.title("🏦 Welcome to Python Bank")

menu = st.sidebar.radio("Select Operation", [
    "Create Account", 
    "Deposit Money", 
    "Withdraw Money", 
    "View/Update Details", 
    "Delete Account"
])

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Enter your Name")
    email = st.text_input("Enter your Email")
    age = st.number_input("Enter your Age", min_value=0, max_value=100)
    phone = st.text_input("Enter 10-digit Phone Number")
    pin = st.text_input("Enter 4-digit PIN", type="password")

    if st.button("Create Account"):
        if not (name and email and phone and pin):
            st.warning("Please fill all fields.")
        elif len(phone) != 10 or not phone.isdigit():
            st.error("Invalid phone number.")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be 4 digits.")
        elif age < 18:
            st.error("You must be at least 18 years old.")
        else:
            status = bank.create_user_gui(name, email, age, phone, pin)
            st.success(status)

elif menu == "Deposit Money":
    st.subheader("Deposit Money")
    ac = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1)

    if st.button("Deposit"):
        msg = bank.deposit_gui(ac, pin, amount)
        st.info(msg)

elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")
    ac = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Enter Amount", min_value=1)

    if st.button("Withdraw"):
        msg = bank.withdraw_gui(ac, pin, amount)
        st.info(msg)

elif menu == "View/Update Details":
    st.subheader("View or Update Account Details")
    ac = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Fetch Details"):
        user = bank.get_user_gui(ac, pin)
        if user:
            st.json(user)

            with st.form("update_form"):
                name = st.text_input("Update Name", user['name'])
                age = st.text_input("Update Age", user['age'])
                email = st.text_input("Update Email", user['email'])
                phone = st.text_input("Update Phone Number", user['phonenumber'])
                new_pin = st.text_input("Update PIN", user['pin'])
                submit = st.form_submit_button("Update Details")
                if submit:
                    msg = bank.update_user_gui(ac, pin, name, age, email, phone, new_pin)
                    st.success(msg)
        else:
            st.error("Invalid account or PIN")

elif menu == "Delete Account":
    st.subheader("Delete Account")
    ac = st.text_input("Enter Account Number")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Delete Account"):
        msg = bank.delete_user_gui(ac, pin)
        st.warning(msg)