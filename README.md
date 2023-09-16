# Objaverse-XL_Experience

Now, I'm exploring to download the dataset of Objaverse-XL.

The official Huggingface website is [here](https://huggingface.co/datasets/allenai/objaverse-xl/tree/main).

## Something to do for downloading the dataset

0) Clone the objaverse-xl repository.

```python
git clone https://huggingface.co/datasets/allenai/objaverse-xl
```

1) Before using the test_api.py, you need to install the "pyarrow" or "fastparquet". I attempt the fastparquet and it works.

```python
pip install fastparquet
```

2) Use the script "download_script_test.py" for testing the downloading and get some examples of smithsonian subdataset.

```python
python download_script_test.py
```
Then, you will get some ".glb" files.

3) I use the check_glb.py file to check the status of the ".glb" file.

```python
python check_glb.py
```

4) **Sample the point clouds and visualization**

a) Sampling

The sampled point clouds can be obtained through sampling vertices or meshes (using open3d). (pip install open3d)

**The trimesh is preferred.** The code is referred by the openshape demo, from [here](https://huggingface.co/OpenShape/openshape-demo-support/blob/main/openshape/demo/misc_utils.py).

```python
python point_cloud_sampling.py
```

Note, I tried the smithsonian sub-dataset, but the first five files (.glb) seem not to be read by open3d, and similar errors are reported by trimesh. The ".glb" contains the color inforamtion.

I turn to try the thingiverse sub-dataset. The format is ".stl", which doesn't have any color information. I'm not sure about the effect of the color on rendering and point cloud-image-text contrastive learning.


b) Visualization (TODO)






