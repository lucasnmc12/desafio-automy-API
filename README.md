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
git clone https://github.com/lucasnmc12/desafio-automy-API.git
cd desafio-automy-API
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se não existir o arquivo `requirements.txt`, instale manualmente:
> ```bash
> pip install flask flask-cors requests
> ```

### 3. Execute o servidor Flask

```bash
python src/app.py
```

### 4. Acesse no navegador

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

**Nome:** Lucas Nogueira MAzzieiro de Carvalho 
**E-mail:** lucas.nogueira20mc@gmail.com
**Telefone:** (31) 99241-0320  
**CPF:** 018.728.636-12

---
