if __name__ == '__main__':
    chart = Chart()

def main():
 df = pd.read_csv(r"C:\Users\U01_LEECHSEED\Downloads\lightweightcharts\ohlcv.csv")
    chart.set(df)
    
    chart.show(block=True)