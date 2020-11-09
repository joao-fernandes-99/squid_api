from sql_alchemy import banco
from path import ARQUIVOS

class ArquivoModel(banco.Model):

    __tablename__ = "arquivos"
    id = banco.Column(banco.Integer, primary_key = True, autoincrement=True)
    nome = banco.Column(banco.String(40))
    bloqueio = banco.Column(banco.String(10))

    def __init__(self, nome, bloqueio):
        self.nome = nome
        self.bloqueio = bloqueio

    def json(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'bloqueio': self.bloqueio
        }
    @classmethod
    def find_all(cls):
        arquivo = cls.query.all()
        if arquivo:
            return arquivo
        return None
    
    @classmethod
    def find_by_id(cls, id):
        arquivo = cls.query.filter_by(id=id).first()
        if arquivo:
            return arquivo
        return None

    @classmethod
    def find_filter_bloq(cls):
        arquivos = cls.query.filter_by(bloqueio = "S").all()
        if arquivos:
            return arquivos
        return None
    @classmethod
    def find_filter_dbloq(cls):
        arquivos = cls.query.filter_by(bloqueio = "N").all()
        if arquivos:
            return arquivos
        return None
    
    def atualiza_txt(self):
        path = ARQUIVOS
        arquivos = ArquivoModel.find_filter_bloq()
        try:
            arquivo = open(path, 'w')
            for arq in arquivos:
                arquivo.write(arq.nome + "\n")
            arquivo.close()
        except Exception as ex:
            print(str(ex))
    
    def update_arquivos(self, nome, bloqueio):
        self.nome = nome
        self.bloqueio = bloqueio
    
    def save_arquivo(self):
        banco.session.add(self)
        banco.session.commit()