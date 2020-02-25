module load anaconda3/5.3.1
module load cuda/9.0
conda create --name quickdraw python=3.7.4
source activate quickdraw
cd $PBS_O_WORKDIR
conda install pandas
conda install pytorch torchvision cudatoolkit=9.2 -c pytorch
conda install opencv
conda install numpy
conda env export > config/environment.yml # save conda environment description
