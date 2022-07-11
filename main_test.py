from json import dump
import unittest
from OmniDocument.omni_document import OmniDocument
from testes.testes_perguntas import *




def defini_perguntas(document:OmniDocument):
    danos_morais = document.pergunta_boleana('ha danos morais ?')
    if danos_morais == True:
        valor_dos_danos_morais = document.pergunta_numero('valor dos danos morais')
        
        if valor_dos_danos_morais > 1000:
            descricao = document.pergunta_texto('descreva o por que o valor está tão alto')

        motivos = document.lista_unica('informe o motivo do dano moral',
            opcoes=['pq me tacaram no pau','pq eu bati no carro dele','sei lá porra']
        )
    sub = document.sub_document()
    teste = sub.pergunta_boleana('eai parsa')
    sub_sub = sub.sub_document()
    r = sub_sub.pergunta_texto('eai')
    

respostas = {
    'danos_morais':True,
    'valor_dos_danos_morais':20000
}
x = OmniDocument(respostas)
defini_perguntas(x)
r = x._render()
dump(r,open('teste.json','w'),indent=4,ensure_ascii=False)
#if __name__ == '__main__':
#    unittest.main()