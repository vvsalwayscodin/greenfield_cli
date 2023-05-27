const client = require("../client");

async function getSpecificProvider(address){
    const provider = await client.sp.getStorageProviderInfo(address);
    return {
        msg : "Specific provider successfully got",
        data : provider
    };
}

module.exports = getSpecificProvider;