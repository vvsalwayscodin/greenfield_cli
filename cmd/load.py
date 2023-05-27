import execjs

# Load the JavaScript library
with open('../node/node_modules/@bnb-chain/greenfield-chain-sdk', 'r') as file:
    sdk_code = file.read()

# Create an execution context
ctx = execjs.compile(sdk_code)


