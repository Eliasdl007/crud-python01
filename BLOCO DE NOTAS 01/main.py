import os
from sqlalchemy import create_engine, Column,  String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
Meu_Banco = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=Meu_Banco)
Session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True )
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=Meu_Banco)

os.system("cls || clear ")

print("Solicitando dados para o uasuario")
inserir_nome = input("Digite seu nome: ")
inserir_nome = input("Digite seu email: ")
inserir_nome = input("Digite seu nome: ")

usuario = Usuario(nome="Marta", email="matar@gamail", senha="123")
Session.add(usuario)
Session.commit()

usuario = Usuario(nome="Marta", email="matar@gamail", senha="456")
Session.add(usuario)
Session.commit()

print("\nExibindo todos os usuarios do banco de dados")
lista_usarios = Session.query(Usuario).all()

for usuario in lista_usarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

Session.close()