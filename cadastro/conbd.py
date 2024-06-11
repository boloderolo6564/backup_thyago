from datetime import datetime,date
def menu():
    print("0-encerrar programa")
    print("1-cadastrar")
    print("2-alterar")
    print("3-deletar")
    print("4-buscar")
    print("5-pedido")
    op = int(input("digite o que deseja:"))
    return op
def menu2():
    print("1-produto")
    print("2-cliente")
    print("3-funcionario")
    print("4-fornecedores")
    print("5-promoções")
    op = int(input("digite o que deseja:"))
    return op
def cadastrarproduto(conbd,nome,descricao,preco,tipo,catego,quantidade,data):
    mycursor = conbd.cursor()
    sql = "insert into produtos(Nome,Descricao,Preco) values (%s,%s,%s)"
    val = (nome,descricao,preco,)
    mycursor.execute(sql,val)
    id_produto = mycursor.lastrowid
    sql2 = "insert into estoque(ID_produto,Quantidade) values (%s,%s)"
    val2=(id_produto,quantidade,)
    mycursor.execute(sql2,val2,)
    sql3 = "insert into categoriasprodutos(Nome,Descricao) values (%s,%s)"
    val3 = (tipo ,catego)
    mycursor.execute(sql3,val3)
    sql4 = "insert into precos(Id_produto,Data_Preco,preco) values (%s,%s,%s)"
    val4 = (id_produto,data,preco)
    mycursor.execute(sql4,val4)

    conbd.commit()
    mycursor.close()
    print("produto cadastrado com sucesso")
def cadastrarcliente(conbd,nome,sobrenome,endereco,cidade,codigopostal):
    mycursor = conbd.cursor()
    sql = "insert into clientes(nome,sobrenome,endereco,cidade,codigopostal) values (%s,%s,%s,%s,%s)"
    val = (nome,sobrenome,endereco,cidade,codigopostal,)
    mycursor.execute(sql,val,)
    conbd.commit()
    mycursor.close()
    print("cliente cadastrado com sucesso")
def cadastrarfuncionario(conbd,nome,cargo,departamento):
    mycursor = conbd.cursor()
    sql = "insert into funcionarios(nome,cargo,departamento) values (%s,%s,%s)"
    val = (nome,cargo,departamento)
    mycursor.execute(sql,val)
    conbd.commit()
    print("funcionario cadastrado com sucesso")
    mycursor.close()
def cadastrarfornecedores(conbd,nome,contato,endereco):
    mycursor = conbd.cursor()
    sql = "insert into fornecedores(nome,contato,endereco) values (%s,%s,%s)"
    val = (nome,contato,endereco)
    mycursor.execute(sql,val)
    conbd.commit()
    print("fornecedor cadastrado com sucesso")
    mycursor.close()
def cadastrarpromocoes(conbd,nome,descricao,datainicio,datafim):
    mycursor = conbd.cursor()
    sql = "insert into promocoes(nome,descricao,datainicio,datafim) values (%s,%s,%s,%s)"
    val = (nome,descricao,datainicio,datafim)
    mycursor.execute(sql,val)
    conbd.commit()
    print("promoção cadastrada com sucesso")
    mycursor.close()
def alterar(conbd,):
    mycursor = conbd.cursor()
    rota = buscaralt(conbd,)
    distino = rota[0]
    op = rota[1]
    if op == 1:
        nome = rota[2]
        descricao = rota[3]
        preco = rota[4]
        idd = rota[5]
        sql = distino 
        val = (nome,descricao,preco,idd,)
        mycursor.execute(sql,val)

    elif op == 2:
        nome = rota[2]
        sobrenome = rota[3]
        endereco = rota[4]
        cidade = rota[5]
        codigo = rota[6]
        idd = rota[7]
        sql =  distino
        val = (nome,sobrenome,endereco,cidade,codigo,idd,)
        mycursor.execute(sql,val)
    elif op == 3:
        nome = rota[2]
        cargo = rota[3]
        departamento = rota[4]
        idd = rota[5]
        sql = distino 
        val =(nome,cargo,departamento,idd,)
        mycursor.execute(sql,val)
    elif op == 4:
        nome = rota[2]
        contato = rota[3]
        endereco = rota[4]
        idd = rota[5]
        sql = distino 
        val = (nome,contato,endereco,idd,)
        mycursor.execute(sql,val)
    elif op == 5:
        nome = rota[2]
        descricao = rota[3]
        datainicio = rota[4]
        datafim = rota[5]
        idd = rota[6]

        sql = distino 
        val = (nome,descricao,datainicio,datafim,idd,)
    else:
        print("algo de errado não está certo")
    conbd.commit()
    mycursor.close()
def deletar(conbd,):
    mycursor = conbd.cursor()
    rota = buscardel(conbd,)
    idd = int(input("digite o idd do item que deseja remover do sistema:"))
    sql = rota
    val = (idd,)
    mycursor.execute(sql,val)
    conbd.commit()
    print("item removido com sucesso")
    mycursor.close()

