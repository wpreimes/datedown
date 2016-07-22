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
Interface for the package.
'''

from datedown.down import check_downloaded


def download_by_dt(dts, url_create_fn,
                   fpath_create_fn, download_fn,
                   passes=3):
    """
    Download data for datetimes. If files are missing try
    again passes times.

    Parameters
    ----------
    dts: list
        list of datetime.datetime objects
    url_create_fn: function
        function that creates an URL from a datetime object
    fpath_create_fn: function
        function that creates a filename from a datetime object
    download_fn: function
        function that transfers data from a list
        of URLs to a list of filenames.
        Takes two arguments (url_list, fname_list)
    passes: int, optional
        if files are missing then try again passes times
    """
    urls = map(url_create_fn, dts)
    fnames = map(fpath_create_fn, dts)
    for p in range(passes):
        download_fn(urls, fnames)
        no_urls, no_fnames = check_downloaded(urls, fnames)
        if len(no_urls) == 0:
            break
        else:
            urls = no_urls
            fnames = no_fnames
