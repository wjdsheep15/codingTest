"""

"""


class Election():
    def __init__(self):
        self.candidates = {}

    def enroll(self, candName):
        self.candidates[candName] = 0

    def vote(self, voteTo):
        if voteTo in self.candidates:
            self.candidates[voteTo] += 1
        else:
            print("올바르지 않은 후보입니다.")

    def deadline(self):
        arr = []
        for x, y in self.candidates.items():
            if y == max(self.candidates.values()):
                arr.append(x)
        return arr


elelc1 = Election()
elelc1.enroll("abc")
elelc1.enroll("def")
elelc1.enroll("qwe")

elelc1.vote("abc")
elelc1.vote("ABC")
elelc1.vote("def")
elelc1.vote("def")
elelc1.vote("def")
elelc1.vote("qwe")
elelc1.vote("qwe")
elelc1.vote("qwe")

print(elelc1.candidates)

result_arr = elelc1.deadline()
if len(result_arr) >1:
    print("동점자가 존재")
else:
    print(result_arr)
