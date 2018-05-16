# Dataset Parties

Provides methods to split a *PyTorch* dataset (i.e. an instance of `torch.utils.data.Dataset`) into several subsets.

Tested with
 - PyTorch 0.4
 - Python 3.6.4 :: Anaconda, Inc.

## Usage example

Let `dataset` an instance of `torch.utils.data.Dataset`, then you can

```py
import dataset_parties

train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
```

to split the dataset into train, dev and test set. All new datasets are themselves instances of `torch.utils.data.Dataset`.

## Partitioning methods

### `ng_style(dataset)`
Splits the given dataset into train, dev and test set, where dev and test sets each hold 20%, but not more than 10,000 samples.

## Development

You can run all tests using

```sh
python -m unittest discover tests
```
