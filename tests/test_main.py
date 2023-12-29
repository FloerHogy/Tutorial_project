import pytest
from myproject.__main__ import main

def test_main(capsys):
    main('Ceci est un test')
    captured = capsys.readouterr()
    assert captured.out == "Results = Ceci\n"