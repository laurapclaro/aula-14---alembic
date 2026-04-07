from models import Session, Curso, Aluno
#criar as funções do crud
# Função criar um curso com sqlalchemy

#função criar um aluno c sqlalchemy

def cadastrar_curso():
    with Session() as session:
        try:
            nome = input("Digite o nome do curso: ").capitalize()
            carga_horaria = input("Digite a carga horaria do curso: ")
            curso = Curso(nome=nome, carga_horaria=carga_horaria)
            session.add(curso)
            session.commit()
        except Exception as erro:
            Session.rollback()
            print(f"Ocorreu um erro {erro}")
cadastrar_curso()

#função criar um aluno com sqlalchemy
def cadastrar_aluno():
    with Session() as session:
        try: 
            nome = input("Digite o nome do curso para cadastrar o aluno: ").capitalize()
            curso = session.query(Curso).filter_by(nome=nome).first()

            nome_aluno = input('Digit o nome do aluno: ').capitalize()
            email_aluno = input("Digite o email: ").capitalize()

            aluno = Aluno(nome=nome_aluno, email=email_aluno, curso=curso)

        except Exception as erro:
            Session.rollback()
            print(f"Ocorreu um erro {erro}")

#listar os alunos de um curso

def listar_alunos():
    lista = Session.queyr().all()
    print(f"Lista de alunos d")

