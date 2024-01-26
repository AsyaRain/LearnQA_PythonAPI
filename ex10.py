def test_lenght():
    phrase = input("Set a phrase: ")

    assert len(phrase) <15, 'Длина > 15 символов'
