import streamlit as st
st.title('Revenue Prediction')
a = st.number('Input Temperature')
if st.button('Predict'):
    y_pred = model.predict(x)
st.write(y_pred)