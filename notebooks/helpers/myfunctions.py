# Module myfunctions

def find_winner(result_first, result_second, variable):
    """
    This function compares the test scores of a cross-validation
    fold by fold, summarizes the amount of times the test scores
    were higher.
    input parameters: first data set, second data set, variable to compare 
    (normally 'test_score' for cross-validation) 
    """
    sum_first, sum_second = 0, 0
    for i in range(0, result_first[variable].count()):
        if result_first.loc[i, 'test_score'] > result_second.loc[i,'test_score']:
            sum_first = sum_first + 1
        else:
            sum_second = sum_second + 1
    print(f"Test scores comparison for First result set and Second result set \n"
          f"First Result set wins {sum_first} times, Second result set wins {sum_second} times")

def plot_pipe():
    from sklearn import set_config

    # To get a diagram visualization of the pipeline
    set_config(display="diagram")