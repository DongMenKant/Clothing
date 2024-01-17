def getValue():
    # 读取文件内容
    with open("select_item.txt", "r") as f:
        content = f.read()

    selected = int(content)
    return selected