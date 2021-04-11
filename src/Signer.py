from .Utils import Utils
from hashlib import sha256
import random
import os


class Signer:
    def __init__(self, input_file: str, key_file: str):
        self.input_file = input_file
        self.key_file = key_file

        with open(key_file + '.pub', 'r') as key_input_file:
            self.p = int(key_input_file.readline().strip())
            self.g = int(key_input_file.readline().strip())
            self.public_key = int(key_input_file.readline().strip())

        with open(self.key_file, 'r') as key_input_file:
            self.private_key = int(key_input_file.readline().strip())

    def getHash(self):
        message = ''
        with open(self.input_file, 'r') as input_file:
            for line in input_file:
                message += line
        return int.from_bytes(sha256(message.encode("UTF-8")).digest(), 'big')

    def sign(self):
        hash_message = self.getHash()

        k = random.randint(2, self.p - 1)
        while Utils.gcd(self.p - 1, k) != 1:
            k = random.randint(2, self.p - 1)
        a = Utils.fastModuloPow(self.g, k, self.p)
        inv = Utils.extendedGcd(k, self.p - 1)[0]
        b = inv * (hash_message - self.private_key * a) % (self.p - 1)

        output_file = os.path.splitext(self.input_file)[0] + '.sgn'
        Utils.createFoldersInPath(output_file)
        with open(output_file, 'w', encoding='utf8') as output_file:
            output_file.write(str(a) + '\n')
            output_file.write(str(b) + '\n')

    def checkSign(self) -> bool:
        a, b = 0, 0
        sign_file = os.path.splitext(self.input_file)[0] + '.sgn'
        with open(sign_file, 'r') as sign_input:
            a = int(sign_input.readline().strip())
            b = int(sign_input.readline().strip())

        hash_message = self.getHash()


        if a < 1 or a > self.p - 1:
            return False

        first_val = Utils.fastModuloPow(self.public_key, a, self.p) % self.p * Utils.fastModuloPow(a, b, self.p) % self.p
        second_val = Utils.fastModuloPow(self.g, hash_message, self.p)
        return first_val == second_val
