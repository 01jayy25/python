

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def channel_up(self):
        if self._status:
            self._channel = (self._channel % self.MAX_CHANNEL) + 1

    def channel_down(self):
        if self._status:
            self._channel = (self._channel - 1) % self.MAX_CHANNEL

    def volume_up(self):
        if self._status:
            if not self._muted:
                self._volume = min(self._volume + 1, self.MAX_VOLUME)
            else:
                self._muted = False

    def volume_down(self):
        if self._status:
            if not self._muted:
                self._volume = max(self._volume - 1, self.MIN_VOLUME)
            else:
                self._muted = False

    def __str__(self):
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
