# from maxoftwo import max
from questions.Q2 import max_of_three
from questions.Q4 import is_vowel
from questions.Q7 import reverse_string
from questions.Q9 import is_member
from questions.Q13 import maximuminlist
from questions.Q15 import longestLength

# def test_max_of_two():
#     result = max(1,2)
#     expected = 2
#     assert result == expected

def test_max_of_three():
    result = max_of_three(1,2,3)
    expected = 3
    assert result == expected

def test_is_vowel():
    result = is_vowel("h")
    expected = False
    assert result == expected


def test_reverse_string():
    result = reverse_string("Hello World")
    expected = "dlroW olleH"
    assert result == expected
    
def test_is_member():
    result = is_member(4, [5, 4,6])
    expected = True
    assert result == expected   
    
    
def test_maximuminlist():
    result = maximuminlist([34,56,88])
    expected = 88
    assert result == expected       
    
def test_longestLength():
    result = longestLength(["bountiess","milka", "python"])
    expected = 9
    assert result == expected  