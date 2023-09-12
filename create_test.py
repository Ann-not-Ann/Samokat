
# Анна Алексеенко, 8-я когорта — Финальный проект. Инженер по тестированию плюс


import sender_stand_request

#эта функция проверяет, что при выполнении запроса на получение заказа по треку заказа, приходит код ответа 200
def test_poluchenie_zakaza_po_nomeru():
    response = sender_stand_request.get_an_order_by_its_number()
    assert response.status_code == 200








