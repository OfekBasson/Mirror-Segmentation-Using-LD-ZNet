from setuptools import setup, find_packages

setup(
    name='ld-znet',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'numpy',
        'tqdm',
        'matplotlib',
        'pillow',
        'opencv-python',
        'einops',
        'omegaconf',
        'pytorch-lightning==1.6.5',
        'transformers',
        "kornia",
        "gdown",
        "diffusers"
    ],
)
