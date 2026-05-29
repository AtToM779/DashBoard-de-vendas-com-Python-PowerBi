import pandas as pd
import glob
import os
from pathlib import Path

# Carregamentos de todos os CSV em "arquivos"
arquivos = Path("Dados")

dfs = {}

for arquivos in arquivos.glob("*.csv"):
    nome = arquivos
    dfs[nome] = pd.read_csv(arquivos)
    print(f"  {nome}: {dfs[nome].shape}")

# Limpeza dos dados


