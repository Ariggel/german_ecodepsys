import pandas
from src.functions import get_data
from src.utilities import save_data

def clean_data() -> pandas.DataFrame:
    table_id = "51000-0007"
    data_raw = get_data(table_id)
    save_data.raw(data_raw, table_id)