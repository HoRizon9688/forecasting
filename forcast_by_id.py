from pandas import read_csv

# series = read_csv('./test_dataset/test_data.csv')
# raw_values = series['price'].values
# print(series)
# print(raw_values)



def get_price_by_id(id, df):
    selected_df = df[(id-1) * 48:(id-1) * 48 + 48]
    raw_values = selected_df['price'].values
    raw_values = raw_values.reshape(len(raw_values),)
    return raw_values


df = read_csv('./test_dataset/merge_data.csv', usecols=[1, 2])
print(get_price_by_id(1, df))
