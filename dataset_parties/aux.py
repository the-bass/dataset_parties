from .dataset_partition import DatasetPartition


def __slice__(dataset, start, end):
    raw_partition = []

    for n in range(start, end):
        raw_partition.append(dataset[n])

    partition = DatasetPartition(raw_partition)

    return partition
