import time
import matplotlib.pyplot as plt
import csv
from sympy import isprime
from prettytable import PrettyTable

def find_prime_fibonacci(time_limit=12):
    start_time = time.time()
    a, b = 0, 1
    fib_count = 0
    prime_fibs = []
    table = PrettyTable(["Time (s)", "Fibonacci Count", "Prime Fibonacci Number"])
    prime_indices = []
    prime_times = []
    table_data = []
    
    while time.time() - start_time < time_limit:
        a, b = b, a + b  # Generate next Fibonacci number
        fib_count += 1
        time_elapsed = time.time() - start_time
        
        if isprime(b):
            prime_fibs.append(b)
            row = [round(time_elapsed, 2), fib_count, b]
            table.add_row(row)
            table_data.append(row)
            prime_indices.append(len(prime_fibs))  # Number of prime Fibonacci found so far
            prime_times.append(time_elapsed)
    
    return table, table_data, prime_indices, prime_times

if __name__ == "__main__":
    table, table_data, prime_indices, prime_times = find_prime_fibonacci()
    print(table)
    
    # Save table to CSV file
    with open("prime_fibonacci.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time (s)", "Fibonacci Count", "Prime Fibonacci Number"])
        writer.writerows(table_data)
    
    # Plot number of prime Fibonacci numbers found vs. time taken to find them (logarithmic y-axis)
    plt.plot(prime_indices, prime_times, marker='o', linestyle='-')
    plt.xlabel("Number of Prime Fibonacci Numbers Found")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.title("Prime Fibonacci Count vs Time Taken")
    plt.grid()
    plt.show()
