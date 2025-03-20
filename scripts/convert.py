import re

def convert_bbox_to_yolo(bbox, image_width, image_height):
    x_min, y_min, x_max, y_max = bbox
    bbox_height = y_max - y_min
    bbox_width = x_max - x_min
    x_center = (x_max + x_min)/2.0
    y_center = (y_max + y_min)/2.0

    normalized_x = x_center / image_width
    normalized_y = y_center / image_height
    normalized_width = bbox_width / image_width
    normalized_height = bbox_height / image_height

    return normalized_x, normalized_y, normalized_width, normalized_height


def convert_pickle_to_yolo(pickle_data, image_width, image_height):
    bbox_info = re.search(r'bbox: BoundingBox: <\((.*?), (.*?), (.*?), (.*?)\)', pickle_data)
    class_id_info = re.search(r'category: Category: <id: (.*?),', pickle_data)
    pred_info = re.search(r'score: PredictionScore: <value: (.*?)>,', pickle_data)

    if bbox_info and class_id_info:
        bbox = tuple(map(float, bbox_info.groups()))
        class_id = int(class_id_info.group(1))
        pred_id = float(pred_info.group(1))

        yolo_data = convert_bbox_to_yolo(bbox, image_width, image_height)
        yolo_txt = f"{class_id} {' '.join(map(str, yolo_data))} {pred_id}"
        return yolo_txt
    else:
        return None