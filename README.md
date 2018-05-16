# Dataset Parties

Provides methods to partition a dataset into several subsets, for example train, dev and test set.

Last tested with **Python 3.6.4 :: Anaconda, Inc.** and **PyTorch 0.4**.

## Installation

Clone this repository and run

```py
pip install .
```

inside the root directory to make the module available as `dataset_parties`.

## Usage example

Let `dataset` an instance of `list`, `torch.utils.data.Dataset` or another iterable class, then you can do

```py
from dataset_parties import ng_style

train_set, dev_set, test_set = ng_style(dataset)
```

to split the dataset into train, dev and test set. All new datasets are instances of `torch.utils.data.Dataset`.

## Partitioning methods

### `ng_style(dataset)`

Splits the given dataset into train, dev and test set, where dev and test sets each hold 20%, but no more than 10,000 samples.

## Development

*Unless noted otherwise, all commands are expected to be executed from the root directory of this repository.*

### Building the package for local development

To make the package available locally while making sure changes to the files are reflected immediately, run

```sh
pip install -e .
```

### Test suite

Run all tests using

```sh
python -m unittest discover tests
```
