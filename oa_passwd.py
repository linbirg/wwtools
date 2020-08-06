## 打印指定日期是一年中的第几周，默认当前日期

import random

numbers = '0123456789'
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
specials = '!~@_&'

all_characters = [numbers, characters, specials]


def random_pick(some_list, probabilities):
    '''
    根据概率随机挑选
    '''
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def random_char():
    item = random_pick(all_characters, [0.3, 0.6, 0.1])
    return item[random.randint(0, len(item) - 1)]


def gen_rand_pwd():
    pw_str = ''
    pw_len = 12

    for _ in range(pw_len):
        pw_str += random_char()

    return pw_str


if __name__ == '__main__':
    passwd = gen_rand_pwd()
    print('passwd:', passwd)
