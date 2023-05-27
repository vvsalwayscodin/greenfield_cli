const client = require("../client");

async function getProviderPrice(address){
    const price = await client.sp.getStoragePriceByTime(address);
    return {
        msg : "Price for specific storage provider is successfully got",
        data : {readPrice : price.readPrice, storePrice : price.storePrice}
    }
}

module.exports = getProviderPrice;