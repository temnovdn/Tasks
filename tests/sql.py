# users
# UID Name
# 1. Платон Щукин
# 2. Лера Страза
# 3. Георгий Атласов
#
# messages
# UID msg
# 1 – "Привет, Платон!"
# 3 – "Срочно пришли карту."
# 3 – "Жду на углу Невского и Тверской."
# 1 – "Это снова я, пиши чаще"

# Напишите SQL-запрос, результатом которого будет таблица из двух полей: «Имя пользователя» и «Общее количество сообщений».

import sqlite3

sqlite3.connect(":memory:")
cursor = sqlite3.Cursor()

query = "SELECT Name FROM users AS 'Имя пользователя' " \
        "FROM messages JOIN (messages.UID COUNT DISTINCT) AS 'Общее количество сообщений' " \
        "ON users.UID = messages.UID ORDER BY UID;"

cursor.execute(query)