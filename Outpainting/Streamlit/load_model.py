from tensorflow.keras import Model, models

def load_model(model_path_gen,model_path_dis)
    """
    load the latest saved model
    """


    model_generator = models.load_model(model_path_gen)
    print("\n✅ generator loaded from ComputeEngine")

    model_discriminator = models.load_model(model_path_dis)

    print("\n✅ discriminator loaded from ComputeEngine")

    return model_generator, model_discriminator
