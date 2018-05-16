from .aux import __slice__


def ng_style(dataset):
    """
    Named after Andrew Ng.

    Splits the given dataset into train, dev and test set, where dev and test
    sets each hold 20%, but not more than 10,000 samples.
    """
    cardinality = len(dataset)
    valid_sets_size = min([round(0.2 * cardinality), 10000])
    train_set_size = cardinality - 2 * valid_sets_size

    train_set = __slice__(dataset, 0, train_set_size)
    dev_set = __slice__(dataset, train_set_size, train_set_size + valid_sets_size)
    test_set = __slice__(dataset, train_set_size + valid_sets_size, cardinality)

    return train_set, dev_set, test_set
