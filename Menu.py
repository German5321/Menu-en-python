salir=False
while not salir:
    print("1) Crear lista")
    print("2) Añadir elemento")
    print("3) Eliminar elemento")
    print("4) Modificar elemento")
    print("5) Mostrar datos")
    print("6) Mostar datos de forma inversa")
    print("7) Limpiar lista")
    print("8) Borrar lista")
    print("9) Salir")
    opc=input("\n Numero de la acción: ")
    
        
    if(opc=='1'):
        print("\n\n\n\n1)crear lista")
        if 'lista' in locals():
            print("ya existe la lista")
        else:
            lista=[]
            print("\nLista lista\n")

    elif(opc=='2'):
        print("\n\n\n\n2)añadir elemento")
        if 'lista' in locals():
            ll=input("Ingrese elemento: ")
            lista.append(ll)
            print("\ningresado\n\n\n")
        else:
            print("\n\nLista inexistente\n\n")
            

    elif(opc=='3'):
        print("\n\n\n\n3)Eliminar elemento")
        if 'lista' in locals():
            lista[0]=''
            print("\nelemento vacio\n")
        else:
            print("\n\nNo existe ninguna lista\n\n")

    elif(opc=='4'):
        print("\n\n\n\n4)Modificar elemento")
        if 'lista' in locals():
            lista[0]=input('Cambiar elemento por: ')
            print("\nelemento modificado\n")
        else:
            print("\n\nNo existe ninguna lista\n\n\n")

    elif(opc=='5'):
        print("\n\n\n\n5)Mostrar datos")
        if 'lista' in locals():
            print("\n",lista,"\n\n\n")
        else:
            print("\n\nNo hay nada que mostrar\n\n\n")

    elif(opc=='6'):
        print("\n\n\n\n6)mostar datos de forma inversa")
        if 'lista' in locals():
            for x in reversed(lista):
                print("\n",x,"\n\n\n")
        else:
            print("\n\nNo hay nada que mostrar\n\n\n")

    elif(opc=='7'):
        print("\n\n\n\n7)limpiar lista")
        if 'lista' in locals():
            del(lista)
            lista=[]
            print("\nlista vacia\n")
        else:
            print("\n\nNo hay nada que vaciar, sera redirigido\n\n\n")

    elif(opc=='8'):
        print("\n\n\n\n8)borrar lista")
        if 'lista' in locals():
            del(lista)
            print("lista borrada")
        else:
            print("\n\nNo hay nada que borrar, sera redirigido\n\n\n")

    elif(opc=='9'):
        print("Adio miamol <3")
        salir=True
    else:
        print("\n\nopcion o valor incorrecto, sera redirigido al menu\n\n\n")
