import pytest
import student 



def test_lower(capsys):
    input_values=['3']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()

def test_exact(capsys):
    input_values=['18']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()

def test_lower_17(capsys):
    input_values=['17']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()
    
def test_higher(capsys):
    input_values=['80']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()

