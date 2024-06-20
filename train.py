def train_model(model, images, stl_data, epochs=50, batch_size=32):
    vertices = np.array([data[0] for data in stl_data])  # Extract vertices
    model.fit(images, vertices, epochs=epochs, batch_size=batch_size)

train_model(model, images, stl_data)
