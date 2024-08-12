#Павел Мичка, 20-я когорта, - Финальный проект. Инженер по тестированию плюс.
import sender_stand_request


#Тест для проверки, что при получении заказа по номеру возвращается 200 код
def test_order_creation_and_return():
    response = sender_stand_request.get_order()
    assert response.status_code == 200, (f"Ошибка! Получен статус код отличный от 200 - {response.status_code}. "
                                         f"Сообщение: {response.text}")
