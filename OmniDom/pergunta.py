
class Pergunta:

    def __init__(self,nome:str,tipo:str,request:str,value=None) -> None:
        self._nome = nome 
        self._tipo = tipo.__name__
        self._texto_da_pergunta = request
        self.value = value
    
    def _render(self):
        return {
            'nome':self._nome,
            'tipo':self._tipo,
            'pergunta':self._texto_da_pergunta,
            'value': self.value
        }

