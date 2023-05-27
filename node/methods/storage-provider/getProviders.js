const client = require("../client");

async function getProviders(){
    const providers = await client.sp.getStorageProviders()
    return {
      msg : "Providers successfully got",
      data : providers
    };
}

module.exports = getProviders;