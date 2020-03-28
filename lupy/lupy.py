"""Tools collection"""
from lupy.modules import *


def array2csv(array: list, header: list = None) -> list:
    """ translate a 2d array in a 2d csv array
    :param array: list
    :param header: list
    :return: list
    """
    if not check_types(array, list):
        raise InvalidOperation('the array must be 2d array')
    lst = [list2csv(row) for row in array]
    if header:
        try:
            header = list2csv(header)
            lst.insert(0, header)
        except InvalidHeader:
            header = None
    return lst


def check_anagram(word1: str, word2: str) -> bool:
    """Checking if two words are anagrams:"""
    return Counter(word1) == Counter(word2)


def check_types(lst: list, model_type: type = None) -> bool:
    """Checks if the items in a list are all of the same type
        """
    if not lst:
        raise InvalidOperation('the list has no length')
    if not model_type:
        first = type(lst[0])
    else:
        first = model_type
    for item in lst:
        if type(item) != first:
            return False
    return True


def create_temp_folder(*args, first_folder='minio') -> str:
    """
    create temp folder recursively into os default.
    if already present the tree will be erased
    before recreating
    example:
    c:\\Windows\\Temp\\minio\\input\\1303
    :param args: list of folders
    :param first_folder: first folder of the tree
    :return: last folder path as str
    """
    system_tmp = tempfile.gettempdir()
    folders = [system_tmp, first_folder] + [*args]
    temp_folder = os.path.join(*folders)
    try:
        os.makedirs(temp_folder)
        return temp_folder
    except FileExistsError:
        try:
            print(f'recreating folder {temp_folder}')
            shutil.rmtree(temp_folder, ignore_errors=True)
            return create_temp_folder(*args)
        except FileNotFoundError as err:
            pass
    except OSError as err:
        print(err)


def files_insubs(dirName):
    """List all the files in directories and subs"""
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + files_insubs(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def list2csv(items: list) -> str:
    """Convert list to CSV"""
    if not check_types(items) or type(items[0]) is not str:
        try:
            return ','.join(map(str,items))
        except Exception as error:
            raise InvalidOperation(error)
    return ','.join(items)


def min_or_max_index(lst: list, _min=None, _max=None):
    """Find Index of Min/Max element in al list"""
    if not _min and not _max:
        _min = True
        _max = False
    elif _max is not None:
        _min = not _max
    return min(range(len(lst)), key=lst.__getitem__) if _min else max(range(len(lst)), key=lst.__getitem__)


def most_freq_val(lst: list = None) -> list:
    """Find the most frequent element in a list:"""
    if not lst:
        lst = [1,1,2,2,2,4,5,5,6,6,7,7,7,7,7]
    cnt = Counter(lst)
    return cnt.most_common(3)


def recursive_split(path):
    """
    split a path recursively
    :param path: path
    :return: tuple
    """
    rest, tail = os.path.split(path)
    if rest == '':
        return tail,  # return a tuple
    return recursive_split(rest) + (tail,)


def remove_duplicates(lst: list):
    """Remove duplicates from a list
        while keeping order"""
    lst = list(OrderedDict.fromkeys(lst).keys())
    return lst


def remove_tmp(target='minio'):
    """
    remove folder tree from the filesystem
    """
    try:
        system_tmp = tempfile.gettempdir()
        tmp_folder = os.path.join(system_tmp, target)
        shutil.rmtree(tmp_folder, ignore_errors=True)
    except OSError as err:
        print(err)


def sort_dict_vals(dic: dict) -> dict:
    """Sort dict by value

    d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
    print(sorted(d.items(), key=lambda x: x[1]))

    # using operator.itemgetter instead of a lambda

    print(sorted(d.items(), key=itemgetter(1)))

    # sort dict keys by value
    print(sorted(d.items(), key=d.get))
    """
    return {k: val for k, val in sorted(dic.items(), key=lambda x: x[1])}


def trans_2d_array(array: list):
    """Transpose 2D array
        [['a', 'b'], ['c', 'd',], ['e', 'f']] --> [['a', 'c', 'e'], ['b', 'd', 'f']]"""
    #
    array = [['a', 'b'], ['c', 'd',], ['e', 'f']]
    return zip(*array)
