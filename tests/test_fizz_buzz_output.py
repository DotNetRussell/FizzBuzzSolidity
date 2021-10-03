from brownie import FizzBuzz, accounts


def test_no_output():
    account = accounts[0]
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 != 0 and index % 5 != 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == ""


def test_fizz_output():
    account = accounts[0]
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 == 0 and index % 5 != 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Fizz"


def test_buzz_output():
    account = accounts[0]
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 != 0 and index % 5 == 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Buzz"


def test_fizzbuzz_output():
    account = accounts[0]
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 == 0 and index % 5 == 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Fizz Buzz"
