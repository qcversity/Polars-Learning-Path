import zipfile
import tempfile
import os
import sys
from urllib.request import urlretrieve
from urllib.parse import urlparse, unquote
import pathlib

def download_zipped_csv_data(dataset_root_url, dataname, target_dir=None, local_root_path=None, verbose=False):
    """
    Downloads and extracts a zip file from a given dataset URL.

    Parameters
    ----------
    dataset_root_url : str
        Root URL to the dataset directory.
    dataname : str
        Name of the dataset zip file.
    target_dir : str, optional
        Target directory to store the extracted files. If not provided, uses the dataset name.
    local_root_path : str, optional
        Local root path to store the extracted files. Defaults to the current working directory.
    verbose : bool, optional
        Flag to enable verbose output. Default is False.

    Returns
    -------
    None
    """
    if not local_root_path:
        local_root_path = os.getcwd()

    if target_dir:
        if not os.path.isabs(target_dir):
            home_dir = os.path.expanduser('~')
            target_dir_path = os.path.join(home_dir, target_dir)
        else:
            target_dir_path = target_dir
    else:
        parsed_url = urlparse(dataset_root_url)
        dataset_dir = unquote(os.path.basename(parsed_url.path))
        dataset_dir = pathlib.Path(dataset_dir).stem
        target_dir_path = os.path.join(local_root_path, dataset_dir)

    try:
        dataset_url = os.path.join(dataset_root_url, dataname)

        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)
            if verbose:
                print(f"Created directory: {target_dir_path}")

        with tempfile.TemporaryDirectory() as tmp_dir:
            zip_path = os.path.join(tmp_dir, 'temp.zip')
            urlretrieve(dataset_url, zip_path)

            if verbose:
                print(f"Downloading {dataname}...")

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir_path)
                if verbose:
                    print(f"Extracted to {target_dir_path}")

    except zipfile.BadZipFile:
        if verbose:
            sys.stderr.write("Corrupted zip file encountered, aborting.\n")
        return None
    except Exception as e:
        if verbose:
            sys.stderr.write(f"An error occurred: {e}\n")
        return None