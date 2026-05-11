import pytest

from src.detection_metrics import (
    box_area,
    count_detections,
    f1_score,
    iou,
    precision,
    recall,
)


def test_box_area_normal_box():
    assert box_area([0, 0, 10, 10]) == 100


def test_box_area_invalid_box():
    assert box_area([10, 10, 0, 0]) == 0


def test_iou_identical_boxes():
    assert iou([0, 0, 10, 10], [0, 0, 10, 10]) == 1.0


def test_iou_no_overlap():
    assert iou([0, 0, 10, 10], [20, 20, 30, 30]) == 0.0


def test_precision():
    assert precision(8, 2) == 0.8


def test_recall():
    assert recall(8, 2) == 0.8


def test_f1_score():
    assert f1_score(8, 2, 2) == pytest.approx(0.8)


def test_f1_score_zero_precision_and_recall():
    assert f1_score(0, 0, 0) == 0.0


def test_count_detections_one_match():
    pred_boxes = [[0, 0, 10, 10]]
    gt_boxes = [[0, 0, 10, 10]]

    assert count_detections(pred_boxes, gt_boxes) == {"tp": 1, "fp": 0, "fn": 0}


def test_count_detections_no_predictions():
    pred_boxes = []
    gt_boxes = [[0, 0, 10, 10]]

    assert count_detections(pred_boxes, gt_boxes) == {"tp": 0, "fp": 0, "fn": 1}


def test_count_detections_no_ground_truths():
    pred_boxes = [[0, 0, 10, 10]]
    gt_boxes = []

    assert count_detections(pred_boxes, gt_boxes) == {"tp": 0, "fp": 1, "fn": 0}


def test_count_detections_one_gt_matches_only_once():
    pred_boxes = [[0, 0, 10, 10], [0, 0, 10, 10]]
    gt_boxes = [[0, 0, 10, 10]]

    assert count_detections(pred_boxes, gt_boxes) == {"tp": 1, "fp": 1, "fn": 0}
