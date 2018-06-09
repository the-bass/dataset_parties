from .aux import __slice__


def ng_style(datasets, max_valid_set_size=10000, valid_set_size_relative=0.2):
    """
    Named after Andrew Ng.

    Splits the given dataset into train, dev and test set, where dev and test
    sets each hold 20%, but not more than 10,000 samples.

    `datasets` may be one dataset (i.e. a *list* of samples or another iterable
    object that are **not** tuples) or a tuple of datasets.

    If a tuple of datasets instead of 1 dataset is given, it will be taken
    care of that each resulting set has an almost equal percentage from each
    given set.
    """
    if not isinstance(datasets, tuple):
        datasets = (datasets,)

    cardinality = sum([len(dataset) for dataset in datasets])
    valid_set_size_relative = min([max_valid_set_size / cardinality, valid_set_size_relative])
    train_set_size_relative = 1 - 2 * valid_set_size_relative

    train_set = []
    dev_set = []
    test_set = []

    train_set_amounts = []
    dev_set_amounts = []

    for dataset in datasets:
        set_size = len(dataset)
        required_amount = round(set_size * train_set_size_relative)
        train_set_amounts.append(required_amount)
        train_set += __slice__(dataset, 0, required_amount)

    for index, dataset in enumerate(datasets):
        set_size = len(dataset)
        required_amount = round(set_size * valid_set_size_relative)
        dev_set_amounts.append(required_amount)
        dev_set += __slice__(dataset, train_set_amounts[index], train_set_amounts[index] + required_amount)

    for index, dataset in enumerate(datasets):
        set_size = len(dataset)
        test_set += __slice__(dataset, train_set_amounts[index] + dev_set_amounts[index], set_size)

    return train_set, dev_set, test_set
