import click
import os

from src.UserKeyGenerator import UserKeyGenerator
from src.Signer import Signer


@click.group()
def elgamal():
    pass


@elgamal.command()
@click.option('-l', '--length', 'length', default=2048, help='Bit length of key')
@click.option('-o', '--output-file', 'output_file', default='key', help='File where to generate keys')
def generate_key(length, output_file):
    """ Generate user keys for El-Gamal sign algorithm """
    key_generator = UserKeyGenerator(length=length, output_file=output_file)
    key_generator.generate()


@elgamal.command()
@click.option('-i', '--input-file', 'input_file', default=None, help='Input text file', required=True)
@click.option('-k', '--key', 'key_file', default=None, help='Key file location', required=True)
def sign(input_file, key_file):
    """Sign input file with El-Gamal algorithm"""

    if not os.path.isfile(input_file):
        print("Can not find input file {}".format(input_file))
        return

    key_file = key_file.replace('.pub', '')
    if not os.path.isfile(key_file + '.pub'):
        print("Can not find public key file {}".format(key_file + '.pub'))
        return

    if not os.path.isfile(key_file):
        print("Can not find private key file {}".format(key_file))
        return

    Signer(input_file, key_file).sign()


@elgamal.command()
@click.option('-i', '--input-file', 'input_file', default=None, help='Input text file', required=True)
@click.option('-k', '--key', 'key_file', default=None, help='Private key file location', required=True)
def checkSign(input_file, key_file):
    """Check input file El-Gamal sign"""

    if not os.path.isfile(input_file):
        print("Can not find input file {}".format(input_file))
        return

    key_file = key_file.replace('.pub', '')
    if not os.path.isfile(key_file + '.pub'):
        print("Can not find public key file {}".format(key_file + '.pub'))
        return

    if not os.path.isfile(key_file):
        print("Can not find private key file {}".format(key_file))
        return

    if Signer(input_file, key_file).checkSign():
        print("Sign verified")
    else:
        print("SIGN WAS NOT VERIFIED! DANGER!!!")



if __name__ == '__main__':
    elgamal()
