#!/usr/bin/env python
import asyncio
from lsst.dm.CCArchiver.ccarchiver_csc import CCArchiverCSC


csc = CCArchiverCSC(index=None)
asyncio.get_event_loop().run_until_complete(csc.done_task)
