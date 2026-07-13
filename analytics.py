import numpy as np
import matplotlib.pyplot as plt

from pricer import monte_carlo_option_pricer, analytical_call_price, monte_carlo_antithetic


def convergence_test(S_0,r,sigma,T,K,num_experiments):
    true_analytical_price = analytical_call_price(S_0,r,sigma,T,K)
    path_counts = [100,1000,10000,100000,1000000]
    print(f"Analytical Price: £{true_analytical_price:.2f}\n")

    pricers = {
        "Naive MC": monte_carlo_option_pricer,
        "Antithetic MC": monte_carlo_antithetic
    }

    errors_dict = {
        "Naive MC": [],
        "Antithetic MC": []
    }

    for name,pricer_func in pricers.items():
        print(f"--- Running {name} ---")
        print(f"{'Paths (N)':<12} | {'MC Price':<10} | {'Abs Error':<10}")
        print("-" * 38)
        for N in path_counts:
            total_mc_price = 0
            total_mc_error = 0
            for experiment in range(num_experiments):
                mc_price = pricer_func(S_0,r,sigma,T,K,N)
                abs_mc_error = abs(mc_price - true_analytical_price)
                total_mc_price+= mc_price
                total_mc_error += abs_mc_error
            avg_mc_price = total_mc_price/num_experiments
            avg_mc_error = total_mc_error/num_experiments
            errors_dict[name].append(avg_mc_error)
            print(f"{N:<12} | £{avg_mc_price:<9.2f} | £{avg_mc_error:<10.4f}")
        print("\n")

    plt.figure(figsize = (10,6))
    markers=['o','s']


    for (name,error_list), marker in zip(errors_dict.items(),markers):
        log_path_counts = np.log(path_counts)
        log_error = np.log(error_list)
        gradient, intercept = np.polyfit(log_path_counts,log_error,1)
        plt.plot(path_counts,error_list,marker=marker,label=f"{name}, Gradient={gradient:.2f}, y-intercept={intercept:.2f}")
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Error of MC value against number of paths simulated')
    plt.xlabel('Number of paths')
    plt.ylabel('Absolute error')
    plt.legend()

    plt.show()
            



if __name__ == "__main__":
    convergence_test(100,0.05,0.2,1,100,100)