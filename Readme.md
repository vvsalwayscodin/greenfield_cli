# greenfield-cmd

---
Greenfield client cmd tool, supporting commands to make requests to greenfield


## Disclaimer
**The software and related documentation are under active development, all subject to potential future change without
notification and not ready for production use. The code and security audit have not been fully completed and not ready
for any bug bounty. We advise you to be careful and experiment on the network at your own risk. Stay safe out there.**

## Cmd usage

### installation
```
git clone https://github.com/vvsalwayscodin/greenfield_cli
cd greenfield_cli

# create vitrual machine
virtualenv venv

# activate venv

# On Unix-like systems (e.g., Linux, macOS), 
source venv/bin/activate
# On Windows
venv/Scripts/activate

# after successfull activation of VM
pip install --editable .

# use cli 
gnfd --help
```

### basic config 
The default config file is ".env".

Below is an example of the config file. The rpcAddr and chainId should be consistent with the Greenfield network.
For Greenfield Testnet, you can refer to [Greenfield Testnet RPC Endpoints](https://greenfield.bnbchain.org/docs/guide/resources.html#rpc-endpoints).
The rpcAddr indicates the Tendermint RPC address with the port info.
The configuration for passwordFile is the path to the file containing the password required to generate or parse the keystore.
Users need to set the password on passwordFile before running commands and the password can be any random string.
```
rpcAddr = "https://gnfd-testnet-fullnode-tendermint-us.bnbchain.org:443"
chainId = "greenfield_5600-1"
passwordFile = "password.txt"
```
or set it by CLI
```
gnfd config --help
```
