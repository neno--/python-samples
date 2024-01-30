import asyncio


async def co_test(number: int) -> int:
  print('I am co', number)
  await asyncio.sleep(1)


# tasks are scheduled to run as soon as possible

async def main() -> None:
  one, two, three = co_test(1), co_test(2), co_test(3)
  print('Executing 1')
  await one
  print('Executing 2')
  await two
  print('Executing 3')
  await three
  print('The End')


asyncio.run(main())
