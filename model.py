import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Reshape

def build_model():
    model = tf.keras.Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
        Conv2D(64, (3, 3), activation='relu'),
        Conv2D(128, (3, 3), activation='relu'),
        Flatten(),
        Dense(1024, activation='relu'),
        Dense(2048, activation='relu'),
        Dense(4096, activation='relu'),
        Dense(3 * 10000, activation='linear'),  # Assuming output is 10000 vertices with 3 coordinates each
        Reshape((10000, 3))
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

model = build_model()
model.summary()
