import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model_bmi.pkl')

# Mapping hasil prediksi ke label
label_mapping = {
    0: 'Sangat Kurus',
    1: 'Kurus',
    2: 'Normal',
    3: 'Kelebihan Berat Badan',
    4: 'Obesitas',
    5: 'Sangat Obesitas'
}

st.title("Prediksi Status Berat Badan (SVM)")

st.write("Masukkan data berikut untuk memprediksi status berat badan:")

gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
height = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0)
weight = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0)

if st.button("Prediksi"):
    # Encoding gender
    gender_encoded = 1 if gender == 'Male' else 0
    
    # Buat DataFrame
    input_data = pd.DataFrame([[gender_encoded, height, weight]],
                              columns=['Gender', 'Height', 'Weight'])

    # Prediksi
    predicted = model.predict(input_data)[0]
    label = label_mapping.get(predicted, 'Tidak diketahui')

    st.success(f"Status berat badan: **{label}**")
