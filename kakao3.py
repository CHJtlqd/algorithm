from itertools import combinations
def solution(info, query):
    answer = []
    head = Node()
    for data in info:
        temp = data.split()
        score_temp = temp[4]
        # print(temp)

        head.child[temp[0]].child[temp[1]].child[temp[2]].child[temp[3]].score.append(score_temp)

    for data in query:
        temp = data.split('and')
        for i in range(len(temp)):
            temp[i]=temp[i].strip()
        count=0
        node=[]
        node1=[]
        node2=[]
        node3=[]
        print(temp)
        if temp[0]=='-':
            node.append(head.child['cpp'])
            node.append(head.child['python'])
            node.append(head.child['java'])
        else:
            node.append(head.child[temp[0]])

        if temp[1]=='-':
            for i in node:
                node1.append(i.child['frontend'])
                node1.append(i.child['backend'])
        else:
            for i in node:
                node1.append(i.child[temp[1]])

        if temp[2]=='-':
            for i in node1:
                node2.append(i.child['junior'])
                node2.append(i.child['senior'])
        else:
            for i in node1:
                node2.append(i.child[temp[2]])
        tt = temp[3].split()
        if tt[0]=='-':
            for i in node2:
                node3.append(i.child['chicken'])
                node3.append(i.child['pizza'])
        else:
            for i in node2:
                node3.append(i.child[tt[0]])
        count=0
        for i in node3:
            temp=i.values()
            count=[x for x in temp if int(x)>=int(tt[1])]
            count=len(count)
        answer.append(count)








    return answer


class Node:
    def __init__(self):
        cpp = Language('cpp')
        java = Language('java')
        python = Language('python')
        nothing = Language('-')
        self.child = {'cpp': cpp, 'java': java, 'python': python,'-':nothing}


class Language:
    def __init__(self, name):
        self.name = name
        frontend = Occupation('frontend')
        backend = Occupation('backend')
        nothing = Occupation('-')
        self.child = {'frontend': frontend, 'backend': backend,'-':nothing}


class Occupation:
    def __init__(self, name):
        self.name = name
        junior = Career('junior')
        senior = Career('senior')
        nothing = Career('-')
        self.child = {'junior': junior, 'senior': senior,'-':nothing}



class Career:
    def __init__(self, name):
        self.name = name
        chicken = Food('chicken')
        pizza = Food('pizza')
        nothing = Food('-')
        self.child = {'chicken': chicken, 'pizza': pizza,'-':nothing}


class Food:
    def __init__(self, name):
        self.name = name
        self.score = []

    def values(self):
        return reversed(self.score)


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
