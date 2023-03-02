from RNE_CS import task_21_multi


def test_task_21_multi(capfd):  # sourcery skip: extract-duplicate-method
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
