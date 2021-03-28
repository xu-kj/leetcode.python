https://en.wikipedia.org/wiki/Modulo_operation

Properties (identities)

* Identity:
    * `(a mod n) mod n = a mod n`
    * `n^x mod n = 0` for all positive integer values of `x`
    * If `p` is a prime number which is not a divisor of `b`, then `ab^(p−1) mod p = a mod p`, due to Fermat's little theorem.
* Inverse:
    * `[(−a mod n) + (a mod n)] mod n = 0`
    * `b^−1 mod n` denotes the modular multiplicative inverse, which is defined if and only if `b` and `n` are relatively prime, which is the case when the left hand side is defined: `[(b^−1 mod n)(b mod n)] mod n = 1`.
* Distributive:
    * `(a + b) mod n = [(a mod n) + (b mod n)] mod n`
    * `ab mod n = [(a mod n)(b mod n)] mod n`
