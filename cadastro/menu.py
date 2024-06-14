from test import*
from cone import*
from conbd import*
from datetime import datetime
conbd = conexao()
while True:
    op = menu()
    if op == 1:
        op = menu2()
        if op == 1:
            nome = input("digite o nome do produto:")
            descricao = input("digite a descrição do produto:")
            preco = float(input("digite o valor do produto:"))
            tipo = input("digite o categoria do seu produto:")
            catego = input("digite a descrição da categoria dele:")
            quantidade = int(input("digite a quantidade deste produto:"))
            data = input("digite a data seguindo o seguinte parametro DD-MM-AAAA:")
            data = datetime.strptime(data,"%d-%m-%Y").strftime("%Y-%m,%d")
            cadastrarproduto(conbd,nome,descricao,preco,tipo,catego,quantidade,data)
        elif op ==2:
            inputclientes(conbd,)
        elif op ==3:
            nome = input("digite o nome do funcionario:")
            cargo = input("digite o cargo:")
            departamento = input("digite o departamento:")
            cadastrarfuncionario(conbd,nome,cargo,departamento)
        elif op ==4:
            nome = input("digite o nome do fornecedor:")
            contato = input("digite seu email para contato:")
            endereco = input("digite seu endereço :")
            cadastrarfornecedores(conbd,nome,contato,endereco)
        
        elif op == 5:
            nome = input("digite o nome da promoção :")
            descricao = input("digite a descrição da promoção:")
            datainicio = input("digite a data inicial seguinto os paramentros DD-MM-AAAA:")
            datainicio = datetime.strptime(datainicio ,("%d-%m-%Y")).strftime("%Y-%m-%d")
            datafim = input("digite a data final seguinto os paramentros DD-MM-AAAA:")
            datafim = datetime.strptime(datafim ,("%d-%m-%Y")).strftime("%Y-%m-%d")
            cadastrarpromocoes(conbd,nome,descricao,datainicio,datafim)
    elif op == 2:
        alterar_espec(conbd)
    elif op == 3:
        deletar(conbd,)
    elif op == 4:
        buscar(conbd,)
    elif op ==5:
        criarpedido(conbd,)
    elif op == 6:
        alterar(conbd,)
    
    elif op == 0 :
        print("programa encerado")
        break