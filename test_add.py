import pytest
from add import add

#every function that tests, has to begin with test_
@pytest.mark.parametrize("a,b,result", [(3, 5, 8)])
def test_add(a,b,result):
	c = add(a, b)
	assert c == result #assert is the keyword in python
