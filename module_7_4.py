# Задание:
# cоздайте новый проект или продолжите работу в текущем проекте.
# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:
#
# Использование %:
team1 = '"Мастера кода"'
team2 = '"Волшебники данных"'

team1_num = 5
team2_num = 6
print('В команде %s участников: %s!' % (team1, team1_num))
print('В команде %s участников: %s!' % (team2, team2_num))
print('Итого сегодня в командах участников: %s, и %s!' % (team1_num, team2_num))

# Использование format():

score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 17012.1

print('Команда {} решила задач: {}!'.format(team1, score_1))
print('Команда {} решила задач: {}!'.format(team2, score_2))
print('{} решили задачи за {} c !'.format(team1, team1_time))
print('{} решили задачи за {} c !'.format(team2, team2_time))

# Использование f-строк:

score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'кто же победил?'
tasks_total = 82
time_avg = 350.4

print(f'Скоро узнаем результат битвы, {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды "Мастера кода"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды "Волшебники Данных"!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')

