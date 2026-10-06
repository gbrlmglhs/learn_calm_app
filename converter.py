import sqlite3
from bs4 import BeautifulSoup

# 1. Abre seu arquivo HTML original do Parque
with open('sap-cloud-alm-parque.html', 'r', encoding='utf-8') as arquivo:
    soup = BeautifulSoup(arquivo.read(), 'html.parser')

# 2. Conecta ao banco de dados do app Python
conn = sqlite3.connect('progresso.db')
cursor = conn.cursor()

# Cria a tabela de progresso se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS progresso (
        item TEXT PRIMARY KEY,
        concluido INTEGER,
        tipo TEXT
    )
''')

print("⏳ Lendo dados do seu HTML...")

# 3. Varre os checkboxes e listas do seu HTML para pegar as atividades
itens_salvos = 0

# Buscaremos todos os elementos de texto relevantes do seu HTML original
for tag in soup.find_all(['label', 'p', 'li']):
    texto = tag.get_text().strip()
    
    # Filtramos para pegar textos que realmente sejam lições, tópicos ou títulos de blocos
    if len(texto) > 3 and not texto.startswith('{') and not texto.startswith('.'):
        # Evita duplicados e insere no banco
        cursor.execute('''
            INSERT OR IGNORE INTO progresso (item, concluido, tipo)
            VALUES (?, 0, 'aula')
        ''', (texto,))
        itens_salvos += cursor.rowcount

conn.commit()
conn.close()

print(f"✅ Sucesso! {itens_salvos} tópicos de estudo foram migrados para o seu Banco de Dados!")
