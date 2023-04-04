class Kassa(object):
    cl_vo = 0
    x = 0

    def __init__(self, cl_vo, x):
        self.cl_vo = cl_vo
        self.x = x

    def top_up(self):
        sym = self.cl_vo + self.x
        return sym

    def count_1000(self):
        count = 0
        tmp = self.cl_vo
        while tmp >= 1000:
            count += 1
            tmp -= 1000
        return count

    def take_away(self):
        if self.cl_vo - self.x < 0:
            return "Error, not enough money in the cash register"
        else:
            return self.cl_vo - self.x


s = Kassa(20000, 4500)
s.count_1000()
s.take_away()
s.top_up()
print(s.count_1000(), s.take_away(), s.top_up())
