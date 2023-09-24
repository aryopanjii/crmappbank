st.title('Bank Customer Churn Prediction')
credit_score = st.number_input('Credit Score')
country = st.text_input('Country')
gender = st.text_input('Gender')
age = st.number_input('Age')
tenure = st.number_input('Tenure')
balance = st.number_input('Balance')
products_number = st.number_input('Products Number')
credit_card = st.number_input('Credit Card')
active_member = st.number_input('Active Member')
estimated_salary = st.number_input('Estimated Salary')

if st.button('Predict'):
    pred = prediction(credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary)

    if pred is not None:
        if pred == 1:
            st.write("The customer has left.")
        else:
            st.write("The customer is still active.")
