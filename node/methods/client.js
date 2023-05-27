const { Client } = require("@bnb-chain/greenfield-chain-sdk");

const client = Client.create(process.env.RPC_ADDR, process.env.CHAIN_ID);

module.exports = client;