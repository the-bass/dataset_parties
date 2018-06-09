import unittest
import dataset_parties
from fixtures.limited_nature_dataset import LimitedNatureDataset


class TestNgStylePartitioner(unittest.TestCase):

    def test_with_a_small_dataset(self):
        dataset = LimitedNatureDataset(set_size=(10))
        train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
        self.assertEqual(len(train_set), 6)
        self.assertEqual(len(dev_set), 2)
        self.assertEqual(len(test_set), 2)

    def test_with_a_dataset_containing_over_50000_samples(self):
        dataset = LimitedNatureDataset(set_size=(50013))
        train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
        self.assertEqual(len(train_set), 30013)
        self.assertEqual(len(dev_set), 10000)
        self.assertEqual(len(test_set), 10000)

    def test_with_a_dataset_containing_over_50000_samples(self):
        datasetA = range(0, 284315)
        datasetB = range(284315, 284315 + 492)
        train_set, dev_set, test_set = dataset_parties.ng_style((datasetA, datasetB))
        self.assertEqual(len(train_set), 264807)
        self.assertEqual(len(dev_set), 10000)
        self.assertEqual(len(test_set), 10000)

    def test_with_several_datasets(self):
        datasetA = ['A'] * 5000
        datasetB = ['B'] * 15000
        datasetC = ['C'] * 80000

        train_set, dev_set, test_set = dataset_parties.ng_style((datasetA, datasetB, datasetC))

        self.assertEqual(train_set.count('A'), 4000)
        self.assertEqual(train_set.count('B'), 12000)
        self.assertEqual(train_set.count('C'), 64000)

        self.assertEqual(dev_set.count('A'), 500)
        self.assertEqual(dev_set.count('B'), 1500)
        self.assertEqual(dev_set.count('C'), 8000)

        self.assertEqual(test_set.count('A'), 500)
        self.assertEqual(test_set.count('B'), 1500)
        self.assertEqual(test_set.count('C'), 8000)

    def test_resulting_sets_distinct(self):
        datasetA = range(0, 5000)
        datasetB = range(5000, 15000)
        datasetC = range(15000, 20000)

        partitions = dataset_parties.ng_style((datasetA, datasetB, datasetC))
        train_set_set, dev_set_set, test_set_set = [set(dataset) for dataset in partitions]

        self.assertEqual(sum([len(partition) for partition in partitions]), 20000)

        self.assertEqual(len(train_set_set.intersection(dev_set_set)), 0)
        self.assertEqual(len(dev_set_set.intersection(test_set_set)), 0)
        self.assertEqual(len(train_set_set.intersection(test_set_set)), 0)

if __name__ == '__main__':
    unittest.main()
