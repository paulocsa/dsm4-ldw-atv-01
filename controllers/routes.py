from flask import Flask, render_template, request

personagens = []


def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    from flask import render_template, request


    @app.route('/lista', methods=['GET', 'POST'])
    def lista_personagens():
        titulo = 'Personagens de Hora de Aventura'
        personagens = [
            {'nome': 'Finn', 'especie': 'Humano'},
            {'nome': 'Jake', 'especie': 'Cão Mágico'},
            {'nome': 'Princesa Jujuba', 'especie': 'Doce'},
            {'nome': 'Rei Gelado', 'especie': 'Humano Transformado'},
            {'nome': 'Marceline', 'especie': 'Vampira'}
        ]
    
        if request.method == 'POST':
            nome = request.form.get('nome')
            especie = request.form.get('especie')
    
            if nome and especie:
                personagens.append({'nome': nome, 'especie': especie})
    
        return render_template('lista.html', titulo=titulo, personagens=personagens)
