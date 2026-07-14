import numpy as np
import matplotlib.pyplot as plt

from pricer import monte_carlo_option_pricer, analytical_call_price, monte_carlo_antithetic, monte_carlo_control


def convergence_test(S_0,r,sigma,T,K,num_experiments):
    true_analytical_price = analytical_call_price(S_0,r,sigma,T,K)
    path_counts = [100,1000,10000,100000,1000000]
    print(f"Analytical Price: £{true_analytical_price:.2f}\n")

    pricers = {
        "Naive MC": monte_carlo_option_pricer,
        "Antithetic MC": monte_carlo_antithetic,
        "Control MC": monte_carlo_control
    }

    errors_dict = {
        "Naive MC": [],
        "Antithetic MC": [],
        "Control MC": []
    }

    for name,pricer_func in pricers.items():
        print(f"--- Running {name} ---")
        print(f"{'Paths (N)':<12} | {'MC Price':<10} | {'Standard Error':<10}")
        print("-" * 38)
        for N in path_counts:
            simulated_prices =[]
            for experiment in range(num_experiments):
                mc_price = pricer_func(S_0,r,sigma,T,K,N)
                simulated_prices.append(mc_price)
            avg_mc_price = np.mean(simulated_prices)
            std_error = np.std(simulated_prices, ddof=1)
            errors_dict[name].append(std_error)
            print(f"{N:<12} | {avg_mc_price:<10.2f} | {std_error:<10.4f}")
         
            

    plt.figure(figsize = (10,6))
    markers=['o','s', '^']


    for (name,error_list), marker in zip(errors_dict.items(),markers):
        log_path_counts = np.log(path_counts)
        log_error = np.log(error_list)
        gradient, intercept = np.polyfit(log_path_counts,log_error,1)
        plt.plot(path_counts,error_list,marker=marker,label=f"{name}, Gradient={gradient:.2f}, y-intercept={intercept:.2f}")
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Standard error of MC value against number of paths simulated')
    plt.xlabel('Number of paths')
    plt.ylabel('Standard error')
    plt.legend()
    plt.savefig('convergence_graph.png', dpi=300, bbox_inches='tight')

    plt.show()
            



if __name__ == "__main__":
    convergence_test(100,0.05,0.2,1,100,100)