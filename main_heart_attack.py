import pickle
import streamlit as st

prediksi = pickle.load(open('model-heart-attack.sav', 'rb'))

st.title ('Skrining serangan Jantung Menggunakan SVM')

st.text('HANYA FORMAT ANGKA YANG BISA DIOLAH...!!!!')

Age= st.text_input('Input Age')
Sex= st.text_input('Input Gender Male = 1/ famale = 0')
ChestPainType= st.text_input('Input Chest Pain Type')
CP= st.text_input ('Input BP')
Cholestrol= st.text_input('InputColestrol')
FBSOper= st.text_input('Input FBS Over')
Restecg= st.text_input('Input EKG')
Thalach= st.text_input('Input Max HR')
ExerciseAngina= st.text_input('Input Exercise angina')
Depression= st.text_input('Input Depression')
SlopeOfSt= st.text_input('Input Slope of St')
Caa= st.text_input('Input Number of Vessels Fluro')
Thallium= st.text_input('Input Thalium')


Heart_Diag = ''

if st.button('Test serangan jantung'):
    heart_predi = prediksi.predict([[Age, Sex, ChestPainType, CP, Cholestrol, FBSOper, Restecg, Thalach, ExerciseAngina, Depression, SlopeOfSt, Caa, Thallium]])

    if(heart_predi[0] == 1):
        Heart_Diag = 'Faktor resiko serangan jantung'
    else : 
        Heart_Diag = 'Faktor resiko tidak terkena serangan jantung'
    st.success(Heart_Diag)
