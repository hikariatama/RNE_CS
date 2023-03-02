import itertools

# region: input
ПЕРЕМЕННЫЕ = "x"  # Список всех переменных без "A"


def ФУНКЦИЯ(x: int, A: int) -> bool:
    """Логическая функция из условия"""
    return x & 51 == 0 or ((x & A == 0) ** (x & 41 == 0))


НАЙТИ_МАКСИМАЛЬНОЕ = False  # True если нужно найти наибольшее A


# endregion: input
# region: logic


def main():
    maximum = 0
    for A in range(1000):
        for variables in itertools.product(range(1000), repeat=len(ПЕРЕМЕННЫЕ)):
            if not ФУНКЦИЯ(*variables, A=A):
                break
        else:
            if not НАЙТИ_МАКСИМАЛЬНОЕ:
                print("Answer:", A)
                break
            else:
                maximum = max(maximum, A)

    if НАЙТИ_МАКСИМАЛЬНОЕ:
        print("Answer:", maximum)


# endregion: logic

if __name__ == "__main__":
    main()
