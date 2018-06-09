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

Accepts either 1 dataset (i.e. a *list* of samples) or a tuple of datasets. If a tuple of datasets is given it will be taken care of that each resulting partition consists of an (almost) equal percentage of each of the given datasets.

#### Examples

##### 1 dataset

```py
import dataset_parties


dataset = SomeDataset()
train_set, dev_set, test_set = dataset_parties.ng_style(dataset)
```

##### Tuple of datasets

Let's say you have a binary classification problem and you want to make sure that each partition consists of 50% of each class.

```py
import dataset_parties


dataset = CatDogDataset()
cat_dataset = [(x, y) for x, y in dataset if y == 1]
dog_dataset = [(x, y) for x, y in dataset if y == 0]

train_set, dev_set, test_set = dataset_parties.ng_style((cat_dataset, dog_dataset))
```

The train, dev and test set will now all contain about 50% dogs and 50% cats.


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
