const client = require("./client")

const selectSp = async () => {
    const sps = await client.sp.getStorageProviders();
    const finalSps = (sps ?? []).filter((v) => v?.description?.moniker !== 'QATest');
    const selectIndex = 0;
    const secondarySpAddresses = [
        ...finalSps.slice(0, selectIndex),
        ...finalSps.slice(selectIndex + 1),
    ].map((item) => item.operatorAddress);

    const selectSpInfo = {
        endpoint: finalSps[selectIndex].endpoint,
        primarySpAddress: finalSps[selectIndex]?.operatorAddress,
        sealAddress: finalSps[selectIndex].sealAddress,
        secondarySpAddresses,
    };
    return selectSpInfo;
};


module.exports = selectSp;