import asyncio


def snitch() -> None:
  print("I am called")


async def co_test(arg: None) -> None:
  print('I am co')
  await asyncio.sleep(1)


async def main() -> None:
  print('Prepare')
  co = co_test(snitch())
  print('Execute')
  await co
  print('The End')


asyncio.run(main())
