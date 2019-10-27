class Clock(object):

    minutes = 0
    reset_value = 24 * 60

    def __init__(self, hour, minute):
        self.minutes = hour * 60 + minute
        self.keep_in_24_hour_format()

    @property
    def hour(self):
        return self.minutes // 60

    @property
    def minute(self):
        return self.minutes % 60

    def keep_in_24_hour_format(self):
        if self.minutes >= self.reset_value:
            self.minutes = self.minutes % self.reset_value
        if self.minutes < 0:
            self.minutes = self.reset_value - ((self.minutes * -1) % self.reset_value)

    def __repr__(self):
        msg = '{hour}:{minute}'.format(hour=str(self.hour).zfill(2), minute=str(self.minute).zfill(2))
        return msg

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        self.minutes += minutes
        self.keep_in_24_hour_format()
        return self

    def __sub__(self, minutes):
        self.minutes -= minutes
        self.keep_in_24_hour_format()
        return self
