def solution(args):
    #necesito recorrer el array buscando una sucesión de números para añadirlos a una cadena de texto
    #viendo si tienen como mínimo una sucesión de 3 integers y ponerlos así 1-3 incluyendo ambos
    #si no, simplemente me printeas el integer sea este negativo o positivo
    #hay un problema y es cuando hay pocos numeros en una serie CHCKED
    #se puede refactorizar quitando la variable last_number_range, es uso de memoria redundante
    #se puede refactorizar cambiando la variable first_number_range por un acumulador para buscar el indice del mismo
    #se puede refactorizar haciendo qu el condicional tercer que comprueba contenido de la serie se ponga en segundo lugar
    check,first_number_range,last_number_range = 0,0,0
    answer = ""
    for arg in range(len(args)):
        #este condicional si es la ultima serie del array
        if len(args) == arg+1 and check >= 1:
            answer += str(first_number_range) + "-" + str(args[arg])
            break
        #esto es para romper el bucle si el indice se pasa
        if len(args) == arg+1:
            answer += str(args[arg])
            break
        # este condicional mira si es el principio de una serie
        if args[arg+1] == args[arg]+1 and check == 0:
            first_number_range = args[arg]
            check += 1
        #este condicional mira si entra dentro del rango de una serie
        elif args[arg+1] == args[arg]+1 and check >= 1:
            check +=1
            continue   
        #este condicional mira si es el final de una serie válida
        elif args[arg+1] != args[arg]+1 and check >= 2:
            last_number_range = args[arg]
            check = 0
            answer += str(first_number_range) + "-" + str(last_number_range) + ","
        #esto es si no hacen series de 3 (es decir de 2)
        elif args[arg+1] != args[arg]+1 and check == 1:
            answer += str(first_number_range) + "," + str(args[arg]) + ","
            check = 0
        #esto es si no hay ninguna serie
        else:
            answer += str(args[arg]) + ","
    return answer

if __name__ == "__main__":
    assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
    assert solution([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20'
    assert solution([1,2,3,0]) == '1-3,0'