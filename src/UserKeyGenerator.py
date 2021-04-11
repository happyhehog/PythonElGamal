from .PrimeNumberGenerator import PrimeNumberGenerator
from .Utils import Utils
import random


class UserKeyGenerator:
    def __init__(self, length=None, output_file=None):
        self.length = 1024 if length is None else length
        self.output_file = 'key' if output_file is None else output_file

        self.length = self.length // 2
        self.png = PrimeNumberGenerator(length=self.length)

    def generate(self) -> None:
        self.p = self.png.getSophiePrime()
        self.g = self.png.getPrimitiveRootModulo(self.p)
        self.private_key = random.randint(2, self.p - 1)
        self.public_key = Utils.fastModuloPow(self.g, self.private_key, self.p)
        self.saveKeys()

    def saveKeys(self) -> None:
        Utils.createFoldersInPath(self.output_file)
        with open(self.output_file + '.pub', 'w') as output:
            output.write(str(self.p) + '\n')
            output.write(str(self.g) + '\n')
            output.write(str(self.public_key) + '\n')
        with open(self.output_file, 'w') as output:
            output.write(str(self.private_key) + '\n')
