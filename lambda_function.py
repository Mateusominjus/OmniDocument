
from json import dumps
from typing import Any






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



