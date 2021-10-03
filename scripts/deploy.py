from brownie import accounts, FizzBuzz, network, config


def deplayFizzBuzz():
    if(network.show_active() != "development"):
        accounts.add(config["wallets"]["from_key"])

    FizzBuzz.deploy({"from": accounts[0]})


def getResults():
    fizzBuzz = FizzBuzz[-1]

    for index in range(100):
        result = fizzBuzz.CheckNumber(index)
        print(f"Number: {index} Result: {result}")


def main():
    deplayFizzBuzz()
    getResults()
