SELECT Name FROM users AS "Имя пользователя"
FROM messages JOIN
(messages.UID COUNT DISTINCT) AS "Общее количество сообщений"
ON users.UID = messages.UID
ORDER BY UID;