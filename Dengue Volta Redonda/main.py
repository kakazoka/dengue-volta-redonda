from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

bootstrap = Bootstrap5(app)

load_dotenv()

UID = os.getenv('UID')
API_KEY = os.getenv('API_KEY')


@app.route('/')
def index():
    response = requests.get(f'https://simplescraper.io/api/{UID}?apikey={API_KEY}')
    data = response.json()
    data_items = data.get('data', [])

    return render_template("index.html", data_items=data_items)


@app.route('/plano-de-contingencia')
def plano_de_contingencia():
    return render_template("plano-de-contingencia.html")


@app.route('/alertas-epidemiologicos')
def alertas_epidemiologicos():
    return render_template("alertas-epidemiologicos.html")


@app.route('/notificacoes-de-suspeitas')
def notificacoes_de_suspeitas():
    return render_template("notificacoes-de-suspeitas.html")


@app.route('/cuidados-com-o-imovel')
def cuidados_com_o_imovel():
    return render_template("cuidados-com-o-imovel.html")


@app.route('/cuidados-em-viagens')
def cuidados_em_viagens():
    return render_template("cuidados-em-viagens.html")


@app.route('/suspeita-de-dengue')
def suspeita_de_dengue():
    return render_template("suspeita-de-dengue.html")


@app.route('/estou-com-dengue')
def estou_com_dengue():
    return render_template("estou-com-dengue.html")


@app.route('/denuncie-focos-de-mosquito')
def denuncie_focos_de_mosquito():
    return render_template("denuncie-focos-de-mosquito.html")


@app.route('/habitat')
def habitat():
    return render_template("habitat.html")


@app.route('/ciclo-de-vida')
def ciclo_de_vida():
    return render_template("ciclo-de-vida.html")


if __name__ == '__main__':
    app.run(debug=True)
