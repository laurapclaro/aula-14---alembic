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
