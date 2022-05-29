class Counter:

    def __init__(self, minimal: int, maximal: int):
        self.minimal = minimal
        self.maximal = maximal
        self.current = minimal

    def increment(self):
        self.current += 1
        if self.current > self.maximal:
            self.current = self.minimal

    def __repr__(self):
        return f'Counter(minimal={self.minimal}, maximal={self.maximal}), current position={self.current}'


if __name__ == '__main__':
    counter = Counter(3, 100)
    print(counter)
    for _ in range(97):
        counter.increment()
        print(counter.current)
    print('Check resetting')
    counter.increment()
    print(counter.current)