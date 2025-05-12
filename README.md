# 🔧 Desafio Técnico — Integração com API (Automy)

Este projeto consulta dados de baterias (corridas) agendadas em um kartódromo com base no e-mail informado, utilizando uma API via proxy com autenticação JWT.

---

## ✅ Funcionalidades

- 🔐 Autenticação na API Automy com token JWT
- 📩 Consulta de baterias associadas a um e-mail
- 📅 Separação de baterias em:
  - Próximos agendamentos
  - Agendamentos anteriores
- 🌐 Interface web interativa com Bootstrap e JavaScript
- 🧪 Testes unitários automatizados com `unittest` e `mock`
- 🐳 Dockerfile para build e execução local

---

## 🚀 Executando com Docker (recomendado)

### 1. Clone o repositório

```bash
git clone https://github.com/lucasnmc12/desafio-automy-API.git
cd desafio-automy-API
```

### 2. Construa a imagem Docker

```bash
docker build -t desafio-api .
```

Este comando irá:
- Instalar as dependências
- Executar os testes (`test_app.py`)
- Preparar a imagem pronta para execução

### 3. Execute o container

```bash
docker run -p 5000:5000 desafio-api
```

### 4. Acesse no navegador

[http://localhost:5000](http://localhost:5000)

---

## 💻 Executando sem Docker (modo alternativo)

### 1. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Rode o servidor:

```bash
python src/app.py
```

---

## 🧪 Executar testes manualmente

```bash
python3 -m unittest discover -s src -p "test_*.py"
```

---

## 🗂 Estrutura do Projeto

```
desafio-automy-API/
├── src/
│   ├── app.py            # Servidor Flask
│   ├── auth.py           # Autenticação com a API
│   ├── query.py          # Consulta SQL
│   ├── mensagens.py      # Geração de mensagens personalizadas (opcional)
│   ├── templates/
│   │   └── index.html    # Interface do usuário
│   ├── static/
│   │   └── style.css     # Estilo visual da interface
│   └── test_app.py       # Testes unitários com mocks
├── requirements.txt      # Dependências
├── Dockerfile            # Dockerfile com build e testes
├── Doc.md                # Documentação completa do desafio
└── README.md             # Este arquivo
```

---

## 📩 Contato

- **Nome:** Lucas Nogueira Mazzieiro de Carvalho  
- **E-mail:** lucas.nogueira20mc@gmail.com  
- **Telefone:** (31) 99241-0320  
- **CPF:** 018.728.636-12
