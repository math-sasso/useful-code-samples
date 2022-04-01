import pytest
import pyspark


@pytest.fixture
def monkeypatched_spark_dataframe_saveAsTable(
    monkeypatch, mocked_output_spark_dataframe
):
    """Everytime saveAsTable is called from a pyspark.sql.DataFrameWriter when this monkeypatch function is passed as reference we have a the mockreturn

    """
    def mockreturn(*args, **kwargs):
        return mocked_output_spark_dataframe

    monkeypatch.setattr(pyspark.sql.DataFrameWriter, "saveAsTable", mockreturn)