import pytest
import my_module as m 
import numpy as np
def test_plot(capsys):
    f = np.sin
    xVals = np.linspace(0,2*np.pi,20)
    m.generate_plot(f,xVals)
    captured = capsys.readouterr()
    assert "Error" not in captured.err

def test_twosum():
    assert m.twoSum([3,3],6) == [0,1]

def test_getValue():
    c = m.Chooser([1,2,3])
    assert c.get_value() in [1,2,3]
