
def decompress(fname):

    import tarfile

    #fname = 'example/20211129_2021231.tar.gz' # Example on the latest (daily) package of XML files

    if fname.endswith("tar.gz"):

        tar = tarfile.open(fname, "r:gz")
        folder_name  = tar.getnames()[0]
        file_names = tar.getnames()[1:]
        tar.extractall('./') # maybe we can use an extraction folder if we want to decompress and combine multipe files
        tar.close()
        print("File was decompressed successfully")
        return file_names