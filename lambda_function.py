
from json import dumps
from typing import Any





class OmniDom:
    pass 
    def __init__(self,respostas:dict) -> None:
        self._resposta = respostas
        self._perguntas = []


    def pergunta(self,nome:str, tipo:str,request:str,default:Any=None)->Pergunta:
        
        value = self._resposta.get(nome)
                 
        if not value:
            value = default
    
        pergunta = Pergunta(nome,tipo,request,value)

        self._perguntas.append(pergunta)
        return pergunta
    
    def copile(self):
        return list(map(lambda p: p._render(),self._perguntas))





def defini_perguntas(omni_dom:OmniDom):

    danos_morais = omni_dom.pergunta('danos_morais',bool,'ha pedido de danos morais',False)
   
    if danos_morais.value:
        quantificado = omni_dom.pergunta('quantificado',bool,'o pedido foi quantificado em salarios minimos')
        if quantificado.value:    
            quantidade_de_sarios_minimos= omni_dom.pergunta(
            'quantidade_de_sarios_minimos',
            int,
            'informe a quantidade de salarios minimos'
            ) 



def lambda_handler(event:dict,context):
    body = event['body']
    omni_dom = OmniDom(body)
    defini_perguntas(omni_dom)
    return {
        'statusCode':'ok',
        'body':dumps(omni_dom.copile(),indent=4,ensure_ascii=False)
    }

