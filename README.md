# LabAnalyzer

**LabAnalyzer** é uma aplicação web desenvolvida para facilitar a gestão e análise de dados biomédicos. O sistema permite o cadastro de pacientes, exames e tipos de exames, possibilitando o gerenciamento eficaz de informações clínicas.

---

## ⚡ Tecnologias Utilizadas

- **Back-end:** Flask (Python)
  - Flask-SQLAlchemy
  - Flask-Migrate
- **Banco de Dados:** MySQL (via SQLAlchemy/PyMySQL)
- **Visualização de Dados:** Matplotlib e Seaborn
- **Outras Bibliotecas:**
  - Pandas e NumPy (para manipulação de dados)
  - fpdf (geração de relatórios em PDF)
  - dotenv (gerenciamento de variáveis de ambiente)

---

## 🔧 Funcionalidades Principais

- **Gestão de Pacientes:** Cadastro e consulta de pacientes com informações como nome e idade.
- **Gestão de Exames:** Cadastro e consulta de exames associados a pacientes.
- **Tipos de Exames:** Registro de tipos de exames para análise personalizada.
- **Relatórios:** Geração de relatórios detalhados em PDF com base nos dados registrados.
- **Análise de Dados:** Visualização de dados clínicos através de gráficos.

---

## ⚙ Configuração do Ambiente

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/LabAnalyzer.git
   cd LabAnalyzer
   ```

2. Configure o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` com suas variáveis de ambiente:
   ```env
   SECRET_KEY=sua_chave
   DATABASE_URI=mysql+pymysql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>
   ```

5. Inicialize o banco de dados:
   ```bash
   flask db init
   flask db migrate -m "Migração inicial"
   flask db upgrade
   ```

6. Inicie o servidor Flask:
   ```bash
   python run.py
   ```

7. Acesse a aplicação em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🎨 Estrutura do Projeto

```
LabAnalyzer
├── app/
│   ├── __init__.py       # Inicialização da aplicação
│   ├── config/           # Configurações do sistema
│   │   ├── config.py
│   │   └── db.py
│   ├── models/           # Definição dos modelos do banco de dados
│   │   ├── exams.py
│   │   ├── exam_types.py
│   │   ├── pacients.py
│   │   └── users.py
│   ├── routes/           # Rotas da aplicação
│   │   ├── pacients.py
│   │   ├── users.py
│   │   └── __init__.py
│   └── templates/        # Templates HTML
│       └── index.html
├── migrations/           # Arquivos de migração do banco
├── .env                  # Variáveis de ambiente
├── requirements.txt      # Dependências do projeto
└── run.py                # Arquivo principal para iniciar o servidor
```

---

## 🌐 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

## 🔍 Meta

Autor: **Leonan**  
[LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com/seu-usuario)

