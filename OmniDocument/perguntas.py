
class Pergunta:

    def __init__(self,nome:str,tipo:str,texto_da_pergunta:str,value=None) -> None:
        self._nome = nome 
        self._tipo = tipo.__name__
        self._texto_da_pergunta = texto_da_pergunta
        self._value = value

    def get_value(self):
        return self._value    
  
    def __eq__(self, __o: object) -> bool:
        return self._value == __o
    

  
    def _render(self):
        return {
            'nome':self._nome,
            'tipo':self._tipo,
            'texto_da_pergunta':self._texto_da_pergunta,
            'value': self._value
        }



class PerguntaBoleana(Pergunta):
    def __init__(self, nome: str, texto_da_pergunta: str, value=None) -> None:
        super().__init__(nome, bool, texto_da_pergunta, value)


class PerguntaTexto(Pergunta):
    def __init__(self, nome: str, texto_da_pergunta: str, value=None) -> None:
        super().__init__(nome, str, texto_da_pergunta, value)



class PerguntaNumero(Pergunta):
    def __init__(self, nome: str, texto_da_pergunta: str, value=None) -> None:
        super().__init__(nome, float, texto_da_pergunta, value)

    def __gt__(self, __o: object) -> bool:
        return self._value > __o

    def __gte__(self, __o: object) -> bool:
        return self._value >= __o
        

    
        


