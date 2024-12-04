import pandas as pd
import psycopg2

# Caminho do arquivo CSV
csv_path = r"C:\Users\nicol\Documents\ProjetoBDA\cars_24_combined.csv"

# 1. Carregar o arquivo CSV
try:
    df = pd.read_csv(csv_path)
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")
    exit()

# 2. Pré-processamento básico
# Remover colunas desnecessárias (ex.: índice "Unnamed")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Tratar valores nulos removendo registros com dados faltantes
df = df.dropna()
df.reset_index(drop=True, inplace=True)

# Garantir que os tipos das colunas estejam corretos
try:
    df['year'] = df['year'].astype(int)
    df['distance'] = df['distance'].astype(int)
    df['owner'] = df['owner'].astype(int)
    df['price'] = df['price'].astype(float)  # Alterado para DECIMAL
    # Converter strings para eliminar espaços extras
    string_cols = ['car_name', 'fuel', 'location', 'drive', 'type']
    for col in string_cols:
        df[col] = df[col].str.strip()
except Exception as e:
    print(f"Erro ao ajustar tipos: {e}")
    exit()

# Validar valores (exemplo: anos válidos, preços positivos)
df = df[df['year'] > 1900]  # Remover registros com ano inválido
df = df[df['price'] > 0]    # Garantir que o preço seja positivo

# Adicionar coluna "id" com valores incrementais
df.insert(0, 'id', range(1, len(df) + 1))

# 3. Exibir informações sobre os dados
print("Amostra dos dados:")
print(df.head())
print("\nInformações dos dados:")
print(df.info())

# 4. Preparar para inserção no PostgreSQL
try:
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="producao",
        user="postgres",
        password=""
    )
    cursor = conn.cursor()

    # Criar a tabela, se ainda não existir
    create_table_query = """
    CREATE TABLE IF NOT EXISTS carros (
        id SERIAL PRIMARY KEY,
        car_name VARCHAR(100),
        year INT,
        distance INT,
        owner INT,
        fuel VARCHAR(20),
        location VARCHAR(10),
        drive VARCHAR(20),
        type VARCHAR(20),
        price DECIMAL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Tabela criada ou já existente.")

    # Inserir os dados no banco
    for _, row in df.iterrows():
        insert_query = """
        INSERT INTO carros (id, car_name, year, distance, owner, fuel, location, drive, type, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, tuple(row))
    conn.commit()
    print("Dados inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao interagir com o PostgreSQL: {e}")
finally:
    cursor.close()
    conn.close()
