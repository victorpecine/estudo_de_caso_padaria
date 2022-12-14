from dis import dis
from statistics import mode
from turtle import color
import numpy as np
import pandas as pd
import pyDOE2 as doe
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm


# Matriz de ensaios com planejamento fatorial com 2 variáveis
ensaios = doe.ff2n(2)

df_ensaios = pd.DataFrame(ensaios, columns=['farinha', 'chocolate'])

# Resultado dos ensaios no dataframe (quantidade de cupcakes)
df_ensaios['quantidade'] = [19, 37, 24, 49]


# Modelo estatístico
modelo = smf.ols(data=df_ensaios, formula='quantidade ~ farinha + chocolate + farinha:chocolate')
# ~ representa igualdade
# : representa interação entre variáveis

modelo_ajustado = modelo.fit()
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:             quantidade   R-squared:                       1.000
# Model:                            OLS   Adj. R-squared:                    nan
# Method:                 Least Squares   F-statistic:                       nan
# Date:                Mon, 03 Oct 2022   Prob (F-statistic):                nan
# Time:                        19:12:47   Log-Likelihood:                 126.02
# No. Observations:                   4   AIC:                            -244.0
# Df Residuals:                       0   BIC:                            -246.5
# Df Model:                           3
# Covariance Type:            nonrobust
# =====================================================================================
#                         coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------
# Intercept            32.2500        inf          0        nan         nan         nan
# farinha              10.7500        inf          0        nan         nan         nan
# chocolate             4.2500        inf          0        nan         nan         nan
# farinha:chocolate     1.7500        inf          0        nan         nan         nan
# ==============================================================================
# Omnibus:                          nan   Durbin-Watson:                   1.500
# Prob(Omnibus):                    nan   Jarque-Bera (JB):                0.167
# Skew:                           0.000   Prob(JB):                        0.920
# Kurtosis:                       2.000   Cond. No.                         1.00
# ==============================================================================

# Graus de liberdade = 0

# Aumento dos graus de liberdade (1 kg de farinha, 0,3 kg de chocolate)
centro_area_experimentacao = np.array([[0, 0, 29],
                                       [0, 0, 30],
                                       [0, 0, 29],
                                       [0, 0, 30]])

df_centro = pd.DataFrame(centro_area_experimentacao, columns=['farinha', 'chocolate', 'quantidade'], index=[4, 5, 6, 7])


# Mescla dos dataframes
df_ensaios = pd.concat([df_ensaios, df_centro])


# Novo modelo para teste de significância estatística
modelo = smf.ols(data=df_ensaios, formula='quantidade ~ farinha + chocolate + farinha:chocolate')

modelo_ajustado = modelo.fit()
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:             quantidade   R-squared:                       0.971
# Model:                            OLS   Adj. R-squared:                  0.950
# Method:                 Least Squares   F-statistic:                     45.21
# Date:                Mon, 03 Oct 2022   Prob (F-statistic):            0.00152
# Time:                        19:47:35   Log-Likelihood:                -14.155
# No. Observations:                   8   AIC:                             36.31
# Df Residuals:                       4   BIC:                             36.63
# Df Model:                           3
# Covariance Type:            nonrobust
# =====================================================================================
#                         coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------
# Intercept            30.8750      0.710     43.494      0.000      28.904      32.846
# farinha              10.7500      1.004     10.708      0.000       7.963      13.537
# chocolate             4.2500      1.004      4.233      0.013       1.463       7.037
# farinha:chocolate     1.7500      1.004      1.743      0.156      -1.037       4.537
# ==============================================================================
# Omnibus:                        4.655   Durbin-Watson:                   0.841
# Prob(Omnibus):                  0.098   Jarque-Bera (JB):                1.080
# Skew:                          -0.180   Prob(JB):                        0.583
# Kurtosis:                       1.237   Cond. No.                         1.41
# ==============================================================================

# Graus de liberdade = 4
# A hipótese da variável de relação farinha:chocolate deve ser removida do modelo por ter um p_valor > 0,05 (significância)


# Modelo atualizado sem a variável de relação farinha:chocolate
modelo_atualizado = smf.ols(data=df_ensaios, formula='quantidade ~ farinha + chocolate')

modelo_atualizado_ajustado = modelo_atualizado.fit()
#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:             quantidade   R-squared:                       0.950
# Model:                            OLS   Adj. R-squared:                  0.929
# Method:                 Least Squares   F-statistic:                     47.09
# Date:                Mon, 03 Oct 2022   Prob (F-statistic):           0.000571
# Time:                        23:04:38   Log-Likelihood:                -16.416
# No. Observations:                   8   AIC:                             38.83
# Df Residuals:                       5   BIC:                             39.07
# Df Model:                           2
# Covariance Type:            nonrobust
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept     30.8750      0.842     36.658      0.000      28.710      33.040
# farinha       10.7500      1.191      9.025      0.000       7.688      13.812
# chocolate      4.2500      1.191      3.568      0.016       1.188       7.312
# ==============================================================================
# Omnibus:                        2.106   Durbin-Watson:                   1.850
# Prob(Omnibus):                  0.349   Jarque-Bera (JB):                1.245
# Skew:                           0.868   Prob(JB):                        0.537
# Kurtosis:                       2.153   Cond. No.                         1.41
# ==============================================================================

# Graus de liberdade = 5


coeficientes_ajustados = modelo_atualizado_ajustado.params

# Função baseada no modelo para calcular a quantidade de cupcakes
def receita(farinha, chocolate):
    limite_normalizado = [-1, 1]
    limite_farinha = [0.5, 1.5]
    limite_chocolate = [0.1, 0.5]

    # Conversão dos valores reais em valores normalizados
    farinha_normalizada = np.interp(farinha, limite_farinha, limite_normalizado)

    chocolate_normalizada = np.interp(chocolate, limite_chocolate, limite_normalizado)

    quantidade = coeficientes_ajustados['Intercept'] + coeficientes_ajustados['farinha'] * farinha_normalizada + coeficientes_ajustados['chocolate'] * chocolate_normalizada

    return math.floor(quantidade)


# Mapa de calor
x_farinha = np.linspace(start=0.5, stop=1.5, num=10)

x_chocolate = np.linspace(start=0.1, stop=0.5, num=10)


pontos = []

for cont_1 in x_farinha:
    temp = [] # Lista temporária

    for cont_2 in x_chocolate:
        temp.append(receita(cont_1, cont_2))
    
    pontos.append(temp)


# Configurações do mapa de calor
plt.figure(figsize=(18, 10))

plt.xlabel('Farinha (kg)', fontsize=14)

plt.ylabel('Chocolate (kg)', fontsize=14)

plt.tick_params(axis='both', labelsize=14)


mapa_cor = plt.imshow(pontos, cmap=cm.rainbow, interpolation='quadric', extent=(0.5, 1.5, 0.1, 0.5), origin='lower',)


# Barra de cor
plt.colorbar().set_label('Quantidade', fontsize=14)


# Isolinhas
linhas = plt.contour(x_farinha, x_chocolate, pontos, colors='k', linewidths=1.5)

plt.clabel(linhas, inline=True, fontsize=14, inline_spacing=10)


plt.savefig('graficos/mapa_de_calor.png')
