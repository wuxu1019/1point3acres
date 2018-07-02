"""
用户从Alexa打电话  会说"Zero Eight Nine balabala" 我们希望翻译成"0 8 9 balabala"。 电话一定是10位，不考虑国际电话。 做一个translation。
   确定输入用空格隔开。  乍一看很简单对吧？ 诡异的来了。
   他说，有时候别人会写一些奇怪的service 来处理语音输入 所以有可能会变成"Zeeero, Eigght, N, balaba" 你一样要翻译成"0 8 9 baabala"。。。 所以其实就是有个容错机制问题。
   然后我就讨论了下这个机制。 他说要我自己设计，自己看着办。 我想的办法不是很好，一开始没意识到： 我说if A contains all B letters || B contains all A letters 我们会认为他们互相能够映射。 然后有个dic 进来 存的是 Zero TO Ten 和1 -10的Mapping. 这样能把用户的东西split开了做比对。 他们觉得不满意。
   想了很久以后我突然发现这个其实是Edit distance那题。 但是需要有个数据结构来处理String word, int Distance. 也就是记录某个单词和dic 里面的每一个word的距离， 返回以后用PriorityQueue 排序返回最近的距离的List<Distance>。
"""

def find_min_distance(word1, word2):

    C, R = len(word1), len(word2)
    dp = [[0] * (C+1) for _ in range(R+1)]

    for i in range(1, R+1):
        dp[i][0] = i

    for j in range(1, C+1):
        dp[0][j] = j

    for i in range(1, R+1):
        for j in range(1, C+1):

            if word2[i-1] == word1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
    return dp[-1][-1]


def analysis(string):

    candi = {'One':1,
             'Two':2,
             'Three':3,
             'Four':4,
             'Five':5,
             'Six':6,
             'Seven':7,
             'Eight':8,
             'Nine':9,
             'Zero':0}

    words = string.split()
    rt = ''
    for word in words:
        ct = [(find_min_distance(word, k), v) for k, v in candi.items()]
        dis, number = min(ct)
        rt += str(number)
    return rt


if __name__ == '__main__':
    string = "Zeeero, Eigght, Nin, balaba"
    rt = analysis(string)
    print rt
