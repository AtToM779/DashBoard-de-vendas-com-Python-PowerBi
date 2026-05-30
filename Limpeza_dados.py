import pandas as pd
import glob
import os
from pathlib import Path
import numpy as np

# Carregamentos de todos os CSV em "arquivos"

tabelas = {
    "orders":      pd.read_csv("Dados/olist_orders_dataset.csv"),
    "items":       pd.read_csv("Dados/olist_order_items_dataset.csv"),
    "products":    pd.read_csv("Dados/olist_products_dataset.csv"),
    "customers":   pd.read_csv("Dados/olist_customers_dataset.csv"),
    "geolocation": pd.read_csv("Dados/olist_geolocation_dataset.csv"),
    "pagamentos":  pd.read_csv("Dados/olist_order_payments_dataset.csv"),
    "reviews":     pd.read_csv("Dados/olist_order_reviews_dataset.csv"),
    "vendedores":  pd.read_csv("Dados/olist_sellers_dataset.csv"),
    "traducao":    pd.read_csv("Dados/product_category_name_translation.csv"),
}

# Limpeza dos dados

for nome, df in tabelas.items():
    nulos = df.isna().sum()
    nulos = nulos[ nulos > 0]
    print(f"\n{nome}")
    print(nulos)

