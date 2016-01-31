# -*- coding: utf-8 -*-
"""
Первое задание
"""
from collections import Counter
import pandas as pd


def write_file(task_name, value):
    """
    Функция для записи ответа в файл
    """
    file_name = "./answers/%s.txt" % task_name
    with open(file_name, 'w') as af:
        af.write(value)


data = pd.read_csv('titanic.csv', index_col='PassengerId')
print data.columns.values


# Сколько мужчин и женщин плыло на корабле?
sex_stat = data['Sex'].value_counts()
sex_stat = "%d %d" % (sex_stat[0], sex_stat[1])
write_file("sex_stat", sex_stat)
print "Сколько мужчин и женщин плыло на корабле?: %s" % sex_stat

# вычисляем процент спасшихся
survived = data['Survived'].value_counts()
survived_in_percent = float(survived[1])/survived.sum()*100
write_file("survived_in_percent", "%.2f" % survived_in_percent)
print "Вычисляем процент спасшихся: %.2f" % survived_in_percent

# Процент плывших первым классом
first_class = data['Pclass'].value_counts()
first_class_in_percent = float(first_class[1])/first_class.sum()*100
write_file("first_class_in_percent", "%.2f" % first_class_in_percent)
print "Сколько пассажиров 1 класса: %.2f" % first_class_in_percent

# Статистика по возрасту
age_stat = "%.2f %.2f" % (data['Age'].mean(), data['Age'].median())
write_file("age_stat", age_stat)
print "Среднее и медиана возраста: %s" % age_stat

#Счтаем корреляцию Пирсона
sib_par = data[['SibSp', 'Parch']]
sib_par_corr = "%.2f" % sib_par.corr()['SibSp']['Parch']
write_file("sib_par_corr", sib_par_corr)
print "Корреляция меньше 0.5: %s" % sib_par_corr

#Самое интересное: считаем женские имена

# Нам нужна только колонка с именем
female_names = data[data['Sex'] == "female"]['Name']

# Для простоты все имена положим в список
my_names = []


def get_female_name(name, my_names):
    """
    Извлекаем имена из полного имени
    Два случая с мисс и миссис
    """
    if "Miss." in name:
        nn = name.split("Miss.")
        my_names += nn[1].strip().replace('"', '').replace('(', '').replace(')', '').split()
    if "Mrs." in name:
        nn = name.split("(")
        if len(nn) > 1:
            first_name = nn[1].split()[0]
            my_names.append(first_name.replace('(', '').replace(')', ''))

# применяем функцию к каждому имени
female_names.apply(get_female_name, args = (my_names, ))

# Подсчет сколько имя встречается
names_count = Counter(my_names)
# самые популярные 10
most_common = names_count.most_common(10)
# самое популярное имя
most_common_name = most_common[0][0]

write_file("most_common_name", most_common_name)
print "Имя: %s" % most_common_name