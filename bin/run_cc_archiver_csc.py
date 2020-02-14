#!/usr/bin/env python
import asyncio
from lsst.dm.CCArchiver.ccarchiver_csc import CCArchiverCSC


csc = CCArchiverCSC(index=None, schema_file='CCArchiver.yaml', initial_simulation_mode=False)
asyncio.get_event_loop().run_until_complete(csc.done_task)
