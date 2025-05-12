FROM python:3.11

# Define o diretório da aplicação dentro do container
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta src para o container
COPY src/ ./src

# Executa os testes unitários automaticamente durante o build
RUN python3 -m unittest discover -s src -p "test_*.py"

# FLASK port
EXPOSE 5000

# Comando padrão: inicia o app.py
CMD ["python", "src/app.py"]
