#Configurar alembic
#pip install alembic
#Inicializar o alembic

#No terminal:
#alembic init alembic
#ou
#python -m alembic init alembic
#Configurar a conexao com db

#Abra o arquivo: alembic.ini
#procure pela linha:
#sqlalchemy.url = driver:\\user:pass@localhost\dbname

#Altere para a conexao com seu banco
#sqlalchemy.url = sqlite:\\\escola.db


#Conectando o alembic ao sqlalchemy

#Abra o arquivo: alembic/env.py
Importe o Base do seu projeto. exemplos:
from models import Base

#Depois, encontre a linha:
target_metadata = None
3alete para:
#target_metadata = Base.metadata