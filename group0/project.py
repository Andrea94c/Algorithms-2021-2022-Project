
# Global data to store information
your_variables_here = ""

def prepare(filename : str, threshold : float):
    """ The method is responsable to create the needed data structures to 
        answer the queries. 

    Args:
        filename (str): the input file with the dataset
        threshold (float): a special threshold used to compute the correlation between stocks. 
    """
    global your_variables_here
    your_variables_here = {} 


def query(stock : str, corr_level : int) -> list:
    """
    Some stocks can be correlated and have a similar behavior.

    This method aims at finding all the correlated stocks respect to the input stock.
    In particular we define the corr_level as follows:
        corr_level = 1 identify all the stocks that are directly correlated to the input stock.
        corr_level = 2 identify all the stocks that are NOT directly correlated to the input stock, but they are correlated through a stock at corr_level = 1. 
        corr_level = 3 identify all the stocks that are NOT directly correlated to the input stock, but they are correlated through a stock at corr_level = 2. 
        ..
        corr_level = i identify all the stocks that are NOT directly correlated to the input stock, but they are correlated through a stock at corr_level = i-1. 
    
    Returns:
        list: a list of correlated stocks at corr_level. The list should be in an alphabetical order. If the stock has not correlated stocks, the output should be an empty list.

    E.g., :
        The execution query(GOOGL, 4) may returns: ['AMZN', 'FISV', 'XEL'] 
        Notice the output is ordered!

    """
    return []

# Optional!
def num_connected_components() -> int:
    """ 
        Some stocks can be correlated and create connected componentes / clusters, while others can be alone (not correlated).

        This method should count the number of connected components: 
            A connected component is a set of vertices (stocks) that are linked (correlated) to each other by edges.
         
    Returns:
        int : number of connected components
    """
    # TODO: implement here your approach
    return -1   
    

# Some code to test your approach (if you need)
if __name__ == "__main__":
    prepare("data/small_dataset.txt", 0.05)
    res = query("AAPL", correlation_steps = 2) 
    # It should return ['CHTR', 'VRTX']
    print(res)
    ncc = num_connected_components()
    # It should return 9 
    print(ncc)
