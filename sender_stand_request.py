import configuration
import data
import requests


#Метод создания заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


#Метод получения заказа по номеру
def get_order():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                            params={'t': create_order(data.order_body).json()["track"]})
    return response
