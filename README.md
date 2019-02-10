# lottery_oop

## Test Cases
def test_get_answer():<br />
    &nbsp;&nbsp;l = Lottery(numbers=[9])<br />
    &nbsp;&nbsp;assert l.get_answer() is not None<br />
    &nbsp;&nbsp;assert l.get_answer() == 9<br />
    
def test_random_range():<br />
        l = Lottery()<br />
        assert l.get_answer() is not None<br />
        assert l.play(l.get_answer()) is True<br />
        
def test_play():<br />
    l = Lottery(numbers=[9])<br />
    assert l.play(1) is False<br />
    assert l.play(9) is True<br />
