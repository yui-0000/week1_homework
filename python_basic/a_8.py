users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for user in users_info:
    # 変数に置き換えたほうがprint文で見やすい
    name = user[0]
    age = user[1]

    print(f"Name: {name}, Age: {age}")
