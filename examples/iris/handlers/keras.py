import numpy as np

iris_labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]


def pre_inference(sample, metadata):
    return {
        metadata[0].name: [
            sample["sepal_length"],
            sample["sepal_width"],
            sample["petal_length"],
            sample["petal_width"],
        ]
    }


def post_inference(prediction, metadata):
    probabilites = prediction[0][0]
    predicted_class_id = int(np.argmax(probabilites))
    return {
        "class_label": iris_labels[predicted_class_id],
        "class_index": predicted_class_id,
        "probabilities": probabilites,
    }