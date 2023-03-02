from RNE_CS import task_21_single


def test_task_21_single(capfd):  # sourcery skip: extract-duplicate-method
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
