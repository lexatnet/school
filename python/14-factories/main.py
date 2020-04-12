def func_creator(some_arg):
  def new_func():
    print('new_func->', some_arg)
  return new_func

f1 = func_creator('first')

f1()
f1()
f1()
