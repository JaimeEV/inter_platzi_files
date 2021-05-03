def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**3

    # my_dict = {i : i**3 for i in range(1,101) if i % 3 != 0}
    # print(my_dict)

# Reto. Llaves los primeros mil numeros y los valores sus raices cuadradas
        my_dict_sqr = { i: i**(1/2) for i in range(1, 1001)}
        print(my_dict_sqr)




if __name__ == "__main__":
    run()