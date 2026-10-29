import streamlit as st 
import pandas as pd 
import joblib

# loading the model 
with open('D:/CODING/ML using Python/Venv/Code/projects/placement_predictor.joblib', 'rb') as f:
    model = joblib.load(f)

st.set_page_config(
    page_title="Campus Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Placement Predictor")
st.subheader("_This is a Machine Learning model which can predict the plcaement of student based on the data provided by student._")
with st.container(border=True):
    st.write('''**_This Machine learning model is trained on the placement dataset of students.
                This is only just a simple model and may not be 100% accurate. So, please use the predictions for reference only._**''')
st.divider()

def user_input():
        col1, col2 = st.columns(2)
        with col1:
            st.write("Technical and Academic skills:- ")
            st.session_state.cgpa = st.number_input("What is your CGPA (Cumulative Grade Point Average)", min_value=0.0000, max_value=11.0000)
            st.session_state.sgpa = st.number_input("What is your SGPA (Previuos Semester Grade Point Average)", min_value=0.0000, max_value=11.0000)
            st.session_state.iq = st.number_input("What is your IQ Level (Intelligence Quotient) in Grade points",min_value=0, max_value=160)
            st.session_state.academic = st.number_input("What is your Academic Score in Grade points (1 to 10)", min_value=1, max_value=10)

        with col2:
            st.write("Soft and Professional skills:- ")
            st.session_state.comm_skill = st.number_input('What is your Commmunication skill score in Grade points (1 to 10)',min_value=1.00, max_value=10.00)
            st.session_state.extra = st.number_input("What is your Extra Curricular Activities score in Grade points (0 to 10)", min_value=0, max_value=10)
            st.session_state.projects = st.number_input('How many projects you have done in your academic or professional career (in numbers)', min_value=0)
            st.session_state.intern = st.selectbox("Have you done any Internship? (Yes/No)", options=['Yes', 'No'])
        st.divider()

        if st.session_state.intern == 'Yes':
            st.session_state.intern = 1
        else:
            st.session_state.intern = 0

        features = {
             'IQ': [st.session_state.iq],
             'Prev_Sem_Result':[st.session_state.sgpa],
             'CGPA': [st.session_state.cgpa],
             'Academic_Performance':[st.session_state.academic],
             'Extra_Curricular_Score':[st.session_state.extra],
             'Communication_Skills':[st.session_state.comm_skill],
             'Projects_Completed':[st.session_state.projects],
             'Internship_Experience_Yes':[st.session_state.intern]
        }
        return pd.DataFrame(features, index=[0])
            
input_df = user_input()

if 'prediction' not in st.session_state:
    st.session_state.prediction = None

if st.button("Predict Placement"):
    #if input_df.isnull().values.any() or (input_df == 0).values.any():
     #   st.warning(
      #      "Please fill all values properly before predicting the placement."
       # )
    #else:
        st.session_state.prediction = model.predict(input_df)

if st.session_state.prediction is not None:
    if st.session_state.prediction[0] == 1:
        st.success("Congratulations! You are likely to get placed.")
    else:
            st.error("Sorry! You are not likely to get placed.")

if 'probablity' not in st.session_state:
    st.session_state.probablity = None

if st.button("Probablity of Placement"):
    #if input_df.isnull().values.any() or (input_df == 0).values.any():
     #   st.warning(
      #      "Please fill all values properly before predicting the placement."
       # )
    #else:
        st.session_state.probablity = model.predict_proba(input_df)

if st.session_state.probablity is not None:
    st.write(f"**Probablity of getting placed is:- {st.session_state.probablity[0][1]*100:.2f}%**")
    st.write(f"**Probablity of not getting placed is:- {st.session_state.probablity[0][0]*100:.2f}%**")

if st.button('Clear',help='Click to clear the results'):
    st.session_state.prediction = None
    st.session_state.probablity = None
    st.rerun()
