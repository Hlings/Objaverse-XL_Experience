# Objaverse-XL_Experience

Now, I'm exploring to download the dataset of Objaverse-XL.

The official Huggingface website is (here)[https://huggingface.co/datasets/allenai/objaverse-xl/tree/main].

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
Then you will get some ".glb" files.

3) I use the check_glb.py file to check the status of the ".glb" file.

```python
python check_glb.py
```

4) **Sample the point clouds and visualization**
The sampled point clouds can be obtained throunh sampling vertices or meshes (using open3d). (pip install open3d)

```python
python point_cloud_sampling.py
```




