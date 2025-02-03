import math
import multiprocessing

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

def even_digits(num):
    return [int(d) for d in str(num) if int(d) % 2 == 0]

def odd_digits(num):
    return [int(d) for d in str(num) if int(d) % 2 != 0]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def analyze_number(num):
    # Pool içinde çalıştırılacak fonksiyonları tek tek çağır
    with multiprocessing.Pool(processes=4) as pool:
        sum_result = pool.apply_async(sum_of_digits, (num,))
        even_result = pool.apply_async(even_digits, (num,))
        odd_result = pool.apply_async(odd_digits, (num,))
        prime_result = pool.apply_async(is_prime, (num,))

        # Sonuçları al
        sum_of_digits_res = sum_result.get()
        even_digits_res = even_result.get()
        odd_digits_res = odd_result.get()
        is_prime_res = prime_result.get()

    print(f"Number: {num}")
    print(f"Sum of Digits: {sum_of_digits_res}")
    print(f"Even Digits: {even_digits_res}")
    print(f"Odd Digits: {odd_digits_res}")
    print(f"Is Prime: {is_prime_res}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    analyze_number(num)
