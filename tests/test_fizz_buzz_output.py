from brownie import FizzBuzz, accounts, network, config


def get_account():
    if network.show_active() != "development":
        accounts.add(config["wallets"]["from_key"])

    return accounts[0]

def test_no_output():
    account = get_account()
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 != 0 and index % 5 != 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == ""


def test_fizz_output():
    account = get_account()
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 == 0 and index % 5 != 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Fizz"


def test_buzz_output():
    account = get_account()
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 != 0 and index % 5 == 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Buzz"


def test_fizzbuzz_output():
    account = get_account()
    fizzBuzz = FizzBuzz.deploy({"from": account})

    for index in range(100):
        if index % 3 == 0 and index % 5 == 0:
            result = fizzBuzz.CheckNumber(index)
            assert result == "Fizz Buzz"
