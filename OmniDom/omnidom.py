from OmniDom.perguntas import Pergunta, PerguntaBoleana
from typing import Any

class OmniDom:
  
    def __init__(self,respostas:dict) -> None:
        self._respostas = respostas
        self._perguntas = []


    def _value_ou_default(self,nome:str,default:Any):
        value = self._respostas.get(nome)
        if not value:
            value = default
        return value


    def pergunta_boleana(self,nome:str,request:str,default:Any=None)->Pergunta:        
        value = self._value_ou_default(nome,default)
        pergunta = PerguntaBoleana(nome,request,value)
        self._perguntas.append(pergunta)
        return pergunta
    

    def pergunta_texto(self,nome:str,request:str,default:Any=None)->Pergunta:        
        value = self.retorna_value_ou_default(nome,default)
        pergunta = PerguntaBoleana(nome,request,value)
        self._perguntas.append(pergunta)
        return pergunta
    
    
    def lista_unica(self):
        pass 

    def lista_multipla(self):
        pass 


    def _copile(self):
        return list(map(lambda p: p._render(),self._perguntas))


