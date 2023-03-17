import pickle
import streamlit as st
filename = 'model.pickle'

model = pickle.load(open(filename, "rb"))
st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    model = pickle.load(open('revenue_prediction.pickle', 'rb'))
    st.write(model.predict(a))
