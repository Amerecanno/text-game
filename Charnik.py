from types import CoroutineType
#import Welcome

#Welcome.Start_Game.welcomes

class city():
    print("Спустя много времени ты добрался до города")
    def city_get():
        city_select = int(input("Ты зашёл в город куда зайдем? \n 1. Рынок(Не работает) \n 2. Замок Дворянина\n 3. Дом(Нету если не куплено) \n 4. что-то я не придумал \n 5. Посмотреть Навыки, и уровень \n Выбирите вашу цифру:"))
        if city_select == 1:   
            print("Рынок закрыт")
        elif city_select == 2:
            print("Рынок закрыт")
        elif city_select == 3:
            print("Рынок закрыт")
        elif city_select == 4:
            print("Рынок закрыт")
        elif city_select == 5:
            print("Смотрим на себя....")
        else:
            print("Только цифры от одного до 5")
            city.city_get()




city.city_get()