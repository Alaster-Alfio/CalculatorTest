from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected

    def test_divide_one(self):
        # arrange
        a = 4444
        b = 1111
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected

def test_divide_two():
    # arrange
    a = 4444
    b = 0
    cal = Calculator()

    # act and assert
    try:
        cal.divide(a, b)
    except ZeroDivisionError:
        # If a ZeroDivisionError is raised, pass the test
        pass

