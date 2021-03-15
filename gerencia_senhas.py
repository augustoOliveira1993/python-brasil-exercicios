import sqlite3

conn = sqlite3.connect('gerencia_senha.db')
cursor = conn.cursor()

# Caso nao tenha o banco
# cursor.execute("""DROP TABLE gerencia_senha""")
# cursor.execute("""CREATE TABLE gerencia_senha
#                 (service, username, password)
#              """)


MASTER_PASSWORD = "123456"

# senha = input("Insira sua senha master: ")
senha = '123456'
if senha != MASTER_PASSWORD:
    print('Senha invalida!.. Encerrando...')
    exit()

def menu():
    print("***********")
    print("* i: inserir nova senhas      *")
    print("* l: lista de serviços salvos *")
    print("* r: recuperar uma senha      *")
    print("* s: sair                     *")
    print("***********")

def get_pasword(service):
    cursor.execute(f"""
        SELECT username, password, FROM gerencia_senha
        WHERE service='{service}""")
    if cursor.rowcount == 0:
        print("Serviço nao cadastrado (use 'l' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    sql = f"INSERT INTO gerencia_senha (service, username, password) VALUES ({service}, {username}, {password})"
    cursor.execute(sql)
    conn.commit()
    
def show_services():
    sql = 'SELECT service FROM gerencia_senha'
    cursor.execute(sql);
        
while True:
    menu()
    # insert_password('GitHub', 'gutim160', '88146347')
    pesq = cursor.execute("""INSERT INTO gerencia_senha (service, username, password) VALUES ('GitHub', 'gutim160', '8146347')""")
    pesq = cursor.execute("""INSERT INTO gerencia_senha (service, username, password) VALUES ('GitHub', 'gutim160', '8146347')""")
    pesq = cursor.execute("""INSERT INTO gerencia_senha (service, username, password) VALUES ('GitHub', 'gutim160', '8146347')""")
    exe = cursor.execute("""SELECT * FROM gerencia_senha""")
    for e in exe:
        print(e)
    op = str(input('O que voçe deseja fazer? '))
    if op not in ['i','l','r','s']:
        print('Opçao invalida')
        continue
     
    if op == 's':
        break
        
    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome do usuario? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)
        
    if op == 'l':
        show_services()
        
    if op == 'r':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_pasword(service)
    
conn.close()
