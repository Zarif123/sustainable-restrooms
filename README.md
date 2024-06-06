# Getting Started
This repository consists of multiple python scripts that is used for preprocessing of audio files. 
The Jupyter Notebook is used for model training, saving of model weights and loading model wieghts.
The requirements.txt holds all the libraries you would need for the python scripts. To run the Jupyter
Notebook, you will also need to install pytorch audio.

## Preprocessing Data
sound.py is the python script that allows you to quantize an audio file to the specified bit. You can 
use this through the command line or import the file and use the functions in your own script like. 
converter.py gives a good example. audio_segment.py can also be used through the command line or imported 
into another python script. Its main job is to split the given audio file into a specified length. For
both sound.py and audio_segment.py you can run the code below to see what the command line inputs are.
converter.py and out_to_training_script.py are examples on how to use these preprocessing scripts in another
script.

```
py PYTHON_SCRIPT_HERE -h
```
or
```
python3 PYTHON_SCRIPT_HERE -h
```

## Running Model
Our model can be ran in the Python notebook preprocessing.ipynb. It will take in data from our training_set and testing_set folders and process them so
that they are useable for our model. We also take in speech data from HuggingFace. Our model is a convolutional neural network that will take in audio
data in the form of spectrograms. Our model's parameters, training, and testing functions can all be adjusted. For testing, we input segments of an audio file
and see what our model predicts is the class for each segment.
