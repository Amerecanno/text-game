

#weclome 



from msilib.schema import Class
from venv import create


 
class Start_Game():
    print("Вы зашли в игру!")
    def welcomes():
        welcome = int(input("Будем играть?(1-Да. 2-Нет.): "))
        if welcome == 1 :
            print("Добро Пожаловать!")
            Start_Game.chartesetape()
        elif welcome == 2:
            exit
        else:
            print("(1-Да. 2-Нет.)")
            Start_Game.welcomes()
            

    def chartesetape():
        print("Время создать вашего персонажа")
        global player , desc_player
        player = str(input("Как зовут вашего персонажа?: "))
        desc_player = str(input("Опишите вашего персонажа!(Опционально): "))
        print("И так вы создали персонажа. Время отправится в путешествие.")
        file = open( 'savefile',mode='w', encoding='utf-8')
        file.writelines([ "player = " , player])
        file.writelines(["\ndesc_player = " , desc_player])
        file.close()
Start_Game.welcomes()