import pandas as pd
import numpy as np
import pyDOE2 as doe
import seaborn as sns

# Matriz de ensaios com planejamento fatorial com 2 variáveis
ensaios = doe.ff2n(2)

df_ensaios = pd.DataFrame(ensaios, columns=['farinha', 'chocolate'])

# Resultado dos ensaios no dataframe (quantidade de cupcakes)
df_ensaios['quantidade'] = [19, 37, 24, 49]


# Análises gráficas
sns.set_palette('terrain')

sns.set_style('darkgrid')

# Farinha
ax1 = sns.lmplot(data=df_ensaios, x='farinha', y='quantidade', ci=False, hue='chocolate')

ax1.set(xticks=(-1, 1))

ax1.set_xlabels('Farinha')

ax1.set_ylabels('Quantidade de cupcakes')

ax1.savefig('graficos/farinha_qtd_cupcakes.png')

# Chocolate
ax2 = sns.lmplot(data=df_ensaios, x='chocolate', y='quantidade', ci=False, hue='farinha')

ax2.set(xticks=(-1, 1))

ax2.set_xlabels('Chocolate')

ax2.set_ylabels('Quantidade de cupcakes')

ax2.savefig('graficos/chocolate_qtd_cupcakes.png')
