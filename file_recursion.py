
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
       a list of paths
    """
    result = []

    for f in os.listdir(path):
        fp = os.path.join(path, f)
        if os.path.isdir(fp):
            result += find_files(suffix, fp)
        elif os.path.isfile(fp) and fp.endswith(suffix):
            result.append(fp)
            
    return result

def test_suffix(suffix, files):
    for f in files:
        if not f.endswith(suffix):
            return False
    return True

def test_functions(basedir):
    # test files that end with .h
    files = find_files('.h', basedir)
    test_result = test_suffix('.h', files)
    print(f'Pass' if test_result else 'Fail')

    # test files that end with .md, which does not exist
    files = find_files('.md', basedir)
    test_result = test_suffix('.md', files)
    print(f'Pass' if test_result else 'Fail')

    # test files that end with .c
    files = find_files('.c', basedir)
    test_result = test_suffix('.md', files)
    print(f'Pass' if test_result else 'Fail')

if __name__ == "__main__":
    basedir = os.path.join(os.getcwd(), 'testdir')

    test_functions(basedir)

    files_c = find_files('.c', basedir)
    print(files_c)
