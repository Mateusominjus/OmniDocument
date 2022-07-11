import unittest

from OmniDocument.perguntas import Pergunta, PerguntaBoleana


class TestPerguntas(unittest.TestCase):

    def test_criacao(self):
        pergunta = Pergunta(
            nome='teste',tipo=bool,
            texto_da_pergunta='texto',
            value=True)

        self.assertEqual(pergunta._nome,'teste')
        self.assertEqual(pergunta._tipo,'bool')
        self.assertEqual(pergunta._texto_da_pergunta,'texto')
        self.assertEqual(pergunta.value,True)


    def test_render(self):
        pergunta = Pergunta(
            nome='teste',tipo=bool,
            texto_da_pergunta='texto',
            value=True)
        esperado = {
            'nome':'teste',
            'tipo':'bool',
            'pergunta':'texto',
            'value': True
        }
        self.assertEqual(pergunta._render(),esperado)


    def test_render_com_modificacao(self):
        pergunta = Pergunta(
            nome='teste',tipo=bool,
            texto_da_pergunta='texto',
            value=True)
        pergunta.value = False
        esperado = {
            'nome':'teste',
            'tipo':'bool',
            'pergunta':'texto',
            'value':False
        }
        self.assertEqual(pergunta._render(),esperado)

    def test_pergunta_boleana(self):
        pergunta = PerguntaBoleana('teste','texto',False)
        self.assertEqual(pergunta._nome,'teste')
        self.assertEqual(pergunta._tipo,'bool')
        self.assertEqual(pergunta._texto_da_pergunta,'texto')
        self.assertEqual(pergunta.value,False)

    def test_pergunta_texto(self):
        pergunta = Pergunta('teste','texto',False)
        self.assertEqual(pergunta._nome,'teste')
        self.assertEqual(pergunta._tipo,'bool')
        self.assertEqual(pergunta._texto_da_pergunta,'texto')
        self.assertEqual(pergunta.value,False)