def printStr(string):
    if (string == ''):
        return 

    print(string[0],end='')
    printStr(string[1:])



def printStrInvertida(string):
    if (string == ''):
        return 
    printStrInvertida(string[1:])
    print(string[0],end='')

def tamanhoStr(string):
    if string == '':
        return 0
    
    else:
        tamanho = 1 + tamanhoStr(string[1:])
        return tamanho



str = 'Curso superior de tecnologia em sistema para internet '
printStr(str)
print()
printStrInvertida(str)
print()
print('Tamanho',tamanhoStr(str))




def listaInvertida(self,list):
    cursor = self.__start
    printAuxiliar(self,cursor)

def printAuxiliar(self,node):
    if(node == None):
        return
    printAuxiliar(node.prox)
    print(node.carga)
    
