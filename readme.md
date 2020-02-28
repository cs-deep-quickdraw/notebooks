# Notebooks

This repository contains the codes used for the study on the quickdraw dataset conducted for the CentraleSupélec Deep Learning class.

## Introduction

The goal of the project was to train models to classify elements from the [quickdraw dataset](https://quickdraw.withgoogle.com/data).

[Quickdraw](https://quickdraw.withgoogle.com/) is a game release by Google that prompts the participant with the name of an item  (for instance drums), the participant then has 20 seconds to draw it and make a neural network guess the correct item name. Thanks to this game, the Quickdraw team collected a lot of annotated images and made them available publicly, there are 345 different items and each has at least $100,000$ samples.

## Description

The notebooks are located in the `notebooks/` directory:
- [lstm_quickdraw.ipynb](./notebooks/lstm_quickdraw.ipynb) is used for the training of LSTMs on the strokes data
- [strokes2image_quickdraw.ipynb](./notebooks/strokes2image_quickdraw.ipynb) is used for the training of CNNs on images generated from strokes
- TODO: desc of CNN notebook

To be able to run the notebooks you will need the following dependencies:
- pytorch
- torchvision
- opencv
- numpy

For a detailed list of dependencies, you can have a look at [this file](./mesocentre/config/environment.yml)

Results can be found in the `results/` directory in `markdown` files, there is also a helper script to generate graphs of results.

Finally in the `mesocentre/` are the configuration for running the training jobs on a [PBS](https://en.wikipedia.org/wiki/Portable_Batch_System) queue, as well as a [conda](https://docs.conda.io/en/latest/) environment configuration
