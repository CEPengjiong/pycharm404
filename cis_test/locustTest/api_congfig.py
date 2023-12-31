import time
import random
import os
import logging

# 获取根目录
baseDir = os.path.dirname(os.path.abspath(__file__))

# 10位时间戳
t = time.time()
_t = int(t)

# 2021-11-16 20:28:09 格式
visitTime = time.strftime('%Y-%m-%d %H:%M:%S')

# 生成随机手机号
str_start = random.choice(['131', '132', '135', '138', '151', '156', '157', '158', '171', '172', '173', '174', '175', '181', '182', '183', '186', '187', '188', '189', '199'])
str_end = ''.join(random.sample('0123456789', 8))
str_phone = str_start + str_end


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

# 随机取姓氏字典
def first_name():
    first_name_list = [
        '赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
        '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
        '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
        '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
        '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
        '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
        '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危',
        '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍',
        '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓',
        '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊',
        '於', '惠', '甄', '麴', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦',
        '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇',
        '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎',
        '蓟', '薄', '印', '宿', '白', '怀', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂',
        '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯',
        '相', '查', '後', '荆', '红', '游', '竺', '权', '逯', '盖', '益', '桓', '公', '晋', '楚', '闫', '法', '汝', '鄢', '涂',
        '钦', '归', '海', '帅', '缑', '亢', '况', '后', '有', '琴', '梁', '丘', '左', '丘', '商', '牟', '佘', '佴', '伯', '赏',
        '南', '宫', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '言', '福', '百', '家', '姓', '终']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def second_name():
    # 随机取数组中字符，取到空字符则没有second_name
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()

def create_name():
    name = first_name() + second_name() + last_name()
    return name


# 初始化项目日志
logPath = baseDir + "\logs\clinic-{}.logs".format(time.strftime('%Y%m%d-%H%M%S'))
# print('logPath:',logPath)

def init_log():
    """日志初始化配置"""
    # 创建日志器对象
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器对象  -控制台显示
    sh = logging.StreamHandler()
    # 处理器对象  -文件存储
    fh = logging.handlers.TimedRotatingFileHandler(logPath, backupCount=7, encoding="UTF-8")
    # 创建格式化器对象
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 将格式化器添加导处理器
    sh.setFormatter(logging.Formatter(fmt))
    fh.setFormatter(logging.Formatter(fmt))
    # 将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


