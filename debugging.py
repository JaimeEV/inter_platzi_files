#Ejemplos con list_comprehension, ciclo for y lambda function
# def divisors(num:int) -> list:  
#     divisors_list_comp = [ divisor for divisor in range(1, num + 1) if num % divisor == 0 ]
#     return divisors_list_comp
#     #---------------------------------------------
#     divisors = []
#     for i in range(1 , num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num <= 0:
            raise ValueError
        divisors = lambda num: [ i for i in range(1, num + 1) if num % i == 0]
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número mayor que 0")

if __name__ == "__main__":
    run()