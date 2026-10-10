# 1. 把5道题存进一个字典列表里
questions = [
    {
        "q": "离岛免税政策适用人群为多少周岁以上？",
        "options": ["1. 16","2. 18","3. 20"],
        "answer": "2",
        "explanation": "根据最新政策，离岛免税购物年龄已由年满16周岁调整为年满18周岁。"
    },
    {
        "q": "离岛旅客每年每人免税购物额度为多少人民币？",
        "options": ["1. 5万元", "2. 10万元", "3. 20万元"],
        "answer": "2",
        "explanation": "（2）离岛旅客每年每人免税购物额度为10万元人民币，不限次数。"
    },
    {
        "q": "离岛免税政策是否适用于海南省居民？",
        "options": ["1. 是","2. 否"],
        "answer": "1",
        "explanation": "该政策适用于离开海南本岛但不离境的国内外旅客，包括海南省居民。"
    },
    {
        "q": "离岛免税政策免税税种为哪三样？",
        "options": ["1. 印花税、资源税和土地增值税‌","2. 企业税、个人税和企业税","3. 关税、进口环节增值税和消费税"],
        "answer": "3",
        "explanation": "离岛免税政策免税税种为关税、进口环节增值税和消费税。"
    },
    {
        "q": "手机、手持（包括车载）式无线电话机每次限购几件？",
        "options": ["1. 4","2. 5","3. 6"],
        "answer": "1",
        "explanation": "手机、手持（包括车载）式无线电话机每次限购4件。"
    }
]

# 2. 初始化得分
while True:
    score = 0

    # 3. 用 for 循环出题
    for item in questions:
        print("---")
        print(item["q"])
        for opt in item["options"]:
            print(opt)

        answer = input("请输入你的答案：")

        if answer == item["answer"]:
            print("回答正确！")
            print("答案：" + item["answer"])
            print("解析：" + item["explanation"])
            score = score + 1
        else:
            print("回答错误")
            print("正确答案是：" + item["answer"])
            print("解析：" + item["explanation"])

    # 4. 打印最终得分
    print("===================")
    print("答题结束，你的总分是：" + str(score) + "分")

    # 5. 根据得分给出评语
    if score == 5:
        print("评语：满分！你已经是反走私小专家了！")
    elif score >= 3:
        print("评语：不错哦，基本了解反走私知识，继续加油！")
    else:
        print("评语：看来还需再学习一下反走私知识哦，再挑战一次吧！")

    # 6. 询问是否再来一轮
    again = input("是否再来一轮？（输入 y 重新开始，输入其他任意键退出）：")
    if again.lower() != "y":
        print("感谢参与，再见！")
        break # 负责彻底结束 while 循环，退出程序