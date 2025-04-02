#!/bin/bash
#SBATCH --job-name=train_model
#SBATCH --partition=dgx-small
#SBATCH --mem=16G
#SBATCH --time=8:00:00
#SBATCH --output=output_%j.log
#SBATCH --error=error_%j.log

module load cuda

python main.py --config ./config/RawGATST_baseline.conf
