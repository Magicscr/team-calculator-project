#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// Базовые операции
int add(int a, int b);
int subtract(int a, int b);

// Операции Alice
int multiply(int a, int b);
double divide(int a, int b);
double square_root(double x);
double sine(double x);
double cosine(double x);

// Операции Bob
int modulo(int a, int b);
double power(double base, double exponent);
double floor_func(double x);
double ceil_func(double x);

// Система памяти (Bob)
void memory_store(double value);
double memory_recall();
void memory_clear();
void memory_add(double value);

#endif
