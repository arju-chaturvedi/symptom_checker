import streamlit as st
from main import process_symptoms

st.title("🩺 AI-Powered Symptom Checker")

user_input = st.text_area("Describe your symptoms:")

if st.button("Get Diagnosis"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = process_symptoms(user_input)

            st.subheader("Summary of Symptoms")
            st.write(result.get("summary", "N/A"))

            st.subheader("Possible Conditions")
            conditions = result.get("conditions", [])
            if isinstance(conditions, list):
                for cond in conditions:
                    st.markdown(f"- {cond}")
            else:
                st.write(conditions)

            st.subheader("Recommended Specialist")
            st.write(result.get("specialist", "N/A"))
    else:
        st.warning("Please describe your symptoms first.")
