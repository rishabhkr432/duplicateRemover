import hashlib
import os
import yaml
config = "config.yaml"

config_import = "./config.yaml"



# Returns the hash string of the given file name
with open(config_import, "r") as config_file:
    config = yaml.safe_load(config_file)

def hashFile(filename):
    # For large files, if we read it all together it can lead to memory overflow, So we take a blocksize to read at a time
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        # Reads the particular blocksize from file
        buf = file.read(config['BLOCKSIZE'])
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(config['BLOCKSIZE'])
    return hasher.hexdigest()


if __name__ == "__main__":
    # Dictionary to store the hash and filename
    hashMap = {}

    # List to store deleted files
    deletedFiles = []
    filelist = [f for f in os.listdir() if os.path.isfile(f)]
    for f in filelist:
        key = hashFile(f)
        # If key already exists, it deletes the file
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)
        else:
            hashMap[key] = f
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')