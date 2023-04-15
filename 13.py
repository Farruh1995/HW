#1.
# Implement a Counter class which optionally accepts the start value and the
# counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."

class Counter:
    def __init__(self, start=0, stop=None):
        self.counter = start
        self.stop = stop
    def increment(self):
        if self.stop is not None and self.counter >= self.stop:
            raise ValueError('Максимум.')
        self.counter += 1
    def get(self):
        return self.counter

#2.
# Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.


