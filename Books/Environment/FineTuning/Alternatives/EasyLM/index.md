# EasyLM

EasyLM will be our fine-tuning manager, where I want to avoid TensorFlow, Hugging Face and their dependencies: we don't run into supporting _two_ packages for the same purpose, and we try to make it _feel_ open source, our platform in it's completeness.


Installing EasyLM:
- Follow the instructions to clone it from GitHub
- From command line, install python dependencies such as: pip install jax jaxlib flax optax numpy tqdm
- Do not install hugging face and tensorflow services: pip install tensorflow tensorboard datasets
  - It's important that your work does not get "addicted": you might unconsciously start depending on installations in case you have them installed specifically for this purpose.
