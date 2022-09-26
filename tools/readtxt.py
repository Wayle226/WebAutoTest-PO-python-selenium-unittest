def read_txt(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8")as f:
        return f.readlines()


if __name__ == '__main__':
    datas = read_txt("login.txt")
    arr_list = []
    for data in datas:
        arr_list.append(tuple(data.strip().split(",")))
    print(arr_list)
    # 写法：
    arr_list = []
    for data in read_txt("login.txt"):
        arr_list.append(tuple(data.strip().split(",")))
    print(arr_list)

