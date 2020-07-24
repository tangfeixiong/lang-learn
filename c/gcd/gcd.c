/*
  calculates the greatest common divisor of two given integers
  the classic algorithm for computing the GCD, known as Euclid's algorithm, goes as follows: Let m and
  n be the two numbers we want to get the gcd for. If n is 0, then stop since m is the gcd. Otherwise,
  compute the remainder when m is divided by n . Copy n into m and copy the remainder into n . Then
  repeat the process, starting with testing whether n is 0.
*/

int gcd(int m, int n) {
    int i;
    
    if (n==0)
        return m;
    
    if (m <=0 || n < 0)
        return 0;
        
    if (m < n) {
        i = m;
        m = n;
        n = i;
    }
        
    return gcd(n, m%n);
}

// no recursive
int gcd2(int m, int n) {
    while (n != 0) {
        int i = m%n;
        m = n;
        n = i;
    }
    return m;
}