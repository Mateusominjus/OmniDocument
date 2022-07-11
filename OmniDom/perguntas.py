
class Pergunta:

    def __init__(self,nome:str,tipo:str,texto_da_pergunta:str,value=None) -> None:
        self._nome = nome 
        self._tipo = tipo.__name__
        self._texto_da_pergunta = texto_da_pergunta
        self.value = value
    
    def _render(self):
        return {
            'nome':self._nome,
            'tipo':self._tipo,
            'texto_da_pergunta':self._texto_da_pergunta,
            'value': self.value
        }

class PerguntaBoleana(Pergunta):
    def __init__(self, nome: str, request: str, value=None) -> None:
        super().__init__(nome, bool, request, value)


class PerguntaTexto(Pergunta):
    def __init__(self, nome: str, request: str, value=None) -> None:
        super().__init__(nome, str, request, value)


