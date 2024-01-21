#!/usr/bin/python3

from python_graphql_client import GraphqlClient
import asyncio

ws = GraphqlClient(
    endpoint=
    "wss://streaming.bitquery.io/graphql?token=ory_at_TjkH2g0OhPSK_tChlxQssU1uxkZT1DCX3ATy1zjCfH8.IV6Oea6BZzFfTExXnbZfYb8pUSi7l_ziWMzNCh9c4nU",
    headers={
        "Sec-WebSocket-Protocol": "graphql-ws",
        "Content-Type": "application/json"
    })

query = """
subscription MyQuery {
  EVM(network: eth) {
    count: Blocks {
      Block {
        TxCount
      }
    }
    hash: Blocks {
      Block{
        TxHash
      }
    }
  }
}
"""

asyncio.run(ws.subscribe(query=query, handle=print))

