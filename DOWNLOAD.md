Dataset **STN PLAD** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/2/f/P8/0n223CRcjisZMvyX96ggm5gWrZUk7ARe59phSsHdHNo4zhQ0vW9CcU8Fd4JVLBrtMkzSv01kl37Nvcz6FkDW2uFhK8pul3TSICD6FBJBddkwFcuFpQkyMdbPnPSW.tar)

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
