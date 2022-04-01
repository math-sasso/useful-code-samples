Useful piece of code to create queries and save them in a external folder.

To use it basically create a query:

```python

qry_builder = SqlBuilder()
query = qry_builder(
            "my_query",
            arg1=arg1,
            arg2=arg2,
            arg3=arg3,
        )
```

And call your data connector:

```python
data_conn = SparkConnector()
data = data_conn(query)

```
