import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import helper
import numpy as np
import plotly.express as px
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM

csv_file_path = "/Users/vaniachow/Downloads/query_result_2023-05-16T07_29_53.719636Z.csv"
df = pd.read_csv(csv_file_path)
df = df.drop(['created_at_pst'], axis=1)
store_lat, store_long = 34.068866, -118.449074

## Data Cleaning
columns1 = ['dispatch_time', 'customer_location', 'longitude', 'latitude', 'trip_id', 'courier_id']
df_delivery = df[columns1]
df_delivery['distance'] = np.nan
df_delivery['items_per_trip'] = np.nan
for i in range(len(df_delivery)):
    df_delivery.loc[i, 'distance'] = helper.distcalculate(store_lat, store_long, df_delivery.loc[i, 'latitude'], df_delivery.loc[i, 'longitude'])
    df_delivery.loc[i, 'items_per_trip'] = helper.items_trip(df_delivery)
## Identifying relationships between data
figure_dist = px.scatter(data_frame=df_delivery,
                    x="distance",
                    y="dispatch_time",
                    size="dispatch_time",
                    trendline="ols",
                    title="Relationship Between Time Taken and Distance")
figure_num_items = px.scatter(data_frame=df_delivery,
                    x="items_per_trip",
                    y="dispatch_time",
                    size="dispatch_time",
                    trendline="ols",
                    title="Relationship Between Time Taken and Num Items")

#Building an LSTM Model to Make Predictions
x = np.array(df_delivery[["distance", "items_per_trip"]])
y = np.array(df_delivery[["dispatch_time"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.20,
                                                random_state=33)
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape= (xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=9)

print("Order Delivery Time Prediction using LSTM")
a = float(input("Distance: "))
b = int(input("Items per trip: "))
features = np.array([[a, b]])
delivery_time = model.predict(features)
print("Estimated delivery time:", delivery_time)