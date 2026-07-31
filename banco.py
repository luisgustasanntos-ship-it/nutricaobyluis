import sqlite3


def conectar():
    return sqlite3.connect("nutricaobyluis.db")


# ==========================
# PACIENTES
# ==========================

def criar_tabela():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        sexo TEXT,
        peso REAL,
        altura REAL,
        objetivo TEXT

    )
    """)

    conexao.commit()
    conexao.close()



def inserir_paciente(nome, idade, sexo, peso, altura, objetivo):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO pacientes
    (nome, idade, sexo, peso, altura, objetivo)

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        nome,
        idade,
        sexo,
        peso,
        altura,
        objetivo
    ))

    conexao.commit()
    conexao.close()



def listar_pacientes():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM pacientes"
    )

    dados = cursor.fetchall()

    conexao.close()

    return dados



# ==========================
# EVOLUÇÃO
# ==========================

def criar_tabela_evolucao():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evolucao (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        peso REAL,
        data TEXT,

        FOREIGN KEY(paciente_id)
        REFERENCES pacientes(id)

    )
    """)

    conexao.commit()
    conexao.close()



def inserir_evolucao(paciente_id, peso, data):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO evolucao
    (paciente_id, peso, data)

    VALUES (?, ?, ?)

    """,
    (
        paciente_id,
        peso,
        data
    ))

    conexao.commit()
    conexao.close()



def listar_evolucao(paciente_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT data, peso
    FROM evolucao
    WHERE paciente_id = ?

    """,
    (paciente_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados



# ==========================
# PLANO ALIMENTAR
# ==========================

def criar_tabela_plano():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plano_alimentar (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        refeicao TEXT,
        alimento TEXT,
        quantidade TEXT,
        calorias REAL,

        FOREIGN KEY(paciente_id)
        REFERENCES pacientes(id)

    )
    """)

    conexao.commit()
    conexao.close()



def inserir_alimento(
    paciente_id,
    refeicao,
    alimento,
    quantidade,
    calorias
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO plano_alimentar
    (
        paciente_id,
        refeicao,
        alimento,
        quantidade,
        calorias
    )

    VALUES (?, ?, ?, ?, ?)

    """,
    (
        paciente_id,
        refeicao,
        alimento,
        quantidade,
        calorias
    ))

    conexao.commit()
    conexao.close()



def listar_plano(paciente_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT refeicao, alimento, quantidade, calorias
    FROM plano_alimentar
    WHERE paciente_id = ?

    """,
    (paciente_id,))

    dados = cursor.fetchall()

    conexao.close()

    return dados



# ==========================
# BANCO DE ALIMENTOS
# ==========================

def criar_tabela_alimentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alimentos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        porcao TEXT,
        calorias REAL,
        proteina REAL,
        carboidrato REAL,
        gordura REAL

    )
    """)

    conexao.commit()
    conexao.close()



def inserir_alimento_base(
    nome,
    porcao,
    calorias,
    proteina,
    carboidrato,
    gordura
):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO alimentos
    (
        nome,
        porcao,
        calorias,
        proteina,
        carboidrato,
        gordura
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        nome,
        porcao,
        calorias,
        proteina,
        carboidrato,
        gordura
    ))

    conexao.commit()
    conexao.close()



def listar_alimentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT *
    FROM alimentos
    """)

    dados = cursor.fetchall()

    conexao.close()

    return dados