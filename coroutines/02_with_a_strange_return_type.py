def fun_add_one(number: int) -> int:
  return number + 1


async def co_add_one(number: int) -> int:
  return number + 1


print(type(fun_add_one(1)))
print(type(co_add_one(1)))
