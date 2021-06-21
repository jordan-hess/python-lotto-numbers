import unittest, random

ent_list = [int()]
def lotto_no():
    loto_list = random.sample(range(1, 49), 6)
    loto_list.sort()
    return loto_list
class Random(unittest.TestCase):
    def set(self):
        self.a = 1
        self.b = 49
    def test_gen_age(self):
        lotto_no()
        self.assertTrue(self.a >= 1 and self.b <= 49);

if __name__ == '__main__':
    unittest()