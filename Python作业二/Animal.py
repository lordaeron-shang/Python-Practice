import yaml


class Animal:

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print(f'{self.name}会叫')

    def run(self):
        print(f'{self.name}会跑')


class cat(Animal):
    def __init__(self, name, color, age, gender, hair='短毛'):
        super(cat, self).__init__(name, color, age, gender)
        self.hair = hair

    def catch(self, name):
        print(f'{self.name} 抓老鼠')
        return (f'{self.name}抓到了老鼠')

    def call(self):
        print(f"{self.name}'喵喵叫'")


class dog(Animal):
    def __init__(self, name, color, age, gender, hair='长毛'):
        super(dog, self).__init__(name, color, age, gender)
        self.hair = hair

    def watch(self, name):
        print(f'{self.name}会看家')

    def call(self):
        print(f'{self.name}汪汪叫')


if __name__ == '__main__':
    with open("Animal_configure.yml", encoding="UTF-8") as f:
        data = yaml.safe_load(f)
    # (cat)
    cat1 = data['cat']
    name1 = cat1['name']
    color1 = cat1['color']
    age1 = cat1['age']
    gender1 = cat1['gender']
    hair1 = cat1['hair']

    Catattr = cat(name1, color1, age1, gender1, hair1)
    ability1 = Catattr.catch(name1)

    print(f"{name1}是{color1}的，今年{age1}岁了，它是只{gender1}猫，它是{hair1}猫,{ability1}")

    # (Dog)
    dog1 = data['dog']
    name2 = dog1['name']
    color2 = dog1['color']
    age2 = dog1['age']
    gender2 = dog1['gender']
    hair2 = dog1['hair']

    Dogattr = dog(name2, color2, age2, gender2, hair2)
    ability2 = Dogattr.watch(name2)

    print(f"{name2}是{color2}色的，今年{age2}岁了，它是只{gender2}狗，他的毛是{hair2}")
