import os

try:
  import numpy as np
except ImportError:
  print("Trying to Install required module: numpy\n")
  os.system('python -m pip install numpy')
  import numpy as np

def print_hi():
    print(f'Hello World!!!!')
    a = np.arange(15).reshape(3,5)
    print(a)

if __name__ == '__main__':
    print_hi()
