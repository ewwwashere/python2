
import pandas as pd
from typing import List

def find_perfect_matches(boys: List[str], girls: List[str]) -> str:
    """
    Находит идеальные пары по алфавитной сортировке.
    
    Правила:
    1. Сортируем мальчиков и девочек по алфавиту
    2. Создаем пары по индексам
    3. Если разное количество - никто не получает пару
    """
    
    # Проверяем равенство количества
    if len(boys) != len(girls):
        return "Внимание, кто-то может остаться без пары!"
    
    # Сортируем по алфавиту
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    
    print("Идеальные пары:")
    matches = []
    
    # Создаем пары и выводим
    for boy, girl in zip(sorted_boys, sorted_girls):
        match_str = f"{boy} и {girl}"
        print(match_str)
        matches.append(match_str)
    
    return "\n".join(matches)

# Тест 1: Равное количество
print("=== ТЕСТ 1: Идеальные пары ===")
boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

result1 = find_perfect_matches(boys1, girls1)
print()

# Тест 2: Разное количество
print("=== ТЕСТ 2: Несовпадение ===")
boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

result2 = find_perfect_matches(boys2, girls2)
print()



def visualize_matches(boys: List[str], girls: List[str]):
    """Визуализация пар с помощью pandas."""
    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары!")
        return
    
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    
    # Создаем DataFrame для красивого вывода
    matches_df = pd.DataFrame({
        'Мальчик': sorted_boys,
        'Девочка': sorted_girls,
        'Пара': [f"{b} ↔ {g}" for b, g in zip(sorted_boys, sorted_girls)]
    })
    
    print("\n📊 ТАБЛИЦА ПАР:")
    print(matches_df.to_string(index=False))
    
    return matches_df

# Дополнительный тест с визуализацией
print("=== ВИЗУАЛИЗАЦИЯ ПАР ===")
visualize_matches(boys1, girls1)


def interactive_mode():
    """Интерактивный режим для ввода списков."""
    print("\n🔥 ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("Введите имена через запятую (или 'exit' для выхода)")
    
    while True:
        boys_input = input("\nМальчики: ").strip()
        if boys_input.lower() == 'exit':
            break
            
        girls_input = input("Девочки: ").strip()
        
        try:
            boys_list = [name.strip() for name in boys_input.split(',')]
            girls_list = [name.strip() for name in girls_input.split(',')]
            
            result = find_perfect_matches(boys_list, girls_list)
            print()
            
        except KeyboardInterrupt:
            print("\n👋 До свидания!")
            break

