# region: input
ПОБЕДА = 68  # Сумма, нужная для победы
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]  # Операции (+1, +4, *5)
# endregion: input
# region: logic


def main():  # sourcery skip: assign-if-exp, reintroduce-else
    def f(x: int, r: int = 1) -> bool:
        # Если кто-то выиграл раньше, чем нужный ход
        if r < 3 and x >= ПОБЕДА:
            # Этот случай нам не подходит
            return False

        # Если мы достигли нужного количества ходов
        if r == 3:
            # Нужно проверить, победил ли нужный нам игрок
            return x >= ПОБЕДА

        # Стратегия для наихудших ходов противника
        return any(f(op(x), r + 1) for op in ОПЕРАЦИИ)

    print("Answer:", next(x for x in range(1, ПОБЕДА) if f(x)))


# endregion: logic

if __name__ == "__main__":
    main()
