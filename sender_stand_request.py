import configuration
import requests
import data



#эта функция создает новый заказ
def post_new_zakaz(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ZAKAZ_PATH,
                         json=body)



#эта функция получает заказ по его номеру
def get_an_order_by_its_number():
    response = post_new_zakaz(data.zakaz_body);
    track = response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track))



