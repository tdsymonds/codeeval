def solve_problem():
    primes = get_prime_list(1000)

    for prime in primes:
        if is_palindrome(prime):
            largest_palindrome = prime

    print largest_palindrome


def get_prime_list(n):
    """ 
    Returns  a list of primes < n 
    """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def is_palindrome(number):
    """
    Returns true if a number is a palindrome.
    """
    number_string = str(number)
    number_length = len(number_string)
    
    # set the default cutpoints
    cutpoint = number_length / 2
    first_partition = number_string[:cutpoint]
    second_partition = number_string[cutpoint:]
    
    # if odd need to cut the middle number
    # out of the partitions
    if number_length % 2 != 0:
        second_partition = number_string[cutpoint + 1:]
    
    # do the partitions match?
    if first_partition == second_partition[::-1]:
        # have a palindrome!
        return True

    # no palindrome
    return False


if __name__ == '__main__':
    solve_problem()