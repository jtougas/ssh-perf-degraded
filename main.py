import asyncssh
from asyncssh import (
    SSHClientConnection,
    SSHClientConnectionOptions,
    SSHReader,
    SSHWriter,
)
import asyncio
import cryptography
import logging

async def main():
    root = logging.getLogger()
    root.setLevel("DEBUG")

    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter("[%(asctime)s] %(message)s"))
    root.addHandler(sh)

    root.info(f"Using cryptography {cryptography.__version__}")
    try:
        await asyncssh.connect(
            host="github.com",
            port=22,
            username="irrelavant",
            password="foo",
            options=SSHClientConnectionOptions(
                kex_algs="diffie-hellman-group-exchange-sha256",
                known_hosts=None,
            ),
        )
    except asyncssh.misc.PermissionDenied:
        pass

    root.info("Completed")

asyncio.run(main())
