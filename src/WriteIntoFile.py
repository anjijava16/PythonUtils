def mainOne():
    f = open("E:/abhi.csv", "w+")
    for k in range(1000):
        #strOperation=k,"|",k + 1,"|",k + 2;
        f.write(str(k))
        f.write("\n");
        print(k)


if __name__ == "__main__":
    mainOne();
