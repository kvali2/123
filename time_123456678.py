from datetime import datetime
from dateutil.parser import parse

# Завдання 1: Вивести поточну дату та час
now = datetime.now()
print(now.strftime("%d.%m.%Y %H:%M:%S"))


# Завдання 4: Різниця між двома датами

d1_str = input("Перша (20.12.2024),(2024-12-20),(December 20, 2024) пиши так тогошо за допомогою parse так можна : ")
d2_str = input("Друга (20.12.2024),(2024-12-20),(December 20, 2024) пиши так тогошо за допомогою parse так можна : ")
try:
    d1 = parse(d1_str, dayfirst=True)
    d2 = parse(d2_str, dayfirst=True)
    delta = abs((d2 - d1).days)
    print(f"Між тим і тим  пройшло {delta}  днів наверно сам пощитай")
except:
    print("неправильно роби правильно")


# Завдання 5: Привітання залежно від часу доби
def time_12341():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        time = "Доброго ранку"
    elif 12 <= hour < 18:
        time = "Доброго дня"
    elif 18 <= hour < 23:
        time = "Доброго вечора"
    else:
        time = "Доброї ночі"
    print(f"{time}")


time_12341()
