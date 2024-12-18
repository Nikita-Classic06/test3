import runner
from runner_and_tournament import Runner, Tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen,"Тесты в этом кейсе заморожены")
    def test_walk(self):
        p = runner.Runner("Anton")
        for i in range(10):
            p.walk()
        self.assertEqual(p.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        q = runner.Runner("Vita")
        for i in range(10):
            q.run()
        self.assertEqual(q.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        a1 = runner.Runner("Nikita")
        a2 = runner.Runner("Dima")
        for i in range(10):
            a1.run()
            a2.walk()
        self.assertNotEqual(a1.distance,a2.distance)


if __name__ == "__main__":
    RunnerTest()
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.b1 = Runner("Усэйн", 10)
        self.b2 = Runner("Андрей", 9)
        self.b3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, k in cls.all_results.items():
            print(k)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        p = Tournament(90, self.b1, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        p = Tournament(90, self.b2, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        p = Tournament(90, self.b1, self.b2, self.b3)
        self.all_results[len(self.all_results)] = p.start()
        last_result = list(self.all_results.values())[-1]
        self.assertTrue(last_result[len(last_result)] == "Ник")


if __name__ == "__main__":
    TournamentTest()