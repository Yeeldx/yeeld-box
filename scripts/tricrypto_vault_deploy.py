import click

from brownie import Token, Vault, Registry, accounts, network, web3

DEFAULT_VAULT_NAME = lambda token: f"{token.symbol()} yVault"
DEFAULT_VAULT_SYMBOL = lambda token: f"yv{token.symbol()}"


def main():

    rewards = "0x56a394cCa23c90EE1Ec39F05Abb1CA18C95bC4D4"
    token = Token.at("0x8e0B8c8BB9db49a46697F3a5Bb8A308e744821D2")  # Tricrypto

    governance = accounts.load("seed-accounts")
    click.echo(f"You are using: 'dev' [{governance.address}] with balance {governance.balance()}")

    vaultArgs = [
        token,
        governance.address,
        rewards,
        DEFAULT_VAULT_NAME(token),
        DEFAULT_VAULT_SYMBOL(token),
    ]
    vault = governance.deploy(Vault)
    vault.initialize(*vaultArgs)
    vault.setDepositLimit(10000000000000000000000)
    
    click.echo(f"Vault address: [{vault.address}]")

    vault.setManagement("0x7EE536e1FC3638EAdF5be06E8dCC562BDccBc340")

    # Make it so vault has some AUM to start
    #token.approve(vault, token.balanceOf(dev.address) // 2, {"from": dev})
    #click.echo(f"Token balance: [{token.balanceOf(dev.address)}]")
    #vault.deposit(token.balanceOf(dev.address) // 2, {"from": dev})

    vault.setGuardian("0x73d82dd7E3053Fd268F4ee3c1d61b0df9F233b12", {"from": governance})


