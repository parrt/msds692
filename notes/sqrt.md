# Approximating square root

## Goals

* Encode and solve a recurrence relation from mathematics using iteration in Python to approximate a real-world, real valued function: `sqrt`.
* Make a function within a function

The end result is file `sqrt.py`.

## Description

To approximate square root, the idea is to pick an initial estimate, x0, and then iterate with better and better estimates, xi, using the recurrence relation:

<center>
<img src=figures/sqrt-recurrence.png width=120>
</center>

There’s a great deal on the web you can read to learn more about why this process works but it relies on the average (midpoint) of x and n/x getting us closer to the square root of n. The cool thing is that the iteration converges quickly.

Our goal is to write a function that takes a single  number and returns it square root

```python
# Stop iterating when the new approximation is within
# PRECISION of the old value.
PRECISION = 0.00000001
def sqrt(n):
    "compute square root of n"
    # print "Compute sqrt(%f)" % n 
    x_0 = 1.0 # pick any old initial value
    x_prev = x_0 
    while True:
        x_new = 0.5 * (x_prev + n/x_prev)
        delta = abs(x_new - x_prev)
        if delta < PRECISION:
            print "sqrt(%f) = %f" % (n, x_new)
            return x_new
        # print x_new
        x_prev = x_new 
```

And then to test it, we can use `numpy`:

```python
import math
def test_sqrt():
    def check(n):
        assert np.isclose(sqrt(n), math.sqrt(n))
    check(125348)
    check(89.2342)
    check(100)
    check(1)
    check(0)

test_sqrt()
```

As you can see you can define a function within a function. It's not special in any way except that code outside of `test_sqrt()` cannot see function `check()`. On the other hand, `check()` **can** see the symbols outside of `test_sqrt()`, such as our `sqrt()`.