const client = require("../client");
const selectSp = require("../spInfo");

async function createBucket(bucketName, type) {
    const spInfo = await selectSp();
    const createBucketTx = await client.bucket.createBucket({
        bucketName : bucketName,
        creator : process.env.ADDRESS,
        visibility : type.toLowerCase() === 'private' ? 'VISIBILITY_TYPE_PUBLIC_READ' : 'VISIBILITY_TYPE_PRIVATE',
        chargedReadQuota : '0',
        spInfo
    });
    const simulateInfo = await createBucketTx.simulate({
        denom : "BNB"
    });
    const res = await createBucketTx.broadcast({
        denom: 'BNB',
        gasLimit: Number(simulateInfo?.gasLimit),
        gasPrice: simulateInfo?.gasPrice || '5000000000',
        payer: process.env.ADDRESS,
        granter: '',
        privateKey : `0x${process.env.PRIVATE_KEY}`
    });

    if (res.code === 0) {
        return {
            msg: "",
            data: res
        };
    }
}

module.exports = createBucket;