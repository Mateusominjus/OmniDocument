

from OmniDocument.omni_document import OmniDocument

class SubDom(OmniDocument):

    def __init__(self, value: dict,nome:str) -> None:
        super().__init__(value)
        self._nome = nome 
    
    def _render(self):
        return {
            'nome':self._nome,
            'tipo':'document',
            'itens':super()._render()
        }