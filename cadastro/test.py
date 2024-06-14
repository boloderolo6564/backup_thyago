from conbd import*
from datetime import datetime,date
def alterar4(conbd,):
    mycursor = conbd.cursor()

    buscar = buscar3(conbd,)
    op = buscar[0]
    idd = buscar[1]
    if op == 1:
        print("1-para alterar nome:")
        print("2-para alterar descrição:")
        print("3-para alterar preço:")
        print("4-para alterar todos os itens:")
        onde = int(input("digite o que deseja:"))
        if onde ==1:
            att = input("digite o novo nome que deseja:")
            rota = "update produtos set nome = %s where id_produto = %s "
        elif onde ==2:
            att = input("digite a nova descrição do produto:")
            rota = "update produtos set descricao = %s where id_produto = %s"
        elif onde == 3:
            att = int(input("digite o novo preço do produto:"))     
            rota = "update produtos set preco = %s where id_produto = %s"
        elif onde == 4:
            alterar(conbd,op,idd)
            res = 1
    elif op == 2:
        print("1-para alterar nome:")
        print("2-para alterar sobrenome:")
        print("3-para alterar endereço:")
        print("4-para alterar cidade:")
        print("5-para alterar codigo postal:")
        print("6-para alterar todos os itens:")
        onde = int(input("digite o que deseja:"))
        if onde ==1:
            att = input("digite o novo nome que deseja:")
            rota = "update clientes set nome = %s where id_cliente = %s"
        elif onde ==2:
            att = input("digite o novo sobrenome que deseja:")
            rota = "update clientes set sobrenome = %s where id_cliente = %s"
        elif onde == 3:
            att = input("digite o novo endereço:")
            rota = "update clientes set endereco = %s where id_cliente = %s"
        elif onde == 4:
            att = input("digite a nova cidade :")
            rota = "update clientes set cidade = %s where id_cliente = %s"
        elif onde == 5:
            att = input("digite o novo codigo postal:")
            rota = "update clientes set codigopostal = %s where id_cliente = %s"
        elif onde ==6:
            alterar(conbd,op,idd)
            res = 1
    elif op == 3:
        print("1-para alterar nome:")
        print("2-para alterar cargo:")
        print("3-para alterar departamento:")
        print("4-para alterar todos os itens:")
        onde = int(input("digite o que deseja :"))
        if onde == 1:
            att = input("digite o novo nome:")
            rota = "update funcionarios set nome = %s where id_funcionario = %s"
        elif onde ==2:
            att = input("digite o novo cargo:")
            rota = "update funcionarios set cargo = %s where id_funcionario = %s"
        elif onde == 3:
            att = input("digite o novo departamento:")
            rota = "update funcionarios set departamento = %s where id_funcionario = %s"
        elif onde == 4:
            alterar(conbd,op,idd)
            res = 1
    elif op ==4:
        print("1-para alterar nome:")
        print("2-para alterar contato:")
        print("3-para alterar endereço:")
        print("4-para alterar todos os itens:")
        onde = int(input("digite o que deseja:"))
        if onde == 1:
            att = input("digite o novo nome:")
            rota = "update fornecedores set nome = %s where id_fornecedor = %s "
        elif onde == 2:
            att = input("digite o novo contato:")
            rota = "update fornecedores set contato = %s where id_fornecedor = %s"
        elif onde == 3:
            att = input("digite o novo endereço:")
            rota = "update fornecedores set endereco = %s where id_fornecedor = %s"
        elif onde ==4:
            alterar(conbd,op,idd)
            res = 1
    elif op ==5:
        print("1-para alterar nome:")
        print("2-para alterar descrição:")
        print("3-para alterar data inical:")
        print("4-para alterar data final:")
        print("5-para alterar todos os itens:")
        onde = int(input("digite o que deseja :"))
        if onde == 1:
            att = input("digite o novo nome :")
            rota = "update promocoes set nome = %s where id_promocao = %s"
        elif onde == 2:
            att = input("digite a nova descrição:")
            rota = "update promocoes set descricao = %s where id_promocao = %s"
        elif onde == 3:
            att = input("digite a nova data siga o paramentro DD-MM-AAAA:")
            att = datetime.strptime(att,"%d-%m-%y").strftime("%Y-%m-%d")
            rota = "update promocoes set datainicio = %s where id_promocao = %s"
        elif onde == 4:
            att = input("digite a nova data siga o paramentro DD-MM-AAAA:")
            att = datetime.strptime(att,"%d-%m-%y").strftime("%Y-%m-%d")
            rota = "update promocoes set datafim = %s where id_promocao = %s"
        elif onde ==5:
            alterar(conbd,op,idd)
            res = 1
    if res != 1:
        sql = rota
        val = (att,idd,)
        print(sql,val)
        mycursor.execute(sql,val)
    
    conbd.commit()
    mycursor.close()
    print("alteração feita com sucesso")
def buscar3(conbd,):
    mycursor = conbd.cursor()
    op = menu2()
    nome = input("digite o que deseja encontrar:")
    if op == 1:
        conteu = "select*from produtos"
    elif op == 2:
        conteu = "select*from clientes"
    elif op == 3:
        conteu = "select*from funcionarios"
    elif op == 4:
        conteu = "select*from fornecedores"
    elif op == 5:
        conteu = "select*from promocoes"
    
    sql = conteu
    mycursor.execute(sql)
    resultados = mycursor
    for linha in resultados:
        if nome in linha[1]:
            if op ==1:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|preco:",linha[3])
                
                
            elif op ==2:
                print("|id:",linha[0],"|nome:",linha[1],"|sobrenome:",linha[2],"|cidade:",linha[3],"|endereco:",linha[4],"|codigo_postal:",linha[5])
                
                
            elif op ==3:
                print("|id:",linha[0],"|nome:",linha[1],"|cargo:",linha[2],"|departamento:",linha[3])
                
                
            elif op ==4:
                print("|id:",linha[0],"|nome:",linha[1],"|contato:",linha[2],"|endereço:",linha[3])
                
                
            elif op ==5:
                print("|id:",linha[0],"|nome:",linha[1],"|descrição:",linha[2],"|data inicial:",linha[3],"|data final:",linha[4])
    idd = int(input("digite o idd do item para confirmar:"))
    return op,idd
    conbd.commit()
    mycursor.close()
