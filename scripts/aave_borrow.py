from scripts.helpers import get_account
from scripts.get_weth import get_weth
from brownie import config,network

def main():
    account = get_account()
    weth_address = config["networks"][network.show_active()]["weth_token"]
    if(network.show_active() in ["mainnet-fork"]):
        get_weth()
    
