import os
import shutil
import sys


# Search Directory
def search_dir(dirname):
    result_list = []
    filenames = os.listdir(dirname)

    for filename in filenames:
        full_path = os.path.join(dirname, filename)

        if os.path.isdir(full_path):
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)

    return result_list


# Prograss Bar
def printProgress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' %
                     (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


lists = search_dir(os.path.realpath(__file__)[:-7])
dest = os.path.realpath(__file__)[:-7] + "Videos"

if not(os.path.isdir(dest)):
    os.makedirs(dest)

# 파일 이동
for i, list in enumerate(lists):
    printProgress(i, len(lists), 'Progress:', 'Complete', 1, 50)
    if list.endswith(".py"):
        continue

    if list.endswith(".mp4"):
        try:
            shutil.move(list, dest)
        except:
            continue
