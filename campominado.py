from random import randint

def criaCampo():
    field=[]
    for i in range(5):
        line = [0,0,0,0,0]
        field.append(line)
    return field
        
def colocaMinas(field):
    qtdMinas = randint(5,12)
    for i in range(qtdMinas):
        linha = randint(0,4)
        coluna = randint(0,4)
        if (field[linha][coluna] == 1):
            qtdMinas+=1
        else:
            field[linha][coluna] = 1
    return field
        
        
if __name__ == "__main__":
    
    campo = criaCampo()
    campo = colocaMinas(campo)

    for i in range(25):
        a = input('digite a linha e coluna').split(',')
        a[0]=int(a[0])+1
        a[1]=int(a[1])+1
        if (campo[a[0]-1][a[1]-1] == 1):
           raise SystemExit("Você acertou uma mina!")
            
