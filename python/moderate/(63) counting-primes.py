import sys

def main(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line:
                line = line.strip().split(',')
                a = int(line[0])
                b = int(line[1])
    
                primes = get_prime_list(b+1)
                count = 0
                for prime in primes[::-1]:
                    if prime < a:
                        break
                    count += 1
    
                print count 

def get_prime_list(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

if __name__ == '__main__':
    main(sys.argv[1])