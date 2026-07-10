import numpy as np
import matplotlib.pyplot as plt

from pricer import monte_carlo_option_pricer, analytical_call_price

def convergence_test(S_0,r,sigma,T,K,num_experiments):
    true_analytical_price = analytical_call_price(S_0,r,sigma,T,K)
    path_counts = [100,1000,10000,100000,1000000]
    mc_errors=[]
    print(f"Analytical Price: £{true_analytical_price:.4f}\n")
    print(f"{'Paths (N)':<12} | {'MC Price':<10} | {'Abs Error':<10}")
    print("-" * 38)
    for N in path_counts:
        total_error = 0
        total_mc_price = 0
        for experiment in range(num_experiments):
            mc_price = monte_carlo_option_pricer(S_0,r,sigma,T,K,N)
            abs_error = abs(mc_price-true_analytical_price)
            total_error = total_error + abs_error
            total_mc_price = total_mc_price+mc_price
        avg_mc_price = total_mc_price / num_experiments
        avg_error = total_error / num_experiments
        mc_errors.append(avg_error)
        print(f"{N:<12} | £{avg_mc_price:<9.2f} | £{avg_error:<10.4f}")

    plt.figure(figsize=[10,6])
    plt.plot(path_counts,mc_errors, marker='o')
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Error of MC value against number of paths simulated')
    plt.xlabel('Number of paths')
    plt.ylabel('Absolute error')

    plt.show()



if __name__ == "__main__":
    convergence_test(100,0.05,0.2,1,100,100)