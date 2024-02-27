from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def produtos():
    return render_template("produtos.html")


@app.route("/criar")
def criar():
    return render_template("criar.html")

@app.route('/editar')
def editar():
    return render_template('editar.html')

@app.route('/deletar')
def deletar():
    return render_template('deletar.html')


#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)