import pickle
import streamlit as st

st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    model = pickle.load(open('model.pickle', 'rb'))
    r = model.predict([[a]])[0]
    st.write(r)
