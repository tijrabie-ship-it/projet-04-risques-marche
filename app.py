import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# 1. تدريب النموذج (كما في السابق)
@st.cache_resource
def train_model():
    data = {
        'Make': ['Renault', 'Renault', 'Dacia', 'Dacia', 'Volkswagen', 'Volkswagen', 'Toyota', 'Toyota', 'Hyundai', 'Hyundai', 'Mercedes', 'Mercedes'],
        'Model': ['Clio', 'Megane', 'Sandero', 'Duster', 'Golf', 'Passat', 'Yaris', 'Corolla', 'i10', 'Tucson', 'Class A', 'Class E'],
        'Year': [2020, 2021, 2019, 2022, 2020, 2021, 2022, 2021, 2020, 2023, 2021, 2022],
        'Mileage': [50000, 40000, 60000, 30000, 45000, 35000, 20000, 25000, 40000, 15000, 30000, 25000],
        'Price': [120000, 160000, 90000, 150000, 190000, 260000, 140000, 180000, 95000, 220000, 320000, 480000]
    }
    df = pd.DataFrame(data)
    df_encoded = pd.get_dummies(df, columns=['Make', 'Model'])
    X = df_encoded.drop('Price', axis=1)
    y = df_encoded['Price']
    model = RandomForestRegressor().fit(X, y)
    return model, X.columns

model, feature_names = train_model()

# 2. الواجهة التفاعلية
st.title("📊 نظام إدارة المخاطر السوقية للمرابحة")
st.sidebar.header("إعدادات التقييم")

# إضافة تأثير الاقتصاد الكلي
market_status = st.sidebar.select_slider(
    "حالة السوق الاقتصادية",
    options=["كساد حاد", "كساد طفيف", "مستقر", "تضخم طفيف", "تضخم مرتفع"],
    value="مستقر"
)

market_impact = {
    "كساد حاد": 0.80, "كساد طفيف": 0.90, "مستقر": 1.0,
    "تضخم طفيف": 1.05, "تضخم مرتفع": 1.15
}

data_structure = {
    'Renault': ['Clio', 'Megane'], 'Dacia': ['Sandero', 'Duster'],
    'Volkswagen': ['Golf', 'Passat'], 'Toyota': ['Yaris', 'Corolla'],
    'Hyundai': ['i10', 'Tucson'], 'Mercedes': ['Class A', 'Class E']
}

selected_make = st.sidebar.selectbox("الماركة", list(data_structure.keys()))
selected_model = st.sidebar.selectbox("الطراز", data_structure[selected_make])
year = st.sidebar.slider("سنة الصنع", 2015, 2026, 2020)
mileage = st.sidebar.number_input("المسافة (كم)", 0, 300000, 50000)
price = st.sidebar.number_input("سعر الشراء المقترح (درهم)", 20000, 1000000, 150000)

# 3. محرك القرار مع التعديل الاقتصادي
if st.button("تحليل مستوى المخاطرة"):
    input_data = pd.DataFrame(0, index=[0], columns=feature_names)
    input_data['Year'] = year
    input_data['Mileage'] = mileage
    input_data[f'Make_{selected_make}'] = 1
    input_data[f'Model_{selected_model}'] = 1
    
    # التنبؤ الأساسي ثم التعديل حسب حالة السوق
    base_pred = model.predict(input_data)[0]
    final_pred = base_pred * market_impact[market_status]
    
    margin = (final_pred - price) / final_pred
    
    st.write(f"### السعر العادل في ظل سوق ({market_status}): {final_pred:,.2f} درهم")
    
    if margin < -0.15:
        st.error("خطر مرتفع: السعر المقترح مبالغ فيه!")
    elif margin < -0.05:
        st.warning("خطر متوسط: تأكد من حالة السيارة.")
    else:
        st.balloons()
        st.success("عملية آمنة.")