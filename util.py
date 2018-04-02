# 实现文本快生成器把文本分成一个一个的文本块，以便接下来对每一个文本进行解析


def lines(file):
    # 生成器，在文本最后加一空行
    for line in file: yield line
    yield '\n'

def blocks(file):
    # 生成器，生成单独的文本块
    block = []
    for line in lines(file):
        if line.strip():
        # 如果line不是 空行
        # str.strip()可以取出字符串中前后的空格以及换行符，如果在strip()函数中添加不同的参数，
        # 如strip('a')，则可以取出字符串中前后的'a'字符
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