def encontrarcliente(conbd,):
    while True:
        active = "off"
        mycursor = conbd.cursor()
        cliente = input("digite o seu nome :")
        sql = "select*from clientes where Nome = %s"
        val = (cliente,)
        mycursor.execute(sql,val)
        resultados = mycursor
        for linha in resultados:
            if cliente in linha[1]:
                id_cliente = linha[0]
                active = "on"
                
            
        if active == "off":
            inputclientes(conbd)
        if active == "on":
            break            
    return id_cliente
def comprarproduto(conbd,):
    res = 0
    mycursor = conbd.cursor()
    produto = input("digite o produto que deseja:")
    sql = "select*from produtos"
    mycursor.execute(sql,)
    resultados = mycursor
    for linha in resultados:
        if produto in linha[1]:
            print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preco:",linha[3])
    id_produto = int(input("digite o id do produto que deseja para confirmar:"))
    sql2 ="select*from produtos where id_produto = %s"
    val2 = (id_produto,)
    mycursor.execute(sql2,val2,)
    resultados = mycursor
    for linha in resultados:
            preco = linha[3]               
    quantidade = int(input("quantas unidades deste produto você deseja:"))
    pg= input("digite qual metodo de pagamento ira utilizar:")
    valor = preco * quantidade    
    res += valor
    print("compra realizada no valor :",res)
    avaliacao = int(input("de 1 a 5 quanto satisfeito está com o produto :"))
    coment = input("digite seu comentarios sobre o produto:")

    return id_produto,res,quantidade,pg,avaliacao,coment
def criarpedido(conbd,):
    data = date.today()
    mycursor = conbd.cursor()
    id_cliente =encontrarcliente(conbd,)
    dentro = comprarproduto(conbd,)
    id_produto = dentro[0]
    valor = dentro[1]
    quantidade = dentro[2]
    pg = dentro[3]
    avaliacao = dentro[4]
    coment = dentro[5]
    sql = "insert into pedidos(data_pedido,id_cliente,total) values (%s,%s,%s)"
    val = (data,id_cliente,valor,)
    mycursor.execute(sql,val)
    id_pedido = mycursor.lastrowid
    sql1 = "insert into detalhespedido(ID_Pedido,ID_Produto,Quantidade) values (%s,%s,%s)"
    val1 = (id_pedido,id_produto,quantidade)
    mycursor.execute(sql1,val1)
    sql2 = "insert into vendas(data,id_cliente,metodopagamento,total) values (%s,%s,%s,%s)"
    val2 = (data,id_cliente,pg,valor)
    mycursor.execute(sql2,val2)
    id_venda = mycursor.lastrowid
    sql3 = "insert into pagamentos(id_venda,data,valor) values (%s,%s,%s)"
    val3 = (id_venda,data,valor)
    mycursor.execute(sql3,val3,)
    sql4 = "insert into comentariosavaliacoes(id_produto,id_cliente,comentario,avaliacao,data) values (%s,%s,%s,%s,%s)"
    val4 = (id_produto,id_cliente,coment,avaliacao,data)
    mycursor.execute(sql4,val4)
    print("produto comprado com sucesso")
    conbd.commit()
    mycursor.close()
def inputclientes(conbd,):
    nome = input("digite o nome do cliente:")
    sobrenome = input("digite o sobrenome do cliente:")
    endereco = input("digite o endereço do cliente:")
    cidade = input("digite a cidade do cliente:")
    codigopostal = int(input("digite o codigo postal do cliente:"))
    cadastrarcliente(conbd,nome,sobrenome,endereco,cidade,codigopostal)
def buscar(conbd,):
    op = menu2()
    if op == 1:
        conteu = "select*from produtos"
    elif op == 2:
        conteu ="select*from clientes"
    elif op == 3:
        conteu = "select*from funcionarios"
    elif op == 4:
        conteu = "select*from fornecedores"
    elif op == 5:
        conteu = "select*from promocoes"
    nome = input("digite o que deseja encontrar:")
    mycursor = conbd.cursor()
    sql = conteu
    mycursor.execute(sql,)
    resultados = mycursor
    for linha in resultados:
        if conteu == "select*from produtos":
            rota = "produtos"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preco:",linha[3])
        elif conteu =="select*from clientes":
            rota = "delete from clientes where id_cliente = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|sobrenome:",linha[2],"|cidade:",linha[3],"|endereco:",linha[4],"|codigo_postal:",linha[5])
        elif conteu == "select*from fornecedores":
            rota = "delete from fornecedores where id_fornecedor = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|contato:",linha[2],"|endereço:",linha[3])
        elif conteu == "select*from funcionarios":
            rota = "delete from funcionarios where id_ = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|cargo:",linha[2],"|departamento:",linha[3])
        elif conteu == "select*from promocoes":
            rota = "delete from promocoes where id_promocao = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|data inicial:",linha[3],"|data final:",linha[4])
    conbd.commit()
    mycursor.close()
    
