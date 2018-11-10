# Пойдем дальше в использовании выученных нами ранее приёмов и
# вынесим все определенные нами функции в отдельный модуль
# поместив отдельный файл каждую часть нашего приложения
# таким образом наш главный файл довольно сильно упроститься

from engine import initialize, process_events, modify, render
from config import state

initialize(state)
while 1:
  process_events(state)
  modify(state)
  render(state)
