import re

def ngram(n, data):
    result = []
    len_data = len(list(data))

    for i in range(len_data):
        if i + n - 1 < len_data:
            result.insert(i, "".join(list(data)[i: i + n]))

    return result

def main():
    result = {}
    str1 = "paraparaparadise"
    str2 = "paragraph"
    x = ngram(2, str1)
    set_x = set(x)
    # print(x)
    # print(set_x)
    y = ngram(2, str2)
    set_y = set(y)
    # print(y)
    # print(set_y)
    result["or"] = list(set_x | set_y)
    result["and"] = list(set_x & set_y)
    result["diff"] = list(set_x - set_y)
    print(result["or"])
    print(result["and"])
    print(result["diff"])

if __name__== '__main__':
    main()
