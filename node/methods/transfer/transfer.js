const client = require("../client");

async function transfer(from_address, to_address, amount) {
    const transferTx = await client.account.transfer({
        fromAddress: transferInfo.to,
        toAddress: to_address,
        amount: [
            {
                denom: 'BNB',
                amount: amount
            },
        ],
    });
}

module.exports = transfer;