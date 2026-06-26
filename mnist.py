import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = (
    tf.keras.datasets.mnist.load_data()
)

# Normalize data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Build model
model = models.Sequential([
    tf.keras.Input(shape=(28, 28)),

    layers.Flatten(),

    layers.Dense(
        128,
        activation="relu"
    ),

    layers.Dropout(0.2),

    layers.Dense(
        64,
        activation="relu"
    ),

    layers.Dense(
        10,
        activation="softmax"
    )
])

# Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Summary
model.summary()

# Train
history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_split=0.1,
    verbose=1
)

# Evaluate
test_loss, test_acc = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print(f"\nTest Accuracy: {test_acc:.4f}")
print(f"Test Loss: {test_loss:.4f}")

# Predictions
predictions = model.predict(
    x_test,
    verbose=0
)

# First sample
predicted_digit = np.argmax(
    predictions[0]
)

confidence = (
    np.max(predictions[0]) * 100
)

actual_digit = y_test[0]

print(
    f"Actual Digit: {actual_digit}"
)

print(
    f"Predicted Digit: {predicted_digit}"
)

print(
    f"Confidence: {confidence:.2f}%"
)

# Display image
plt.figure(figsize=(5, 5))

plt.imshow(
    x_test[0],
    cmap="binary"
)

plt.title(
    f"Actual: {actual_digit} | "
    f"Predicted: {predicted_digit}\n"
    f"Confidence: {confidence:.2f}%"
)

plt.axis("off")
plt.show()

# Accuracy Graph
plt.figure(figsize=(8, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")
plt.legend()

plt.show()

# Loss Graph
plt.figure(figsize=(8, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()

plt.show()