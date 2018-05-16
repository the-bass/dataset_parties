import unittest
import dataset_parties
from fixtures.limited_nature_dataset import LimitedNatureDataset


class TestDatasetParties(unittest.TestCase):

    def test_ng_style(self):
        dataset = LimitedNatureDataset(set_size=(10))
        train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
        self.assertEqual(len(train_set), 6)
        self.assertEqual(len(dev_set), 2)
        self.assertEqual(len(test_set), 2)
        self.assertEqual(train_set[5], dataset[5])
        self.assertEqual(dev_set[0], dataset[6])
        self.assertEqual(test_set[1], dataset[9])

        dataset = LimitedNatureDataset(set_size=(50003))
        train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
        self.assertEqual(len(train_set), 30003)
        self.assertEqual(len(dev_set), 10000)
        self.assertEqual(len(test_set), 10000)

if __name__ == '__main__':
    unittest.main()
