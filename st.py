import streamlit as st
import pickle
import numpy as np

# Load model
with open('log_reg.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('🚢 Titanic Survival Prediction')

# Input UI
pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3])
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.slider('Age', 0, 100, 25)
sibsp = st.number_input('Siblings/Spouses Aboard (SibSp)', 0, 10, 0)
parch = st.number_input('Parents/Children Aboard (Parch)', 0, 10, 0)
fare = st.slider('Fare', 0.0, 512.0, 100.0)
embarked = st.selectbox('Port of Embarkation', ['C', 'Q', 'S'])

# Convert inputs
sex_numeric = 0 if sex == 'Male' else 1
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

# Final input format
input_data = np.array([[pclass, sex_numeric, age, sibsp, parch, fare, embarked_Q, embarked_S]])

# Predict button
if st.button('Predict'):
    try:
        prediction = model.predict(input_data)
        st.success('Prediction: 🎉 Survived' if prediction[0] == 1 else 'Prediction: ❌ Did Not Survive')
    except Exception as e:
        st.error(f"Error: {e}")
