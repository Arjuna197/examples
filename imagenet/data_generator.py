import torch

class RandomDataset(torch.utils.data.Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self):
        'Initialization'
        self.labels = torch.ones([1], dtype=torch.long)
        self.list_IDs = [0]

  def __len__(self):
        'Denotes the total number of samples'
        return 100000

  def __getitem__(self, index):
        'Generates one sample of data'
        # Select sample
        ID = self.list_IDs[0]
        # Load data and get label
        X = torch.rand([3, 224,224])
        y = self.labels[0]

        return X, y
