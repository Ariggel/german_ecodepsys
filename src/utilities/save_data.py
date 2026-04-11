import pandas as pd
from datetime import datetime
from pathlib import Path
from src.utilities import logging

from config import paths


def raw(data_raw: pd.DataFrame, table_id: str) -> None:
    
    logger = logging.get_logger(__name__)

    data_raw_file = paths.dir_data_raw / f"{table_id}.csv"
    data_history_dir = paths.dir_data_raw_history

    his_data_flag = False

    if data_raw_file.exists():
        try:
            data_raw_historized = pd.read_csv(
                 data_raw_file
                ,delimiter      = ';'
                ,decimal        = ','
            )

            if not data_raw.equals(data_raw_historized):
                his_data_flag = True
                logger.info("Data change detected for table_id=%s", table_id)
            else:
                logger.info("No data change detected for table_id=%s", table_id)

        except Exception:
            his_data_flag = True
            logger.exception("Failed to compare existing data, forcing historization")

    else:
        his_data_flag = True
        logger.info("No existing file found, continue to historize data for table_id=%s", table_id)

    if his_data_flag:
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
        history_path = data_history_dir / f"{table_id}_{timestamp}.csv"

        try:
            data_raw.to_csv(
                history_path
                ,sep        = ';'
                ,decimal    = ','
                ,index      = False
            )
            logger.info("Historized data at %s", history_path)

        except Exception:
            logger.exception("Failed to write history file")
            raise

    try:
        data_raw.to_csv(
            data_raw_file
            ,sep        = ';'
            ,decimal    = ','
            ,index      = False
        )
        logger.info("Saved current data to %s", data_raw_file)

    except Exception:
        logger.exception("Failed to save current data")
        raise