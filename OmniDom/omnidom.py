from varname import varname
from OmniDom.lista_unica import ListaUnica
from OmniDom.perguntas import Pergunta, PerguntaBoleana

from typing import Any, List

class OmniDom:
  
    def __init__(self,respostas:dict) -> None:
        self._respostas = respostas
        self._arvore = []


    def _value_ou_default(self,nome:str,default:Any):
        value = self._respostas.get(nome)
        if not value:
            value = default
        return value


    def pergunta_boleana(self,texto_da_pergunta:str,default:Any=None)->Pergunta:        
        nome = varname()
        value = self._value_ou_default(nome,default)
        pergunta = PerguntaBoleana(nome,texto_da_pergunta,value)
        self._arvore.append(pergunta)
        return pergunta
    

    def pergunta_texto(self,texto_da_pergunta:str,default:Any=None)->Pergunta:  
        nome = varname()      
        value = self._value_ou_default(nome,default)
        pergunta = PerguntaBoleana(nome,texto_da_pergunta,value)
        self._arvore.append(pergunta)
        return pergunta
    
    
    def lista_unica(self,texto_da_pergunta:str,opcoes:List[str]):
        nome = varname()      
        lista_unica = ListaUnica(nome,texto_da_pergunta,opcoes)
    
    

    def _copile(self):
        return list(map(lambda p: p._render(),self._arvore))


