"""Quick script to fizzbuzz"""
"""for i in range(1, 101):
    print_string = ''
    if i%3==0:
        print_string += "Fizz"
    if i%5==0:
        print_string += "Buzz"
    # if print_string:
    print(str(i), print_string)"""
# declarative paradigms
factors = [[3, 'Fizz'], [5, 'Buzz']]
fizzbuzz = lambda val: ''.join(text for factor, text in factors if val % factor == 0) or str(val)
outputs = map(fizzbuzz, range(1, 101))
print('\n'.join(outputs))

# imperative paradigms
class FizzBuzzer:
    def __init__(self, value, factor_mapping=None):
        self.value = value
        self.factor_mapping = factor_mapping

    def __mod__(self, div):
        return self.value % div

    def __str__(self):
        result = ''
        for factor, text in self.factor_mapping.items():
            if self % factor == 0:
                result += text

        if not result:
            result += str(self.value)

        return result


def fizzbuzz(factor_mapping, start, stop):
        return [FizzBuzzer(i, factor_mapping) for i in range(start, stop)]


fizzbuzz_factors = {
    3: 'Fizz',
    5: 'Buzz',
}

for val in fizzbuzz(fizzbuzz_factors, 1, 101):
    print(val)