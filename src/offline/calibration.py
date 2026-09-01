"""Calibration and Validation Harness for Flood Depth Surrogates.

Evaluates flood predictions against held-out SWMM runs and real incident reports:
- POD (Probability of Detection) = TP / (TP + FN)
- FAR (False Alarm Rate) = FP / (TP + FP)
- CSI (Critical Success Index / Threat Score) = TP / (TP + FP + FN)
- MAE / RMSE on water depth (cm).
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
import numpy as np

from src.config import settings


class CalibrationHarness:
    """Calculates formal hydrological verification metrics for flood nowcasting."""

    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = output_dir or settings.CALIBRATION_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def compute_contingency_metrics(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        threshold_cm: float,
    ) -> Dict[str, float]:
        """Calculates 2x2 contingency table metrics for flood occurrence at threshold."""
        obs_flood = (y_true >= threshold_cm)
        pred_flood = (y_pred >= threshold_cm)

        tp = float(np.sum(obs_flood & pred_flood))
        fp = float(np.sum((~obs_flood) & pred_flood))
        fn = float(np.sum(obs_flood & (~pred_flood)))
        tn = float(np.sum((~obs_flood) & (~pred_flood)))

        pod = tp / (tp + fn) if (tp + fn) > 0 else 1.0
        far = fp / (tp + fp) if (tp + fp) > 0 else 0.0
        csi = tp / (tp + fp + fn) if (tp + fp + fn) > 0 else 1.0

        return {
            "threshold_cm": threshold_cm,
            "true_positives": tp,
            "false_positives": fp,
            "false_negatives": fn,
            "true_negatives": tn,
            "POD": round(pod, 4),
            "FAR": round(far, 4),
            "CSI": round(csi, 4),
        }

    def evaluate_surrogate(
        self,
        ground_truth_depths: np.ndarray,
        predicted_depths: np.ndarray,
        thresholds: List[float] = [5.0, 15.0],
    ) -> Dict[str, any]:
        """Runs full calibration verification across multiple severity thresholds."""
        mae = float(np.mean(np.abs(ground_truth_depths - predicted_depths)))
        rmse = float(np.sqrt(np.mean((ground_truth_depths - predicted_depths) ** 2)))

        metrics_by_threshold = {}
        for th in thresholds:
            metrics_by_threshold[f"{th}cm"] = self.compute_contingency_metrics(
                ground_truth_depths, predicted_depths, threshold_cm=th
            )

        report = {
            "overall_mae_cm": round(mae, 3),
            "overall_rmse_cm": round(rmse, 3),
            "threshold_metrics": metrics_by_threshold,
            "meets_deployment_criteria": (
                metrics_by_threshold["5.0cm"]["CSI"] >= 0.70
                and metrics_by_threshold["15.0cm"]["CSI"] >= 0.75
            ),
        }

        report_file = self.output_dir / "calibration_report.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        return report


if __name__ == "__main__":
    harness = CalibrationHarness()
    # Sample synthetic evaluation
    y_true = np.random.uniform(0, 25, size=(1000,))
    y_pred = y_true + np.random.normal(0, 1.5, size=(1000,))
    y_pred = np.maximum(0.0, y_pred)
    res = harness.evaluate_surrogate(y_true, y_pred)
    print("Calibration evaluation completed:")
    print(json.dumps(res, indent=2))
