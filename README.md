# AI Watcher
Cooking....


# Installation of the environment :

```bash
conda create --name AI_Watcher python=3.8
conda activate AI_Watcher
conda install -c anaconda cudatoolkit -y
conda install pytorch-cuda=12.1 -c pytorch -c nvidia -y
conda install pytorch torchvision torchaudio -c pytorch -c nvidia -y
pip install torch torchvision
pip install pycocotools
pip install tqdm opencv-python
```

Install the repository :
```bash
git clone https://github.com/lucas04200/Ai_watcher.git
cd Ai_watcher
```

## TODO
- [ ] Update README

## Citation
RAPiD source code is available for non-commercial use. If you find our code and dataset useful or publish any work reporting results using this source code, please consider citing our paper
```
Z. Duan, M.O. Tezcan, H. Nakamura, P. Ishwar and J. Konrad, 
“RAPiD: Rotation-Aware People Detection in Overhead Fisheye Images”, 
in IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 
Omnidirectional Computer Vision in Research and Industry (OmniCV) Workshop, June 2020.
```
