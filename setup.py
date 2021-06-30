from os.path import join, exists, dirname, realpath
from setuptools import setup
import os, sys

# validate python version
if sys.version_info < (3,6):
  sys.exit('Sorry, PixPlot requires Python 3.6 or later')

# populate list of all paths in `./pixplot/web`
web = []
dirs = [join('pixplot', 'web'), join('pixplot', 'models')]
for i in dirs:
  for root, subdirs, files in os.walk(i):
    if not files: continue
    for file in files:
      web.append(join(root.replace('pixplot/', '').replace('pixplot\\',''), file))

setup(
  name='pixplot',
  version='0.0.109',
  packages=['pixplot'],
  package_data={
    'pixplot': web,
  },
  keywords = ['computer-vision', 'webgl', 'three.js', 'tensorflow', 'machine-learning'],
  description='Visualize large image collections with WebGL',
  url='https://github.com/kruus/pix-plot',
  author='Douglas Duhaime',
  author_email='douglas.duhaime@gmail.com',
  license='MIT',
  install_requires=[
    #'tensorflow==1.14.0', to support "pose" module
    #'h5py==2.10.0', # let this requirement come from tensorflow
    #'Keras<=2.3.0', # python 3.9 likes keras >= 2.4.3
    #'umap-learn>=0.5.1', # was ==, manually install "constraint" fork from kruus/
    'tensorflow-gpu>=2.4.1',
    'Keras==2.4.3',
    #'tensorflow>=2.2.0',
    #'Keras<=2.3.0',
    'cmake>=3.15.3',
    'Cython>=0.29.21',
    'glob2>=0.6',
    'iiif-downloader>=0.0.6',
    'numba>=0.51.2', # was ==
    'numpy>=1.16.0',
    'Pillow>=6.1.0',
    'pointgrid>=0.0.2',
    'python-dateutil>=2.8.0',
    'scikit-learn>=0.24.2', # was ==
    'scipy>=1.4.0', # was ==
    'yale-dhlab-rasterfairy>=1.0.3',    # or pip install rasterfairy-py3 ?
    'yale-dhlab-keras-preprocessing>=1.1.1', # ? some local fork ?
    'matplotlib',
  ],
  entry_points={
    'console_scripts': [
      'pixplot=pixplot:parse',
    ],
  },
)
