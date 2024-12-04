# Projeto Final - Banco de Dados 2  

Entrega para a segunda nota da disciplina Banco de Dados 2. Este projeto abrange os seguintes módulos:  

1. **Modelagem Dimensional entre Bancos de Dados**  
   - Criação de dois bancos de dados:
     - **Banco de Produção**: Contém a tabela `carros`, que armazena os dados brutos do arquivo CSV.  
     - **Banco de Homologação**: Contém tabelas dimensionais e uma tabela de fato:  
       - Dimensões:  
         - `dim_carro` (detalhes do carro)  
         - `dim_localizacao` (estado)  
         - `dim_combustivel` (tipo de combustível)  
       - Fatos:  
         - `fato_precos` (preço e outros dados quantitativos)  

2. **CRUD e Pesquisas Interativas**  
   - Um aplicativo web criado com Flask que se conecta ao banco de dados e permite:  
     - Gerenciamento completo dos dados com operações de CRUD.  
     - Pesquisa interativa com criação de relatórios personalizados.  
     - Exportação de relatórios para formatos Excel/CSV.  

3. **Projeto da Nova "Área de Dados"**  
   - Uso criativo de conceitos de Banco de Dados, Engenharia de Dados e Análise de Dados para gerar insights baseados nos dados do projeto.  

---

## Ferramentas Utilizadas  

- **IDE**: Visual Studio Code  
- **Servidor de Banco de Dados**: PostgreSQL  
- **Cliente para Manipulação do Banco**: DBeaver  
- **Linguagens e Bibliotecas**:  
  - **SQL**: Para criação e manipulação de tabelas.  
  - **Python**: Para integração com o banco, geração de relatórios e manipulação de dados, usando:  
    - `psycopg2`  
    - `pandas`  
  - **Flask**: Para criar a API e interface web.  
  - **HTML/CSS**: Para o design da interface.  

---

## Estrutura do Projeto  

### Bancos de Dados  
- **Banco de Produção**  
  - Tabela `carros`: Contém os dados brutos do CSV.  

- **Banco de Homologação**  
  - **Dimensões**:  
    - `dim_carro`  
    - `dim_localizacao`  
    - `dim_combustivel`  
  - **Fato**:  
    - `fato_precos`  

### Telas do Aplicativo  

1. **Index**: Apresenta o resumo do projeto e os integrantes.  
2. **Cars**: Exibe os dados brutos do banco de dados.  
3. **Insights**: Mostra gráficos gerados pelo script `insights.py`, incluindo:  
   - Média de preço por tipo de veículo.  
   - Quilometragem média por tipo de veículo.  
   - Distribuição percentual de veículos por tipo de combustível.  

---

## Scripts  

### 1. `app.py`  
Implementa a aplicação web com Flask. Possui:  
- Rotas para páginas HTML (`index`, `insights`).  
- Funções CRUD para gerenciar dados na rota `/cars`.  
- Geração de relatórios exportáveis na rota `/report`.  

### 2. `importar_csv.py`  
Carrega o arquivo CSV com dados de carros, processa as informações e insere no banco de dados:  
- Remove colunas desnecessárias e trata valores nulos.  
- Adiciona uma coluna `id` incremental.  
- Cria a tabela `carros` se não existir e insere os dados.  

### 3. `insights.py`  
Gera gráficos baseados nos dados do banco:  
- Média de preço por tipo de veículo.  
- Quilometragem média por tipo de veículo.  
- Distribuição percentual de veículos por tipo de combustível.  
- Salva os gráficos no formato `.png`.  

---

## Como Executar  

1. Clone este repositório.  
2. Configure o banco de dados PostgreSQL e ajuste as credenciais no código.  
3. Instale as dependências do Python:  
   ```bash  
   pip install -r requirements.txt  
   ```  
4. Execute o script `importar_csv.py` para carregar os dados do CSV.  
5. Inicie a aplicação Flask:  
   ```bash  
   python app.py  
   ```  
6. Acesse a aplicação em [http://localhost:5000](http://localhost:5000).  

---

## Contribuição  
Este projeto foi desenvolvido como requisito para a disciplina Banco de Dados 2.  
Fonte do Dataset: https://www.kaggle.com/datasets/ujjwalwadhwa/cars24com-used-cars-dataset
--- 
