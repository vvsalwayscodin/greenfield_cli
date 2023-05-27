const client = require("../client");

async function getBucketByName(bucketName){
    const bucketInfo = await client.bucket.headBucket(bucketName);
    return {
        msg : "Bucket info successfully got",
        data : bucketInfo
    };
}

module.exports = getBucketByName;