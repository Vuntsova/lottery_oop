# lottery_oop

# Test Cases
 Test Get Answer - RUN TEST
def test_get_answer():
    l = Lottery(numbers=[9])
    assert l.get_answer() is not None
    assert l.get_answer() == 9
 Test Random Range - RUN TEST
def test_random_range():
    l = Lottery()
    assert l.get_answer() is not None
    assert l.play(l.get_answer()) is True
 Test Play - RUN TEST
def test_play():
    l = Lottery(numbers=[9])
    assert l.play(1) is False
    assert l.play(9) is True
