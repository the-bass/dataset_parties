import torch.utils.data


class LimitedNatureDataset(torch.utils.data.Dataset):

    def __init__(self, set_size):
        self.records = list(range(set_size))

    def __len__(self):
        return len(self.records)

    def __getitem__(self, index):
        return self.records[index]
