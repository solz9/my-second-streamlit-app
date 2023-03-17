import pickle
import streamlit as st
filename = 'model.pickle'


model = pickle.load(open(filename, "rb"))
st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    y_pred = model.predict(a)
    st.write(y_pred)