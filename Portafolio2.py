#PORTAFOLIO DE EVIDENCIA #2

"""
Nombre: invertirLista
Entrada: una lista
Parametros: lista
Salida: la lista que ingreso invertida
Restricciones: debe ser una lista y debe contener digitos
"""
def invertirLista(lista):
    if(isinstance(lista,list)):
        if(lista==[]):
            return 0
        else:
            return invetirLista_Aux(lista,[])
    else:
        print("Error: el dato ingresado debe ser una lista")

def invetirLista_Aux(lista,resultado):
    if(lista==[]):
        return resultado
    else:
        return invetirLista_Aux(lista[:-1],resultado+[lista[-1]])
#--------------------------------------------------------------------------------------

"""
Nombre: extremosLista
Entrada: una lista
Parametros: lista
Salida: el numero menor y mayor de la lista
Restrincciones: debe ser una lista 
"""
def extremosLista(lista):
    if(isinstance(lista,list)):
        if(lista==[]):
            print("Error: La lista no puede ser vacía. debe contener al menos dos digitos")
        else:
            
            menor=menor_aux(lista,lista[0])
            mayor=mayor_aux(lista,lista[0])
            return  extremosLista_aux(menor,mayor,[])
    else:
        print("Error: Debe ingresar una lista.")

#Mayor y menor de la lista que se ingresa
def menor_aux(lista,result):
    if(lista==[]):
        return result
    elif(int(lista[0]))<result:
        return menor_aux(lista[1:],lista[0])
    else:
        return menor_aux(lista[1:],result)

def mayor_aux(lista,result):
    if(lista==[]):
        return result
    elif(int(lista[0]))>result:
        return mayor_aux(lista[1:],lista[0])
    else:
        return mayor_aux(lista[1:],result)
#Divididos los dos extremos y los muestra
def extremosLista_aux(menor,mayor,result):
    if(menor==0)or mayor==0:
        return result
    elif(menor==mayor):
        return [mayor]
    else:
        return extremosLista_aux(0,0,result+[menor]+[mayor])


#---------------------------------------------------------------------------
"""
Nombre:eliminarDigito
Entrada: numero entero y numero que desea borrar
Parametros: num,eliminar
Salida: el numero ingresado, sin el que deseo eliminar
Restrincciones: Tienen que ser enteros positivos mayor a cero
"""
def eliminarDigito(num,eliminar):
    if(isinstance(num,int)and isinstance(eliminar,int)):
       if(eliminar>=0 and num>=0):
           if(num==0):
               return 0
           else:
               return eliminarDigito_aux(str(num),str(eliminar),"")
       else:
            print("Error: los numeros deben ser mayor a cero")
    else:
        print("Error: Los digitos ingresados deben ser enteros")

def eliminarDigito_aux(num,eliminar,result):
    if(num==""):
        return int(result)
    elif(num[0]==eliminar):
        return eliminarDigito_aux(num[1:],eliminar,result)
    else:
        return eliminarDigito_aux(num[1:],eliminar,result+num[0])

#---------------------------------------------------------------------------------
"""
Nombre: nivelesLista
Entrada: una lista
Parametros: lista
Salida: numero de sublistas que tiene la lista ingresada
Restricciones: Debe ingresar una lista
"""
def nivelesLista(lista):
    if(isinstance(lista,list)):
        return nivelesLista_Aux(lista,[])
    else:
        print("Error: Debe ingresar una lista")


def nivelesLista_Aux(lista,resultado):
    if(lista==[]):
        return resultado
    else:
        
        if(isinstance(lista[0],list)):
            sub=contar_aux(lista[0],1)
            return nivelesLista_Aux(lista[1:],resultado+[sub])
        else:
            return nivelesLista_Aux(lista[1:],resultado+[0])


def contar_aux(lista,cont):
    if(lista==[]):
        return cont
    else:
        if(isinstance(lista[0],list)):
           return contar_aux(lista[0],cont+1)
        else:
            return 1

#---------------------------------------------------------------------------------

"""
Nombre: obtenerIndicesListaVectore
Entrada: tres vectores a evaluar
Parametros: vectorq,vector2,vector3
Salida: posiciones(indices) de los numero cero y los negativos
Restricciones: Debe ingresar una lista
               Deben ser numeros enteros
               Deben tener el mismo largo los vectores
"""
def obtenerIndicesListaVectore(vector1,vector2,vector3):
    if(isinstance(vector1,list)and isinstance(vector2,list))and isinstance(vector3,list):
        if(verificar(vector1)):
            if(verificar(vector2)):
                if(verificar(vector3)):
                    if(tamañoV(vector1,vector2,vector3)==1):
                        indice=indices(vector1,0,[])
                        indice2=indices(vector2,0,[])
                        indice3=indices(vector3,0,[])
                        return [indice]+[indice2]+[indice3]
                    else:
                        print("Error: Los indices deben ser del mismo tamaño")
                else:
                    print("Error: Deben ser numeros enteros")
            else:
                print("Error: Deben ser numeros enteros")
        else:
            print("Error: Deben ser numeros enteros")
    else:
        print("Error: Debe ingresar tres listas, con numeros enteros y mismo tamaño")


def verificar(vector):
    if(vector==[]):
        return True
    else:
        if(isinstance(vector[0],int)):
            return verificar(vector[1:])
        else:
            return False

def tamañoV(vector1,vector2,vector3):
    if(vector1==[])or vector2==[] or vector3==[]:
        if(vector1==[])and vector2==[] and vector3==[]:
            return True
        else:
            return False
    else:
        return tamañoV(vector1[1:],vector2[1:],vector3[1:])


def indices(vector,cont,resultado):
    if(vector==[]):
        return resultado
    elif(vector[0]<=0):
        return indices(vector[1:],cont+1,resultado+[cont])
    else:
        return indices(vector[1:],cont+1,resultado)
            
