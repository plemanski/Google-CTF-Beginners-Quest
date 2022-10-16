# Credit for randcrack Maxim: https://github.com/tna0y
# Repo: https://github.com/tna0y/Python-random-module-cracker
# While I did start by trying to create my own MT19937 cracker
# I inevitably resorted to using the random module cracker.
# Don't fix what isn't broken

from randcrack import RandCrack

def __main__():
    rc = RandCrack()
    with(open('robo_numbers_list.txt', 'r') as file):
        for line in file:
            i = line.replace("-","").strip()
            i = int(i) - (1<<31)
            rc.submit(int(line.replace("-", "")) - (1<<31))
    with(open("secret.enc", 'rb')) as file:
        secret=list(file.read())
        
    key = [rc.predict_getrandbits(8) for _ in range(len(secret))]
    flag=""
    
    for a,b in zip(key, secret):
        flag+=chr(a^b)
    print(flag)

if __name__ == "__main__":
    __main__()