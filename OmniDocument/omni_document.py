from varname import varname,ImproperUseError
from OmniDocument.lista_unica import ListaUnica
from OmniDocument.perguntas import Pergunta, PerguntaBoleana, PerguntaNumero, PerguntaTexto

from typing import Any, List



class OmniDocument:
  
    def __init__(self,respostas:dict) -> None:
        self._respostas = respostas
        self._text = ''
        self._arvore = []
        

    def _value_ou_default(self,nome:str,default:Any):
        value = self._respostas.get(nome)
        if not value:
            value = default
        return value


    def pergunta_boleana(self,texto_da_pergunta:str,default:Any=None)->Pergunta:        
        try:
            nome = varname()
        except ImproperUseError:
            raise Exception('sempre deve haver uma variável antes do elemento')
        value = self._value_ou_default(nome,default)
        pergunta = PerguntaBoleana(nome,texto_da_pergunta,value)
        self._arvore.append(pergunta)
        return pergunta
    

    def pergunta_texto(self,texto_da_pergunta:str,default:Any=None)->Pergunta:  
        try:
            nome = varname()
        except ImproperUseError:
            raise Exception('sempre deve haver uma variável antes do elemento')
        value = self._value_ou_default(nome,default)
        pergunta = PerguntaTexto(nome,texto_da_pergunta,value)
        self._arvore.append(pergunta)
        return pergunta


    def pergunta_numero(self,texto_da_pergunta:str,default:Any=None)->Pergunta:  
        try:
            nome = varname()
        except ImproperUseError:
            raise Exception('sempre deve haver uma variável antes do elemento')
        value = self._value_ou_default(nome,default)
        if not value:
            value  = 0
        pergunta = PerguntaNumero(nome,texto_da_pergunta,value)
        self._arvore.append(pergunta)
        return pergunta
    
    
    def lista_unica(self,texto_da_pergunta:str,opcoes:List[str]):
        try:
            nome = varname()
        except ImproperUseError:
            raise Exception('sempre deve haver uma variável antes do elemento')

        lista_unica = ListaUnica(nome,texto_da_pergunta,opcoes)
        self._arvore.append(lista_unica)
        return lista_unica
    
    
    def sub_document(self):
        try:
            nome = varname()
        except ImproperUseError:
            raise Exception('sempre deve haver uma variável antes do elemento')

        value = self._value_ou_default(nome,{})
        from OmniDocument.sub_document import SubDom
        
        sub_document = SubDom(value,nome)
        self._arvore.append(sub_document)
        return sub_document
    

    def print(self,text:str):
        self._text+=text
    
    def _render_text(self):
        pass 
    
    def _render(self):
        return list(map(lambda p: p._render(),self._arvore))


