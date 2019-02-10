# lottery_oop

# Test Cases
def test_get_answer(): "\n"
    l = Lottery(numbers=[9])
    assert l.get_answer() is not None
    assert l.get_answer() == 9
