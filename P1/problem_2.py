import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths"""

    list_of_paths = []

    for i in os.listdir(path):
        x = os.path.join(path, i)
        #print(x)
        if os.path.isfile(x):
            #print("file", x)
            if x.endswith(suffix):
                #print("suffex winner", x)
                list_of_paths.append(x)
        if os.path.isdir(x):
            #print("dir", x)
            list_of_paths.extend(find_files(suffix, x))

    return(list_of_paths)
