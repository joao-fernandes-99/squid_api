from sql_alchemy import banco
from path import URLECOMMERCE, REDESSOCIAIS, SITESPORNOGRAFICOS, JOGOSONLINE

class SiteModel(banco.Model):
    
    __tablename__ = "sites"

    id = banco.Column(banco.Integer, primary_key = True, autoincrement=True)
    nome_site = banco.Column(banco.String(40))
    tpo_site = banco.Column(banco.Integer, banco.ForeignKey('tipo_site.id'), nullable=False)
    bloqueio = banco.Column(banco.String(10))
    

    def __init__(self,nome_site, tipo_site, bloqueio):
        self.nome_site = nome_site
        self.tpo_site = tipo_site
        self.bloqueio = bloqueio

    def json(self):
        return {
            'id' : self.id,
            'nome_site':self.nome_site,
            'tpo_site': self.tpo_site,
            'bloqueio': self.bloqueio
        }
    
    @classmethod
    def find_all(cls):
        site = cls.query.filter_by(bloqueio="S").all()
        if site:
            return site
        return None

    @classmethod
    def find_by_id(cls, id):
        site = cls.query.filter_by(id=id).first()
        if site:
            return site
        return None
    
    @classmethod
    def find_by_tipo_site(cls, tipo_site):
        sites = cls.query.filter_by(tpo_site = tipo_site, bloqueio = "S").all()
        return sites

    @classmethod
    def find_all_bloqu(cls):
        sites = cls.query.filter_by(bloqueio="N").all()
        if sites:
            return sites
        return None


    @classmethod
    def retorna_path(cls,tipo_site):
        if tipo_site == 1:
            return URLECOMMERCE

        elif tipo_site == 2:
            return REDESSOCIAIS

        elif tipo_site == 3:
            return JOGOSONLINE

        elif tipo_site == 4:
            return SITESPORNOGRAFICOS

    def atualiza_txt(self):
        tipo_de_site = self.tpo_site
        sites = SiteModel.find_by_tipo_site(tipo_de_site)
        path = SiteModel.retorna_path(tipo_de_site)
        try:
            arquivo = open(path, 'w')
            for site in sites:
                arquivo.write(site.nome_site + "\n")
            arquivo.close()
        except Exception as ex:
            print(str(ex))

    def update_site(self, nome_site, tpo_site, bloqueio):
        self.nome_site = nome_site
        self.tpo_site = tpo_site
        self.bloqueio = bloqueio

    def save_site(self):
        banco.session.add(self)
        banco.session.commit()
