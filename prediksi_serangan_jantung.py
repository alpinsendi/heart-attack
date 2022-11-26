import pickle
import streamlit as st

prediksi = pickle.load(open('heart-model.sav', 'rb'))

st.title ('Skrining serangan Jantung Menggunakan SVM')

Age= st.text_input('Age')
Sex= st.text_input(' Male = 1/ famale = 0')
ChestPainType= st.text_input('Chest Pain Type')
CP= st.text_input ('BP')
Cholestrol= st.text_input('Colestrol')
FBSOper= st.text_input('gula darah')
Restecg= st.text_input('EKG')
Thalach= st.text_input('Max HR')
ExerciseAngina= st.text_input('Exercise angina')
Depression= st.text_input('Depression')
SlopeOfSt= st.text_input('Slope of St')
Caa= st.text_input('Number of Vessels Fluro')
Thallium= st.text_input('Thalium')


Heart_Diag = ''

if st.button('Test serangan janutng'):
    heart_predi = prediksi.predict([[Age, Sex, ChestPainType, CP, Cholestrol, FBSOper, Restecg, Thalach, ExerciseAngina, Depression, SlopeOfSt, Caa, Thallium]])

    if(heart_predi[0] == 1):
        Heart_Diag = 'Faktor resiko serangan jantung'
    else : 
        Heart_Diag = 'Faktor resiko tidak terkena serangan jantung'
    st.success(Heart_Diag)
