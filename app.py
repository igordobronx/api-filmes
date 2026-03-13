from flask import Flask, request, jsonify

app = Flask(__name__)

filmes = []
filme_id_control = 1

@app.route('/filmes', methods=['POST'])
def adicionar_filme():
    global filme_id_control
    data = request.get_json()
    novo_filme = {
        "id": filme_id_control,
        "titulo": data.get("titulo"),
        "genero": data.get("genero"),
        "assistido": False 
    }
    filme_id_control += 1
    filmes.append(novo_filme)
    print(filmes)
    return jsonify({"mensagem": "filme adicionado com sucesso"})

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(filmes)

@app.route('/filmes/<int:id>', methods=['GET'])
def listar_filmes_id(id):
    filme = None
    for i in filmes:
        if i["id"] == id:
            filme = i 
            return jsonify(filme)

    return jsonify({"mensagem": "nao foi possivel encontrar seu filme"}), 404

@app.route('/filmes/<int:id>', methods=['PUT'])
def atualizar_filme(id):
    filme = None
    for i in filmes:
        if i["id"] == id:
            filme = i
    print(filme)

    if filme is None:
        return jsonify({"mensagem": "nao foi possivel encontrar seu filme"}), 404

    data = request.get_json()
    filme["titulo"] = data.get("titulo", filme["titulo"]) #dicionario["chave"] = novo_dicionario.get("chave", valor_padrao)
    filme["genero"] = data.get("genero", filme["genero"])
    filme["assistido"] = data.get("assistido", filme["assistido"])
    return jsonify({"mensagem": "filme atualizado com sucesso.", "filme": filme })

@app.route('/filmes/<int:id>', methods=['DELETE'])
def deletar_filme(id):
    filme = None
    for i in filmes:
        if i["id"] == id:
            filme = i
            break

    if filme is None:
        return jsonify({"mensagem": "nao foi encontrado seu filme"}), 404
    
    filmes.remove(filme)
    return jsonify({"mensagem": "filme tirado da lista com sucesso."})
    

if __name__ == "__main__":
    app.run(debug=True)