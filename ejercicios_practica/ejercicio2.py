# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.



    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json() 

    
    user_total = []
    user1 = 0
    user2 = 0
    user3 = 0
    user4 = 0
    user5 = 0
    user6 = 0
    user7 = 0
    user8 = 0
    user9 = 0
    user10 = 0

    for user in data: 
        if user['completed'] == True:
            if user['userId'] == 1:
                user1 = user1 + 1
            elif user['userId'] == 2:
                user2 = user2 + 1
            elif user['userId'] == 3:
                user3 = user3 + 1
            elif user['userId'] == 4:
                user4 = user4 + 1
            elif user['userId'] == 5:
                user5 = user5 + 1
            elif user['userId'] == 6:
                user6 = user6 + 1
            elif user['userId'] == 7:
                user7 = user7 + 1
            elif user['userId'] == 8:
                user8 = user8 + 1
            elif user['userId'] == 9:
                user9 = user9 + 1
            elif user['userId'] == 10:
                user10 = user10 + 1

    user_total = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]
    numero_usuario = [1,2,3,4,5,6,7,8,9,10]

    



    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.


    fig = plt.figure()
    fig.suptitle('Titulos logrados por los usuarios')
    ax = fig.add_subplot()


    ax.bar(numero_usuario, user_total, color = 'darkred')
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel('Q titulos logrados')
    ax.set_xlabel('Numero de Usuario')
    plt.show()




    print("terminamos")