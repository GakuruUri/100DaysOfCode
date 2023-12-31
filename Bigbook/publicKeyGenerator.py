#Public Key Generator
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys,os


def main():
    # Create a public/private keypair with 1024-bit keys:
    
    print('Making key files.....')
    makeKeyFiles('al_swegart', 1024)
    print('key files made.')
    
def generateKey(keySize):
    # Creates public/private keys keySize bits size.
    p = 0
    q = 0
    # Step 1: Create two prime numbers p and q.
    # Calculate n = p * q:
    
    print('Generating p prime...')
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
        
    n = p * q
    
    # Step 2: Create a number e that is relatively prime to (p - 1)*(q - 1):
    print('Generating e that is relatively prime to (p - 1)*(q - 1)...')
    
    
    
    while True:
        # Keep trying random numbers for e until one is valid:
        e = random.randrange(2 ** (keySize - 1), 2 **(keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
        
    # Step 3: Calculated d, the mod inverse of e:
    print('Calculating d that is mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
    
    publicKey = (n, e)
    privateKey = (n, d)
    
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    
    
    return(publicKey, privateKey)





def makeKeyFiles(name, keySize):
    # Create two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
    #is the value in name) with the n,e and d,e integers written in them delimited by a comma.
    
    
    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists ('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name of delete these files and rerun this program.' % (name, name))
        
    publicKey, privateKey = generateKey(keySize)
    
    
    print()
    
    print('The public key is a %s and a %s digit number,' %
          (len(str(publicKey[0])), len(str(publicKey[1]))))
    
    print('Writing public key to file %s_public.txt...' % (name))
    
    fo = open('%s_pubkey.txt' % (name) , 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    
    
    print()
    print('The private key is a %s and a %s digit number.' %
          (len(str(publicKey[0])), len(str(publicKey[1]))))
    
    
    print('Writing private key to file %s_privkey.txt...' % (name))
    
    fo = open('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()
    
    
# If makePublicPrivateKeys.py is run (instead of imported as a madule),
# Call the main() function:

if __name__ == '__main__':
    main()
    














    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    