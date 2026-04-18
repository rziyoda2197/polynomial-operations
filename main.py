class Polinom:
    def __init__(self, koeffs):
        self.koeffs = koeffs

    def __add__(self, other):
        max_deg = max(len(self.koeffs) - 1, len(other.koeffs) - 1)
        result = [0] * (max_deg + 1)
        for i in range(max_deg + 1):
            if i < len(self.koeffs):
                result[i] += self.koeffs[i]
            if i < len(other.koeffs):
                result[i] += other.koeffs[i]
        return Polinom(result)

    def __mul__(self, other):
        result = [0] * (len(self.koeffs) + len(other.koeffs) - 1)
        for i in range(len(self.koeffs)):
            for j in range(len(other.koeffs)):
                result[i + j] += self.koeffs[i] * other.koeffs[j]
        return Polinom(result)

    def __str__(self):
        return ' + '.join(f'{coeff}x^{deg}' if deg > 0 else f'{coeff}' for deg, coeff in enumerate(self.koeffs) if coeff != 0)


# Misol:
p1 = Polinom([1, 2, 3])
p2 = Polinom([4, 5, 6])
p3 = Polinom([7, 8, 9])

print("Polinom 1:", p1)
print("Polinom 2:", p2)
print("Polinom 3:", p3)

print("Polinom 1 + Polinom 2:", p1 + p2)
print("Polinom 1 * Polinom 2:", p1 * p2)
print("Polinom 1 + Polinom 2 + Polinom 3:", p1 + p2 + p3)
```

Bu kodda biz `Polinom` classini yaratdik, uda polinomlarni qo'shish va ko'paytirish uchun `__add__` va `__mul__` metodlarini implement oldik. `__str__` metodidan foydalanib, biz polinomlarni string sifatida chiqarish uchun metodni implement oldik. Misol uchun, biz uchta polinom yaratdik va ulardan foydalanib, qo'shish va ko'paytirish amalga oshirdik.
