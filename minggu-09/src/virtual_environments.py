# cara membuat lingkungan virtual dengan anaconda
conda create --name tutorial-env python=3.11
# output:
# Collecting package metadata (current_repodata.json): done
# Solving environment: done


# ==> WARNING: A newer version of conda exists. <==
#   current version: 23.3.1
#   latest version: 23.5.0

# Please update conda by running

#     $ conda update -n base -c defaults conda

# Or to minimize the number of packages updated during conda update use

#      conda install conda=23.5.0



# ## Package Plan ##

#   environment location: C:\Users\ianma\anaconda3\envs\tutorial-env

#   added / updated specs:
#     - python=3.11


# The following packages will be downloaded:

#     package                    |            build
#     ---------------------------|-----------------
#     ca-certificates-2023.05.30 |       haa95532_0         120 KB
#     libffi-3.4.4               |       hd77b12b_0         113 KB
#     openssl-3.0.9              |       h2bbff1b_0         7.4 MB
#     pip-23.1.2                 |  py311haa95532_0         3.4 MB
#     python-3.11.3              |       he1021f5_1        17.9 MB
#     setuptools-67.8.0          |  py311haa95532_0         1.4 MB
#     sqlite-3.41.2              |       h2bbff1b_0         894 KB
#     tzdata-2023c               |       h04d1e81_0         116 KB
#     wheel-0.38.4               |  py311haa95532_0          96 KB
#     xz-5.4.2                   |       h8cc25b3_0         592 KB
#     ------------------------------------------------------------
#                                            Total:        32.0 MB

# The following NEW packages will be INSTALLED:

#   bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
#   ca-certificates    pkgs/main/win-64::ca-certificates-2023.05.30-haa95532_0
#   libffi             pkgs/main/win-64::libffi-3.4.4-hd77b12b_0
#   openssl            pkgs/main/win-64::openssl-3.0.9-h2bbff1b_0
#   pip                pkgs/main/win-64::pip-23.1.2-py311haa95532_0
#   python             pkgs/main/win-64::python-3.11.3-he1021f5_1
#   setuptools         pkgs/main/win-64::setuptools-67.8.0-py311haa95532_0
#   sqlite             pkgs/main/win-64::sqlite-3.41.2-h2bbff1b_0
#   tk                 pkgs/main/win-64::tk-8.6.12-h2bbff1b_0
#   tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0
#   vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
#   vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
#   wheel              pkgs/main/win-64::wheel-0.38.4-py311haa95532_0
#   xz                 pkgs/main/win-64::xz-5.4.2-h8cc25b3_0
#   zlib               pkgs/main/win-64::zlib-1.2.13-h8cc25b3_0


# Proceed ([y]/n)? y


# Downloading and Extracting Packages

# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate tutorial-env
#
# To deactivate an active environment, use
#
#     $ conda deactivate

# Mengaktifkan environment
conda activate tutorial-env
# output:
(tutorial-env) PS C:\Users\ianma>

# REPL
python
# output:
Python 3.11.3 | packaged by Anaconda, Inc. | (main, May 15 2023, 15:41:31) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

import sys
sys.path
# output:
# ['', 'C:\\Users\\ianma\\anaconda3\\envs\\tutorial-env\\python311.zip', 'C:\\Users\\ianma\\anaconda3\\envs\\tutorial-env\\DLLs', 'C:\\Users\\ianma\\anaconda3\\envs\\tutorial-env\\Lib', 'C:\\Users\\ianma\\anaconda3\\envs\\tutorial-env', 'C:\\Users\\ianma\\anaconda3\\envs\\tutorial-env\\Lib\\site-packages']

# deactivate
conda deactivate
# output:
(base) PS C:\Users\ianma>

# Mengelola Paket dengan pip
python -m pip install novas
python -m pip install requests==2.6.0
# output
# Collecting requests==2.6.0
#   Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
#      ---------------------------------------- 469.8/469.8 kB 1.1 MB/s eta 0:00:00
# Installing collected packages: requests
# Successfully installed requests-2.6.0

python -m pip show requests
# output
# Name: requests
# Version: 2.6.0
# Summary: Python HTTP for Humans.
# Home-page: http://python-requests.org
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.com
# License: Apache 2.0
# Location: C:\Users\ianma\anaconda3\envs\tutorial-env\Lib\site-packages
# Requires:
# Required-by:

python -m pip list
# output:
# Package    Version
# ---------- -------
# ez-setup   0.9
# pip        23.1.2
# requests   2.6.0
# setuptools 67.8.0
# wheel      0.38.4