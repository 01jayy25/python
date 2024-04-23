# television.py

class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 10

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = 0
        self._channel = 0

    def power(self) -> None:

        self._status = not self._status

    def mute(self) -> None:

        self._muted = not self._muted
        if self._muted:
            self._volume = 0

    def channel_up(self) -> None:
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        if self._status:
            if self._muted:
                self._muted = False
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        if self._status:
            if self._muted:
                self._muted = False
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        return f"Power - [{self._status}], Channel - [{self._channel}], Volume - [{self._volume}]"

# Assertions for testing
if __name__ == "__main__":
    tv = Television()

    assert tv._status == False
    assert tv._muted == False
    assert tv._volume == 0
    assert tv._channel == 0

    tv.power()
    assert tv._status == True

    tv.mute()
    assert tv._muted == True
    assert tv._volume == 0

    tv.mute()
    assert tv._muted == False

    tv.channel_up()
    assert tv._channel == 1

    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == 0

    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

    tv.volume_up()
    assert tv._volume == 1

    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME

    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME



