import os
import time

list_load = ['10%', '50%', '90%']
def loading():
    for j in range(3):
        print("Loading " + list_load[j])
        time.sleep(1)

def rename_files():
    path = input("File path - ")  # File path (example - C:\Users\Admin\Desktop)
    name = input("Name file - ")  # Name file (example - img)
    name_l = len(name)  # Text length
    name_end = name[:name_l - 1]  # Slicing text
    formatn = input("File type - ")  # File type (example - jpg)
    n = int(input("Number of files - "))  # Number of files
    for i in range(1, n + 1):
        try:
            if i < 10:
                os.rename(r"{}\{}.{}".format(path, name_end + str(i), formatn),
                          r"{}\{}.{}".format(path, str(i), formatn))  # Rename
            else:
                try:
                    name_end = name[:name_l - 2]  # Slicing text
                    os.rename(r"{}\{}.{}".format(path, name_end + str(i), formatn),
                              r"{}\{}.{}".format(path, str(i), formatn))  # Rename
                except:
                    name_end = name[:name_l - 1]  # Slicing text
                    os.rename(r"{}\{}.{}".format(path, name_end + str(i), formatn),
                              r"{}\{}.{}".format(path, str(i), formatn))  # Rename
        except:
            print("Error 0_o")  # Error
    loading()


def main():
    rename_files()
    print("Program complete - 100% ")
    print(10 * '-' + "by Quanta / Deffryda" + 10 * '-')
    print("https://github.com/Deffryda")


if __name__ == "__main__":
    main()
