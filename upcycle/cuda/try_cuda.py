import torch


def try_cuda(obj):
    if torch.cuda.is_available():
        return obj.cuda()
