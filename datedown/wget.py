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
Interface to wget command line utility.
'''

import subprocess


def download(url, store_at, username=None, password=None, cookie_file=None):
    """
    Download a url using wget.
    Retry as often as necessary and store cookies if
    authentification is necessary.

    Parameters
    ----------
    url: string
        URL to download
    store_at: string
        path on local filesystem where to store the results
    username: string, optional
        username
    password: string, optional
        password
    cookie_file: string, optional
        file where to store cookies
    """
    cmd_list = ['wget',
                url,
                '-r',
                '-P', store_at,
                '--retry-connrefused']

    if username is not None:
        cmd_list.append('--user={}'.format(username))
    if password is not None:
        cmd_list.append('--password={}'.format(password))
    if cookie_file is not None:
        cmd_list = cmd_list + [
            '--load-cookies', cookie_file,
            '--save-cookies', cookie_file,
            '--keep-session-cookies']

    subprocess.call(cmd_list)
