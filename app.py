import pandas as pd
import streamlit as st
import joblib

st.title(':orange[Bankruptcy Prediction]')

st.subheader(':blue[User Input Parameters]')

def user_input_features():
    industrial_risk_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}
    management_risk_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}
    financial_flexibility_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}
    credibility_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}
    competitiveness_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}
    operating_risk_Mapping = {'Low': 0, 'Medium': 0.5, 'High': 1}

    col1, col2 = st.columns(2)

    with col1:
        industrial_risk = st.selectbox('Industrial Risk:', list(industrial_risk_Mapping.keys()), index=0)
        industrial_risk_Numeric = industrial_risk_Mapping[industrial_risk]

        management_risk = st.selectbox("Management Risk", list(management_risk_Mapping.keys()), index=0)
        management_risk_Numeric = management_risk_Mapping[management_risk]

        financial_flexibility = st.selectbox("Financial Flexibility", list(financial_flexibility_Mapping.keys()), index=0)
        financial_flexibility_Numeric = financial_flexibility_Mapping[financial_flexibility]

    with col2:
        credibility = st.selectbox("Credibility", list(credibility_Mapping.keys()), index=0)
        credibility_Numeric = credibility_Mapping[credibility]

        competitiveness = st.selectbox("Competitiveness", list(competitiveness_Mapping.keys()), index=0)
        competitiveness_Numeric = competitiveness_Mapping[competitiveness]

        operating_risk = st.selectbox("Operating Risk", list(operating_risk_Mapping.keys()), index=0)
        operating_risk_Numeric = operating_risk_Mapping[operating_risk]

    data = {'industrial_risk': industrial_risk_Numeric,
            'management_risk': management_risk_Numeric,
            'financial_flexibility': financial_flexibility_Numeric,
            'credibility': credibility_Numeric,
            'competitiveness': competitiveness_Numeric,
            'operating_risk': operating_risk_Numeric}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.write(df)


if st.button('Predict'):
    
    loaded_model = joblib.load("model.joblib")

    prediction = loaded_model.predict(df)
   
    result = ":red[Bankruptcy]" if prediction[0] == 0 else ":green[Non-Bankruptcy]"
    
    st.subheader('Predicted Result')
    st.write(result)
