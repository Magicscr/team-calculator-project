#include "math_utils.h"
#include <stdexcept>
#include <cmath>

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Division by zero!");
    }
    return static_cast<double>(a) / b;
}

// Функции Bob - остаток от деления и степень
int modulo(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Modulo by zero!");
    }
    return a % b;
}

double power(double base, double exponent) {
    return std::pow(base, exponent);
}
