from flask_restful import Resource, reqparse
from models.palavra import PalavraModel

class Palavras(Resource): 
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome_palvra', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")

    def get(self):
        palavra = PalavraModel.find_filter_bloq()
        if palavra:
            palavras = {}
            for i in palavra:
                palavras[i.id] = i.json()
            return {'response' : palavras}, 200
        return {'message' : 'palavras Not Found'}, 404
    
    def post(self):
        dados = Palavras.arguments.parse_args()
        palavra = PalavraModel(dados.nome_palvra, dados.bloqueio)
        try:
            palavra.save_palavra()
            return {"Message":"Palavra Cadastrada com Sucesso"}
        except Exception as ex:
            return {"Message":"Errp ap Cadastrar Palavra"}
    
class Palavra(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome_palvra', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")

    def get(self, id):
        palavra = PalavraModel.find_by_id(id)
        if palavra:
            return palavra.json(), 200
        return {"Message" : "Palavra não encontrada"}

    def put(self, id):
        dados = Palavra.arguments.parse_args()
        palavra = PalavraModel.find_by_id(id)
        if palavra:
            palavra.update_palavra(dados.nome_palvra, dados.bloqueio)
            try:
                palavra.save_palavra()
                palavra.atualiza_txt()
                return {'Message' : 'Palavra Alterada com Sucesso'}, 200
            except Exception as ex:
                return {"Message" : str(ex)}, 500
        return {"Message":'Palavra não existe'}

    def delete(self, id):
        palavra = PalavraModel.find_by_id(id)
        palavra.atualiza_txt()

class Palavrasbloq(Resource):
    def get(self):
        palavra = PalavraModel.find_filter_dbloq()
        if palavra:
            palavras = {}
            for i in palavra:
                palavras[i.id] = i.json()
            return {'response' : palavras}