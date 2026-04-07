# Configurar alembic
# pip install alembic

# inicializar o alembic

# No terminal:
# alembic init alembic
# ou
# python -m alembic init alembic

# Configurar a conexão com db
# --------------------------------------------------
# Abra o arquivo: alembic.init
# Procure pela linha:  
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Altere para a conexão com o seu banco
# sqlalchemy.url = sqlite:///escola.db


# Conectando o alembic ao sqlalchemy
# --------------------------------------------------
# Abra o arquivo: alembic/env.py
# Importe o Base do seu projeto. exemplo:
# from models import Base

# Depois, encontre a linha:
# target_metadata = None
# e alterar para:
# target_metadata = Base.metadata

# Criando a migração
# --------------------------------------------------
# no terminal:
# python -m alembic revision --autogenerate -m "Criando tabelas"
# e depois aplica a migração no banco
# no terminal:
# python -m alembic upgrade head

# As tabelas foram criadas no banco de dados
