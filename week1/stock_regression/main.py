import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import sys
# add imports as needed

def download_data(ticker):
    # hint: stock_info = yf.Ticker(ticker)
    # call some functions here
    # return a numpy array of the closing prices of the stock
    return []


def pre_process_data(data):
    # turn closing prices into daily returns
    # model input will be 10 days of returns, output is following day's return
    # x_data shape is (len(data)-11, 10), y_data shape is (len(data)-11,)
    # return x_data, y_data
    return [], []


if __name__ == "__main__":
    ticker = "SPY" # stock symbol to train on
    if len(sys.argv) > 1:
        ticker = sys.argv[1]
    
    historical_data = download_data(ticker)
    x_data, y_data = pre_process_data(historical_data)
    
    model = LinearRegression()

    # x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)
    # model.fit(x_data, y_data)

    # for error_formula in [mean_squared_error, mean_absolute_error, mean_absolute_percentage_error]:
    #     print(error_formula.__name__, error_formula(y_data, model.predict(x_data)))

    # print("Ground Truth", "Prediction")
    # y_pred = model.predict(x_test)
    # for i in range(len(x_test)):
    #     print(y_pred[i], y_test[i])

