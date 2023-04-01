class Name:
    def __init__(self, name: str):
        self.name = name
        self.title: SportTitle = None

    def get_name(self):
        return f'Имя--> {self.name}'

    def get_experience(self):
        return {self.title.get_experiences() if self.title else 0}

class UpdateName(Name):
    def __init__(self, name: str, surname: str, age: int, height: float, weight: int):
        super().__init__(name)
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight

    def get_update(self):
        return (f'Фамилия--> {self.surname}\n'
                f'Возраст--> {self.age}\n'
                f'Рост--> {self.height}\n'
                f'Вес--> {self.weight}')


class SportType:
    def __init__(self, sport: str, position: str):
        self.sport = sport
        self.position = position
    def Sport_Typ(self):
        return (f'Вид спорта --> {self.sport}\n'
                f'Позиция --> {self.position}')


class SportTitle(SportType):
    def __init__(self, sport: str, experience: float, position: str):
        super().__init__(sport, position)
        self.experience = experience

    def get_experiences(self):
         return {self.experience}'


main = Name('Никита')
print(main.get_name())
main.title = SportTitle("Футбол", 10, "Правый вингер")
up = UpdateName('Никита', 'Белоусов', 17, 175, 75)
print(up.get_update())
sporttype = SportType('Футбол', "Правый вингер ")
print(sporttype.Sport_Typ())


print(main.title.experience)