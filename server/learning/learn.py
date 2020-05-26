import logging
import os

import tensorflow as tf
import matplotlib.pyplot as plt

# from django.conf import settings
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator


MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_model/')
# MODEL_DIR = settings.MODEL_DIR

batch_size = 10
epochs = 15
IMG_HEIGHT = 150
IMG_WIDTH = 150

PATH_MOUTH = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '/ShoppingAppTraining/mouthwash/')
PATH_TP = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '/ShoppingAppTraining/toothpaste/')
PATH_ALL = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), '/ShoppingAppTraining/')

def run_training():
    num_mouthwashes = len(os.listdir(PATH_MOUTH))
    num_tps = len(os.listdir(PATH_TP))

    total_train = num_mouthwashes + num_tps

    print(f"The total number of items is {total_train}.")

    train_image_generator = ImageDataGenerator(rescale=1./255)  # Generator for our training data

    train_data_gen = train_image_generator.flow_from_directory(
        batch_size=batch_size,
        directory=PATH_ALL,
        shuffle=True,
        target_size=(
            IMG_HEIGHT, IMG_WIDTH),
        class_mode='binary'
    )
    sample_training_images, _ = next(train_data_gen)

    model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu',
            input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1)
    ])

    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=['accuracy']
    )

    model.summary()

    # Fit
    history = model.fit_generator(
        train_data_gen,
        steps_per_epoch=total_train // batch_size,
        epochs=epochs,
        validation_data=train_data_gen,
        validation_steps=total_train // batch_size
    )

    # Visualise results
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs_range = range(epochs)

    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    # Fetch the Keras session and save the model
    # The signature definition is defined by the input and output tensors,
    # and stored with the default serving key

    version = 1
    export_path = MODEL_DIR

    print('export_path = {}\n'.format(export_path))

    tf.keras.models.save_model(
        model,
        export_path,
        overwrite=True,
        include_optimizer=True,
        save_format=None,
        signatures=None,
        options=None
    )
