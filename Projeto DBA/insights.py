import matplotlib.pyplot as plt
import pandas as pd
import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect("dbname=producao user=postgres password= host=localhost port=5432")

# Função para executar consultas no banco e retornar os dados como um DataFrame
def query_to_df(query):
    return pd.read_sql_query(query, conn)

# Gráfico 1: Média de Preço por Tipo de Veículo
query_price = "SELECT type, AVG(price) as average_price FROM carros GROUP BY type"  # 'type' em minúsculo
df_price = query_to_df(query_price)
df_price.set_index('type')['average_price'].plot(kind='bar', color='skyblue')
plt.title('Média de Preço por Tipo de Veículo')
plt.ylabel('Preço Médio')
plt.xlabel('Tipo de Veículo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('price_by_type.png')
plt.clf()  # Limpa o gráfico atual

# Gráfico 2: Quilometragem Média por Tipo de Veículo
query_distance = "SELECT type, AVG(distance) as average_distance FROM carros GROUP BY type"  # 'type' em minúsculo
df_distance = query_to_df(query_distance)
df_distance.set_index('type')['average_distance'].plot(kind='bar', color='orange')
plt.title('Quilometragem Média por Tipo de Veículo')
plt.ylabel('Quilometragem Média (Km)')
plt.xlabel('Tipo de Veículo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('distance_by_type.png')
plt.clf()

# Gráfico 3: Distribuição do Número de Veículos por Tipo de Combustível
query_fuel = "SELECT fuel, COUNT(*) as fuel_count FROM carros GROUP BY fuel"  # 'fuel' em minúsculo
df_fuel = query_to_df(query_fuel)
df_fuel.set_index('fuel')['fuel_count'].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'gold', 'lightgreen', 'skyblue'])
plt.title('Distribuição de Veículos por Tipo de Combustível')
plt.ylabel('')  # Remove o rótulo automático
plt.tight_layout()
plt.savefig('fuel_distribution.png')
plt.clf()

# Fechando a conexão com o banco de dados
conn.close()
