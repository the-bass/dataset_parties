def __slice__(dataset, start, end):
    raw_partition = []

    for n in range(start, end):
        raw_partition.append(dataset[n])

    return raw_partition
