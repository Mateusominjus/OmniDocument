
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

