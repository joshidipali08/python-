#Write a Python function that evaluates the mathematical functions f(x)=cos(2x),f^' (x)=-2 sin⁡(2x),and f^'' (x)=-4 cos⁡(2x).Return these three values. Write out the results of these values for x=π

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

# test with x = pi
import math
x = math.pi
f, f_prime, f_double_prime = evaluate_functions(x)

print("f(x) =", f)
print("f'(x) =", f_prime)
print("f''(x) =", f_double_prime)
