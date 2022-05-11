# The following python code may be used to automatically do the train test split

import splitfolders
splitfolders.ratio(r'C:\Users\nelso\Downloads\Imagenet-10-1500',
                   output=r'C:\Users\nelso\Downloads\Imagenet-10-1500-splits',
                   seed=1337, ratio=(.9, 0.0,0.1))