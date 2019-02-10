# lottery_oop

# Test Cases
def test_random_range():<br />
        l = Lottery()<br />
        assert l.get_answer() is not None<br />
        assert l.play(l.get_answer()) is True<br />
