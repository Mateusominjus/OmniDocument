

from OmniDom.omnidom import OmniDom

class SubDom(OmniDom):

    def __init__(self, value: dict,nome:str) -> None:
        super().__init__(value)
        self._nome = nome 
    
    def _render(self):
        return {
            'nome':self._nome,
            'itens':super()._render()
        }