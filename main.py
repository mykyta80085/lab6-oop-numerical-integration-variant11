"""Головний модуль запуску чисельного інтегрування."""
'''
Учень - Возний Микита
Варінат - 11
Лабораторна робота 6
'''

import math

from integrators import (
    RectangleIntegrator,
    SimpsonIntegrator,
    TrapezoidIntegrator,
)


def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""
    return((math.cos(x)-1)/(x*x))


def main():
    """Точка входу програми."""
    func = target_function
    params = {"a": 0.0, "b":1.0}
    eps = 0.00002
    integrators = [RectangleIntegrator.from_dict(func, params), TrapezoidIntegrator.from_dict(func, params), SimpsonIntegrator.from_dict(func, params)]
    for integrator in integrators:
        print(f"\t{integrator}")
        res = integrator.adaptive_integrate(eps, initial_n=2)
        print(f"Уточнений результат: {res[0]} (n_min = {res[1]}, похибка = {res[2]})")


if __name__ == "__main__":
    main()
