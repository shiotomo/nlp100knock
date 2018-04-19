import re

def ngram(data, mode):
    if mode == "char":
        split_data = re.sub(" ", "", data)
        split_data = list(split_data)

        # print(split_data)

        for i in range(len(split_data) - 1):
            tmp = split_data[i] + split_data[i + 1]
            print(tmp)

    elif mode == "word":
        split_data = data.split()
        for i in range(len(split_data) - 1):
            tmp = split_data[i] + split_data[i + 1]
            print(tmp)


# Start
data = "I am an NLPer"

# 文字バイアグラム
ngram(data, "char")

# 単語バイアグラム
ngram(data, "word")
