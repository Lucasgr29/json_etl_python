import requests
import json
import matplotlib.pyplot as plt





def fetch():

    response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50')
    data = response.json()
    json_response = data['results']



    lista_filtrada = []
    dic = {}

    currency_ars = [x for x in json_response if x['currency_id'] == 'ARS']
    for depto in currency_ars:
        dic['precio'] = depto['price']
        dic['condicion'] = depto['condition']
        lista_filtrada.append(dic.copy())


    return lista_filtrada


def transform(dataset, min, max):

    bajo_min = [x for x in dataset if x['precio'] < min]
    medio = [x for x in dataset if min <= x['precio'] <= max ]
    sobre_min = [x for x in dataset if x['precio'] > max]

    cant_min = len(bajo_min)
    cant_medio = len(medio)
    cant_max = len(sobre_min)

    return[cant_min, cant_medio, cant_max]


def report(data):

    etiquetas = ["< $4000", '$4000 a $12000', '> $12000']
    fig = plt.figure()
    fig.suptitle('Distribucion precios alquileres', fontsize = 16)
    ax = fig.add_subplot()

    ax.pie(data, labels = etiquetas)

    plt.show()






if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")


    min = 5000
    max = 11000

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)