from pathlib import Path

dir_root = Path(__file__).resolve().parent.parent

dir_src = dir_root / "src"
dir_data = dir_root / "data"
dir_data_raw = dir_data / "raw"
dir_data_processed = dir_data / "processed"

dir_config = dir_root / "config"