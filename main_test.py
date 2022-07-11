import unittest
from OmniDom.omnidom import OmniDom
from testes.testes_perguntas import *




def defini_perguntas(document:OmniDom):
    danos_morais = document.pergunta_boleana('ha danos morais ?')
    if danos_morais == True:
        valor_dos_danos_morais = document.pergunta_texto('valor dos danos morais')
    pass 





respostas = {
    'a':True,
    'b':False 
}
x = OmniDom(respostas)
defini_perguntas(x)
r = x._render()
print(r)
#if __name__ == '__main__':
#    unittest.main()