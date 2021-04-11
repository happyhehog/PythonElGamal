import errno
import os


class Utils:
    @staticmethod
    def createFoldersInPath(filename: str) -> None:
        if os.path.dirname(filename) and not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    @staticmethod
    def fastModuloPow(num: int, pow: int, modulo: int) -> int:
        result = 1
        while pow:
            if pow % 2 == 0:
                num = (num ** 2) % modulo
                pow = pow // 2
            else:
                result = (num * result) % modulo
                pow -= 1
        return result

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while a != b:
            if a > b:
                a, b = b, a
            b = b - a
        return a

    @staticmethod
    def extendedGcd(a: int, b: int) -> int:
        x, xx, y, yy = 1, 0, 0, 1
        while b:
            q = a // b
            a, b = b, a % b
            x, xx = xx, x - xx*q
            y, yy = yy, y - yy*q
        return (x, y, a)
