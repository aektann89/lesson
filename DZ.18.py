class My_temp:


    def __init__(self, base, value):  # base - input value, value -[f, c, k]
        self.K = My_temp.cvt_kelvin(base, value)
        self.C = My_temp.cvt_celcius(base, value)
        self.F = My_temp.cvt_farenheight(base, value)





    @staticmethod
    def cvt_farenheight(base, value):
        if base == 'C':
            return (float(value) * (9 / 5)) + 32
        elif base == 'K':
            return (float(value) - 273.15) * (9 / 5) + 32

    @staticmethod
    def cvt_celcius(base, value):
        if base == 'F':
            return (float(value) - 32) * (5 / 9)
        elif base == 'K':
            return float(value) - 273.16

    @staticmethod
    def cvt_kelvin(base, value):
        if base == 'C':
            return (float(value) + 273.16)
        elif base == 'F':
            return (float(value) - 32) * (5 / 9) + 273.15
temp1 = My_temp.cvt_kelvin('C', 5 )
temp2 = My_temp.cvt_farenheight('C', 5)
temp3 = My_temp.cvt_celcius('F', 5)
print(temp1)
print(temp2)
print(temp3)
