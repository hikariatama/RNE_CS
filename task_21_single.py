# region: input
ПОБЕДА = 42  # Сумма, нужная для победы
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 3, lambda x: x * 2]  # Операции (+1, +3, *2)
# endregion: input
# region: logic


def main():  # sourcery skip: assign-if-exp, reintroduce-else
    def f(x: int, r: int = 1, guaranteed_win: bool = False) -> bool:
        # Если мы достигли нужного количества ходов и победили
        if ((r == 3) if guaranteed_win else (r in {3, 5})) and x >= ПОБЕДА:
            return True

        # Если мы достигли максимального хода, но не победили
        if ((r == 3) if guaranteed_win else (r == 5)) and x < ПОБЕДА:
            return False

        # Если кто-то выиграл раньше, чем нужный ход
        if ((r < 3) if guaranteed_win else (r < 5)) and x >= ПОБЕДА:
            # Этот случай нам не подходит
            return False

        # Стратегия для наихудших ходов противника
        cases = [f(op(x), r + 1, guaranteed_win=guaranteed_win) for op in ОПЕРАЦИИ]

        # Если ходим мы, то нужно, чтобы хотя бы один ход был победным
        # Если ходит противник, то нужно, чтобы все ходы были победными
        return any(cases) if r % 2 == 0 else all(cases)

    print(
        "Answer:",
        next(x for x in range(1, ПОБЕДА) if f(x) and not f(x, guaranteed_win=True)),
    )


# endregion: logic

if __name__ == "__main__":
    main()
