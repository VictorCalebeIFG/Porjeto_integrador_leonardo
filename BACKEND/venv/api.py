from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo
livros = [
    {'id': 1, 'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes'},
    {'id': 2, 'titulo': 'A Odisséia', 'autor': 'Homero'},
    {'id': 3, 'titulo': 'Orgulho e Preconceito', 'autor': 'Jane Austen'}
]

# Rota para retornar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify({'livros': livros})

# Rota para retornar um livro específico por ID
@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404
    return jsonify({'livro': livro[0]})

if __name__ == '__main__':
    app.run(debug=True)
