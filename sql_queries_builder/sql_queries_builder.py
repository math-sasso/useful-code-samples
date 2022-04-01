from pathlib import Path
from typing import List

class SqlBuilder():
    def __init__(self) -> None:
        self.queries = {}

    @property
    def queries_folder(self) -> Path:
        return Path(__file__).parent.parent.parent / "queries"

    def __setup(self):
        if not self.queries:
            self.queries = {p.stem: p for p in self.queries_folder.glob("*.sql")}

    def __call__(self, query_filename: str, **kwargs) -> str:
        self.__setup()
        query_file_path = self.queries.get(query_filename, None)
        if query_file_path is None:
            raise NotImplementedError(query_filename)
        with open(query_file_path, "r") as q_file:
            query = q_file.read()
        filled_query = query.format(**kwargs)
        return filled_query

    def run_batch(self, query_filenames: List[str], **kwargs) -> List[str]:
        queries = []
        for query_file in query_filenames:
            filled_query = self.__call__(query_file, **kwargs)
            queries.append(filled_query)
        return queries
