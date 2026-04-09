import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')




# CALCULAR DINERO: Creamos la columna 'ca' (precio multiplicado por cantidad)
données['ca'] = données['prix'] * données['qte']

# SUMAR TODO: 
# Le pedimos a Python que junte todos los "Producto A", "Producto B", etc., y sume sus números.
totaux = données.groupby('produit').sum(numeric_only=True).reset_index()

# --- GRÁFICO 1: CANTIDADES TOTALES ---
fig_ventes = px.bar(totaux, x='produit', y='qte', 
                    title='Ventes totales par produit (Quantité)',
                    color='produit',
                    text='qte') # Ponemos el número de la suma sobre la barra
fig_ventes.update_traces(textposition='outside') # El número va arriba de la barra
fig_ventes.update_layout(showlegend=False)
fig_ventes.write_html('ventes-par-produit.html')

# --- GRÁFICO 2: DINERO TOTAL (CA) ---
fig_ca = px.bar(totaux, x='produit', y='ca', 
                title="Chiffre d'affaires par produit",
                color='produit',
                text='ca') # Ponemos el dinero total sobre la barra
fig_ca.update_traces(textposition='outside') # El número va arriba de la barra
fig_ca.update_layout(showlegend=False)
fig_ca.write_html('ca-par-produit.html')

print("Ventes-par-produit.html y ca-par-produit.html générés.")

