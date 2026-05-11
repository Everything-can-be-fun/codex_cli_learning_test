def box_area(box):
    """Compute area of a box in xyxy format: [x1, y1, x2, y2]."""
    x1, y1, x2, y2 = box
    return max(0, x2 - x1) * max(0, y2 - y1)


def iou(box_a, box_b):
    """Compute IoU between two boxes in xyxy format."""
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)

    inter_area = box_area([inter_x1, inter_y1, inter_x2, inter_y2])
    union_area = box_area(box_a) + box_area(box_b) - inter_area

    if union_area == 0:
        return 0.0

    return inter_area / union_area


def precision(tp, fp):
    if tp + fp == 0:
        return 0.0
    return tp / (tp + fp)


def recall(tp, fn):
    if tp + fn == 0:
        return 0.0
    return tp / (tp + fn)
