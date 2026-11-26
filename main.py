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
    pass


if __name__ == "__main__":
    main()
