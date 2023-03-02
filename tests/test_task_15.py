from RNE_CS import task_15


def test_task_15(capfd):  # sourcery skip: extract-duplicate-method
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
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = False
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 0"

    task_15.ПЕРЕМЕННЫЕ = "x"
    task_15.ФУНКЦИЯ = lambda x, A: x & 51 == 0 or ((x & A == 0) ** (x & 41 == 0))
    task_15.НАЙТИ_МАКСИМАЛЬНОЕ = True
    task_15.main()
    out = capfd.readouterr()[0].strip()
    assert out == "Answer: 41"
