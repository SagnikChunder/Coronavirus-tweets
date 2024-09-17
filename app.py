import streamlit as st 
import pickle
model=pickle.load(open('Text_classification.pkl','rb')) 
st.title("Text Classification Model")
review= st.text_input("Enter the review")
submit=st.button("Predict")
if submit:
    prediction= model.predict([review])
    print(prediction)
    st.write(prediction)
        