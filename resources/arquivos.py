from flask_restful import Resource, reqparse
from models.arquivos import ArquivoModel

class Arquivos(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")

    def get(self):
        arquivo = ArquivoModel.find_filter_bloq()
        if arquivo:
            arquivos = {}
            for i in arquivo:
                arquivos[i.id] = i.json()
            return {'response' : arquivos}, 200
        return {'message' : 'Arquivos Not Found'}, 404
    
    def post(self):
        dados = Arquivos.arguments.parse_args()
        arquivo = ArquivoModel(dados.nome, dados.bloqueio)
        try:
            arquivo.save_arquivo()
            return {"Message" :" Arquivo Cadastrado com sucesso"}
        except Exception as ex:
            return {"Message":"Erro ao cadastrar Arquivo"}
    
class Arquivo(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")

    def get(self, id):
        arquivo = ArquivoModel.find_by_id(id)
        if arquivo:
            return arquivo.json()
        return {"Message":"Arquivo não encontrado"}
    
    def put(self, id):
        dados = Arquivo.arguments.parse_args()
        arquivo = ArquivoModel.find_by_id(id)
        if arquivo:
            arquivo.update_arquivos(dados.nome, dados.bloqueio)
            try:
                arquivo.save_arquivo()
                arquivo.atualiza_txt()
            except Exception as ex:
                return {'message': str(ex)}
            return {'message': 'arquivo alterado com sucesso'}, 200
        return {'message':'Arquino não existe'}
    
    def delete(self, id):
        arquivo = ArquivoModel.find_by_id(id)
        arquivo.atualiza_txt()

class Arquinobloq(Resource):
    def get(self):
        arquivo = ArquivoModel.find_filter_dbloq()
        if arquivo:
            arquivos = {}
            for i in arquivo:
                arquivos[i.id] = i.json()
            return {'response': arquivos}

