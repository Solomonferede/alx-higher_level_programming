#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as pyc
    name = dir(pyc)
    for i in range(0, len(name)):
        if name[i][0:2] != '__':
            print(name[i])
