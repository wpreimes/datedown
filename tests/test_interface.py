# The MIT License (MIT)
#
# Copyright (c) 2016,Christoph Paulik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
Tests for the interface including.

We host the test_data directory during the test.
'''

from datetime import datetime
from functools import partial
import os
import shutil

from datedown.urlcreator import create_dt_url
from datedown.fname_creator import create_dt_fpath
from datedown.interface import download_by_dt
from datedown.down import download

from subprocess import Popen
import pytest


@pytest.fixture
def temp_http_server(request):
    pdir = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    p = Popen(["python", "-m", "SimpleHTTPServer", "8888"])
    os.chdir(pdir)

    def func():
        p.terminate()
    request.addfinalizer(func)


@pytest.fixture
def output_path(request):

    output_path = os.path.join(os.path.dirname(__file__), "output")

    def cleanup():
        shutil.rmtree(output_path)

    try:
        cleanup()
    except OSError:
        pass

    request.addfinalizer(cleanup)

    return output_path


def test_interface(output_path, temp_http_server):
    dts = [datetime(2000, 1, 1),
           datetime(2000, 1, 2),
           datetime(2000, 2, 1)]
    fname = "file_%Y_%m_%d.txt"
    subdirs = ["test_data",
               "year_month_subfolders",
               '%Y', '%m']
    url_create_fn = partial(create_dt_url, root="http://localhost:8888",
                            fname=fname, subdirs=subdirs)
    fname_create_fn = partial(create_dt_fpath, root=output_path,
                              fname=fname)
    download_by_dt(dts, url_create_fn,
                   fname_create_fn, download)

    fnames_should = map(fname_create_fn, dts)
    for fname_should in fnames_should:
        assert os.path.exists(fname_should)
