from . import utils
# Global data to store information
your_variables_here = ""

def prepare(filename : str):
    print('Reading file {}'.format(filename))

    # Read from file and store into global data
    global your_variables_here
    your_variables_here = 'Somebody'

    # Read your file here and put the needed data into "your_variables_here".
    # you can also create complex data-structures here, if you need
    print('Done'.format(filename))


def stock_timeseries(stock : str):
    print('Building time-series for stock : {}'.format(stock))
    # Search into global data the prices and days of the input stock
    if stock in your_variables_here:
        days = [1, 2, 3]  # find the correct data - manipulate data
        prices = [100, 150, 130]  # find the correct data - manipulate data
    else:
        # no data available
        days = [1, 2, 3]  # find the correct data - manipulate data
        prices = [100, 150, 130]  # find the correct data - manipulate data

    # NOTE: please return these value with the following order: days, prices
    return days, prices


