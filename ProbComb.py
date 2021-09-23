from itertools import product, permutations, combinations

n_caixas = 0
i = 0
itens = 0
total_a = 0
total_l = 0
total_c = 0
caixa = 0
quant = []
pedido_aux=[]
with open('entrada.txt') as f:
    array = []
    caixas = []
    pedido = []
    for line in f:
        if line == '\n':
            pedido_aux = array.copy()
            pedido.append(pedido_aux)
            array.clear()
        else:
            array.append([int (x) for x in line.split()])
    pedido.append(array)

for teste1 in range(len(pedido)):
    for tt in range(len(pedido[teste1])):
        total_a = pedido[teste1][tt][0] + total_a
        total_l = pedido[teste1][tt][1] + total_l
        total_c = pedido[teste1][tt][2] + total_c
        itens = itens +1
    quant.append(itens)
    itens = 0
    if total_a <= 30 and total_l <= 40 and total_c <= 80:
        print('Caixa 1 é melhor opção')
    elif total_a <= 80 and total_l <= 50 and total_c <= 40:
        print('Caixa 2 é melhor opção')
    elif total_a <= 50 and total_l <= 80 and total_c <= 60:
        print('Caixa 3 é melhor opção')
    else:
        n_caixas = 1
        print('Impossivel enviar todos os itens em uma caixa apenas. Itens sendo divididos em mais de uma caixa...')
    total_a = 0
    total_l = 0
    total_c = 0
flag=0
num5=1

if n_caixas == 1:
    for teste2 in range(len(pedido)):
        while i < len(pedido[teste2]):
            permsList = list(combinations(pedido[teste2], quant[teste2]-num5))
            for num in range(len(permsList)-1):
                for num2 in range(quant[teste2]-num5):
                    total_a = permsList[num][num2][0] + total_a
                    total_l = permsList[num][num2][1] + total_l
                    total_c = permsList[num][num2][2] + total_c
                if total_a <= 30 and total_l <= 40 and total_c <= 80:
                    for k in range(quant[teste2]-num5):
                        print(f'Caixa 1 tem o item {pedido[teste2][pedido[teste2].index(permsList[num][k])]}')
                        pedido[teste2].remove(pedido[teste2][pedido[teste2].index(permsList[num][k])])
                    flag = 1
                elif total_a <= 80 and total_l <= 50 and total_c <= 40:
                    for l in range(quant[teste2] - num5):
                        print(f'Caixa 2 tem o item {pedido[teste2][pedido[teste2].index(permsList[num][l])]}')
                        pedido[teste2].remove(pedido[teste2][pedido[teste2].index(permsList[num][l])])
                    flag = 1
                elif total_a <= 50 and total_l <= 80 and total_c <= 60:
                    for p in range(quant[teste2] - num5):
                        print(f'Caixa 3 tem o item {pedido[teste2][pedido[teste2].index(permsList[num][p])]}')
                        pedido[teste2].remove(pedido[teste2][pedido[teste2].index(permsList[num][p])])
                    flag = 1
                else:
                    print('Combinação excede, testando nova combinação...')
                total_a = 0
                total_l = 0
                total_c = 0
                if flag == 1:
                    break
            if flag == 1:
                flag = 0
            else:
                print('Reduzindo quantidade de itens por caixa...')
                num5 = num5+1
            if len(pedido[teste2]) == 1:
                if total_a <= 30 and total_l <= 40 and total_c <= 80:
                    print(f'Caixa 1 tem o item {pedido[teste2][0]}')
                elif total_a <= 80 and total_l <= 50 and total_c <= 40:
                    print(f'Caixa 2 tem o item {pedido[teste2][0]}')
                elif total_a <= 50 and total_l <= 80 and total_c <= 60:
                    print(f'Caixa 3 tem o item {pedido[teste2][0]}')
                else:
                    print('Nao possuimos caixas para a dimensão deste pedido')
                pedido[teste2].remove(pedido[teste2][0])
        num5 = 1