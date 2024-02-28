from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.sqlite3'

db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80))
    descricao = db.Column(db.Text)
    preco= db.Column(db.Integer)

    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

   
@app.route("/")
def produto():
    produtos=Produto.query.all() 
    return render_template("produto.html", produtos=produtos)


@app.route("/criar", methods=["POST", "GET"])
def criar():
    if request.method == "POST":
       produto=Produto(request.form["nome"], request.form["descricao"], request.form["preco"])
       db.session.add(produto)
       db.session.commit()
       return redirect(url_for('criar'))
    return render_template("criar.html")


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.preco = request.form['preco']
        db.session.add(produto)
        db.session.commit()

        return redirect(url_for('produto'))  # redirecionar para a rota 'produto' após a atualização
    return render_template('editar.html', produto=produto, produto_id=id)







@app.route('/deletar_produto/<int:id>')
def deletar(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produto'))









#colocar site no ar
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
