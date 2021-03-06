#!/bin/bash

#PBS -S /bin/bash
#PBS -N quickdraw_train
#PBS -j oe
#PBS -l walltime=24:00:00
#PBS -q gpuq -l select=1:ncpus=12:ngpus=1:gputype=p100:mem=100gb
#PBS -M sami.tabet@student.ecp.fr
#PBS -m abe
#PBS -q gpuq
#PBS -P test

# Go to the directory where the job has been submitted 
cd $PBS_O_WORKDIR
[ ! -d output ] && mkdir output

# Module load 
module load anaconda3/5.3.1

# Activate anaconda environment code
source activate quickdraw

# Train the network
python imgen_resnet_quickdraw.py
