from flask_restful import Resource, reqparse
from models.site import SiteModel

class Sites(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome_site', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")
    arguments.add_argument('tpo_site', required=True, help="O campo tipo_site é obrigatório")

    def get(self):
        site = SiteModel.find_all()
        if site:
            sites = {}
            #return arquivo.json()
            for i in site:
                #print(i.json())
                sites[i.id] = i.json()
            return {'response' : sites}, 200
        return {'message' : 'Sites Not Found'}, 404
    
    def post(self):
        dados = Sites.arguments.parse_args()
        site = SiteModel(dados.nome_site, dados.tpo_site, dados.bloqueio)
        try:
            site.save_site()
            return {"Message":"Site Cadastrado com sucesso"}, 201
        except Exception as ex:
            return {"Message": "Erro ao Cadastrar Site"}

    
class Site(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome_site', required=True, help="O campo nome é obrigatório")
    arguments.add_argument('bloqueio', required=True, help="O campo bloqueio é obrigatório")
    arguments.add_argument('tpo_site', required=True, help="O campo tipo_site é obrigatório")

    def get(self, id):
        site = SiteModel.find_by_id(id)
        if site:
            return site.json()
        return {"message": "Site não Encontrado!"}, 404


    def put(self, id):
        dados = Site.arguments.parse_args()
        site = SiteModel.find_by_id(id)
        if site:
            site.update_site(dados.nome_site, dados.tpo_site, dados.bloqueio)
            try:
                site.save_site()
                site.atualiza_txt()
                return {'message': 'Site alterada com sucesso'}, 200
            except Exception as ex:
                return {'message': str(ex)}, 500  
        return {'message':'Site não existe'}, 404

    def delete(self, id):
        site = SiteModel.find_by_id(id)
        site.atualiza_txt()

class SitesBloqu(Resource):
    def get(self):
        site = SiteModel.find_all_bloqu()
        if site:
            sites = {}
            for i in site:
                sites[i.id] = i.json()
            return {'response' : sites}, 200
            