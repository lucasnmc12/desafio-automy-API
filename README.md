# 🔧 Desafio Técnico — Integração com API (Automy)

Este projeto consulta dados de baterias (corridas) agendadas em um kartódromo com base no e-mail informado, utilizando uma API via proxy com autenticação JWT.

---

## ✅ Funcionalidades

- Autenticação na API da Automy
- Consulta de baterias associadas a um e-mail
- Separação de baterias em:
  - 📅 Próximos agendamentos
  - 📁 Agendamentos anteriores
- Interface web simples com Bootstrap
- Exibição interativa por botões

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/desafio-automy.git
cd desafio-automy
```

### 2. Crie o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se não existir o arquivo `requirements.txt`, instale manualmente:
> ```bash
> pip install flask flask-cors requests
> ```

### 4. Execute o servidor Flask

```bash
python src/app.py
```

### 5. Acesse no navegador

```
http://localhost:5000
```

---

## 🗂 Estrutura do Projeto

```
desafio-automy/
├── src/
│   ├── app.py               # Arquivo principal com as rotas
│   ├── auth.py              # Função para obter token
│   ├── query.py             # Consulta SQL à API
│   ├── mensagens.py         # Geração de mensagens personalizadas (opcional)
│   ├── templates/
│   │   └── index.html       # Interface web
│   └── static/
│       └── style.css        # Estilos da página
├── Doc.md                   # Documentação completa
└── README.md                # Este arquivo
```

---

## 🧪 Testado com

- Python 3.10+
- Navegador Google Chrome
- API Automy fornecida para o desafio

---

## 📩 Contato

**Nome:** [Seu Nome Aqui]  
**E-mail:** [seu@email.com]  
**Telefone:** (xx) xxxxx-xxxx  
**CPF:** xxx.xxx.xxx-xx

---
