

def find_matches(boys, girls):

    if len(boys) != len(girls):
        print("Внимание, кто-то может остаться без пары!")
        return
    

    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    

    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")


boys1 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls1 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
find_matches(boys1, girls1)
print()

boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
find_matches(boys2, girls2)
