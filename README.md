# Sistema de Cadastro de Usuários✨✨

Este projeto é um sistema simples de cadastro de usuários utilizando **Python** e **SQLite**. O sistema permite adicionar, listar, buscar, deletar e exportar dados de usuários para um arquivo CSV.

## Tecnologias Utilizadas
- **Python**
- **SQLite** (Banco de Dados)
- **Módulos:** `sqlite3`, `re`, `hashlib`, `csv`

## Funcionalidades
1. **Adicionar Usuário**: Cadastra um novo usuário no banco de dados.
2. **Listar Usuários**: Exibe todos os usuários cadastrados.
3. **Buscar Usuário**: Permite buscar usuários por nome ou e-mail.
4. **Deletar Usuário**: Remove um usuário do banco de dados.
5. **Exportar Usuários**: Exporta os dados para um arquivo `usuarios.csv`.

## Como Executar o Projeto
1. Certifique-se de ter o **Python** instalado em seu sistema.
2. Baixe ou clone este repositório.
3. No terminal, execute o arquivo principal:
   ```sh
   python nome_do_arquivo.py
   ```

## Estrutura do Código
- **`criar_banco()`**: Cria a tabela `usuarios` no SQLite caso ainda não exista.
- **`validar_email(email)`**: Valida o formato do e-mail inserido.
- **`validar_telefone(telefone)`**: Valida o formato do telefone no padrão `(XX) XXXXX-XXXX`.
- **`hash_senha(senha)`**: Gera um hash da senha para armazenamento seguro.
- **`adicionar_usuario(nome, email, telefone, senha)`**: Adiciona um novo usuário ao banco de dados.
- **`listar_usuarios()`**: Lista todos os usuários cadastrados.
- **`buscar_usuario(termo)`**: Busca usuários pelo nome ou e-mail.
- **`deletar_usuario(id)`**: Remove um usuário do banco de dados com confirmação.
- **`exportar_usuarios()`**: Exporta os dados dos usuários para um arquivo CSV.
- **`menu()`**: Interface interativa para o usuário escolher as opções.

## Observações
- O sistema já adiciona um usuário fictício para testes.
- O e-mail deve ser único para evitar duplicatas.
- A senha é armazenada de forma segura usando **SHA-256**.

## Contato
Caso tenha dúvidas ou sugestões, fique à vontade para entrar em contato.

---
**Desenvolvido por [Simone Luciano]**

