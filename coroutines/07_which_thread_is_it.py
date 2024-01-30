import asyncio
import threading


async def co_test(number: int) -> int:
  print('I am co in thread', number, f'in thread {threading.get_ident()}')
  print('Done with', number, f'in thread {threading.get_ident()}')


async def main() -> None:
  one, two, three = co_test(1), co_test(2), co_test(3)
  print(f'Executing main in thread {threading.get_ident()}')
  await asyncio.gather(one, two, three)
  print(f'Done main in thread {threading.get_ident()}')


asyncio.run(main())
