import sqlite3
import re
import hashlib
import csv

def criar_banco():
    conn = sqlite3.connect('cadastro_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT,
            senha TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def validar_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validar_telefone(telefone):
    pattern = r'^\(\d{2}\) \d{5}-\d{4}$'
    return bool(re.match(pattern, telefone))

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def adicionar_usuario(nome, email, telefone, senha):
    if not validar_email(email):
        print("Email inválido!")
        return
    if not validar_telefone(telefone):
        print("Telefone inválido! Formato esperado: (XX) XXXXX-XXXX")
        return
    senha_hash = hash_senha(senha)
    try:
        conn = sqlite3.connect('cadastro_usuarios.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, email, telefone, senha)
            VALUES (?, ?, ?, ?)
        ''', (nome, email, telefone, senha_hash))
        conn.commit()
        print("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este email já está cadastrado!")
    finally:
        conn.close()

def listar_usuarios():
    conn = sqlite3.connect('cadastro_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, email, telefone FROM usuarios ORDER BY nome')
    usuarios = cursor.fetchall()
    conn.close()
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")

def buscar_usuario(termo):
    conn = sqlite3.connect('cadastro_usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome LIKE ? OR email LIKE ?", ('%' + termo + '%', '%' + termo + '%'))
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def deletar_usuario(id):
    confirmar = input("Tem certeza que deseja deletar este usuário? (s/n): ")
    if confirmar.lower() == 's':
        conn = sqlite3.connect('cadastro_usuarios.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        print("Usuário deletado com sucesso!")
    else:
        print("Operação cancelada.")

def exportar_usuarios():
    conn = sqlite3.connect('cadastro_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nome", "Email", "Telefone"])
        writer.writerows(usuarios)
    print("Dados exportados para usuarios.csv")

def menu():
    while True:
        print("\nSistema de Cadastro de Usuários")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Buscar Usuário")
        print("4. Deletar Usuário")
        print("5. Exportar Usuários")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            telefone = input("Digite o telefone: ")
            senha = input("Digite a senha: ")
            adicionar_usuario(nome, email, telefone, senha)
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            termo = input("Digite um nome ou e-mail para buscar: ")
            resultados = buscar_usuario(termo)
            for usuario in resultados:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Telefone: {usuario[3]}")
        elif escolha == '4':
            id = int(input("Digite o ID do usuário a ser deletado: "))
            deletar_usuario(id)
        elif escolha == '5':
            exportar_usuarios()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    criar_banco()
    print("\nAdicionando dados fictícios...")
    adicionar_usuario("Ricardo Mendes", "ricardo.mendes@email.com", "(41) 95555-4444", "senha123")
    menu()
