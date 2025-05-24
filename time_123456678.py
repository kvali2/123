from datetime import datetime

# Завдання 1: Вивести поточну дату та час
now = datetime.now()
print(now.strftime("%d.%m.%Y %H:%M:%S"))


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
