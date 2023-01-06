import click

from brownie import Token, Vault, Registry, accounts, network, web3

def main():

    governance = accounts.load("seed-accounts")
    click.echo(f"You are using: 'dev' [{governance.address}] with balance {governance.balance()}")

    strategist = accounts.load("strategist")
    click.echo(
        f"You are using: 'dev' [{strategist.address}] with balance {strategist.balance()}"
    )

    strategy = '0xc4d80C55dc12FF0f2b8680eC31A6ADC4cbC8Dfca'
    Vault.at('0xdeD8B4ac5a4a1D70D633a87A22d9a7A8851bEa1b')

# addStrategy( strategy: address, debtRatio: uint256, minDebtPerHarvest: uint256, maxDebtPerHarvest: uint256, performanceFee: uint256)
   
    # tx = Vault[0].addStrategy(strategy,5000,0,3000000000000000000000000,0,{"from": governance})

    tx = Vault[0].addStrategy(strategy, 10000, 0, 2 ** 256 - 1, 0,{"from": governance})

    click.echo(f"tx: {tx}")

    click.echo(f"checking strategy: {Vault[0].strategies(strategy)}")

    Token.at('0x8e0B8c8BB9db49a46697F3a5Bb8A308e744821D2') #('0x6B175474E89094C44Da98b954EedeAC495271d0F')

    Token[0].balanceOf(strategist.address)

    Token[0].approve('0xdeD8B4ac5a4a1D70D633a87A22d9a7A8851bEa1b',5000000000000000000,{'from':strategist})

    Vault[0].deposit({'from':strategist}) 

    Token[0].balanceOf(strategist.address)