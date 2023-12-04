import hashlib


def create_has(string) -> list:
    has = list()
    string = string.encode('utf-8')

    hash_obj_sha1 = hashlib.sha1()
    hash_obj_sha1.update(string)
    size = hash_obj_sha1.digest_size
    hash_obj_sha1 = hash_obj_sha1.hexdigest()
    has.append('Hash in sha1: ' + hash_obj_sha1 + '\n' + 'Size: ' + str(size))

    hash_obj_sha224 = hashlib.sha224()
    hash_obj_sha224.update(string)
    size = hash_obj_sha224.digest_size
    hash_obj_sha224 = hash_obj_sha224.hexdigest()
    has.append('Hash in sha224: ' + hash_obj_sha224 + '\n' + 'Size: ' + str(size))

    hash_obj_sha256 = hashlib.sha256()
    hash_obj_sha256.update(string)
    size = hash_obj_sha256.digest_size
    hash_obj_sha256 = hash_obj_sha256.hexdigest()
    has.append('Hash in sha256: ' + hash_obj_sha256 + '\n' + 'Size: ' + str(size))

    hash_obj_sha384 = hashlib.sha384()
    hash_obj_sha384.update(string)
    size = hash_obj_sha384.digest_size
    hash_obj_sha384 = hash_obj_sha384.hexdigest()
    has.append('Hash in sha384: ' + hash_obj_sha384 + '\n' + 'Size: ' + str(size))

    hash_obj_sha512 = hashlib.sha512()
    hash_obj_sha512.update(string)
    size = hash_obj_sha512.digest_size
    hash_obj_sha512 = hash_obj_sha512.hexdigest()
    has.append('Hash in sha512: ' + hash_obj_sha512 + '\n' + 'Size: ' + str(size))

    return has


def create_has_sha1(string):
    string = string.encode('utf-8')

    hash_obj_sha1 = hashlib.sha1()
    hash_obj_sha1.update(string)
    hash_obj_sha1 = hash_obj_sha1.hexdigest()
    return hash_obj_sha1
