from src.functions import get_data
from src.utilities import save_data

test_table_id = "12521-0001"
test_data_raw = get_data.download_raw(test_table_id)
save_data.raw(test_data_raw, test_table_id)
