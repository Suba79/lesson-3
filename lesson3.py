import smtplib
import os
from dotenv import load_dotenv  

load_dotenv('lesson3.env')

login = os.getenv("login")
password = os.getenv("password")

site_name = input("Ссылка на проект - ")
name_friend = input("Имя друга - ")
your_name = input("Ваше имя - ")

user = login  
where = input("Куда отправляем - ")
theme = input("Тема письма - ")

text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

text = text.replace("%website%", site_name)
text = text.replace("%friend_name%", name_friend)
text = text.replace("%my_name%", your_name)

letter = """\
From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

{3}
""".format(user, where, theme, text)

letter = letter.encode("UTF-8")

smtp_server = "smtp.yandex.ru"
smtp_port = 465
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.login(login, password)
server.sendmail(user, where, letter)
server.quit()



