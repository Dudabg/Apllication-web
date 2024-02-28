# from flask import Flask, render_template
# import mysql.connector


# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="6352417896857412@Du",
#     database="produtos"
# )

# mycursor = mydb.cursor()

# for i in range(2):
#     nome = input("Nome: ")
#     descricao = input("Descricão: ")
#     preco = input("Preço: ")

#     sql = "INSERT INTO produto (nome,descricao, preco) VALUES (%s, %s, %s)"
#     val = (nome,descricao, preco)
#     mycursor.execute(sql, val)

# mydb.commit()
# mydb.close()


