import streamlit as st
import pickle

# Load the trained model from the pickle file
with open('log_reg.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Titanic Survival Prediction')

# Input fields for the features
pclass = st.selectbox('Pclass', [1, 2, 3])
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.slider('Age', 0, 100, 25)
sibsp = st.number_input('SibSp', min_value=0, max_value=10, value=0)
parch = st.number_input('Parch', min_value=0, max_value=10, value=0)
fare = st.slider('Fare', 0.0, 512.00,100.00, format="%.2f")
embarked = st.selectbox('Embarked',['Q','C','S'])

# Convert categorical variables to numeric
sex_numeric = 1 if sex == 'Male' else 0

# Map embarked to numeric values
if embarked == 'C':
    embarked = 0
elif embarked == 'Q':
    embarked = 1
elif embarked == 'S':
    embarked = 2


# Prepare the input data
input_data = [[pclass, sex_numeric, age, sibsp, parch, fare, embarked]]

# Make prediction
if st.button('Predict'):
    try:
        prediction = model.predict(input_data)
        if prediction == 0:
            st.write('Prediction: Not Survived')
        else:
            st.write('Prediction: Survived')
    except Exception as e:
        st.write(f"Error: {e}")
