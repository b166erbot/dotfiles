from unittest import TestCase
from unittest.mock import patch, MagicMock
from fazer_backup import passar_regex, pegar_caminhos


print('para os testes rodarem, é necessário que as pastas existam no computador')


class TestPassarRegex(TestCase):
    def setUp(self):
        self.expressao = '[\"\']([^\"\']+)[\"\']|([^\'\"\s-]+)'
    
    def test_texto_1(self):
        texto = '~/Downloads/ - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste.py\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '~/Downloads/', 'teste', 'teste.py', 'teste.mp3',
            'teste teste', 'teste teste.mp3', 'teste teste.py'
        ]
        self.assertEqual(resultado, esperado)
    
    def test_texto_2(self):
        texto = '/home/none/Downloads - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '/home/none/Downloads', 'teste', 'teste.py',
            'teste.mp3', 'teste teste', 'teste teste.mp3',
            'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_3(self):
        texto = '"/home/none/teste teste" - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '/home/none/teste teste', 'teste', 'teste.py',
            'teste.mp3', 'teste teste', 'teste teste.mp3',
            'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_4(self):
        texto = '~/Downloads/* - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '~/Downloads/*', 'teste', 'teste.py', 'teste.mp3',
            'teste teste', 'teste teste.mp3', 'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_5(self):
        texto = '~/Downloads/. - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '~/Downloads/.', 'teste', 'teste.py', 'teste.mp3',
            'teste teste', 'teste teste.mp3', 'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_6(self):
        texto = '\'/home/none/teste teste\' - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '/home/none/teste teste', 'teste', 'teste.py',
            'teste.mp3', 'teste teste', 'teste teste.mp3',
            'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_6(self):
        texto = '"~/Downloads/teste teste/." -teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\''
        resultado = passar_regex(self.expressao, texto)
        esperado = [
            '~/Downloads/teste teste/.', 'teste', 'teste.py',
            'teste.mp3', 'teste teste', 'teste teste.mp3',
            'teste teste'
        ]
        self.assertEqual(resultado, esperado)
    
    def teste_texto_7(self):
        texto = '~/Downloads/*'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['~/Downloads/*']
        self.assertEqual(resultado, esperado)
    
    def teste_texto_8(self):
        texto = '~/Downloads/*.*'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['~/Downloads/*.*']
        self.assertEqual(resultado, esperado)
    
    def teste_texto_9(self):
        texto = '~/Downloads'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['~/Downloads']
        self.assertEqual(resultado, esperado)
    
    def teste_texto_10(self):
        texto = '/home/none/*'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['/home/none/*']
        self.assertEqual(resultado, esperado)
    
    def teste_texto_11(self):
        texto = '/home/none/*.*'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['/home/none/*.*']
        self.assertEqual(resultado, esperado)

    def teste_texto_12(self):
        texto = '/home/none'
        resultado = passar_regex(self.expressao, texto)
        esperado = ['/home/none']
        self.assertEqual(resultado, esperado)


class TestPegarCaminhos(TestCase):
    side_eff = [
        '~/Downloads/ - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste.py\'',
        '/home/none/Downloads - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '"/home/none/python scripts" - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '~/Downloads/* - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '~/Downloads/. - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '\'/home/none/python scripts\' - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '"~/python scripts/." - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
        '~/Downloads/*',
        '~/Downloads/*.*',
        '~/Downloads',
        '/home/none/*',
        '/home/none/*.*',
        '/home/none',
        ''
    ]

    @patch('fazer_backup.print')
    @patch('fazer_backup.input', side_effect=side_eff)
    def test_todos_os_textos_possiveis_sendo_testados(self, *_):
        esperado = [
            '~/Downloads/ - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste.py\'',
            '/home/none/Downloads - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '"/home/none/python scripts" - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '~/Downloads/* - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '~/Downloads/. - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '\'/home/none/python scripts\' - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '"~/python scripts/." - teste teste.py teste.mp3 "teste teste" "teste teste.mp3" \'teste teste\'',
            '~/Downloads/*',
            '~/Downloads/*.*',
            '~/Downloads',
            '/home/none/*',
            '/home/none/*.*',
            '/home/none'
        ]
        resultado = pegar_caminhos()
        self.assertEqual(resultado, esperado)
