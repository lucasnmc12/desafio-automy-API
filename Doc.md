##  Informações Pessoais

- **Nome:** Lucas Nogueira Mazzieiro de Carvalho  
- **CPF:** 018.728.636-12  
- **E-mail:** lucas.nogueira20mc@gmail.com  
- **Número:** (31) 99241-0320

---

## Rodando o projeto com Docker

### Requisitos

- Docker instalado na máquina  
- Conexão com a internet para baixar imagens base na primeira execução

---

###  1. Construir a imagem

Navegue até a raiz do projeto (onde está o `Dockerfile`) e execute:

```bash
docker build -t desafio-api .
```

Esse comando:

- Cria a imagem Docker `desafio-api`
- Instala dependências via `requirements.txt`
- Roda os testes automatizados localmente (`test_app.py`)
- Prepara o ambiente completo para execução

---

### ▶ 2. Rodar a aplicação

Após a build, execute:

```bash
docker run -p 5000:5000 desafio-api
```

A aplicação estará acessível em:

🔗 [http://localhost:5000](http://localhost:5000)

---

##  Testes Automatizados

Os testes são executados automaticamente durante a build Docker.  
Para rodá-los manualmente, dentro da pasta `src`, use:

```bash
python3 -m unittest discover -s src -p "test_*.py"
```

---

## 📂 Estrutura do Projeto

```
desafio-automy-API/
├── src/
│   ├── app.py            # Servidor Flask
│   ├── auth.py           # Autenticação com a API
│   ├── query.py          # Consulta SQL via API
│   ├── mensagens.py      # (Não usado no front atual)
│   └── test_app.py       # Testes com mocks
├── requirements.txt      # Dependências
├── Dockerfile            # Ambiente Docker
└── Doc.md                # Este documento
```

---

## ✅ Funcionalidades

- Autenticação via token JWT na API da Automy  
- Consulta com filtro por e-mail  
- Separação de baterias agendadas e passadas  
- Exibição interativa com frontend HTML + JavaScript  
- Testes unitários usando `unittest` e `mock`  
- Deploy local via Docker com execução automática

---


