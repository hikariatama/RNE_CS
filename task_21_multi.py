# region: input
ПОБЕДА = 77  # Сумма, нужная для победы
ПЕРВАЯ_КУЧА = 7  # Кол-во камней в первой куче
ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]  # Операции (+1, *2)
# endregion: input
# region: logic


def main():
    def f(x: int, y: int, r: int = 1, guaranteed_win: bool = False) -> bool:
        # Если мы выиграли на третьем или пятом ходе
        if ((r == 3) if guaranteed_win else (r in {3, 5})) and x + y >= ПОБЕДА:
            # Этот случай нам подходит
            return True

        # Если мы не выиграли к пятому ходу
        if ((r == 3) if guaranteed_win else (r == 5)) and x + y < ПОБЕДА:
            # Этот случай нам не подходит
            return False

        if ((r < 3) if guaranteed_win else (r < 5)) and x + y >= ПОБЕДА:
            # Мы победили не на 3 или 5 ходе, либо победил соперник
            return False

        # Возможные исходы
        cases = [
            *(f(op(x), y, r + 1, guaranteed_win=guaranteed_win) for op in ОПЕРАЦИИ),
            *(f(x, op(y), r + 1, guaranteed_win=guaranteed_win) for op in ОПЕРАЦИИ),
        ]

        # Если ход наш, то мы ищем, чтобы хотя бы один исход был победным
        # Если ход противника, то мы проверяем, чтобы все исходы подходили
        return all(cases) if r % 2 != 0 else any(cases)

    print(
        "Answer:",
        next(
            x
            for x in range(1, ПОБЕДА - ПЕРВАЯ_КУЧА)
            if f(x, ПЕРВАЯ_КУЧА) and not f(x, ПЕРВАЯ_КУЧА, guaranteed_win=True)
        ),
    )


# endregion: logic

if __name__ == "__main__":
    main()
