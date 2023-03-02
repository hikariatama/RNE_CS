from RNE_CS import task_19_multi


def test_task_19_multi(capfd):  # sourcery skip: extract-duplicate-method
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
