# Теперь можем несколько усложнить наше приложение
# сделаем так чтобы в коробке было несколько мячей

from engine import initialize, process_events, modify, render
from config import state

initialize(state)
while 1:
  process_events(state)
  modify(state)
  render(state)
