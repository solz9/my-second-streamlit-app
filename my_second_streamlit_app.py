import pickle
import streamlit as st

st.title('Revenue Prediction')
a = st.number_input('Input Temperature')
if st.button('Predict'):
    model = pickle.load(open('model.pickle', 'rb'))
    st.write(model.predict([[a]]))

  
