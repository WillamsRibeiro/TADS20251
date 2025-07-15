import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame ({
    'idade':[20,23,46,35], 
    'nome': ['joão','Maria','José', 'Helena']
})
plt.hist(tabela ['idade']) 