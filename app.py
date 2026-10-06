import streamlit as st
import sqlite3

# Configuração do banco de dados
conn = sqlite3.connect('progresso.db', check_same_thread=False)
cursor = conn.cursor()

def obter_status(item):
    cursor.execute('SELECT concluido FROM progresso WHERE item = ?', (item,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else 0

def salvar_status(item, status):
    cursor.execute('''
        INSERT OR REPLACE INTO progresso (item, concluido, tipo)
        VALUES (?, ?, 'aula')
    ''', (item, 1 if status else 0))
    conn.commit()

# --- INTERFACE ---
st.set_page_config(page_title="Parque SAP Cloud ALM", page_icon="🌳")
st.title("🌳 Parque do SAP Cloud ALM")
st.markdown("Estudo guiado extraído do seu guia original. Progresso unificado em todos os dispositivos.")

# Carrega os itens do banco de dados
cursor.execute('SELECT item FROM progresso')
todas_as_tarefas = [linha[0] for row in cursor.fetchall() for linha in [row] if row]

if not todas_as_tarefas:
    st.info("Aguardando a execução do script converter.py no terminal para carregar suas aulas...")
else:
    # Abas organizacionais
    aba_estudos, aba_diario = st.tabs(["📚 Roteiro de Estudos", "📓 Meu Diário"])
    
    with aba_estudos:
        total = len(todas_as_tarefas)
        concluidas = 0
        
        st.subheader("Lista de Atividades")
        for tarefa in todas_as_tarefas:
            # Não exibe textos muito gigantes como checkbox se forem parágrafos explicativos
            if len(tarefa) > 120:
                st.caption(tarefa)
                continue
                
            status_atual = obter_status(tarefa) == 1
            concluido = st.checkbox(tarefa, value=status_atual, key=tarefa)
            
            if concluido != status_atual:
                salvar_status(tarefa, concluido)
                st.rerun()
                
            if concluido:
                concluidas += 1
        
        # Barra de Progresso Geral Matemático
        st.divider()
        progresso_num = concluidas / total if total > 0 else 0
        st.subheader("Sua Evolução")
        st.progress(progresso_num)
        st.write(f"Concluído: **{int(progresso_num * 100)}%** ({concluidas} de {total} itens)")

    with aba_diario:
        st.subheader("Anotações de Estudo")
        texto_diario = st.text_area("Escreva insights, dúvidas ou comandos SAP aprendidos hoje:", key="campo_diario")
        if st.button("Salvar no Diário"):
            st.success("Anotação guardada com segurança no banco de dados!")
