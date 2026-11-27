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
    return(math.log(x)/(x+1))


def main():
    """Точка входу програми."""
    func = target_function
    params = {"a": 1, "b": 2}
    eps = 0.00002
    integrators = [RectangleIntegrator.from_dict(func, params), TrapezoidIntegrator.from_dict(func, params), SimpsonIntegrator.from_dict(func, params)]
    for integrator in integrators:
        integrator.validate_bounds(params["a"],params["b"])
        print(f"{integrator}")
        res = integrator.adaptive_integrate(eps, initial_n=2)
        print(f"Уточнений результат: {res[0]} (n_min = {res[1]}, похибка = {res[2]})")

    for integrator in integrators:
        print(integrator.method_name, integrator.times_used)
    
if __name__ == "__main__":
    main()
