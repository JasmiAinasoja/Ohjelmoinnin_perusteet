########################################################
# Task A9_T7
# Developer Jasmi Ainasoja
# Date 2025-12-06
#########################################################


import sys
import os

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Synopsis (usage):")
    print("  python A9_T7.py <src_file> <dst_file>")

def copyFile(src_file: str, dst_file: str) -> None:
    proceed = False

    if os.path.exists(dst_file):
        answer = input('Destination file "{}" exists. Overwrite? (y/n): '.format(dst_file)).strip().lower()
        if answer in ("y", "yes"):
            proceed = True
        else:
            print("Copy canceled.")
            return
    else:
        proceed = True

    if proceed:
        try:
            print('Copying file "{}" to "{}".'.format(src_file, dst_file))
            with open(src_file, "r", encoding="utf-8") as src, open(dst_file, "w", encoding="utf-8") as dst:
                for line in src:
                    dst.write(line)
        except Exception as e:
            print("Error! Failed to copy file: {}".format(e))
            sys.exit(-1)

def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        showHelp()
        print("Program ending.")
        return

    src_file = sys.argv[1]
    dst_file = sys.argv[2]

    print('Source file "{}"'.format(src_file))
    print('Destination file "{}"'.format(dst_file))

    copyFile(src_file, dst_file)

    print("Program ending.")

if __name__ == "__main__":
    main()
