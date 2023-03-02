import task_2
import task_15
import task_19_single
import task_20_single
import task_21_single
import task_19_multi
import task_20_multi
import task_21_multi


def test_task_19_single(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_19_single.ПОБЕДА = 68
    task_19_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]
    task_19_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 3"

    task_19_single.ПОБЕДА = 48
    task_19_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 2]
    task_19_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 12"

    task_19_single.ПОБЕДА = 42
    task_19_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 3, lambda x: x * 2]
    task_19_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 11"


def test_task_20_single(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_20_single.ПОБЕДА = 68
    task_20_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]
    task_20_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 912"

    task_20_single.ПОБЕДА = 48
    task_20_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 2]
    task_20_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 1922"

    task_20_single.ПОБЕДА = 42
    task_20_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 3, lambda x: x * 2]
    task_20_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 101719"


def test_task_21_single(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_21_single.ПОБЕДА = 68
    task_21_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 5]
    task_21_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 8"

    task_21_single.ПОБЕДА = 48
    task_21_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 4, lambda x: x * 2]
    task_21_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 18"

    task_21_single.ПОБЕДА = 42
    task_21_single.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x + 3, lambda x: x * 2]
    task_21_single.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 16"


def test_task_19_multi(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_19_multi.ПОБЕДА = 77
    task_19_multi.ПЕРВАЯ_КУЧА = 7
    task_19_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]
    task_19_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 18"

    task_19_multi.ПОБЕДА = 61
    task_19_multi.ПЕРВАЯ_КУЧА = 3
    task_19_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_19_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 4"

    task_19_multi.ПОБЕДА = 82
    task_19_multi.ПЕРВАЯ_КУЧА = 4
    task_19_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_19_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 5"


def test_task_20_multi(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_20_multi.ПОБЕДА = 77
    task_20_multi.ПЕРВАЯ_КУЧА = 7
    task_20_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]
    task_20_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 3134"

    task_20_multi.ПОБЕДА = 61
    task_20_multi.ПЕРВАЯ_КУЧА = 3
    task_20_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_20_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 1214"

    task_20_multi.ПОБЕДА = 82
    task_20_multi.ПЕРВАЯ_КУЧА = 4
    task_20_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_20_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 1619"


def test_task_21_multi(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_21_multi.ПОБЕДА = 77
    task_21_multi.ПЕРВАЯ_КУЧА = 7
    task_21_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 2]
    task_21_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 30"

    task_21_multi.ПОБЕДА = 61
    task_21_multi.ПЕРВАЯ_КУЧА = 3
    task_21_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_21_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 13"

    task_21_multi.ПОБЕДА = 82
    task_21_multi.ПЕРВАЯ_КУЧА = 4
    task_21_multi.ОПЕРАЦИИ = [lambda x: x + 1, lambda x: x * 4]
    task_21_multi.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 18"


def test_task_2(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_2.ИЗВЕСТНЫЕ = [[..., 0, 0, 0], [..., 0, ..., 0]]
    task_2.ПЕРЕМЕННЫЕ = "xyz"
    task_2.ФУНКЦИЯ = lambda x, y, z: (z == x) ** (x or y)
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: xzy"

    task_2.ПЕРЕМЕННЫЕ = "xyzw"
    task_2.ИЗВЕСТНЫЕ = [
        [1, 1, 1, 0, 1],
        [..., ..., 0, 0, 0],
        [..., 0, ..., ..., 0],
    ]
    task_2.ФУНКЦИЯ = lambda x, y, z, w: (((not y) ** w) and x ** y) ** (x != z)
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: yzxw"

    task_2.ПЕРЕМЕННЫЕ = "xyzw"
    task_2.ИЗВЕСТНЫЕ = [
        [1, ..., ..., 1, 0],
        [1, ..., ..., ..., 0],
        [..., 1, ..., 1, 0],
    ]
    task_2.ФУНКЦИЯ = lambda x, y, z, w: ((y**x) and (w**y)) or (z == (x or y))
    task_2.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: ywzx"


def test_task_15(capfd):
    # sourcery skip: extract-duplicate-method, move-assign-in-block
    task_15.ПЕРЕМЕННЫЕ = "x"
    task_15.ФУНКЦИЯ = lambda x, A: ((x & A != 0) ** (x & 12 == 0)) ** (x & 29 != 0)
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = False
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 17"

    task_15.ПЕРЕМЕННЫЕ = "x"
    task_15.ФУНКЦИЯ = lambda x, A: ((x & A != 0) ** (x & 17 == 0)) ** (x & 25 != 0)
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = False
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 8"

    task_15.ПЕРЕМЕННЫЕ = "x"
    task_15.ФУНКЦИЯ = lambda x, A: ((x & A != 0) ** (x & 33 == 0)) ** (x & 41 != 0)
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = False
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 8"

    task_15.ПЕРЕМЕННЫЕ = "x"
    task_15.ФУНКЦИЯ = lambda x, A: x & 51 == 0 or ((x & A == 0) ** (x & 41 == 0))
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = True
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 41"
