import asyncio


async def co_test() -> None:
  print('Started co')
  await asyncio.sleep(1)
  print('Ended co')


async def main() -> None:
  print('In main')
  task = asyncio.create_task(co_test())
  print('Created task, waiting for result')
  await task
  print('Done with main')


asyncio.run(main())
