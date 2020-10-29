def solution(args):
    #necesito recorrer el array buscando una sucesión de números para añadirlos a una cadena de texto
    #viendo si tienen como mínimo una sucesión de 3 integers y ponerlos así 1-3 incluyendo ambos
    #si no, simplemente me printeas el integer sea este negativo o positivo
    check,first_number_range,last_number_range = 0,0,0
    answer = ""
    for arg in range(len(args)):
        if arg == len(args)-1:
            break
        # este condicional mira si es el principio de una serie
        if args[arg+1] == args[arg]+1 and check == 0:
            first_number_range = args[arg]
            check += 1
        #este condicional mira si es el final de una serie válida
        elif args[arg+1] != args[arg]+1 and check >= 2:
            last_number_range = args[arg]
            check = 0
            answer += str(first_number_range) + "-" + str(last_number_range) + ","
        #este condicional mira si entra dentro del rango de una serie
        elif args[arg+1] == args[arg]+1 and check >= 1:
            check +=1
            continue
        else:
            answer += str(args[arg]) + ","
    return answer

if __name__ == "__main__":
    assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    assert solution([[-3,-2,-1,2,10,15,16,18,19,20]])