import streamlit as st
import joblib

# -------------------------------
# Load Machine Learning Model
# -------------------------------
model = joblib.load("diabetes_model.pkl")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Diabetes Risk Prediction",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    background-color: #F4F8FB;
}

h1{
    color:#1565C0;
}

.stButton>button{
    width:100%;
    height:60px;
    font-size:20px;
    font-weight:bold;
    border-radius:12px;
    background-color:#1565C0;
    color:white;
}

.stButton>button:hover{
    background-color:#0D47A1;
    color:white;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.title("🏥 AI-Powered Diabetes Risk Prediction System")

st.markdown("""
### Machine Learning Based Healthcare Application

Enter the patient's medical details below to predict the risk of diabetes using a trained Random Forest Machine Learning model.
""")

st.divider()

# -------------------------------
# Patient Information
# -------------------------------

st.subheader("🩺 Patient Medical Information")

col1, col2 = st.columns(2)

with col1:

    preg = st.number_input(
        "Pregnancies",
        min_value=0,
        step=1
    )

    glucose = st.number_input(
        "Glucose Level",
        min_value=0.0
    )

    bp = st.number_input(
        "Blood Pressure (mmHg)",
        min_value=0.0
    )

    skin = st.number_input(
        "Skin Thickness",
        min_value=0.0
    )

with col2:

    insulin = st.number_input(
        "Insulin",
        min_value=0.0
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        format="%.1f"
    )

    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        format="%.3f"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        step=1
    )

st.divider()

# -------------------------------
# Predict Button
# -------------------------------

predict = st.button(
    "🔍 Predict Diabetes Risk",
    use_container_width=True
)

# -------------------------------
# Placeholder
# -------------------------------

if predict:

    # -------------------------------
    # Prepare Input Data
    # -------------------------------

    input_data = [[
        preg,
        glucose,
        bp,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ]]

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    confidence = probability[0][prediction[0]] * 100

    # -------------------------------
    # Prediction Dashboard
    # -------------------------------

    st.divider()

    st.header("📊 Prediction Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction[0] == 1:
            st.error("🔴 HIGH RISK")
        else:
            st.success("🟢 LOW RISK")

    with col2:

        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )

    with col3:

        if confidence >= 90:
            level = "Very High"
        elif confidence >= 75:
            level = "High"
        elif confidence >= 60:
            level = "Moderate"
        else:
            level = "Low"

        st.metric(
            "Prediction Reliability",
            level
        )

    st.progress(confidence/100)

    st.write(f"### Confidence Score : {confidence:.2f}%")

    st.divider()

    # -------------------------------
    # BMI Category
    # -------------------------------

    st.subheader("🧮 BMI Analysis")

    if bmi < 18.5:
        bmi_status = "🔵 Underweight"

    elif bmi < 25:
        bmi_status = "🟢 Normal Weight"

    elif bmi < 30:
        bmi_status = "🟠 Overweight"

    else:
        bmi_status = "🔴 Obese"

    st.info(f"**BMI Category : {bmi_status}**")

    st.divider()

    # -------------------------------
    # Health Indicators
    # -------------------------------

    st.subheader("❤️ Health Indicators")

    c1, c2 = st.columns(2)

    with c1:

        if glucose < 100:
            st.success("🟢 Glucose : Normal")
        elif glucose < 126:
            st.warning("🟡 Glucose : Prediabetic")
        else:
            st.error("🔴 Glucose : High")

        if bp < 80:
            st.success("🟢 Blood Pressure : Normal")
        elif bp < 90:
            st.warning("🟡 Blood Pressure : Elevated")
        else:
            st.error("🔴 Blood Pressure : High")

    with c2:

        if bmi < 25:
            st.success("🟢 BMI : Healthy")
        elif bmi < 30:
            st.warning("🟡 BMI : Overweight")
        else:
            st.error("🔴 BMI : Obese")

        if age < 35:
            st.success("🟢 Age Risk : Low")
        elif age < 50:
            st.warning("🟡 Age Risk : Moderate")
        else:
            st.error("🔴 Age Risk : High")

    st.divider()

    # -------------------------------
    # Patient Summary
    # -------------------------------

    st.header("📋 Patient Summary")

    a, b, c, d = st.columns(4)

    a.metric("Age", age)
    b.metric("BMI", bmi)
    c.metric("Glucose", glucose)
    d.metric("Blood Pressure", bp)

    e, f, g, h = st.columns(4)

    e.metric("Pregnancies", preg)
    f.metric("Skin", skin)
    g.metric("Insulin", insulin)
    h.metric("DPF", round(dpf,3))

    st.divider()

    # -------------------------------
    # Recommendations
    # -------------------------------

    st.header("❤️ Personalized Health Recommendations")

    if prediction[0] == 1:

        st.error("High diabetes risk detected.")

        st.markdown("""
✅ Reduce sugar intake

✅ Walk at least 30 minutes daily

✅ Maintain a healthy weight

✅ Drink 2–3 litres of water

✅ Avoid junk food

✅ Consult a doctor for blood sugar testing

✅ Monitor glucose regularly
""")

    else:

        st.success("Your health indicators look good.")

        st.markdown("""
✅ Continue healthy eating

✅ Exercise regularly

✅ Drink enough water

✅ Maintain your weight

✅ Get annual health checkups

✅ Avoid excessive sugary drinks
""")

    st.divider()

    st.info(
        "⚠️ This prediction is generated using a Machine Learning model and is intended for educational purposes only. Please consult a healthcare professional for medical advice."
    )
