Dataset **STN PLAD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/ptyogge5s8f7sqgkrokw7/stn-plad-DatasetNinja.tar?rlkey=ob1lpl6vgew281lhvc2p3uxq9&dl=1)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='STN PLAD', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Full STN PLAD dataset](https://github.com/andreluizbvs/PLAD/releases/download/1.0/plad.zip)
- [Labels](https://github.com/andreluizbvs/PLAD/files/8952243/labels.zip)
