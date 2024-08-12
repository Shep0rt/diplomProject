Павел Мичка, 20-я когорта, - Финальный проект. Инженер по тестированию плюс.
 # **Практический блок: вторая часть**
# Работа с базой данных
- **Задание №1:** 

SELECT a.login, COUNT(b.id) AS "deliveryCount" FROM "Couriers" AS a LEFT JOIN "Orders" AS b ON a.id = b."courierId" WHERE b."inDelivery" = true GROUP BY a.login;
- **Задание №2:** 

SELECT a.track, CASE WHEN a.finished = true THEN 2 WHEN a.cancelled = true THEN -1 WHEN a."inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders" AS a;

# Автоматизация теста к API
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- Для корректного запуска необходимо указать актуальный URL API в файле [configuration.py](configuration.py) в параметре URL_SERVICE
- Все тесты расположены в файле [get_kit_test.py](get_kit_test.py)
