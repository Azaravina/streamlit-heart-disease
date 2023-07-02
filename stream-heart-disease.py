import pickle
import streamlit as st

#Load model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Penyakit Jantung')


#Edith Colomn
col1, col2 = st.columns(2)

with col1 :
    age                     = st.text_input ('Input data Age')

with col2 :
    BP                      = st.text_input ('Input data Blood Pressure')

with col1 :
    cholestrol              = st.text_input ('Input data Cholestrol')

#For Prediction
heart_diagnosis = ''

#Button
if st.button('Prediksi Heart Disease'):
    heart_prediction = heart_disease_model.predict([[age, BP, cholestrol]])

    if(heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien terkena penyakit Jantung'
    else :
        heart_diagnosis = 'Pasien tidak mempunyai penyakit Jantung'
      
    st.success(heart_diagnosis)
