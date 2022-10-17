from Crypto.Util.number import *
from gmpy2 import iroot

#flag = b"REDACTED"

# Gets a random N-bit prime number
#p = getPrime(1024)
#q = getPrime(1024)


#n = p*q

n = 21034814455172467787319632067588541051616978031477984909593707891829600195022041640200088624987623056713604514239406145871910044808006741636513624835862657042742260288941962019533183418661144639940608960169440421588092324928046033370735375447302576018460809597788053566456538713152022888984084306297869362373871810139948930387868426850576062496427583397660227337178607544043400076287217521751017970956067448273578322298078706011759257235310210160153287198740097954054080553667336498134630979908988858940173520975701311654172499116958019179004876438417238730801165613806576140914402525031242813240005791376093215124477
 
# Converts byte string to long int (big endian)
m = bytes_to_long(flag)


# This is just an RSA Problem that has been half solved
# I correct myself, this is an RSA problem htat hasn't been encrypted as the public exponent is not
# large enough. Meaning the result of c=m**e mod n is m**3 = n*k+c

#c = pow(m,3,n)
c = 15478048932253023588842854432571029804744949209594765981036255304813254166907810390192307350179797882093083784426352342087386691689161026226569013804504365566204100805862352164561719654280948792015789195399733700259059935680481573899984998394415788262265875692091207614378805150701529546742392550951341185298005693491963903543935069284550225309898331197615201102487312122192298599020216776805409980803971858120342903012970709061841713605643921523217733499022158425449427449899738610289476607420350484142468536513735888550288469210058284022654492024363192602734200593501660208945967931790414578623472262181672206606709


n = 21034814455172467787319632067588541051616978031477984909593707891829600195022041640200088624987623056713604514239406145871910044808006741636513624835862657042742260288941962019533183418661144639940608960169440421588092324928046033370735375447302576018460809597788053566456538713152022888984084306297869362373871810139948930387868426850576062496427583397660227337178607544043400076287217521751017970956067448273578322298078706011759257235310210160153287198740097954054080553667336498134630979908988858940173520975701311654172499116958019179004876438417238730801165613806576140914402525031242813240005791376093215124477


# My Algo wasn't precise enough, but I kept it here for posterity's sake
def binary_search(c, e):
    # Credit for starting position https://stackoverflow.com/a/358134
    low = 10 ** (len(str(c)) // e)
    high = low * 10
    
    # Normally we would need an error check for precision but we know this is going to be a whole
    # number. So i intentionally ignored it.

    guess = (low + high) // 2
    count = 0
    while low < high:
        count += 1
        guess = int((low + high) // 2 + 1)
        if pow(guess, e) < c and (guess **e) < c:
            low = guess + 1
        if pow(guess, e) > c and (guess ** e) > c:
            high = guess -1
        else:
            return False
    return (guess + 1)



k = 0
flag = ""

while "CTF" not in flag[:6]:
    k += 1
    m, exact = iroot((n*k) + c,3)
    message = long_to_bytes(m) if exact == True else ""
    flag = message.decode(errors="ignore") if message != "" else ""
    open("Challenge 7/message.txt",'w').write(str(flag))


print(flag)
    