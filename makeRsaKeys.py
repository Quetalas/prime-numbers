import random, sys, os, rabinMiller, cryptomath


def generateKey(keySize):

    print('Generating p prime...')
    p = rabinMiller.generateLargePrime(keySize)
    print('Generating q prime...')
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    print('Generating e that is relatively prime to (p-1)(q-1)')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e,(p-1) * (q-1)) == 1:
            break
    print('Calculating d that is mod inverse of e')
    d = cryptomath.findModInverse(e, (p-1) * (q-1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('PrivateKey:', privateKey)

    return (publicKey, privateKey)


if __name__ == '__main__':
    generateKey(1024)