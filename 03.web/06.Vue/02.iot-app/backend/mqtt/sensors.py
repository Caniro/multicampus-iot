from . import add_topic_handler
from .models import Sensor

def save_sensor(topic, value):
    value = float(value)
    _, username, _, place, sensor = topic.split('/')
    # print(username, place, sensor, value)
    s = Sensor(username=username, place=place,
            sensor=sensor, value=value)
    s.save()

# add_topic_handler('iot/+/sensors/#', save_sensor) # 와일드카드 적용 안됨(사전의 키니까)
if __name__=='__main__':
    add_topic_handler('sensors', save_sensor)
