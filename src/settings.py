from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "STN PLAD"
PROJECT_NAME_FULL: Optional[
    str
] = "STN PLAD: A Dataset for Multi-Size Power Line Assets Detection in High-Resolution UAV Images"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.GNU_GPL_v3(source_url="https://github.com/andreluizbvs/PLAD/blob/main/LICENSE")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.Energy(),
    Domain.DroneInspection(),
]
CATEGORY: Category = Category.EnergyAndUtilities(extra=Category.Drones())

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2021-09-10"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://github.com/andreluizbvs/PLAD"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 402895
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/stn-plad"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Full STN PLAD dataset": "https://github.com/andreluizbvs/PLAD/releases/download/1.0/plad.zip",
    "Labels": "https://github.com/andreluizbvs/PLAD/files/8952243/labels.zip",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://arxiv.org/abs/2108.07944"
CITATION_URL: Optional[str] = "https://github.com/andreluizbvs/PLAD#citing"
AUTHORS: Optional[List[str]] = [
    "Vieira-e-Silva, André Luiz Buarque",
    "de Castro Felix, Heitor",
    "de Menezes Chaves, Thiago",
    "Simões, Francisco Paulo Magalhães",
    "Teichrieb, Veronica",
    "dos Santos, Michel Mozinho",
    "da Cunha Santiago, Hemir",
    "Sgotti, Virginia Adélia Cordeiro",
    "Neto, Henrique Baptista Duffles Teixeira Lott",
]

ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "Sistema de Transmissão do Nordeste S.A., Brazil"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://stnordeste.com.br/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
