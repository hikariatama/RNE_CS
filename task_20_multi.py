# region: input
ПОБЕДА = 77  # Сумма, нужная для победы
ПЕРВАЯ_КУЧА = 7  # Кол-во камней в первой куче
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]  # Операции (+1, *2)
# endregion: input
# region: logic


def main():
    def f(x: int, y: int, r: int = 1) -> bool:
        # Если кто-то выиграл раньше, чем нужный ход
        if r < 4 and x + y >= ПОБЕДА:
            # Этот случай нам не подходит
            return False

        # Если мы достигли нужного количества ходов
        if r == 4:
            # Нужно проверить, победил ли нужный нам игрок
            return x + y >= ПОБЕДА

        # Возможные исходы
        cases = [
            *(f(op(x), y, r + 1) for op in ОПЕРАЦИИ),
            *(f(x, op(y), r + 1) for op in ОПЕРАЦИИ),
        ]

        # Если ход наш, то мы ищем, чтобы хотя бы один исход был победным
        # Если ход противника, то мы проверяем, чтобы все исходы подходили
        return all(cases) if r % 2 == 0 else any(cases)

    print(
        "Answer:",
        "".join(str(x) for x in range(1, ПОБЕДА - ПЕРВАЯ_КУЧА) if f(x, ПЕРВАЯ_КУЧА)),
    )


# endregion: logic

if __name__ == "__main__":
    main()
