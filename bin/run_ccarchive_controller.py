#!/usr/bin/env python
import asyncio
from lsst.dm.CCArchiver.ccarchive_controller import CCArchiveController

async def main():
    controller = await CCArchiveController.create("DM_CCARCHIVER", config_filename="ccarchiver_config.yaml",
                                                  log_filename="CCArchiveController.log")
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
loop.close()
