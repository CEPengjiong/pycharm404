# 随机获取手机号
import random


def random_phone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    random_phone = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
    return random_phone
