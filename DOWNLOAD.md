Dataset **STN PLAD** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/w/l/AJ/jEFYpS8kGivKVygJ0oCjbdbjN2xK7bORwSfxPM2oy3l8k1EM0XAa2xPb9f1v3CcaOaFIrYwEb1bdm87E67eEdIWnYpYi5Ygx9825N1h0sARI29AcEB5LQnBy4HAK.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='STN PLAD', dst_path='~/dtools/datasets/STN PLAD.tar')
```
The data in original format can be downloaded here:

- 🔗[images](https://github.com/andreluizbvs/PLAD/releases/download/1.0/plad.zip)
- 🔗[labels](https://github.com/andreluizbvs/PLAD/files/8952243/labels.zip)
