const client = require("../client");

async function getBucketById(bucketId){
    const bucketInfo = await client.bucket.headBucketById(bucketId);
    return {
        msg: "Bucket info successfully got",
        data: bucketInfo
    };
}

module.exports = getBucketById;