print('-----------------------------------------------------------------------------------------------------------------------------------------------')
class Eukaryotes:
    genetic_apparatus = 'ядро'
    def check_kernel(self):
        print(f'Мой генетический апарат содержет {self.genetic_apparatus}.', 'Я отношусь к Эукариотом')
class Animals:
    type_of_food = 'готовые органические соеденения'
    jaws = 'челюсти'
    def move_jaws(self):
        print(f'**Молчаливо открывает и закрывает {self.jaws}**')
    def chek_type_of_food(self):
        print(f'Мой тип питания это {self.type_of_food}.', 'Я животное')
class chordates:
    body_structure = 'хорда'
    gills = 'жабры'
    def move_gills(self):
        print(f'**Надувает {self.gills}**')
    def chek_body_strukture(self):
        print(f'У меня есть {self.body_structure}.', 'Я, хордовое животное')
class Actinopterygii:
    fin_right = 'Правый плавник'
    fin_left = 'Левый плавник'
    fin_top = 'Верхний плавник'
    tail = 'хвост'

    fin_structure = 'мои плавники представляют собой перепонки кожи, поддерживаемые костными или роговыми шипами (лучами)'
    def move(self):
        print(f'**Двигает {self.fin_right}**')
        print(f'**Двигает {self.fin_left}**')
        print(f'**Двигает {self.tail}**')
    def chek_fin_structure(self):
        print(f'Я отношусь к классу лучеперых рыб,{self.fin_structure}')
class herring:
    features = 'Тело сжатое с боков, с зазубренным краем брюха. Чешуя умеренная или крупная, редко мелкая. Верхняя челюсть не выдаётся за нижнюю.'
    distribution_area = 'Атлантический океан'
    def chek_features(self):
        print(f'Мой род - Сельди, у меня {self.features}')
    def distribution(self):
        print(f'Моя среда обитания {self.distribution_area}')

class Breams:
    features = 'Тело сильно сжатое с боков, высокое или удлинённое. Чешуя умеренной величины. Спинной плавник короткий и высокий без толстого шипа'
    def chek_features(self):
        print(f'Мой род - Лещи, у меня {self.features}')
    distribution_area = 'Предпочитаю жить преимущественно в спокойных, больших и глубоких озёрах, также в реках и отчасти солоноватых водах. '
    def distribution(self):
        print(f'Я {self.distribution_area}')

class Atlantic_herring(Eukaryotes, Animals, chordates, Actinopterygii, herring):
    def voice(self):
        print(f'Привет! Я Атлантическая сельдь и меня зовут {self.atlantic_herring_mane}')
    def rofl(self):
        print('Да, да, да... Рыбы не умеют разговаривать, тебе это снится...')

    def __init__(self, atlantic_herring_mane):
         self.atlantic_herring_mane = atlantic_herring_mane
class Bream(Eukaryotes, Animals, chordates, Actinopterygii, Breams):
    def voice(self):
        print(f'Привет! Я Лещ и меня зовут {self.bream_name}')
    def rofl(self):
        print('Атлантическая сельдь сказала тебе, что рыбы не умеют разговаривать? Не верь ей, она соврала;)')

    def __init__(self, bream_name):
        self.bream_name = bream_name




Baltika = Atlantic_herring('Baltika')
Baltika.voice()
Baltika.rofl()
Baltika.check_kernel()
Baltika.chek_type_of_food()
Baltika.move_gills()
Baltika.chek_body_strukture()
Baltika.chek_fin_structure()
Baltika.move()
Baltika.chek_features()
Baltika.distribution()
Baltika.move_jaws()

Nemo = Bream('Nemo')
Nemo.voice()
Nemo.rofl()
Nemo.check_kernel()
Nemo.chek_type_of_food()
Nemo.move_gills()
Nemo.chek_body_strukture()
Nemo.chek_fin_structure()
Nemo.move()
Nemo.chek_features()
Nemo.distribution()
Nemo.move_jaws()

