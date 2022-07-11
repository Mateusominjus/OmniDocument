
class ListaUnica:

    def __init__(self,nome:str,texto_da_pergunta:str,opcoes:list) -> None:
        self._nome = nome 
        self._tipo = 'lista_unica'
        self._texto_da_pergunta = texto_da_pergunta
        self._opcoes = opcoes
    
    def _render(self):
        return {
            'nome':self._nome,
            'tipo':self._tipo,
            'texto_da_pergunta':self._texto_da_pergunta,
            'opcoes': self._opcoes
        }
    