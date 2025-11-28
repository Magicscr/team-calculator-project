#include "math_utils.h"
#include <stdexcept>
#include <cmath>

// Глобальная переменная для памяти калькулятора
double memory = 0.0;

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

int modulo(int a, int b) {
    if (b == 0) {
        throw std::runtime_error("Modulo by zero!");
    }
    return a % b;
}

double power(double base, double exponent) {
    return std::pow(base, exponent);
}

double square_root(double x) {
    if (x < 0) {
        throw std::runtime_error("Square root of negative number!");
    }
    return std::sqrt(x);
}

double sine(double x) {
    return std::sin(x);
}

double cosine(double x) {
    return std::cos(x);
}

// Функции Bob - округление и память
double floor_func(double x) {
    return std::floor(x);
}

double ceil_func(double x) {
    return std::ceil(x);
}

// Система памяти
void memory_store(double value) {
    memory = value;
}

double memory_recall() {
    return memory;
}

void memory_clear() {
    memory = 0.0;
}

void memory_add(double value) {
    memory += value;
}
