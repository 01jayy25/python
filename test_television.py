import test.py
from television import Television

def test_power():
    tv = Television()
    assert not tv._status
    tv.power()
    assert tv._status

def test_channel_up():
    tv = Television()
    tv.power()
    assert tv._channel == tv.MIN_CHANNEL
    tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL + 1



if __name__ == "__main__":
    pytest.main()
