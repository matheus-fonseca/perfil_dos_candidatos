# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from models.dao import generico_dao,uf_dao,ocorrencia_basica_dao

#----------------------DAO----------------------------------
class TestDAO(SimpleTestCase):
    """docstring for TestDAO"""
    def setUp(self):    #configura ambiente para teste
        self.dao = generico_dao.GenericoDAO()
        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                                
    
    def shortDescription(self):
        print "Teste da classe GenericoDAO"

    def test_existing_dao_instance(self):
        self.assertIsNotNone(self.dao)
        
    def test_get_conexao(self):
		self.dao.database = ' '
		self.dao.usuario = ' '
		self.dao.senha = ' '
		self.dao.host = ' '
		self.assertIsNone(self.dao.get_conexao())
		
    def test_try_query(self):
		self.dao.conexao = ''
		self.assertIsNone(self.dao.executa_query("show tables"))
		
	

#----------------------UF-----------------------------------
class TestUF(SimpleTestCase):
    """docstring for TestDAO"""
    def setUp(self):    #configura ambiente para teste
        self.uf = uf_dao.UfDAO()
        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                       

    def shortDescription(self):
        print "Teste da classe GenericoDAO"

    def test_existing_uf_dao_instance(self):
        self.assertIsNotNone(self.uf)

    def test_list_uf(self):
        for i in self.uf.lista_ufs():
            self.assertIsNotNone(i)

class TestOcorrencia(SimpleTestCase):
    """docstring for TestOcorrencia"""
    def setUp(self):    #configura ambiente para teste
        self.ocorrencia = ocorrencia_basica_dao.OcorrenciaBasicaDAO()
        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                       

    def shortDescription(self):
        print "Teste da classe OcorrenciaBasica"

    def test_existing_ocorrencia_dao_instance(self):
        self.assertIsNotNone(self.ocorrencia)

    def test_ocorrencia_por_regiao(self):
        # 97012 = Brasilia
        oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012)
        self.assertIsNotNone(oco)   #verifica se não retorna nulo
        oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012,limite=3)
        self.assertIsNotNone(oco)   #verifica se não retorna nulo
        self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
        for i in oco:               #verifica se todos os retornos estão no DF
            self.assertEqual(i.tmuuf, 'DF')


    def test_ocorrencia_por_periodo(self):
    	oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06')
        self.assertIsNotNone(oco)   #verifica se não retorna nulo
        oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06',limite=3)
        self.assertIsNotNone(oco)   #verifica se não retorna nulo
        self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
        for i in oco:               #verifica se as ocorrencias aconteceram em 2006
            self.assertIn('2006', i.ocodataocorrencia)
