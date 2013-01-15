import os


class FileScanner():

    paths = []

    def __init__(self, ext_list=[]):

        self.ext_list = ext_list if ext_list else []

    def scan(self, path):

        file_list = os.listdir(path)

        #Scanning the whole contents of the folder
        allpaths = [os.path.join(path, name) for name in file_list \
                    if ".%s" % os.path.join(path, name).lower().\
                    split(".")[-1] in self.ext_list]

        #Selecting only folders
        subdirs_paths = [os.path.join(path, name) for name in file_list \
                         if os.path.isdir(os.path.join(path, name))]

        #Adding to the list of the paths
        self.paths.extend(allpaths)

        #Applying the same scheme to the subfolders
        for subdir in subdirs_paths:
            self.scan(subdir)

        return self.paths


def mean_line_len_of_file(path):

    with open(path) as f:
        lengths = []
        lines_cnt = 0

        for line in f:
            lines_cnt += 1
            lengths.append(len(line))

    if lines_cnt:
        return sum(lengths) / lines_cnt
    else:
        return None


if __name__ == '__main__':

    means = []
    fs = FileScanner([".py"])
    paths = fs.scan("/home/folder1/folder2")

    for path in paths:
        mean = mean_line_len_of_file(path)

        if mean:
            means.append(mean)

    if len(means):
        print(sum(means) / len(means))
