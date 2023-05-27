import execjs

# Load the JavaScript library
with open('../node/output.js', 'r') as file:
    sdk_code = file.read()

# Create an execution context
ctx = execjs.compile(sdk_code)


