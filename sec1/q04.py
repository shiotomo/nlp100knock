data = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

data = data.split()
arr = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i in range(len(data)):
    flag = i + 1
    if flag in arr:
        ans = list(data[i])
        print(ans[0])
    else:
        ans = list(data[i])
        answer = ans[0] + ans[1]
        print(answer)

