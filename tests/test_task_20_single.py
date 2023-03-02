from RNE_CS import task_20_single


def test_task_20_single(capfd):  # sourcery skip: extract-duplicate-method
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
