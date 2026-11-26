"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""

    order = 1
    method_name = "Базовий метод"

    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""
        self.func = func
        self.a = a
        self.b = b

    @classmethod
    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""
        return cls(func, params["a"],params["b"])

    @staticmethod
    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""
        if a >= b:
            raise ValueError("Incorrect bounds")

    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError

    def adaptive_integrate(self, eps=1e-4, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""
        n = initial_n
        koef = 2**self.order-1
        I_h = self.integrate(n)
        I_h2 = self.integrate(2*n)
        delta = abs(I_h-I_h2)/koef
        print(f"n = {n} -> I = {I_h}")
        while delta>=eps:
            n*=2
            I_h = I_h2
            I_h2 = self.integrate(2*n)
            delta = abs(I_h2-I_h)/koef
            print(f"n = {n} -> I = {I_h}")
        print(f"n = {2*n} -> I = {I_h2}")
        value = I_h2 + (I_h2 - I_h)/koef
        return value,2*n,delta

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""
        return(f'{self.method_name} на відрізку {[self.a,self.b]} (порядок точності O(h^{self.order})')
    



class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func,a,b)

    def integrate(self, n):
        h = (self.a - self.b)/n
        integral = sum(h*self.func(self.a + h*(i + 0.5)) for i in range(n))
        return(integral)


class TrapezoidIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою трапецій."""

    order = 2
    method_name = "Формула трапецій"

    def __init__(self, func, a, b):
        super().__init__(func,a,b)

    def integrate(self, n):
        h = (self.a - self.b)/n
        integral = h*(self.func(self.a) + self.func(self.b))/2 + sum(h*self.func(self.a + i*h) for i in range(1,n))
        return(integral)


class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""

    order = 4
    method_name = "Формула Сімпсона"

    def __init__(self, func, a, b):
        super().__init__(func,a,b)

    def integrate(self, n):
        h = (self.a - self.b)/n
        Sum1 = sum(self.func(self.a + i*h)for i in range(1,n,2))
        Sum2 = sum(self.func(self.a + i*h)for i in range(2,n-1,2))
        return (h/3)*(self.func(self.a)+self.func(self.b)+4*Sum1+2*Sum2)
    