def buscaralt(conbd,):
    lista = []
    op = menu2()
    if op == 1:
        conteu = "select*from produtos"
    elif op == 2:
        conteu ="select*from clientes"
    elif op == 3:
        conteu = "select*from funcionarios"
    elif op == 4:
        conteu = "select*from fornecedores"
    elif op == 5:
        conteu = "select*from promocoes"
    nome = input("digite o que deseja encontrar:")
    mycursor = conbd.cursor()
    sql = conteu
    mycursor.execute(sql,)
    resultados = mycursor
    for linha in resultados:
        if conteu == "select*from produtos":
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preco:",linha[3])
                active = 1
                
        elif conteu =="select*from clientes":
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|sobrenome:",linha[2],"|cidade:",linha[3],"|endereco:",linha[4],"|codigo_postal:",linha[5])
                active = 2
        elif conteu == "select*from fornecedores":
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|contato:",linha[2],"|endereço:",linha[3])
                active = 3
        elif conteu == "select*from funcionarios":
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|cargo:",linha[2],"|departamento:",linha[3])
                active = 4
        elif conteu == "select*from promocoes":
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|data inicial:",linha[3],"|data final:",linha[4])
                active = 5
    idd = int(input("digite o idd do item que deseja para confirmar a seleção:")) 
    if active == 1:
        rota = "UPDATE produtos SET Nome = %s ,Descricao = %s ,Preco = %s WHERE ID_Produto = %s" 
        nome = input("digite o novo nome:")
        descricao = input("digite a nova descrição:")
        preco = int(input("digite o novo preço:"))
        return rota,op,nome,descricao,preco,idd
    elif active == 2:
        nome = input("digite o novo nome :")
        sobrenome = input("digite o novo sobrenome :")
        endereco = input("digite o novo endereco:")
        cidade = input("digie a nova cidade:")
        codigopostal = input("digite o novo codigo postal:")
        rota = "UPDATE clientes SET Nome= %s,Sobrenome = %s ,Endereco= %s ,Cidade= %s ,CodigoPostal= %s WHERE ID_Cliente = %s"

        return rota,op,nome,sobrenome,endereco,cidade,codigopostal,idd
    elif active == 3:
        rota = "UPDATE `fornecedores` SET nome = %s,`contato`=%s,`Endereco`=%s WHERE Id_fornecedor = %s"
        nome = input("digite novo nome :")
        contato = input("digite o novo contato")
        endereco = input("digite o novo endereço")
        return rota,op,nome,contato,endereco,idd
    elif active == 4:
        rota = "UPDATE `funcionarios` SET `nome`=%s,`cargo`=%s,`departamento`=%s WHERE Id_funcionario = %s"
        nome = input("digite o novo nome:")
        cargo = input("digite o novo cargo:")
        departamento = input("digite o novo departamento")
        return rota,op,nome,cargo,departamento,idd
    elif active == 5:
        rota = "UPDATE `promocoes` SET `nome`=%s,`descricao`=%s,`datainicio`=%s,`datafim`=%s WHERE Id_fornecedor = %s"
        nome = input("digite o novo nome:")
        descricao  = input("digite a nova descrição:")
        datainicio = input("digite a nova data no formato DD-MM-AAAA:")
        datainicio = datetime.strptime(datainicio,"%d-%m-%Y").strftime("Y-%m-%d")
        datafim = input("digite a nova data no formato DD-MM-AAAA:")
        datafim = datetime.strptime(datafim,"%d-%m-%Y").strftime("Y-%m-%d")
        return rota,op,nome,descricao,datainicio,datafim,idd
    conbd.commit()
    mycursor.close()
def buscardel(conbd,):

    op = menu2()
    if op == 1:
        conteu = "select*from produtos"
    elif op == 2:
        conteu ="select*from clientes"
    elif op == 3:
        conteu = "select*from funcionarios"
    elif op == 4:
        conteu = "select*from fornecedores"
    elif op == 5:
        conteu = "select*from promocoes"
    nome = input("digite o que deseja encontra:")
    mycursor = conbd.cursor()
    sql = conteu
    mycursor.execute(sql,)
    resultados = mycursor
    for linha in resultados:
        if conteu == "select*from produtos":
            rota = "produtos"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preco:",linha[3])
        elif conteu =="select*from clientes":
            rota = "delete from clientes where id_cliente = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|sobrenome:",linha[2],"|cidade:",linha[3],"|endereco:",linha[4],"|codigo_postal:",linha[5])
        elif conteu == "select*from fornecedores":
            rota = "delete from fornecedores where id_fornecedor = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|contato:",linha[2],"|endereço:",linha[3])
        elif conteu == "select*from funcionarios":
            rota = "delete from funcionarios where id_ = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|cargo:",linha[2],"|departamento:",linha[3])
        elif conteu == "select*from promocoes":
            rota = "delete from promocoes where id_promocao = %s"
            if nome in linha[1]:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|data inicial:",linha[3],"|data final:",linha[4])
    conbd.commit()
    mycursor.close()
    return rota