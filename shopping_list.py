user_input = input("Quieres agregar algo a la lista de compras?[S/N]")
shopping_list = []


def agregar_objeto(user_input):
    while user_input.upper() == "S":
        objeto_a_agregar = input("Que objeto deseas agregar?")
        shopping_list.append(objeto_a_agregar)
        user_input = input("Quieres agregar otro articulo?[S/N]")
        user_input= check_input(user_input)
    print_shopping_list(shopping_list)

def print_shopping_list(shopping_list):
    i = 1
    for a in shopping_list:
        if i != len(shopping_list):
            print(a, end=",")
            i += 1
        else:
            print(a, end='.')
    exit()

def check_input(user_input):
    while user_input.upper() != "S" and user_input.upper() != "N":
        user_input = input("Por favor introduce un valor valido. [S/N]")
    agregar_objeto(user_input)

if __name__ == '__main__':
    check_input(user_input.upper())
