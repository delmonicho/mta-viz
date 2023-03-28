from flask import Flask
from google.transit import gtfs_realtime_pb2
import requests

app = Flask(__name__)

@app.route('/get_data_one')
def get_data_one_thru_seven():
    url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'  # replace with the actual API endpoint URL
    # headers=
    count = 0
    response = requests.get(url, headers={"x-api-key":"UY8wskD8lp6MKKULyuOV7aQ2YjLjjUho67t7SHku"})
    gfeed = gtfs_realtime_pb2.FeedMessage()

    gfeed.ParseFromString(response.content)

    print(gfeed)
    # for item in response:
    #     if count < 1:
    #         print(item.json())
    #         count += 1
    # # print(response)
    return "<p>Testing response</p>"

@app.route('/get_data_g')
def get_data_g():
    url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g'  # replace with the actual API endpoint URL
    # headers=
    
    response = requests.get(url, headers={"x-api-key":"UY8wskD8lp6MKKULyuOV7aQ2YjLjjUho67t7SHku"})
    gfeed = gtfs_realtime_pb2.FeedMessage()

    gfeed.ParseFromString(response.content)

    print(gfeed)
    # for item in response:
    #     if count < 1:
    #         print(item.json())
    #         count += 1
    # # print(response)
    return "<p>Testing response</p>"

@app.route("/")
def index():
    return "<p>This is the MTA real tracking app!</p>"


if __name__ == '__main__':
    app.run(debug=True)