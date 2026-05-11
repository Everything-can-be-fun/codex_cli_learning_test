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


def f1_score(tp, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)

    if p + r == 0:
        return 0.0

    return 2 * p * r / (p + r)


def count_detections(pred_boxes, gt_boxes, iou_threshold=0.5):
    matched_gt_indices = set()
    tp = 0
    fp = 0

    for pred_box in pred_boxes:
        best_iou = 0.0
        best_gt_index = None

        for gt_index, gt_box in enumerate(gt_boxes):
            if gt_index in matched_gt_indices:
                continue

            current_iou = iou(pred_box, gt_box)
            if current_iou > best_iou:
                best_iou = current_iou
                best_gt_index = gt_index

        if best_iou >= iou_threshold and best_gt_index is not None:
            tp += 1
            matched_gt_indices.add(best_gt_index)
        else:
            fp += 1

    fn = len(gt_boxes) - tp
    return {"tp": tp, "fp": fp, "fn": fn}
