import pickle
import streamlit as st

st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    b = open('model.pickle','rb')
    model = pickle.load(b)
    st.write(model.predict(a))
