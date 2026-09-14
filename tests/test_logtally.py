import unittest
from src.logtally import summarize


class TestSummarize(unittest.TestCase):
    def test_counts_each_level(self):
        counts = summarize(["INFO started", "ERROR failed", "ERROR retry"])
        self.assertEqual(counts["INFO"], 1)
        self.assertEqual(counts["ERROR"], 2)

    def test_unknown_levels_ignored(self):
        counts = summarize(["TRACE noise", "plain line"])
        self.assertEqual(sum(counts.values()), 0)


if __name__ == "__main__":
    unittest.main()
