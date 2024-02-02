from setuptools import setup, find_packages

setup(
    name="siamese",
    py_modules=["siamese"],
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scipy",
        "numpy",
        "matplotlib",
        "opencv_python",
        "tqdm",
        "Pillow",
        "h5py",
    ],
)
