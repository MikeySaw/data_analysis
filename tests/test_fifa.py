import numpy as np
import pandas as pd
import re 
import pytest
import os

from fifa21.make_dataset import main
from tests import _PATH_DATA_FIFA


@pytest.mark.skipif(not os.path.exists(_PATH_DATA_FIFA), reason="Data files not found")
def test_fifa_data_loading():
    data = pd.read_csv(os.path.join(_PATH_DATA_FIFA, "raw/fifa21_raw_data_v2.csv"))
    assert data is not None, "Load the dataset"


@pytest.mark.skipif(not os.path.exists(_PATH_DATA_FIFA), reason="Data files not found")
def test_make_dataset():
    data = pd.read_csv(os.path.join(_PATH_DATA_FIFA, "raw/fifa21_raw_data_v2.csv"))
    main(data)


