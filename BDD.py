import pytest
import cmath
from biquadratic import solve_biquadratic, get_coefficients

def test_solve_biquadratic_real_roots():
  A = 1
  B = -6
  C = 8
  expected_roots = [4.0, 2.0, -4.0, -2.0]
  roots = solve_biquadratic(A, B, C)
  assert roots == expected_roots

def test_solve_biquadratic_complex_roots():
  A = 1
  B = 0
  C = 1
  expected_roots = [1j, -1j, -1j, 1j]
  roots = solve_biquadratic(A, B, C)
  assert roots == expected_roots

def test_solve_biquadratic_zero_discriminant():
  A = 1
  B = -4
  C = 4
  expected_roots = [2.0, 2.0, -2.0, -2.0]
  roots = solve_biquadratic(A, B, C)
  assert roots == expected_roots
