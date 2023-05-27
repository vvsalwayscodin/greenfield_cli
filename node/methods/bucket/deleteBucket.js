const client = require("../client");
async function deleteBucket(bucketName){

    const deleteBucketTx = await client.bucket.deleteBucket({
        bucketName: bucketName,
        operator: process.env.ADDRESS,
    });
    const simulateInfo = await deleteBucketTx.simulate({
        denom: 'BNB',
    });

    const res = await deleteBucketTx.broadcast({
        denom: 'BNB',
        gasLimit : Number(simulateInfo?.gasLimit),
        gasPrice: simulateInfo?.gasPrice || '5000000000',
        payer: process.env.ADDRESS,
        privateKey : `0x${process.env.PRIVATE_KEY}`,
        granter: '',
    });

    if (res.code === 0) {
        return {
            msg : "Bucket deleted successfully",
            data : res
        };
    }
}

module.exports =deleteBucket;