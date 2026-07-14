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
        for N in path_counts:
            simulated_prices =[]
            for experiment in range(num_experiments):
                mc_price = pricer_func(S_0,r,sigma,T,K,N)
                simulated_prices.append(mc_price)
            avg_mc_price = np.mean(simulated_prices)
            std_error = np.std(simulated_prices, ddof=1)
            errors_dict[name].append(std_error)
         
        
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

    md_table = "| Paths (N) | Naive SE | Antithetic SE | Control SE |\n"
    md_table += "|---|---|---|---|\n"
    
    for i, N in enumerate(path_counts):
        naive_se = errors_dict["Naive MC"][i]
        antithetic_se = errors_dict["Antithetic MC"][i]
        control_se = errors_dict["Control MC"][i]
        md_table += f"| {N:,} | {naive_se:.4f} | {antithetic_se:.6f} | {control_se:.6f} |\n"

    try:
        with open("README.md", "r") as file:
            readme_content = file.read()

        start_marker = "[//]: # (START_TABLE)"
        end_marker = "[//]: # (END_TABLE)"

        start_idx = readme_content.find(start_marker)
        end_idx = readme_content.find(end_marker)

        if start_idx != -1 and end_idx != -1:
            top_half = readme_content[:start_idx + len(start_marker)]
            bottom_half = readme_content[end_idx:]

            new_readme = top_half + "\n\n" + md_table + "\n" + bottom_half
            
            with open("README.md", "w") as file:
                file.write(new_readme)
            print("\nSUCCESS: Table safely embedded in README")
        else:
            print("\nWARNING: Could not find the START_TABLE and END_TABLE markers in README.md.")
    except Exception as e:
        print(f"\nError updating README: {e}")
            



if __name__ == "__main__":
    convergence_test(100,0.05,0.2,1,100,100)