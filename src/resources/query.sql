SELECT users.Name AS "Имя пользователя", COUNT(messages.UID) AS "Общее количество сообщений"
FROM users
JOIN
messages
on
users.UID = messages.UID
GROUP BY users.Name
;