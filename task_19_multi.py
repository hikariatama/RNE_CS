# region: input
ПОБЕДА = 77  # Сумма, нужная для победы
ПЕРВАЯ_КУЧА = 7  # Кол-во камней в первой куче
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]  # Операции (+1, *2)
# endregion: input
# region: logic


def main():
    def f(x: int, y: int, r: int = 1) -> bool:
        # Если кто-то выиграл раньше, чем нужный ход
        if r < 3 and x + y >= ПОБЕДА:
            # Этот случай нам не подходит
            return False

        # Если мы достигли нужного количества ходов
        if r == 3:
            # Нужно проверить, победил ли нужный нам игрок
            return x + y >= ПОБЕДА

        # Стратегия для наихудших ходов противника
        return any(f(op(x), y, r + 1) for op in ОПЕРАЦИИ) or any(
            f(x, op(y), r + 1) for op in ОПЕРАЦИИ
        )

    print(
        "Answer:",
        next(x for x in range(1, ПОБЕДА - ПЕРВАЯ_КУЧА) if f(x, ПЕРВАЯ_КУЧА)),
    )


# endregion: logic

if __name__ == "__main__":
    main()
