import task_2, task_19

def test_task_19(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_19.ПОБЕДА = 77
    task_19.ПЕРВАЯ_КУЧА = 7
    task_19.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]
    task_19.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 18"

    task_19.ПОБЕДА = 61
    task_19.ПЕРВАЯ_КУЧА = 3
    task_19.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_19.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 4"

    task_19.ПОБЕДА = 82
    task_19.ПЕРВАЯ_КУЧА = 4
    task_19.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_19.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 5"


def test_task_2(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_2.ИЗВЕСТНЫЕ = [
        [..., 0, 0, 0],
        [..., 0, ..., 0]
    ]
    task_2.ПЕРЕМЕННЫЕ = "xyz"
    task_2.ФУНКЦИЯ = lambda x, y, z: int((z == x) ** (x or y))
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: xzy"

    task_2.ПЕРЕМЕННЫЕ = "xyzw"
    task_2.ИЗВЕСТНЫЕ = [
        [1, 1, 1, 0, 1],
        [..., ..., 0, 0, 0],
        [..., 0, ..., ..., 0],
    ]
    task_2.ФУНКЦИЯ = lambda x, y, z, w: int((((not y) ** w) and x ** y) ** ((not x) == (not not z)))
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: yzxw"

    task_2.ПЕРЕМЕННЫЕ = "xyzw"
    task_2.ИЗВЕСТНЫЕ = [
        [1, ..., ..., 1, 0],
        [1, ..., ..., ..., 0],
        [..., 1, ..., 1, 0],
    ]
    task_2.ФУНКЦИЯ = lambda x, y, z, w: int(((y ** x) and (w ** y)) or (z == (x or y)))
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: ywzx"


