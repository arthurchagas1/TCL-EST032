import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Funções para gerar amostras e calcular médias
def generate_samples(distribution, params, m, n):
    if distribution == 'Binomial':
        return np.random.binomial(n, params['p'], (m, n))
    elif distribution == 'Exponencial':
        return np.random.exponential(1/params['lambda'], (m, n))
    elif distribution == 'Uniforme':
        return np.random.uniform(params['a'], params['b'], (m, n))

def calculate_sample_means(samples):
    return np.mean(samples, axis=1)

# Configuração da interface Streamlit
st.title("Simulação de Distribuições de Probabilidade")

# Seleção da distribuição
distribution = st.selectbox("Escolha a distribuição", ['Binomial', 'Exponencial', 'Uniforme'])

# Parâmetros para cada distribuição
params = {}
if distribution == 'Binomial':
    params['p'] = st.slider('Probabilidade de sucesso (p)', 0.0, 1.0, 0.5)
elif distribution == 'Exponencial':
    params['lambda'] = st.slider('Taxa (lambda)', 0.1, 10.0, 1.0)
elif distribution == 'Uniforme':
    params['a'] = st.slider('Limite inferior (a)', 0.0, 10.0, 0.0)
    params['b'] = st.slider('Limite superior (b)', 0.0, 10.0, 5.0)

# Número de amostras e tamanho de cada amostra
m = st.slider('Número de amostras (m)', 1, 1000, 100)
n = st.slider('Tamanho de cada amostra (n)', 1, 100, 10)

# Botão para gerar amostras
if st.button('Gerar Amostras'):
    samples = generate_samples(distribution, params, m, n)
    sample_means = calculate_sample_means(samples)

    # Plot dos histogramas
    fig, ax = plt.subplots()
    ax.hist(samples.flatten(), bins='auto', density=True, alpha=0.7, label='Amostras')
    ax.hist(sample_means, bins='auto', density=True, alpha=0.7, label='Médias Amostrais')
    ax.legend()
    st.pyplot(fig)

