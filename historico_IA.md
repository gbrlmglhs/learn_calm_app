📝 Resumo do Projeto (Para cópia)
• Objetivo: Transformar um HTML antigo de estudos em um Web App multiplataforma (Mac, iPhone, iPad) sem perder o progresso.
• Tecnologias Utilizadas: Python 3, Streamlit (para interface visual), SQLite (banco de dados local/nuvem) e Git/GitHub (controle de versão e deploy).
• Repositório GitHub: https://github.com (Configurado como Privado).
• Estado Atual:
	1. O arquivo sap-cloud-alm-parque.html foi movido para o VS Code.
	2. O script converter.py foi executado e extraiu com sucesso os 8 tópicos reais de estudo para o banco de dados progresso.db.
	3. O arquivo app.py foi atualizado para carregar os tópicos dinamicamente com checkboxes e uma barra de progresso em porcentagem.
	4. O ambiente local foi testado no Mac rodando com o comando python3 -m streamlit run app.py.
	5. O código foi commitado e enviado com sucesso ao GitHub (working tree clean).
• Comando para rodar o app no Mac localmente:bash
python3 -m streamlit run app.py