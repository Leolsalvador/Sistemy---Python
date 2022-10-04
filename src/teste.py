import datetime
from logging import exception
import sys
from PySide2.QtWidgets import ( QApplication,QMainWindow,  QTableWidgetItem, QWidget)
from PyQt6.QtCore import Qt
from ui_gestaoestoque import Ui_MainWindow
import sqlite3
import pymsgbox as a
import re
import database

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, name = "bank.db") -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Gestão de Estoque")
        self.showMaximized()

        self.btn_realizarvenda.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicial))
        self.btn_estoque.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.estoque))
        self.btn_entradaesaida.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.entradaesaida))
        self.btn_finalizarvenda.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.btn_irfornecedor.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.fornecedor))
        self.btn_irproduto.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.produto))
        self.btn_finalizarvenda_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicial))
        self.btn_cancelar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicial))
        self.btn_entrada.clicked.connect(lambda: self.stackedWidget_4.setCurrentWidget(self.page))
        self.btn_saida.clicked.connect(lambda: self.stackedWidget_4.setCurrentWidget(self.page_2))
        #self.btn_editar.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.editar))
        self.btn_editar_2.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.estoque_2))
        self.btn_detalharvenda_2.clicked.connect(lambda: self.stackedWidget_4.setCurrentWidget(self.page_3))
        self.btn_pesquisar_5.clicked.connect(lambda: self.stackedWidget_4.setCurrentWidget(self.page_2))
        self.btn_voltar_estoque.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.estoque_2))

        self.btn_pesquisar.clicked.connect(self.estocarprodutos)
        self.btn_inserirnocarrinho.clicked.connect(self.quantidade)
        self.btn_apagaritens.clicked.connect(self.apagar_carrinho)
        self.btn_estoque.clicked.connect(self.ver_estoque)
        self.btn_finalizarvenda.clicked.connect(self.verificarvenda)
        self.btn_salvar.clicked.connect(self.v_insert_produtos)
        self.btn_salvar_2.clicked.connect(self.v_insert_produtos)
        self.btn_finalizarvenda_3.clicked.connect(self.zerou)
        self.btn_entradaesaida.clicked.connect(self.saida)
        self.btn_editar_2.clicked.connect(self.att_estoque)
        self.btn_excluir.clicked.connect(self.excluir_estoque)
        self.btn_pesquisar_2.clicked.connect(self.pesquisar_no_estoque)
        self.btn_pesquisar_3.clicked.connect(self.pesquisa_na_saida)
        self.btn_detalharvenda_2.clicked.connect(self.detalharvenda)
        self.btn_entrada.clicked.connect(self.entradas)
        self.btn_pesquisar_6.clicked.connect(self.pesquisar_na_entrada)
        self.btn_pesquisar_4.clicked.connect(self.pesquisar_na_vendadetalhada)
        self.btn_cadastrar.clicked.connect(self.abrir_cad)
        self.btn_editar.clicked.connect(self.abrir_edit)
        
        self.tb_pesquisa.selectionModel().selectionChanged.connect(self.selecionar_pesquisa)
        self.tb_carrinho.selectionModel().selectionChanged.connect(self.selecionar_carrinho)
        self.tb_estoque.selectionModel().selectionChanged.connect(self.selecionar_estoque)
        self.tb_saida.selectionModel().selectionChanged.connect(self.selecionar_saida)

        self.name = name
        self.t = 0

    def abrir_edit(self):

        self.senha = a.password("Digite a senha", "Senha", "", "*")
        if self.senha == "123":
            self.stackedWidget_3.setCurrentWidget(self.editar)
        else:
            a.alert("Senha incorreta", "Alerta")

    def abrir_cad(self):

        self.senha = a.password("Digite a senha", "Senha", "", "*")
        if self.senha == "123":
            self.stackedWidget.setCurrentWidget(self.cadastrarprodutos)
        else:
            a.alert("Senha incorreta", "Alerta")

    def voltar_cadastro(self):
        self.stackedWidget.setCurrentWidget(self.cadastrarprodutos)
    
    def voltar_estoque(self):
        self.stackedWidget_3.setCurrentWidget(self.editar)
        self.editar_estoque()

    def conecta(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def v_insert_produtos(self):
        self.hoje = datetime.datetime.today()
        self.data = format(self.hoje,"%d/%m/%Y")
        self.n1 = self.entry_nome.text()
        self.n = self.n1.upper()
        self.d = self.entry_dimensoes_2.text()
        self.c = self.entry_codigo.text()
        self.vv = self.entry_venda.text()
        self.p = self.entry_peso.text()
        self.vc = self.entry_custo.text()
        self.q = self.entry_quantidade.text()
        self.di = self.entry_dimensoes.text()
        self.nf = self.entry_nfornecedor.text()
        self.tf = self.entry_tfornecedor.text()
        if (self.n1 == "" or self.d == "" or self.c == "" or self.vv == "" or self.p == "" or self.vc == "" or self.q == "" or self.di == "" or self.nf == "" or self.tf == ""):
            a.alert("Preencha todos os campos!","Alerta")
        else:
            self.insert_produtos()

    def insert_produtos(self):

        self.conecta()

        self.hoje = datetime.datetime.today()
        self.data = format(self.hoje,"%d/%m/%Y")
        self.n1 = self.entry_nome.text()
        self.n = self.n1.upper()
        self.d = self.entry_dimensoes_2.text()
        self.c = self.entry_codigo.text()
        self.vv = self.entry_venda.text()
        self.p = self.entry_peso.text()
        self.vc = self.entry_custo.text()
        self.q = self.entry_quantidade.text()
        self.di = self.entry_dimensoes.text()
        self.nf = self.entry_nfornecedor.text()
        self.tf = self.entry_tfornecedor.text()

        self.insert_prod()
        a.alert("Dados inseridos com sucesso", 'Inserido')

        self.n = self.entry_nome.setText("")
        self.d = self.entry_dimensoes_2.setText("")
        self.c = self.entry_codigo.setText("")
        self.vv = self.entry_venda.setText("")
        self.p = self.entry_peso.setText("")
        self.vc = self.entry_custo.setText("")
        self.q = self.entry_quantidade.setText("")
        self.di = self.entry_dimensoes.setText("")
        self.nf = self.entry_nfornecedor.setText("")
        self.tf = self.entry_tfornecedor.setText("")

        

    def ver_estoque(self):
        self.conecta()
        self.view_estoque()
        window.tb_estoque.setRowCount(len(self.v_estoque))
        window.tb_estoque.setColumnCount(11)

        for i in range (0, len(self.v_estoque)):
            for j in range(0, 11):
                window.tb_estoque.setItem(i,j,QTableWidgetItem(str(self.v_estoque[i][j])))

        self.close_connection()

    def ver_produtos(self):
        self.conecta()
        self.view_prod()
        self.close_connection()
        
    def venda_pp_produto(self, nome, quantidade):
        self.conecta()
        self.sold_pp_prod(nome, quantidade)
        self.close_connection()
     
    def pesquisa_saida(self, nome):
        self.conecta()
        self.search_exit(nome)
        self.close_connection()

    def pesquisa_estoque(self,nome):
        self.conecta()
        self.search_store(nome)
        self.close_connection()

    def pesquisa_prodvendas(self,nome):
        
        self.conecta()
        self.search_prod_sold(nome)
        self.close_connection()

    def pesquisa_produto(self,nome):

        self.conecta()
        self.search_prod(nome)
        self.close_connection()
    
    def estocarprodutos(self):

        self.nom= self.entry_pesquisar.text()
        self.nome = self.nom.upper()
        self.conecta()
        self.pesquisa_produto(self.nome)
        window.tb_pesquisa.setRowCount(len(self.result))
        window.tb_pesquisa.setColumnCount(6)

        for i in range (0, len(self.result)):
            for j in range(0, 6):
                window.tb_pesquisa.setItem(i,j,QTableWidgetItem(str(self.result[i][j])))
        self.alfa = self.result[self.id_row]
        self.close_connection()

    def pesquisar_na_entrada(self):
        self.nom= self.entry_pesquisar_5.text()
        self.nome = self.nom.upper()
        self.conecta()
        self.pesquisa_estoque(self.nome)
        window.tb_entrada.setRowCount(len(self.result))
        window.tb_entrada.setColumnCount(11)

        for i in range (0, len(self.result)):
            for j in range(0, 11):
                window.tb_entrada.setItem(i,j,QTableWidgetItem(str(self.result[i][j])))
                    
        self.close_connection()

    def pesquisar_na_vendadetalhada(self):
        self.nom= self.entry_pesquisar_4.text()
        self.nome = self.nom.upper()
        self.conecta()
        self.pesquisa_prodvendas(self.nome)
        window.tb_vendadetalhada.setRowCount(len(self.pdv))
        window.tb_vendadetalhada.setColumnCount(6)

        for i in range (0, len(self.pdv)):
            for j in range(0, 6):
                window.tb_vendadetalhada.setItem(i,j,QTableWidgetItem(str(self.pdv[i][j])))
                    
        self.close_connection()

    def pesquisar_no_estoque(self):
        self.nom= self.entry_pesquisar_2.text()
        self.nome = self.nom.upper()
        self.conecta()
        self.pesquisa_estoque(self.nome)
        window.tb_estoque.setRowCount(len(self.result))
        window.tb_estoque.setColumnCount(11)

        for i in range (0, len(self.result)):
            for j in range(0, 11):
                window.tb_estoque.setItem(i,j,QTableWidgetItem(str(self.result[i][j])))
                    
        self.close_connection()

    def pesquisa_na_saida(self):
        self.nome = self.entry_pesquisar_3.text()
        self.conecta()
        self.pesquisa_saida(self.nome)
        window.tb_saida.setRowCount(len(self.result))
        window.tb_saida.setColumnCount(5)

        for i in range (0, len(self.result)):
            for j in range(0, 5):
                window.tb_saida.setItem(i,j,QTableWidgetItem(str(self.result[i][j])))
                    
        self.close_connection()

    def quantidade(self):
        self.qtd = int(self.entry_quantidade_2.text())

        if self.qtd <=0:
            a.alert("Quantidade de produtos inválido","Alerta")
        else:
            self.conecta()
            self.else_qtd()
            if self.qtd <= int(self.comp[0][0]):
                self.guardar_carrinho()
            else:
                a.alert("Quantidade execedida do estoque", "ALERTA")

    def selecionar_pesquisa(self, selected):
        
        for ix in selected.indexes():
                self.id_row = (ix.row())
                self.id_column = (ix.column())
                self.alfa = self.result[self.id_row]
                print(self.alfa[0])

    def guardar_carrinho(self):
        self.conecta()
        if self.alfa[0] != self.t:
            self.keep_cart()
            window.tb_carrinho.setRowCount(len(self.add_carrinho))
            window.tb_carrinho.setColumnCount(6)

            for i in range (0, len(self.add_carrinho)):
                for j in range(0, 6):
                    window.tb_carrinho.setItem(i,j,QTableWidgetItem(str(self.add_carrinho[i][j])))
            
            self.calcular_preco()
            self.quantidade_produtos()
            self.t = self.alfa[0]
        else:
            a.alert("Produto já inserido no carrinho", "Alerta")
        self.close_connection()
    
    def selecionar_carrinho(self, selected):

        for ix in selected.indexes():
                self.id_row = (ix.row())
                print(self.id_row)
                self.id_column = (ix.column())
                self.teta = self.add_carrinho[self.id_row]

    def apagar_carrinho(self):
        self.t = 0
        self.conecta()
        self.delete_cart()
        window.tb_carrinho.setRowCount(len(self.add_carrinho))
        window.tb_carrinho.setColumnCount(6)

        for i in range (0, len(self.add_carrinho)):
            for j in range(0, 6):
                window.tb_carrinho.setItem(i,j,QTableWidgetItem(str(self.add_carrinho[i][j])))
        self.calcular_preco()
        self.quantidade_produtos()
        self.teta = self.add_carrinho[self.id_row]
        self.close_connection() 

    def calcular_preco(self):
        self.conecta()
        self.calc_price()
        self.f_valor_total = re.sub("\[|\]|\(|\)|\,","",str(self.valor_total))
        print(self.f_valor_total)
        if self.f_valor_total != "None":
            self.label_18.setText(f"R$ {float(self.f_valor_total)}")      
        else:
            self.label_18.setText("0") 
        self.close_connection()

    def selecionar_estoque(self, selected):

         for ix in selected.indexes():
                self.id_row = (ix.row())
                self.id_column = (ix.column())
                self.beta = self.v_estoque[self.id_row]
                print(self.beta[0])

    def att_estoque(self):
        self.conecta()

        self.n1 = self.entry_nome_2.text()
        self.n = self.n1.upper()
        self.d = self.entry_dimensoes_4.text()
        self.c = self.entry_codigo_2.text()
        self.vv = self.entry_venda_2.text()
        self.p = self.entry_peso_2.text()
        self.vc = self.entry_custo_2.text()
        self.q = self.entry_quantidade_3.text()
        self.di = self.entry_dimensoes_3.text()
        self.update_store()
        self.close_connection()
        self.ver_estoque()
        a.alert("Dados atualizados com sucesso", "Atualizado")

    def excluir_estoque(self):

        self.conecta()
        self.delete_store()
        self.ver_estoque()
        self.close_connection() 

    def editar_estoque(self):

        self.conecta()
        self.edit_store()
        print(self.vv_estoque)
        self.entry_nome_2.setText(self.vv_estoque[0][1])
        self.entry_dimensoes_4.setText(self.vv_estoque[0][2])
        self.entry_codigo_2.setText(self.vv_estoque[0][0])
        self.entry_venda_2.setText(self.vv_estoque[0][5])
        self.entry_peso_2.setText(self.vv_estoque[0][7])
        self.entry_custo_2.setText(self.vv_estoque[0][4])
        self.entry_quantidade_3.setText(self.vv_estoque[0][3])
        self.entry_dimensoes_3.setText(self.vv_estoque[0][6])

    def select_carrinho(self):
        self.conecta()
        self.view_cart()
        self.close_connection()
 
    def verificarvenda(self):
        self.pg = self.cb_pagamento.currentText()
        print(self.pg) 
        if self.pg  == "Forma de pagamento":
            a.alert("Selecione uma forma de pagamento!", "Aviso")
        else:
            self.finalizarvenda()
            self.t = 0
    
    def finalizarvenda(self):

        self.hoje = datetime.datetime.today()
        self.data = format(self.hoje,"%d/%m/%Y")
        self.desconto = self.lineEdit.text()
        self.pg = self.cb_pagamento.currentText() 
        self.cal_desconto()
        self.lb_valortotal.setText(f"R$ {self.v_c_desconto}")
        self.lb_valorprodutos.setText(f"{self.f_valor_qtd}")
        self.lb_valorprodutos_2.setText(f"{self.desconto} %")
        self.mostrar_pg()
        
        window.tb_confirmarvenda.setRowCount(len(self.add_carrinho))
        window.tb_confirmarvenda.setColumnCount(6)

        for i in range (0, len(self.add_carrinho)):
            for j in range(0, 6):
                window.tb_confirmarvenda.setItem(i,j,QTableWidgetItem(str(self.add_carrinho[i][j])))

        self.saida()
        self.close_connection()

    def quantidade_produtos(self):
        self.conecta()
        self.qtd_prod()
        self.f_valor_qtd = re.sub("\[|\]|\(|\)|,","",str(self.valor_qtd))
        if self.f_valor_qtd != "None":
            self.label_39.setText(f"{self.f_valor_qtd}")
        else:
            self.label_39.setText("0")
        self.close_connection()

    def mostrar_pg(self):
        self.lb_fpagamento.setText(f"{self.pg}")

    def zerou(self):

        self.att_qtd()
        self.conecta()
        self.zero()
        a.alert("Venda realizada com sucesso!","Confirmação")
        self.deletar_carrinho()
        self.close_connection()
        
    def deletar_carrinho(self):
        self.conecta()
        self.delete_cart()
        window.tb_carrinho.setRowCount(len(self.add_carrinho))
        window.tb_carrinho.setColumnCount(6)
        for i in range (0, len(self.add_carrinho)):
            for j in range(0, 6):
                window.tb_carrinho.setItem(i,j,QTableWidgetItem(str(self.add_carrinho[i][j])))
        self.close_connection()

    def saida(self):
        self.conecta()
        self.exit()
        window.tb_saida.setRowCount(len(self.t_vendas))
        window.tb_saida.setColumnCount(5)

        for i in range (0, len(self.t_vendas)):
            for j in range(0, 5):
                window.tb_saida.setItem(i,j,QTableWidgetItem(str(self.t_vendas[i][j])))
        self.close_connection()

    def selecionar_saida(self, selected):

         for ix in selected.indexes():
            self.id_row = (ix.row())
            self.id_column = (ix.column())
            self.charlie = self.t_vendas[self.id_row]
            print(self.charlie[0])

    def cal_desconto(self):
        if self.desconto != 0:
            self.v_c_desconto = float(self.f_valor_total) - (float(self.desconto)*float(self.f_valor_total)/100)
        else:
            self.v_c_desconto = self.f_valor_total

    def detalharvenda(self):
        self.conecta()
        self.sold_details()
        self.lb_fpagamento_2.setText(f'{self.dv_vendas[0][4]}') 
        self.lb_valordescontovd.setText(f'{self.dv_vendas[0][5]}')
        self.lb_valorprodutos_vd.setText(f'{self.dv_vendas[0][1]}')
        self.lb_valortotal_vd.setText(f'{self.dv_vendas[0][2]}')

        window.tb_vendadetalhada.setRowCount(len(self.dt_vendas))
        window.tb_vendadetalhada.setColumnCount(6)

        for i in range (0, len(self.dt_vendas)):
            for j in range(0, 6):
                window.tb_vendadetalhada.setItem(i,j,QTableWidgetItem(str(self.dt_vendas[i][j])))

    def entradas(self):
        self.conecta()
        self.entrace()
        window.tb_entrada.setRowCount(len(self.delta))
        window.tb_entrada.setColumnCount(11)

        for i in range (0, len(self.delta)):
            for j in range(0, 11):
                window.tb_entrada.setItem(i,j,QTableWidgetItem(str(self.delta[i][j])))
        self.close_connection()

    def att_qtd(self):
        self.conecta() 
        self.update_qtd()
        self.close_connection()
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    