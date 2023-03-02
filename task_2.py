import itertools

# region: input

# Переменные из условия в любом порядке
ПЕРЕМЕННЫЕ = "xyzw"

# Известные значения из условия (пустые клетки - ...)
ИЗВЕСТНЫЕ = [
    [1, 1, 1, 0, 1],
    [..., ..., 0, 0, 0],
    [..., 0, ..., ..., 0],
]


def ФУНКЦИЯ(x: int, y: int, z: int, w: int) -> int:
    """Логическая функция из условия"""
    return int((((not y) ** w) and x ** y) ** ((not x) == (not not z)))


# endregion: input
# region: logic


def main():
    # Перебираем все возможные порядки, в которых могут располагаться переменные
    for order in itertools.permutations(ПЕРЕМЕННЫЕ):
        # Копируем маску локально
        patterns = ИЗВЕСТНЫЕ.copy()
        # Перебираем все возможные значения переменных
        for lst in itertools.product([0, 1], repeat=len(ПЕРЕМЕННЫЕ)):
            # Расставляем значения в соответствии с текущим порядком
            variables = dict(zip(order, lst))
            # Считаем результат с текущими переменными
            variables["f"] = ФУНКЦИЯ(**variables)
            for pattern in patterns:
                # Проверяем, соответствует ли текущая строка с текущим порядком
                # переменных одному из шаблонов
                for pdigit, adigit in zip(
                    pattern, map(lambda x: variables[x], (*order, "f"))
                ):
                    if pdigit is not Ellipsis and pdigit != adigit:
                        break
                else:
                    # Если соответствует, убираем этот шаблон
                    patterns.remove(pattern)
                    break

        # Если мы нашли совпадения для всех шаблонов
        if not patterns:
            # Это ответ"
            print("Answer:", "".join(order))


# endregion: logic

if __name__ == "__main__":
    main()
