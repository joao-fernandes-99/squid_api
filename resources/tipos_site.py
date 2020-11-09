from flask_restful import Resource, reqparse
from models.tipo_site import TipoSiteModel

class TiposSites(Resource):
    def get(self):
        tipo_site = TipoSiteModel.find_all()
        if tipo_site:
            tipo_sites = {}
            for i in tipo_site:
                tipo_sites[i.id] = i.json()
            return {'response' : tipo_sites}, 200
        return {'message' : 'Tipos de Site Not Found'}, 404


