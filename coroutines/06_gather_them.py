import asyncio


async def co_test(number: int) -> int:
  print('I am co', number)
  await asyncio.sleep(1)
  print('Done with', number)


async def main() -> None:
  one, two, three = co_test(1), co_test(2), co_test(3)
  print('Executing')
  await asyncio.gather(one, two, three)
  print('Done')


asyncio.run(main())
