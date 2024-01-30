import asyncio


def fun_add_one(number: int) -> int:
  return number + 1


async def co_add_one(number: int) -> int:
  return number + 1


async def main() -> None:
  print('call fun', fun_add_one(1))
  co = co_add_one(1)
  print('call co, this is a coroutine')
  result = await co
  print('result is', result)
  pass


asyncio.run(main())
