import sqlite3

class DataBase():
    def __init__(self, name = "bank.db") -> None:
        self.name = name
    
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def table_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS produtos(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NULL,
                        nome TEXT NOT NULL,
                        descricao TEXT NULL,
                        quantidade TEXT NOT NULL,
                        valor_compra TEXT NOT NULL,
                        valor_venda TEXT NOT NULL,
                        fornecedor TEXT NOT NULL,
                        tel_fornecedor TEXT NULL,
                        Dimensões TEXT NULL,
                        Peso TEXT NULL,
                        data TEXT NULL

                    );
            
            """)
        except AttributeError:
            print("faça a conexão")
    def table_carrinho(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS carrinho(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NOT NULL,
                        nome TEXT NOT NULL,
                        descricao TEXT NOT NULL,
                        valor_venda CHAR NOT NULL,
                        quantidade INT NULL,
                        FOREIGN KEY (codigo) references table_produtos (codigo),
                        FOREIGN KEY (nome) references table_produtos (nome),      
                        FOREIGN KEY (descricao) references table_produtos (descricao),      
                        FOREIGN KEY (valor_venda) references table_produtos (valor_venda)      

                    );
            
            """)
        except AttributeError:
            print("faça a conexão")

    def table_vendas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS vendas(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        quantidade INT NULL,
                        valor_total CHAR  NULL,
                        data TEXT NOT NULL,
                        forma_pagamento TEXT NULL, 
                        desconto TEXT NULL
        
                    );
            
            """)
        except AttributeError:
            print("faça a conexão")
        
    def table_produtos_vendas(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS produtos_vendas(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        cod_venda INTEGER NULL,
                        nome TEXT NULL,
                        descricao TEXT NULL,
                        quantidade CHAR NULL,
                        valor_venda CHAR NULL,
                        data TEXT NULL,
                        desconto CHAR NULL,
                        FOREIGN KEY (cod_venda) references table_vendas (id), 
                        FOREIGN KEY (nome) references table_produtos (nome),
                        FOREIGN KEY (descricao) references table_produtos (descricao),
                        FOREIGN KEY (quantidade) references table_vendas (quantidade),
                        FOREIGN KEY (valor_venda) references table_vendas (valor_venda),
                        FOREIGN KEY (data) references table_vendas (data),
                        FOREIGN KEY (desconto) references table_vendas (desconto)

                        
                    );
            
            """)

            
        except AttributeError:
            print("faça a conexão")

    def table_entrada(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS entradas(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NULL,
                        nome TEXT NOT NULL,
                        descricao TEXT NULL,
                        quantidade CHAR NOT NULL,
                        valor_compra CHAR NOT NULL,
                        valor_venda CHAR NOT NULL,
                        fornecedor TEXT NOT NULL,
                        tel_fornecedor CHAR NULL,
                        Dimensões CHAR NULL,
                        Peso CHAR NULL,
                        data TEXT NULL
                        
                    );
            
            """)
          
        except AttributeError:
            print("faça a conexão")


    def insert_prod(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO produtos(codigo, nome, descricao, quantidade, valor_compra, valor_venda, fornecedor, tel_fornecedor, Dimensões, Peso, data) VALUES(?,?,?,?,?,?,?,?,?,?,?)
            
            """,(self.c, self.n, self.d, self.q, self.vc, self.vv, self.nf, self.tf, self.di, self.p, self.data))
            self.connection.commit()

            cursor.execute("""

                INSERT INTO entradas(codigo, nome, descricao, quantidade, valor_compra, valor_venda, fornecedor, tel_fornecedor, Dimensões, Peso, data) VALUES(?,?,?,?,?,?,?,?,?,?,?)
            
            """,(self.c, self.n, self.d, self.q, self.vc, self.vv, self.nf, self.tf, self.di, self.p, self.data))
            self.connection.commit()
        except AttributeError:
            print("faça conexão")

    def view_estoque(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT codigo, nome, descricao, quantidade, valor_compra, valor_venda, fornecedor, tel_fornecedor, Dimensões, Peso, data FROM produtos

            """)
            self.v_estoque = cursor.fetchall()

        except AttributeError:
            print("Falha na conexão")
    
    def view_prod(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT nome, descricao, valor_compra, valor_venda, desconto, quantidade FROM produtos

            """)
            self.result = cursor.fetchall()
        except AttributeError:
            print("Falha na conexão")
    
    def sold_pp_prod(self, n, q):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM produtos WHERE nome = ?

            """,(n, q ))

            self.qtd1 = cursor.fetchall()
            print(self.qtd1[0][4])
            cursor.execute("""

                UPDATE produtos SET quantidade = ? WHERE nome = ?

            """,(str(int(self.qtd1[0][4])-int(q)), n))
            self.connection.commit()

        except AttributeError:
            print("Falha na conexão")
    
    def search_exit(self, n):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT id, quantidade, valor_total, data, forma_pagamento, desconto FROM vendas WHERE id = ?

            """,(n, ))
            self.result = cursor.fetchall()
        except AttributeError:
            print("Faça a conexão")
    
    def search_store(self, n):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT codigo, nome, descricao, quantidade, valor_compra, valor_venda, fornecedor, tel_fornecedor, Dimensões, Peso, data  FROM produtos WHERE nome = ? or codigo = ?

            """,(n, n ))

            self.result = cursor.fetchall()
            print(f"este é o result{self.result}")
            return self.result
        except AttributeError:
            print("Faça a conexão")
    
    def search_prod_sold(self, n):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT id, codigo, nome, descricao, quantidade, valor_venda FROM produtos_vendas WHERE codigo = ? and nome = ?

            """,(self.charlie[0], n ))

            self.pdv = cursor.fetchall()
        except AttributeError:
            print("Faça a conexão")

    def search_prod(self, n):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT id, codigo, nome, descricao, valor_venda, quantidade FROM produtos WHERE nome = ? or codigo = ?

            """,(n, n ))

            self.result = cursor.fetchall()
            return self.result
        except AttributeError:
            print("Faça a conexão")
    
    def else_qtd(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT quantidade FROM produtos WHERE id = ?
            
            """,(self.alfa[0],))
            self.comp = cursor.fetchall()
        except AttributeError:
            print("Faça a conexão")
    
    def keep_cart(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO carrinho(codigo, nome, descricao, valor_venda)
                SELECT codigo, nome, descricao, valor_venda FROM produtos 
                WHERE id = ?
            
            """, (self.alfa[0],))
            self.connection.commit()   

            cursor.execute("""
            
                SELECT  id, codigo, nome, descricao, valor_venda, quantidade FROM carrinho

            """)

            self.ad_carrinho = cursor.fetchall()   
            print(self.ad_carrinho)  

            cursor.execute("""
            
                UPDATE carrinho SET quantidade = ? WHERE codigo = ?
            
            """, (self.qtd, self.ad_carrinho[(len(self.ad_carrinho)-1)][1]))    
            self.connection.commit()
            self.ad_carrinho.clear()
            cursor.execute("""
            
                SELECT  id, codigo, nome, descricao, valor_venda, quantidade FROM carrinho

            """)

            self.add_carrinho = cursor.fetchall()
        except AttributeError:
            print("faça conexão")
    
    def delete_cart(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                DELETE FROM carrinho WHERE id = ?
            
            """, (self.teta[0], ))
            self.connection.commit()

            cursor.execute("""
            
                SELECT  id, codigo, nome, descricao, valor_venda, quantidade  FROM carrinho

            """)

            self.add_carrinho = cursor.fetchall()
            print(f"{self.teta[0]} depois de apagar")
            
        except AttributeError:
            print("faça conexão")
    
    def calc_price(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT SUM((valor_venda * quantidade)) FROM carrinho

            """)

            self.valor_total = cursor.fetchall()
            print(self.valor_total)           
        except AttributeError:
            print("falha na conexão")
    
    def update_store(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                UPDATE produtos SET codigo = ?, nome = ?, descricao = ?, quantidade = ?, valor_compra = ?, valor_venda = ?, Dimensões = ?, Peso = ? WHERE codigo = ?

            """,(self.c, self.n, self.d, self.q, self.vc, self.vv, self.di, self.p, self.beta[0]))
            self.connection.commit()
        
        except AttributeError:
            print("Falha a conexão")

    def delete_store(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                DELETE FROM produtos WHERE codigo = ?
            
            """, (self.beta[0], ))
            self.connection.commit()
        except AttributeError:
            print("faça conexão")
    
    def edit_store(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT codigo, nome, descricao, quantidade, valor_compra, valor_venda, Dimensões, Peso 
                FROM produtos WHERE codigo = ?
            
            """,(self.beta[0],))
            self.vv_estoque = cursor.fetchall()
        except AttributeError:
            print("faça conexão")
    
    def view_cart(self):
        try:
            cursor = self.connection.cursor()   
            cursor.execute("""
                
                SELECT * FROM carrinho

            """)        
            self.todo_carrinho = cursor.fetchall()
            print(self.todo_carrinho)

        except AttributeError:
            print("Falha na conexão")
    
    def qtd_prod(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT SUM(quantidade) FROM carrinho

            """)
            self.valor_qtd = cursor.fetchall()
        except AttributeError:
            print("falha na conexão")

    def zero(self):
        try:
            self.select_carrinho()

            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO vendas (quantidade, valor_total, data, forma_pagamento, desconto) VALUES (?,?,?,?,?)
            
            """, (int(self.valor_qtd[0][0]), float(self.v_c_desconto), self.data, self.pg ,self.desconto))

            self.connection.commit()

            cursor.execute("""
            
                SELECT id FROM vendas 
            
            """)
            self.id_v = cursor.fetchall()

            cursor.execute("""
            
                SELECT id FROM vendas WHERE id = ?
            
            """, (self.id_v[len(self.id_v)-1][0], ))

            self.id_uv = cursor.fetchall()
            for self.j in self.todo_carrinho:
                cursor.execute("""

                    INSERT INTO produtos_vendas (codigo, nome, descricao, valor_venda, quantidade) VALUES (?,?,?,?,?)
                
                """, (int(self.id_uv[0][0]), self.j[2], self.j[3], self.j[4], self.j[5]))

                self.connection.commit() 
        except AttributeError:
             print("falha na conexão")
    
    def delete_cart(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                DELETE FROM carrinho 
            
            """)
            self.connection.commit()
            cursor.execute("""
            
                SELECT  id, codigo, nome, descricao, valor_venda, quantidade  FROM carrinho

            """)

            self.add_carrinho = cursor.fetchall()
        except AttributeError:
            print("faça conexão")

    def exit(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            
                SELECT id, quantidade, valor_total, data, forma_pagamento FROM vendas
            
            """)
        self.t_vendas = cursor.fetchall()

    def sold_details(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT id, quantidade, valor_total, data, forma_pagamento, desconto FROM vendas WHERE id = ?
            
            """,(self.charlie[0],))

            self.dv_vendas = cursor.fetchall()
            cursor.execute("""

                SELECT * FROM produtos_vendas WHERE codigo = ?
            
            """,(self.charlie[0], ))

            self.dt_vendas = cursor.fetchall()
        except AttributeError:
            print("Falha na conexão")
    
    def entrace(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT codigo, nome, descricao, quantidade, valor_compra, valor_venda, fornecedor, tel_fornecedor, Dimensões, Peso, data FROM entradas
            
            """)

            self.delta = cursor.fetchall()
        except:
            print("Falha na conexão")
    
    def update_qtd(self):
        for i in self.add_carrinho:
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                
                    SELECT quantidade FROM produtos WHERE codigo = ?
                
                """,(i[1],))

                self.qtd_prod = cursor.fetchall()

                self.att_q = (int(self.qtd_prod[0][0])) - i[5]

                cursor.execute("""
                
                        UPDATE produtos SET quantidade = ? WHERE codigo = ?
                
                """,(self.att_q, i[1]))
                self.connection.commit()

            except:
                print("Falha na conexão")
    
if __name__=="__main__":
    db = DataBase()
    db.conecta()
    db.table_produtos()
    db.table_carrinho()
    db.table_vendas()
    db.table_produtos_vendas()
    db.table_entrada()
    db.close_connection()