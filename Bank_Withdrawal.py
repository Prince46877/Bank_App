elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    name = st.text_input("Account Name", key='name_input', value=get_input_value('name_input'))
    acc_type = st.selectbox(
        "Account Type",
        ["Savings", "Current"],
        key='type_input',
        index=0 if get_input_value('type_input') == "Savings" else 1
    )
    amount = st.number_input("Amount to Withdraw", min_value=0.0, key='amount_input', value=0.0)

    if st.button("Withdraw"):
        key = name.strip().lower()
        if key in accounts:
            account = accounts[key]
            if account.acc_type == acc_type:
                st.success(account.withdraw(amount))
            else:
                st.error(f"Account type mismatch! This is a {account.acc_type} account.")
        else:
            st.error("Account not found.")

        # Reset input fields after transaction
        st.session_state['reset'] = True