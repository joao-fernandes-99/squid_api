from sql_alchemy import banco
from path import PALAVRAS_BLOQUEADAS

class PalavraModel(banco.Model):

    __tablename__ = "palavras"

    id = banco.Column(banco.Integer, primary_key = True, autoincrement=True)
    nome_palavra = banco.Column(banco.String(40))
    bloqueio = banco.Column(banco.String(10))

    def __init__(self, nome_palavra, bloqueio):
        self.nome_palavra = nome_palavra
        self.bloqueio = bloqueio
    
    def json(self):
        return {
            'id' : self.id,
            'nome_palvra' : self.nome_palavra,
            'bloqueio' : self.bloqueio
        }
    
    @classmethod
    def find_all(cls):
        palavra = cls.query.all()
        if palavra:
            return palavra
        return None
    
    @classmethod
    def find_by_id(cls, id):
        palavra = cls.query.filter_by(id=id).first()
        if palavra:
            return palavra
        return None
    
    @classmethod
    def find_filter_bloq(cls):
        palavras = cls.query.filter_by(bloqueio = "S").all()
        if palavras:
            return palavras
        return None
        
    @classmethod
    def find_filter_dbloq(cls):
        palavras = cls.query.filter_by(bloqueio = "N").all()
        if palavras:
            return palavras
        return None

    
    def atualiza_txt(self):
        path = PALAVRAS_BLOQUEADAS
        palavras = PalavraModel.find_filter_bloq()
        try:
            arquivo = open(path, 'w')
            for palavra in palavras:
                arquivo.write(palavra.nome_palavra + "\n")
            arquivo.close()
        except Exception as ex:
            print(str(ex))
    
    def update_palavra(self, nome_palavra, bloqueio):
        self.nome_palavra = nome_palavra
        self.bloqueio = bloqueio
    
    def save_palavra(self):
        banco.session.add(self)
        banco.session.commit()