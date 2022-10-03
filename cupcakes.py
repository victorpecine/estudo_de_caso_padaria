from statistics import mode
import pandas as pd
import pyDOE2 as doe
import statsmodels.api as sm
import statsmodels.formula.api as smf


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
