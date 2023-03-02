from RNE_CS import task_2


def test_task_2(capfd):  # sourcery skip: extract-duplicate-method
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
