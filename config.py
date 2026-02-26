import asyncio
from threading import Lock
from typing import Dict

jobs: Dict[str, Dict[str, object]] = {}
image_ready = False
image_lock = Lock()
main_loop: asyncio.AbstractEventLoop | None = None
