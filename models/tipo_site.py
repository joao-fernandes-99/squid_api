from sql_alchemy import banco

class TipoSiteModel(banco.Model):

    __tablename__ = "tipo_site"

    id = banco.Column(banco.Integer, primary_key = True, autoincrement=True)
    nome_tipo = banco.Column(banco.String(40))
    site = banco.relationship('SiteModel',backref='tipo', lazy=True)

    def __init__(self, id,nome_tipo):
        self.id = id
        self.nome_tipo = nome_tipo
    
    def json(self):
        return {
            'self.id' : self.id,
            'self.nome_tipo' : self.nome_tipo
        }

    @classmethod
    def find_all(cls):
        tipo = cls.query.all()
        if tipo:
            return tipo
        return None


