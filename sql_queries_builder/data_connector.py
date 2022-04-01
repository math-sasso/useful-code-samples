from typing import List

from pyspark.sql import DataFrame, SparkSession

class SparkConnector():
    def __init__(self) -> None:
        self.session = SparkSession.builder.getOrCreate()

    def __call__(self, query: str) -> DataFrame:
        return self.session.sql(query)

    def run_batch(self, queries: List[str]) -> None:
        for query in queries:
            self.__call__(query)
