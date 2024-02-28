# import mysql.connector
# from flask import Flask, render_template



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



# app = Flask(__name__)

# @app.route('/')
# def produto():
#     mydb = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="6352417896857412@Du",
#         database="produtos"
#     )

#     mycursor = mydb.cursor(dictionary=True)

#     mycursor.execute("SELECT * FROM produto")
#     produtos = mycursor.fetchall()

#     return render_template('produto.html', produtos=produtos)

# if __name__ == '__main__':
#     app.run(debug=True)

