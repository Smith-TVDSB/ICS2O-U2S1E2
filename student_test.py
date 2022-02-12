import pytest
import student 



def test_lower():
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
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[1].lower()

def test_exact():
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
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[1].lower()

def test_lower_17():
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
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[1].lower()

def test_higher():
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
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[1].lower()

#Standard test output ONLY (no input)
#No need for the if __name__ condition in the main code, but might as well when done so students get used to it.
"""def test_hello(capsys):
    import hello
    out,err = capsys.readouterr()
    assert out == "Hello world!\n" or "bye" in out, "Should read 'Hello world!' "
"""