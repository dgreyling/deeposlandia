"""Test config setup for training dataset handling
"""

import json
import os
import pytest


@pytest.fixture
def nb_channels():
    return 3


@pytest.fixture
def kernel_size():
    return 3


@pytest.fixture
def conv_depth():
    return 8


@pytest.fixture
def conv_strides():
    return 2


@pytest.fixture
def pool_strides():
    return 2


@pytest.fixture
def pool_size():
    return 2


@pytest.fixture
def mapillary_image_size():
    return 224


@pytest.fixture
def mapillary_input_config():
    return "tests/data/mapillary/config_aggregate.json"


@pytest.fixture
def mapillary_sample_config():
    return "tests/data/mapillary/training.json"


@pytest.fixture
def mapillary_raw_sample():
    """Sample of Mapillary original images (called for populate a Mapillary
    dataset)
    
    """
    return "tests/data/mapillary/sample/"


@pytest.fixture
def mapillary_sample():
    """Sample of preprocessed Mapillary images
    """
    return "tests/data/mapillary/training/"


@pytest.fixture
def mapillary_sample_without_labels_dir():
    return "tests/data/mapillary/sample_no_label/"


@pytest.fixture
def mapillary_nb_images(mapillary_sample):
    return len(os.listdir(os.path.join(mapillary_sample, "images")))


@pytest.fixture
def mapillary_nb_labels(mapillary_input_config):
    with open(mapillary_input_config) as fobj:
        config = json.load(fobj)
    return len(config["labels"])


@pytest.fixture(scope='session')
def mapillary_config(tmpdir_factory):
    return tmpdir_factory.getbasetemp().join('mapillary.json')


@pytest.fixture(scope='session')
def mapillary_temp_dir(tmpdir_factory):
    mapillary_subdir = tmpdir_factory.mktemp('mapillary', numbered=False)
    tmpdir_factory.mktemp('mapillary/images', numbered=False)
    tmpdir_factory.mktemp('mapillary/labels', numbered=False)
    tmpdir_factory.mktemp('mapillary/checkpoints', numbered=False)
    return mapillary_subdir


@pytest.fixture
def shapes_image_size():
    return 64


@pytest.fixture
def shapes_nb_images():
    return 10


@pytest.fixture
def shapes_nb_labels():
    return 4


@pytest.fixture(scope='session')
def shapes_config(tmpdir_factory):
    return tmpdir_factory.getbasetemp().join('shapes.json')


@pytest.fixture
def shapes_sample_config():
    return "tests/data/shapes/training.json"


@pytest.fixture
def shapes_sample():
    return "tests/data/shapes/training/"


@pytest.fixture(scope='session')
def shapes_temp_dir(tmpdir_factory):
    shapes_subdir = tmpdir_factory.mktemp('shapes', numbered=False)
    tmpdir_factory.mktemp('shapes/images', numbered=False)
    tmpdir_factory.mktemp('shapes/labels', numbered=False)
    tmpdir_factory.mktemp('shapes/checkpoints', numbered=False)
    return shapes_subdir

@pytest.fixture(scope='session')
def datapath_repo(tmpdir_factory):
    datapath_subdir = tmpdir_factory.mktemp('datapath', numbered=False)
    return datapath_subdir
