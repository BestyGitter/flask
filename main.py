from flask import Flask
import random
app = Flask(__name__)

facts= [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
"Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",

'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
'Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.',

'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',

'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.',
'Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.',

'Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.'
]

dices = [4, 6, 8, 10, 12, 16, 20]

@app.route("/")
def hello_world():
    return f'<a href="/random_fact">Посмотреть случайный факт!</a><a href="/{random.choice(dices)}">Бросок случайного кубика</a>'

@app.route("/random_fact")
def random_facts():
    return f'<h1>{random.choice(facts)}</h1>'

@app.route("/<dice>")
def random_dice(dice):
    return f'<h1>Вам выпало число: {random.randint(1, int(dice))}</h1>'


app.run(debug=True)