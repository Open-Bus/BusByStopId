from bottle import route, run, template
from google.transit import gtfs_realtime_pb2
import requests

@route('/')
def maps():
    return "Hello"

@route('/hello')
@route('/hello/<name>')
def greet(name = 'Raga'):
    return template('Hello {{name}}, how are you?', name = name)

@route('/trip_update/<stopId>')
def trip_update(stopId = ""):
    feed = gtfs_realtime_pb2.FeedMessage()
    response = requests.get('https://gtfs.translink.ca/v2/gtfsrealtime?apikey=vCz36tMkugk1oY4AIKBj')
    feed.ParseFromString(response.content)
    result = ''
    stop_id = ''

    for entity in feed.entity:
        if entity.HasField('trip_update'):
            #print(entity.trip_update.stop_time_update[0].stop_id)
            #print(entity.trip_update.stop_time_update[0].arrival)
            for stop in entity.trip_update.stop_time_update:
                if stop.HasField('stop_id'):
                    stop_id = str(stop.stop_id)
                    if (stop_id == stopId):
                        result = result + str(stop.arrival.delay)
                        return template('It should arrive to {{stopId}} in {{name}} seconds', name = result, stopId = stopId)

    return template('hi')


run(host = 'localhost', port = 8080, debug = True, reloader = True)
