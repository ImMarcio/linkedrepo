

def invictus(material:float):
    minutes = 0
    halfLife = 0
    if material <= 0.8:
        return material
    else:
         halfLife = 1 +  invictus(material/2)
         return halfLife * 50
                
      

print('Execução--')
print(invictus(50))

gramas = 50
meiavida = 0
while(gramas > 0.8):
    gramas /= 2
    meiavida += 1

segundos = meiavida * 50

print(segundos)


