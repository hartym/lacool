import statsd
import time
import random

c = statsd.StatsClient('localhost', 8125, prefix='cool')


stats = ['toto', 'LumSens1', 'LumSens2', 'Temp1', 'Hum1', 'Temp2', 'Hum2', 'PumpStatus', 'FanStatus1', 'FanStatus2', 'FanStatus3', 'Moist1', 'Led1', 'Led2', 'Led3', 'Led4', 'Led5', 'Led6', 'WaterLvl_Dist']



while True:
  values = {
    name: random.randint(0,10)-5 for name in stats
    }

  for k, v in values.items():
    print(k, v)
    c.gauge(k, v, delta=True)
  time.sleep(1)


