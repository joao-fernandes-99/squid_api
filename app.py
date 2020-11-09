from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from resources.arquivos import Arquivos, Arquivo,Arquinobloq
from resources.palavras import Palavras, Palavra, Palavrasbloq
from resources.tipos_site import TiposSites
from resources.sites import Sites, Site, SitesBloqu
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///confs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

api = Api(app)

api.add_resource(Arquivos, '/arquivos')
api.add_resource(Arquinobloq, '/arquivos-bloqu')
api.add_resource(Arquivo, '/arquivo/<int:id>')

api.add_resource(Palavras, '/palavras')
api.add_resource(Palavrasbloq, '/palavras-bloq')
api.add_resource(Palavra, '/palavra/<int:id>')

api.add_resource(TiposSites, '/tipos-site')

api.add_resource(Sites, '/sites')
api.add_resource(SitesBloqu, '/sites-bloqu')
api.add_resource(Site, '/site/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True, host='192.168.1.103', port=5001)
    