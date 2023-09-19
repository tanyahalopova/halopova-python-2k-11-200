import os


def pwd():
    print(os.getcwd())


def cd(dirname):
    try:
        os.chdir(dirname)
    except FileNotFoundError or NotADirectoryError:
        pass


def touch(filename):
    try:
        with open(filename, 'w'):
            pass
    except FileExistsError:
        pass


def cat(filename):
    try:
        newfile = os.path.join(os.getcwd(), filename)
        with open(newfile, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        pass


def ls():
    files = os.listdir()
    for file in files:
        print(file)


def rm(filename):
    try:
        os.remove(os.path.join(os.getcwd(), filename))
    except FileNotFoundError:
        pass


def main():
    while True:
        command = input("Введите команду: ")
        if command == "pwd":
            pwd()
        elif command.startswith("cd "):
            dirname = command.split(" ", 1)[1]
            cd(dirname)
        elif command.startswith("touch "):
            filename = command.split(" ", 1)[1]
            touch(filename)
        elif command.startswith("cat "):
            filename = command.split(" ", 1)[1]
            cat(filename)
        elif command == "ls":
            ls()
        elif command.startswith("rm "):
            filename = command.split(" ", 1)[1]
            rm(filename)
        elif command == "exit":
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()