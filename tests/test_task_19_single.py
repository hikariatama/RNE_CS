from RNE_CS import task_19_single


def test_task_19_single(capfd):  # sourcery skip: extract-duplicate-method
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
