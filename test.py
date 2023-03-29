from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# Get current hour
currHour = datetime.now().hour
print(currHour)

# Input data
data = pd.DataFrame(columns=['HR', 'T2M', 'RH2M'])

# Scale data into the range of 0-23
scaler = MinMaxScaler(feature_range=(0, 23))

# load Deep learning model
loadedModel = keras.models.load_model('deeplearning.h5')
