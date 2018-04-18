# -*- coding: utf-8 -*-
from flask import Flask
from flask_assistant import Assistant,ask, tell
import vueling
import json
import arrow


app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('flight-number')
def flight_info_by_number(number, date):
    json_response = vueling.getFlightStatusByNumber(number,date)
    return ask(build_response(date,json_response[0]))

def build_response(date,json_response):
    status = json_response['Flight']['StatusInfo']['Status']
    departure_city = json_response['Flight']['RouteInfo']['DepartureCity']
    departure_TimeScheduled = json_response['Flight']['StatusInfo']['DepartureInfo']['ScheduleInfo']['TimeScheduled'].encode(encoding='utf-8')[11:16]
    departure_gate = json_response['Flight']['StatusInfo']['DepartureInfo']['ScheduleInfo']['GateDescription']
    arrival_city = json_response['Flight']['RouteInfo']['ArrivalCity']
    arrival_TimeScheduled = json_response['Flight']['StatusInfo']['ArrivalInfo']['ScheduleInfo']['TimeScheduled'].encode(encoding='utf-8')[11:16]
    operational_arrival_TimeUpdated = json_response['Flight']['StatusInfo']['ArrivalInfo']['OperationalInfo']['TimeUpdated'].encode(encoding='utf-8')[11:16]
    if status == 'OnTime':
        ontime = "Status is ON TIME: Your flight to {} on {} departs at {}.".format(arrival_city,date,departure_TimeScheduled)
        speech = "{} Departure Gate in {} is already available and is {}. Please check the final gate on the airport.".format(ontime, departure_city, departure_gate) if not (departure_gate == None) else ontime
    elif status == 'Delayed':
        speech = "Status is DELAYED: Your flight to {} on {} has new arrival time at {} compare to previous arrival time at {}.".format(arrival_city,date,operational_arrival_TimeUpdated,arrival_TimeScheduled)
    elif status == 'Flying':
        speech = "Status is FLYING: Flight to {} is on the air right now. Expected arrival time is {}.".format(arrival_city,operational_arrival_TimeUpdated)
    elif status == 'Landed':
        speech = "Status is LANDED: Flight just landed in {} at {}".format(arrival_city,operational_arrival_TimeUpdated)
    elif status == 'Cancelled':
        speech = "Status CANCELLED: I am really sorry; but your flight from {} to {} on {} has been cancelled.".format(departure_city, arrival_city,date)
    elif status == 'ProvisionalDelayedByMeteo':
        speech = "Status is DELAYED: Your flight to {} has a provisional delay by meteorology. It's new arrival time is {}.".format(arrival_city,operational_arrival_TimeUpdated)
    elif status == 'ProvisionalDelayedByRegulation':
        speech = "Status is DELAYED: Your flight to {} has a provisional delay by regulations. It's new arrival time is {}.".format(arrival_city,operational_arrival_TimeUpdated)
    else:
        speech = "I am sorry but we don't have the current info for your flight to {} on {}".format(arrival_city,date)
    return speech


@assist.action('no-flight-number')
def getFlightStatusByCities(departure,arrival,date,time):
    json_response = vueling.getFlightStatusByCities(departure,arrival,date)
    flight = find_best_all_day_flight(json_response,date,time)
    return ask(build_response(date,flight))


def find_best_all_day_flight(json_response,date,time):
    diff_hour_closest = 9999999
    closest_flight = []
    str_user_datetime = "{}T{}".format(date,time)
    user_datetime = arrow.get(str_user_datetime, 'YYYY-MM-DDTHH:mm:ss')
    for flight in json_response:
        diff_hour = abs (arrow.get (flight['Flight']['StatusInfo']['DepartureInfo']['ScheduleInfo']['TimeScheduled'], 'YYYY-MM-DDTHH:mm:ss') - user_datetime)
        if diff_hour_closest > diff_hour.seconds:
            closest_flight = flight
            diff_hour_closest = diff_hour.seconds
    return closest_flight


if __name__ == '__main__':
#    logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
    app.run(debug=True)