# region: input
ПОБЕДА = 68  # Сумма, нужная для победы
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]  # Операции (+1, +4, *5)
# endregion: input
# region: logic


def main():  # sourcery skip: assign-if-exp, reintroduce-else
    def f(x: int, r: int = 1) -> bool:
        # Если кто-то выиграл раньше, чем нужный ход
        if r < 4 and x >= ПОБЕДА:
            # Этот случай нам не подходит
            return False

        # Если мы достигли нужного количества ходов
        if r == 4:
            # Нужно проверить, победил ли нужный нам игрок
            return x >= ПОБЕДА

        # Стратегия для наихудших ходов противника
        cases = [f(op(x), r + 1) for op in ОПЕРАЦИИ]

        # Если ходим мы, то нужно, чтобы хотя бы один ход был победным
        # Если ходит противник, то нужно, чтобы все ходы были победными
        return any(cases) if r % 2 != 0 else all(cases)

    print("Answer:", "".join(str(x) for x in range(1, ПОБЕДА) if f(x)))


# endregion: logic

if __name__ == "__main__":
    main()
