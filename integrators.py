"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""

    order = 1
    method_name = "Базовий метод"

    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""
        pass

    @classmethod
    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""
        pass

    @staticmethod
    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""
        pass

    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError

    def adaptive_integrate(self, eps=1e-4, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""
        pass

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""
        return(f'{self.method_name} на відрізку {[self.a,self.b]} (порядок точності O(h^{self.order})')
    



class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):
        super().__init__(func,a,b)
        pass

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
        pass

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
        pass

    def integrate(self, n):
        h = (self.a - self.b)/n
        integral = h/3 * (self.func(self.a)+self.func(self.b))
        + sum(h*4/3*self.func(self.a + i*h) for i in range(1,n,2))
        + sum(h*2/3*self.func(self.a + i*h) for i in range(2,n-1,2))
        return(integral)
    
