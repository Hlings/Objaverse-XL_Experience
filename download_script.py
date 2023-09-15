
"""

import objaverse_xl
import multiprocessing

df = objaverse_xl.load_smithsonian_metadata()
urls = df["url"].tolist()
print("the length of smithsonian_metadata is ", len(urls))
urls_sample = urls[:5]

paths = objaverse_xl.download_smithsonian_objects(urls)

"""

import os
import shutil

import fsspec
import pandas as pd

from objaverse_xl.smithsonian import SmithsonianDownloader

def test_download_objects():
    downloaders = [
        # GitHubDownloader(),
        # SketchfabDownloader(),
        SmithsonianDownloader(),
        # ThingiverseDownloader(),
    ]

    # download_dir = '~/.objaverse-tests'
    download_dir = './objaverse-tests'

    for downloader in downloaders:
        shutil.rmtree(os.path.expanduser(download_dir), ignore_errors=True)

        annotations_df = downloader.get_annotations()

        # df.head(n=5) means return the top5 files
        test_objects = annotations_df.head(n=5)

        out = downloader.download_objects(
            objects=test_objects,
            download_dir=download_dir,
            processes=2,
        )
        assert isinstance(out, dict), f"{out=}"

test_download_objects()







