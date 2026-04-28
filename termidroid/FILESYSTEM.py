VFS = {
    "/home": {},
    "/bin": {},
    "/pkg": {},
    "/plugins": {}
}

def ls(folder):
    return list(VFS.get(folder, {}).keys())

def write(path, content):
    folder, file = path.rsplit("/", 1)
    if folder in VFS:
        VFS[folder][file] = content

def read(path):
    folder, file = path.rsplit("/", 1)
    return VFS.get(folder, {}).get(file, None)
