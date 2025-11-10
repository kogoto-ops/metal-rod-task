def best_rod_cut_value(total_rod_length, price_arr):
    # initial lists with zeros for values and cut(for each possible rod length)
    max_price_for_length = [0 for _ in range(total_rod_length + 1)]
    best_first_cut_length = [0 for _ in range(total_rod_length + 1)]

    # fill and replace the values or the lists above
    for current_rod_length in range(1, total_rod_length + 1):
        for trial_cut_length in range(1, current_rod_length + 1):
            if trial_cut_length <= len(price_list):
                # Compute total price if we cut at this length
                potential_price = (price_list[trial_cut_length - 1] + max_price_for_length[current_rod_length - trial_cut_length])
                # Update if this cut gives a better total price
                if potential_price > max_price_for_length[current_rod_length]:
                    max_price_for_length[current_rod_length] = potential_price
                    best_first_cut_length[current_rod_length] = trial_cut_length

    # generating the optimal sequence of cuts
    optimal_cut_plan = []
    remaining_length = total_rod_length
    while remaining_length > 0:
        optimal_cut_plan.append(best_first_cut_length[remaining_length])
        remaining_length -= best_first_cut_length[remaining_length]

    return optimal_cut_plan, max_price_for_length[-1]


  

  
