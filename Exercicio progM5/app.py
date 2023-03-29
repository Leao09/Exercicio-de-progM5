from flask import Flask, render_template, request, redirect, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.posicao import Position

engine = create_engine('sqlite:///robot.db', echo=True)
Session = sessionmaker(bind=engine)

# Cria a tabela no banco se ela não existe
Base.metadata.create_all(engine)

app = Flask(__name__)


@app.route("/")
def index():
    try:
    # pega os dados do banco de dados
        # abre uma session
        get_session = Session()
        # faz uma query "select"
        get_position = get_session.query(Position).order_by(Position.id.desc()).all()
        print(get_position)
        ## pessoas = session.query(Pessoa).all();        
        # e coloca os dados da query em sla um array

    # retornar json
        return render_template("index.html", positions = get_position)
    except Exception as err:
        print(str(err))


# post
# @app.route("/post", methods=['POST'])
@app.post("/setposition")
def setposition():
    try:
    # pega os dados do frontend
        # pega por meio de forms
        x = request.form['x']
        y = request.form['y']
        z = request.form["z"]
        rot = request.form['rot']

    # coloca esses dados no banco de dados
        # abre uma conexão com o banco ("session")
        post_session = Session()
        # instancia o dado como objeto
        pos = Position(x, y, z, rot)
        print(pos)
        # adiciona no banco
        post_session.add(pos)
        post_session.commit()
        # commit e fecha a conexão
        print(pos)
        # printa se deu bom
        return redirect("/")
    except Exception as err:
        print(str(err))
    
# get
@app.get("/getposition")
def getposition():
    try:
    # pega os dados do banco de dados
        # abre uma session
        get_session = Session()
        # faz uma query "select"
        pos = get_session.query(Position).order_by(Position.id.desc()).limit(1).one() 
        # e coloca os dados da query em sla um array
    # retornar json
        return jsonify(pos.as_json())
    except Exception as err:
        print(str(err))


if __name__ == "__main__":
    app.run(debug=True)