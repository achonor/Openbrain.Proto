import os
import shutil
import sys


def main(sourceDir, targetDir):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        shutil.copy2(sourceFile, targetFile)

if ("__main__" == __name__):
    if (len(sys.argv) < 3):
        print("param need two")
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2])