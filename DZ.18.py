class Tempe:

    dictionary = {'cel': 1, 'fr': 33.8, 'kel': 274.15}

    def __init__(self, temp_in, measure):  # temp_in - input value, measure - [cel, fr, kel]
        # self.cel = temp_in / self.dictionary[measure]
        self.cel = Tempe.to_cel(temp_in, measure)
        self.kel = Tempe.to_cel(temp_in, measure)
        self.fr = Tempe.to_fr(temp_in, measure)

    @staticmethod
    def to_cel(tempe, measure):
        if measure == 'fr':
            temp_in_cel = (tempe - 32) * 5/9
            return temp_in_cel
        elif measure == 'kel':
            temp_in_cel = tempe - 273.15
            return temp_in_cel
        elif measure == 'cel':
            temp_in_cel = tempe * 1
            return temp_in_cel

    @staticmethod
    def to_fr(tempe, measure):
        if measure == 'cel':
            temp_in_fr = (tempe * 9/5) + 32
            return temp_in_fr
        elif measure == 'kel':
            temp_in_fr = (tempe - 273.15) * 9/5 + 32
            return temp_in_fr
        elif measure == 'fr':
            temp_in_fr = tempe * 1
            return temp_in_fr

    @staticmethod
    def to_kel(tempe, measure):
        if measure == 'cel':
            temp_in_kel = tempe + 273.15
            return temp_in_kel
        elif measure == 'fr':
            temp_in_kel = (tempe - 32) * 5/9 + 273.15
            return temp_in_kel
        elif measure == 'kel':
            temp_in_kel = tempe * 1
            return temp_in_kel

    def __cmp__(self, other):
        if self.cel == other.cel:
            return 0
        elif self.cel > other.cel:
            return 1
        else:
            return -1

    def __lt__(self, other):
        if self.cel < other.cel:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.cel > other.cel:
            return True
        else:
            return False
    def __le__(self, other):
        if self.cel <= other.cel:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.cel >= other.cel:
            return True
        else:
            return False

    def __add__(self, other):
        return Tempe(self.cel + other.cel, 'cel')

length1 = Tempe(10, 'cel')
length2 = Tempe(10, 'cel')
print(length1 > length2)
print(length1 >= length2)
print(length1 < length2)
print(length1 <= length2)
print(length1 == length2)
print(length1 != length2)
print((length1 + length2).kel)

length1 = Tempe

print("*******")
print("10 cel")
print('in cel', length1.to_cel(10, 'cel'))
print('in kel', length1.to_kel(10, 'cel'))
print('in fr', length1.to_fr(10, 'cel'))

print("*******")
print("10 kel")
print('in cel', length1.to_cel(10, 'kel'))
print('in kel', length1.to_kel(10, 'kel'))
print('in fr', length1.to_fr(10, 'kel'))

print("*******")
print("10 fr")
print('in cel', length1.to_cel(10, 'fr'))
print('in kel', length1.to_kel(10, 'fr'))
print('in fr', length1.to_fr(10, 'fr'))

print("*******")


