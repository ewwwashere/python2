# Дейтинг-сервис

Описание:
  Алгоритм подбора пар по алфавитной сортировке
  для дейтинг-сервиса (MVP версия)

Принцип работы:
  1. Сортируем мальчиков и девочек по алфавиту
  2. Создаем пары по индексам
  3. НЕ создаем пары, если количество не совпадает

Примеры:
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

РЕЗУЛЬТАТ:
Идеальные пары:
Alex и Emma
Arthur и Kate
John и Kira
Peter и Liza
Richard и Trisha

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

РЕЗУЛЬТАТ:
Внимание, кто-то может остаться без пары!

Запуск:
  python dating_matcher.py

Требования:
  pip install pandas matplotlib seaborn
  
Использование:
  jupyter notebook dating_matcher.ipynb
  или
  python dating_matcher.py
