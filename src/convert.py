# https://github.com/andreluizbvs/PLAD

import glob
import os
from collections import defaultdict

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from supervisely.io.json import load_json_file

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "PLAD"
dataset_path = "./APP_DATA/plad"
ann_json_name = "annotations.json"
batch_size = 10
ds_name = "ds"
images_ext = ".JPG"


def create_ann(image_path, img_name_to_id, id_to_bbox_data):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    image_name = get_file_name_with_ext(image_path)
    image_id = img_name_to_id.get(image_name)

    if image_id is not None:
        curr_im_bboxes = id_to_bbox_data[image_id]
        for curr_bbox in curr_im_bboxes:
            obj_class_id = curr_bbox[0]
            obj_class = idx_to_class[obj_class_id]

            bbox = curr_bbox[1]

            left = bbox[0]
            right = bbox[0] + bbox[2]
            top = bbox[1]
            bottom = bbox[1] + bbox[3]
            rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
            label = sly.Label(rectangle, obj_class)
            labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class_tower = sly.ObjClass("tower", sly.Rectangle)
obj_class_insulator = sly.ObjClass("insulator", sly.Rectangle)
obj_class_spacer = sly.ObjClass("spacer", sly.Rectangle)
obj_class_damper = sly.ObjClass("damper", sly.Rectangle)
obj_class_plate = sly.ObjClass("plate", sly.Rectangle)

idx_to_class = {
    0: obj_class_tower,
    1: obj_class_insulator,
    2: obj_class_spacer,
    3: obj_class_damper,
    5: obj_class_plate,
}


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    ann_json_path = os.path.join(dataset_path, ann_json_name)
    anns_data = load_json_file(ann_json_path)

    img_name_to_id = {}
    id_to_bbox_data = defaultdict(list)

    for img_data in anns_data["images"]:
        img_name_to_id[img_data["file_name"].split("/")[1]] = img_data["id"]

    for bbox_data in anns_data["annotations"]:
        id_to_bbox_data[bbox_data["image_id"]].append((bbox_data["category_id"], bbox_data["bbox"]))

    images_pathes = glob.glob(dataset_path + "/*/*.JPG")

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

    for img_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
        img_names_batch = [get_file_name_with_ext(im_path) for im_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [
            create_ann(image_path, img_name_to_id, id_to_bbox_data)
            for image_path in img_pathes_batch
        ]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))

    return project
