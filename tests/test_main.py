import pytest, os
from myproject.__main__ import main

def test_main_run(capsys):
    # Arrange
    # Act
    main('run', 'Ceci est un test')
    # Assert
    captured = capsys.readouterr()
    assert captured.out == "Results = Ceci\n"

def test_main_train(mocker):
    # Arrange
    mocker.patch('myproject.train_save.MODELPATH', 'tests/data/model.txt')
    try:
        os.remove('tests/data/model.txt')
    except FileNotFoundError:
        pass
    # Act
    main('train','Ceci est un test')
    # Assert
    with open('tests/data/model.txt') as file:
        assert file.read() == 'Ceci est un test'