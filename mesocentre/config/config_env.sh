module load anaconda3/5.3.1
module load cuda/9.0
conda create --name quickdraw
source activate quickdraw
cd $PBS_O_WORKDIR
conda install cudatoolkit=8.0=3
conda install quickdraw
conda install pandas
conda install torch
conda install numpy
conda env export > config/environment.yml # save conda environment description
