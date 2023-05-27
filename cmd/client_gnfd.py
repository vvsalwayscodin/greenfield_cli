# ParseBucket parse the bucket-name from url
def parse_bucket(url_path):
    if "gnfd://" in url_path:
        url_path = url_path.replace("gnfd://", "")

    splits = url_path.split("/", 1)

    return splits[0]
