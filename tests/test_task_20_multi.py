from RNE_CS import task_20_multi


def test_task_20_multi(capfd):  # sourcery skip: extract-duplicate-method
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
