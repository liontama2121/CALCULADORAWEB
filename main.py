def calculadoraDePaginaWeb():
    hora = 40000
    dia =  200000
    print("escoja entre dia trabajadas (t) o horas (h)\n")
    op= str(input())
    if(op =="t"):
        print("dias trabajadas en el dia")
        d=int(input())
        res=d*dia
        return  res
    elif(op=="h"):
        print("horas trabajadas son de:")
        t=int(input())
        res=t*hora
        return res

def main():
    precio=0;
    print("esta calculadora te dara el precio estimado que debes cobrar por proyecto")
    print("es pagina web (w)o cosultoria(c)\n")
    opWC=str(input())
    if(opWC=="w"):
        print("primero calcularemos el tiempo en $COPS\n")
        precio=calculadoraDePaginaWeb()
        print("este proyecto tiene productos a subir\n")
        opP=str(input())
        if(opP=="si"):
            producto=3000
            print("¿cuantos son?\n")
            productoSubido=int(input())
            precio_producto=producto*productoSubido
            precio=precio+precio_producto
        print("¿Es necesario hacer diseño propio?\n")
        opD = str(input())
        if (opD == "no"):
            DiseñoL = 100000
            print("logotipo\n")
            precio = precio + DiseñoL
    elif(opWC=="c"):
        consultoria=60000
        print("cuantos horas son\n")
        hora=int(input())
        precio=precio+(precio*hora)
    precio_formateado = "{:,.2f}".format(precio)
    print("El precio que uste tiene que cobrar es de:",precio_formateado)









main()

