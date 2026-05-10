
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import statsmodels.api as sm

# --- Load the exported components ---
# Make sure these files are in the same directory as your app.py when deploying
loaded_model = joblib.load('ols_regression_model_final.joblib')
loaded_processar_string = joblib.load('processar_string_func.joblib')

# --- Streamlit App Layout ---
st.set_page_config(page_title="Previsão de Preço Unitário de Terrenos", layout="centered")
st.title("🏡 Previsão de Preço Unitário de Terrenos")
st.markdown("--- ---")

st.write("### Insira os dados para prever o preço unitário do terreno")

# Input fields for user
area_input = st.number_input("Área (m²)", min_value=1.0, value=1000.0, step=100.0, format="%.2f")
ids_input = st.number_input("IDS (Índice de Desenvolvimento Social)", min_value=0.0, max_value=1.0, value=0.6, step=0.01, format="%.2f")
indic_rendaresp_pos_sm_input = st.number_input("INDIC_RENDARESP_POS_SM (Indicador de Renda Responsável por Salário Mínimo)", min_value=0.0, value=5.0, step=0.1, format="%.2f")

if st.button("Calcular Preço Unitário"):
    # Prepare the input data for prediction
    # Apply log1p transformation to Area, as used in training
    log_area = np.log1p(area_input)

    # Create a DataFrame from the inputs
    input_data = pd.DataFrame({
        'log_Area': [log_area],
        'IDS': [ids_input],
        'INDIC_RENDARESP_POS_SM': [indic_rendaresp_pos_sm_input]
    })

    # Add a constant term to the input data, as the OLS model expects it
    input_data_with_const = sm.add_constant(input_data)

    # Make prediction using the loaded OLS model
    predicted_log_unit_price = loaded_model.predict(input_data_with_const)

    # Inverse transform the prediction to get the original Unit_Price scale
    # Use np.expm1 because np.log1p was used for transformation
    predicted_unit_price = np.expm1(predicted_log_unit_price[0])

    st.success(f"O Preço Unitário Previsto é: R$ {predicted_unit_price:,.2f}/m²")

st.markdown("--- ---")
st.write("### Demonstração da Função `processar_string`")

# Input for the processar_string function demonstration
string_to_process = st.text_input("Digite uma string para processar (acentos e maiúsculas):", "Botafogó")
processed_string = loaded_processar_string(string_to_process)
st.write(f"String Original: `{string_to_process}`")
st.write(f"String Processada: `{processed_string}`")

st.markdown("--- ---")
st.info("Para executar este aplicativo Streamlit, salve-o como `app.py` e execute `streamlit run app.py` no seu terminal (após instalar o Streamlit: `pip install streamlit`).")
