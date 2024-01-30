import asyncio


async def co_test(id: int, wait: int) -> None:
  print('Started co for id', id)
  await asyncio.sleep(wait)
  print('Ended co for id', id)


async def main() -> None:
  print('In main')
  print("Creating task 1")
  task1 = asyncio.create_task(co_test(1, 3))
  print("Creating task 2")
  task2 = asyncio.create_task(co_test(2, 2))
  print("Creating task 3")
  task3 = asyncio.create_task(co_test(3, 1))
  print('Awaiting task 1')
  await task1
  print('Awaiting task 2')
  await task2
  print('Awaiting task 3')
  await task3
  print('Done with main')


asyncio.run(main())
