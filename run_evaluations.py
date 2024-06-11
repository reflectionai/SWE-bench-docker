import argparse
import shutil
import asyncio
import pathlib
import tempfile
from typing import Any
import uuid
from datasets import load_dataset
import pandas as pd
import run_evaluation
import generate_report
import schema


async def main(
    no_op: bool,
    num_processes: int,
    split: str,
    swe_bench_tasks: str,
):
  # Step 1: Load the dataset
  dataset: pd.DataFrame = load_dataset(
      swe_bench_tasks)[split].to_pandas()  # type: ignore

  unique_filename = f"no_op_{uuid.uuid4()}.txt"

  # Create a patch that adds a new file with a blank line
  no_op_patch = f"""
diff --git a/{unique_filename} b/{unique_filename}
new file mode 100644
index 0000000..e69de29
--- /dev/null
+++ b/{unique_filename}
@@ -0,0 +1 @@
+
"""
  predictions_path = pathlib.Path(
      tempfile.NamedTemporaryFile(delete=False, suffix='.jsonl').name)
  temp_dir = tempfile.TemporaryDirectory()
  log_dir = pathlib.Path(temp_dir.name)
  try:
    assert predictions_path.exists()
    assert log_dir.exists()

    for _, row in dataset.iterrows():  # type: ignore
      row_dict: dict[str, Any] = row.to_dict()  # type: ignore
      data_point = schema.DataPoint.model_validate(row_dict)
      predictions = schema.AllPreds(
          model_name_or_path='none',
          instance_id=data_point.instance_id,
          model_patch=no_op_patch if no_op else data_point.patch,
      )
      with predictions_path.open("a") as f:
        f.write(predictions.model_dump_json() + "\n")

    await run_evaluation.main(
        predictions_path=str(predictions_path),
        swe_bench_tasks=swe_bench_tasks,
        namespace='aorwall',
        log_dir=str(log_dir),
        num_processes=num_processes,
    )
    generate_report.generate_report(
        swe_bench_tasks=swe_bench_tasks,
        predictions_path=str(predictions_path),
        log_dir=str(log_dir),
        output_dir=str(log_dir),
    )
  finally:
    predictions_path.unlink(missing_ok=True)
    shutil.rmtree(log_dir)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--no_op", action="store_true")
  parser.add_argument("--num_processes", type=int, default=-1)
  parser.add_argument("--split", type=str, required=True)
  parser.add_argument(
      "--swe_bench_tasks", type=str, default="princeton-nlp/SWE-bench_Lite")
  args = parser.parse_args()
  asyncio.run(
      main(
          no_op=args.no_op,
          num_processes=args.num_processes,
          swe_bench_tasks=args.swe_bench_tasks,
          split=args.split))
