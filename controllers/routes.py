from flask import render_template, request
import urllib.request
import json

personagens = [
    {'nome': 'Monkey D. Luffy', 'idade': 19},
    {'nome': 'Roronoa Zoro', 'idade': 21},
    {'nome': 'Nami', 'idade': 20},
    {'nome': 'Usopp', 'idade': 19},
    {'nome': 'Sanji', 'idade': 21},
    {'nome': 'Tony Tony Chopper', 'idade': 17}
]

tripulacoes = [
    {
        'nome_tripulacao': 'Chapéu de Palha',
        'capitao': 'Monkey D. Luffy',
        'membros': ['Monkey D. Luffy', 'Roronoa Zoro', 'Nami', 'Usopp', 'Sanji', 'Tony Tony Chopper']
    },
    {
        'nome_tripulacao': 'Baroque Works',
        'capitao': 'Crocodile',
        'membros': ['Crocodile', 'Miss All Sunday', 'Mr. 1', 'Mr. 2 Bon Clay']
    },
    {
        'nome_tripulacao': 'Big Mom Pirates',
        'capitao': 'Charlotte Linlin (Big Mom)',
        'membros': ['Charlotte Linlin', 'Katakuri', 'Cracker', 'Smoothie']
    }
]

def init_app(app):
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/personagens', methods=['GET', 'POST'])
    def personagens_route():
        if request.method == 'POST':
            nome = request.form.get('nome')
            idade = request.form.get('idade')
            if nome and idade:
                personagens.append({'nome': nome, 'idade': idade})
        
        return render_template('personagens.html', personagens=personagens)
    
    @app.route('/tripulacoes', methods=['GET', 'POST'])
    def tripulacoes_route():
        if request.method == 'POST':
            nome_tripulacao = request.form.get('nome_tripulacao')
            capitão = request.form.get('capitao')
            membros = request.form.get('membros')
            if nome_tripulacao and capitão and membros:
                tripulacoes.append({
                    'nome_tripulacao': nome_tripulacao,
                    'capitao': capitão,
                    'membros': membros.split(',') 
                })
        
        return render_template('tripulacoes.html', tripulacoes=tripulacoes)
    
    @app.route('/api-personagens', methods=['GET'])
    def api_personagens():
        url = 'https://api.api-onepiece.com/v2/characters/en'
        try:
            res = urllib.request.urlopen(url)
            data = res.read()
            personagens_api = json.loads(data)
        except Exception as e:
            return f'Ocorreu um erro ao consumir a API: {e}'
        
        return render_template('api_personagens.html', personagens_api=personagens_api)
    
  
