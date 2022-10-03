import pandas as pd
import numpy as np
import pyDOE2 as doe
import seaborn as sns

# Matriz de ensaios com planejamento fatorial com 2 variáveis
ensaios = doe.ff2n(2)

df_ensaios = pd.DataFrame(ensaios, columns=['farinha', 'chocolate'])

# Resultado dos ensaios no dataframe (quantidade de cupcakes)
df_ensaios['quantidade'] = [19, 37, 24, 49]
