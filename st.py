import streamlit as st
import pickle
import numpy as np

# Load model
with open('log_reg.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Titanic Survival Prediction", layout="centered")
st.title('🚢 Titanic Survival Prediction App')
st.markdown("Predict whether a Titanic passenger would survive based on their details.")

# Input UI
pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3])
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.slider('Age', min_value=0, max_value=100, value=25)
sibsp = st.number_input('Siblings/Spouses Aboard (SibSp)', min_value=0, max_value=10, value=0)
parch = st.number_input('Parents/Children Aboard (Parch)', min_value=0, max_value=10, value=0)
fare = st.slider('Fare Paid (in $)', min_value=0.0, max_value=512.0, value=50.0, step=0.5)
embarked = st.selectbox('Port of Embarkation', ['C', 'Q', 'S'])

# Convert inputs
sex_numeric = 0 if sex == 'Male' else 1
embarked_Q = 1 if embarked == 'Q' else 0
embarked_S = 1 if embarked == 'S' else 0

# Final input format
input_data = np.array([[pclass, sex_numeric, age, sibsp, parch, fare, embarked_Q, embarked_S]])

prediction = None

if st.button('Predict'):
    try:
        prediction = model.predict(input_data)
    except Exception as e:
        st.error(f"Error during prediction: {e}")

if prediction is not None:
    st.markdown("### 🎯 Prediction Result:")
    st.success("✅ Survived" if prediction[0] == 1 else "❌ Did Not Survive")
    st.write(f"Predicted Survival: {'Yes' if prediction[0] == 1 else 'No'}")

