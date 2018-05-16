# Dataset Parties

Provides methods to split a dataset into several subsets for training, development, testing etc.

Last tested with
 - PyTorch 0.4
 - Python 3.6.4 :: Anaconda, Inc.

## Usage example

Let `dataset` an instance of `list`, `torch.utils.data.Dataset` or another iterable class, then you can do

```py
import dataset_parties

train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
```

to split the dataset into train, dev and test set. All new datasets are instances of `torch.utils.data.Dataset`.

## Partitioning methods

### `ng_style(dataset)`

Splits the given dataset into train, dev and test set, where dev and test sets each hold 20%, but no more than 10,000 samples.

## Development

You can run all tests using

```sh
python -m unittest discover tests
```
