from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    produtos = buscar_produtos()
    return render_template("index.html", produtos=produtos)

@app.route("/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]

        produto = Produto(None, nome, descricao, preco)
        criar_produto(produto)

        return redirect(url_for("index"))

    return render_template("criar.html")

# Defina rotas para Read, Update e Delete...

if __name__ == "__main__":
    app.run(debug=True)



def conectar_db():
    return MySQLdb.connect(
        host="localhost",
        user="root",
        password="",
        database="produtos",
    )

def criar_produto(produto):
    # Conecta ao banco
    db = conectar_db()
    cursor = db.cursor()

    # Insere o produto na tabela
    sql = """INSERT INTO produtos (nome, descricao, preco) VALUES (%s, %s, %s)"""
    cursor.execute(sql, (produto.nome, produto.descricao, produto.preco))
    db.commit()
    cursor.close()
    db.close()

# Defina funções para Read, Update e Delete...
