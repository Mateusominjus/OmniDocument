import unittest
from OmniDom.omnidom import OmniDom
from testes.testes_perguntas import *


respostas = {
    'a':True,
    'b':False 
}
x = OmniDom(respostas)
a = x.pergunta_boleana()


#if __name__ == '__main__':
#    unittest.main()