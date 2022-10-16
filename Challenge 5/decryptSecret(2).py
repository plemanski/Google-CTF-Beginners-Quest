CURR_DIR = "c:/Users/rossi/Documents/GoogleCTF/Challenge 5/"
from randcrack import RandCrack
def sync_predictor():
    rc = RandCrack()
    with(open(CURR_DIR + 'robo_numbers_list.txt', 'r') as file):
        for line in file:
            i = line.replace("-","").strip()
            i = int(i) - (1<<31)
            rc.submit(int(line.replace("-", "")) - (1<<31))
    with(open(CURR_DIR+"secret.enc", 'rb')) as file:
        secret=list(file.read())
        
    key = [rc.predict_getrandbits(8) for _ in range(len(secret))]
    flag=""
    
    for a,b in zip(key, secret):
        flag+=chr(a^b)
    print(flag)


def __main__():
    sync_predictor()

if __name__ == "__main__":
    __main__()