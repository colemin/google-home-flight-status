import json,requests



def getFlightStatusByCities(departure,arrival,date):
    post_fields = {
                    "DepartureDateTimeMin": date,
                    "DepartureDateTimeMax": date,
                    "DepartureAirport": departure,
                    "ArrivalAirport": arrival,
                    "language": "en"
                  }
    url = 'https://apimobile.vueling.com/Vueling.Mobile.FFServices.WebAPI/api/FlightStatus/GetFlightData/'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()


def getFlightStatusByNumber(number,date):
    post_fields = {
                    "DepartureDateTimeMin": date,
                    "DepartureDateTimeMax": date,
                    "FlightNumber": number,
                    "language": "en"
                  }
    url = 'https://apimobile.vueling.com/Vueling.Mobile.FFServices.WebAPI/api/FlightStatus/GetFlightData/'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()


def GetBlackNPromoDays(departure,arrival,date):
    post_fields = {
        "origen": departure,
        "destino": arrival,
        "month": date[5:7],
        "year": date[0:4],
        "monthRange": "1",
        "Udid": "9b9d-1dce-2036-667e-52cc-7a81",
        "InstallationID": "2B166954-1568-4EB4-8400-41FA18ED55F2",
        "OsVersion": "11.2",
        "Currency": "EUR",
        "DeviceType": "IOS",
        "IP": "127.0.0.1",
        "Language": "ca-ES"
    }
#    url = 'https://apimobile.vueling.com/Vueling.Mobile.CalendarServices.WebApi/api/Calendar/GetBlackNPromoDays'
    url = 'https://apimobile-int.vueling.com/Vueling.Mobile.CalendarServices.WebApi/api/Calendar/GetBlackNPromoDays'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()['FirstAvailableDay']


def get_flights_oneway_ams(body, session):
    post_fields = {
                    "cultureCode": "es-ES",
                    "currencyCode": "EUR",
                    "serviceCode": "Search1Day",
                    "itineraryType": "OneWay",
                    "flightType": "All",
                    "passengers": [
                      {
                        "count": 1,
                        "type": "Adult"
                      }
                    ],
                    "criteria": [
                      {
                        "origin": "BCN",
                        "destination": "PMI",
                        "date": "2018-04-01"
                      }
                    ]
                   }
    url = 'http://ams-rev.vueling.com/avy/v1/AvailabilityServices/search/BBV'
    bearer_header = "Bearer "+session['api_session_token']
    header = {
                "Authorization": bearer_header,
                "Content-Type": "application/json"
             }
    return requests.post (url, headers=header, data=json.dumps (body)).json()


def get_flights_oneway(paxs, departure, arrival, date):
    post_fields = {
        "DiscountType": 0,
        "AppVersion": "881",
        "DeviceModel": "Simulator",
        "CurrencyCode": "EUR",
        "TimeZone": 1,
        "Language": "ES",
        "AirportDateTimeList": [
            {
                "MarketDateDeparture": date,
                "DepartureStation": departure,
                "ArrivalStation": arrival
            }
        ],
        "Paxs":paxs,
        "Xid": "",
        "InstallationID": "2B166954-1568-4EB4-8400-41FA18ED55F2",
        "OsVersion": "11.2",
        "Currency": "EUR",
        "DeviceType": "IOS",
        "IP": "127.0.0.1"
    }
#    url = 'https://apimobile.vueling.com/Vueling.Mobile.BookingServices.WebAPI/api/v3/Price/DoAirPriceSB'
    url = 'https://apimobile-int.vueling.com/Vueling.Mobile.BookingServices.WebAPI/api/v3/Price/DoAirPriceSB'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()

def get_flights_oneway_old(departure, arrival, departure_date):
    post_fields = {
        "DiscountType": 0,
        "AppVersion": "881",
        "DeviceModel": "Simulator",
        "CurrencyCode": "EUR",
        "TimeZone": 1,
        "Language": "ES",
        "AirportDateTimeList": [
            {
                "MarketDateDeparture": departure_date,
                "DepartureStation": departure,
                "ArrivalStation": arrival
            }
        ],
        "Xid": "",
        "InstallationID": "2B166954-1568-4EB4-8400-41FA18ED55F2",
        "Paxs": [
            {
                "Paxtype": "ADT",
                "Quantity": 1
            },
            {
                "Paxtype": "CHD",
                "Quantity": 0
            },
            {
                "Paxtype": "INF",
                "Quantity": 0
            }
        ],
        "OsVersion": "11.2",
        "Currency": "EUR",
        "DeviceType": "IOS",
        "IP": "127.0.0.1"
    }

    url = 'https://apimobile.vueling.com/Vueling.Mobile.BookingServices.WebAPI/api/v3/Price/DoAirPriceSB'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()


def do_booking(name,lastname,fareKey,journeyKey,paxInfoList):
    paxInfoList = [
        {
            "Number": 0,
            "PaxType": "ADT",
            "Title": "Mr",
            "FirstName": "John",
            "LastName": "Nieve",
            "DOB": "1979-10-31T13:11:01.853642+01:00",
            "Gender": "Male",
            "Infant": None,
            "PaxAddress": None,
            "TravelDocument": None
        },
        {
            "Number": 0,
            "PaxType": "ADT",
            "Title": "Mrs",
            "FirstName": "Daenerys",
            "LastName": "Targaryen",
            "DOB": "1976-04-07T13:11:01.853642+01:00",
            "Gender": "Female",
            "Infant": None,
            "PaxAddress": None,
            "TravelDocument": None
        }
    ]
    post_fields = {
        "udid": "",
        "coordinates": "41.3110585 2.0685885",
        "appVersion": "100",
        "discountType": 0,
        "sellKeyList": [
            {
                "fareKey": fareKey,
                "journeyKey": journeyKey
            }
        ],
        "paxInfoList": paxInfoList,
        "currencyCode": "EUR",
        "bookingContact": {
            "typeCode": "A",
            "firstName": name,
            "lastName": lastname,
            "emailAddress": "innovation.lab@vueling.com",
            "homePhone": "663848884",
            "city": "BCN",
            "countryCode": "ES"
        },
        "paymentData": {
            "paymentMethodCode": "MC",
            "quotedCurrencyCode": "EUR",
            "quotedAmount": 100,
            "accountNumber": "5210000010001001",
            "expiration": "2022-02-01T00:00:00",
            "paymentFieldsList": [
                {
                    "name": "CC::VerificationCode",
                    "value": "123"
                },
                {
                    "name": "CC::AccountHolderName",
                    "value": "VUELING INNOVATION LAB"
                }
            ]
        },
        "deviceType": "WEB",
        "language": "es-ES"
    }

    url = 'https://apimobile-int.vueling.com/Vueling.Mobile.BookingServices.WebAPI/api/Booking/DoBooking'
    header = {'Content-Type': 'application/json; charset=utf-8'}
    return requests.post (url, headers=header, data=json.dumps (post_fields)).json ()


def test_flight_list():
    flight_list = {
        "Trip": {
            "IsMac": True,
            "CurrencyCode": "EUR",
            "DiscountType": 0,
            "JourneyMarkets": [
                {
                    "Journeys": [
                        {
                            "JourneySellKey": "VY~7822~ ~~BCN~04/18/2018 07:35~LGW~04/18/2018 08:55~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T08:55:00",
                            "STD": "2018-04-18T07:35:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7822~ ~~BCN~04/18/2018 07:35~LGW~04/18/2018 08:55~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T07:35:00",
                                    "STA": "2018-04-18T08:55:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7822",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 179.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "0~BZ~~UBULLZ~EXCE~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7826~ ~~BCN~04/18/2018 12:30~LGW~04/18/2018 13:50~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T13:50:00",
                            "STD": "2018-04-18T12:30:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7826~ ~~BCN~04/18/2018 12:30~LGW~04/18/2018 13:50~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T12:30:00",
                                    "STA": "2018-04-18T13:50:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7826",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 179.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "0~BZ~~UBULLZ~EXCE~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7525~ ~~BCN~04/18/2018 14:25~LGW~04/18/2018 15:45~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T15:45:00",
                            "STD": "2018-04-18T14:25:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7525~ ~~BCN~04/18/2018 14:25~LGW~04/18/2018 15:45~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T14:25:00",
                                    "STA": "2018-04-18T15:45:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7525",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 179.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "0~BZ~~UBULLZ~EXCE~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 2,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7824~ ~~BCN~04/18/2018 17:25~LGW~04/18/2018 18:45~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T18:45:00",
                            "STD": "2018-04-18T17:25:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7824~ ~~BCN~04/18/2018 17:25~LGW~04/18/2018 18:45~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T17:25:00",
                                    "STA": "2018-04-18T18:45:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7824",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 179.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "0~BZ~~UBULLZ~EXCE~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7840~ ~~BCN~04/18/2018 18:20~LHR~04/18/2018 19:40~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LHR",
                            "STA": "2018-04-18T19:40:00",
                            "STD": "2018-04-18T18:20:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7840~ ~~BCN~04/18/2018 18:20~LHR~04/18/2018 19:40~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LHR",
                                    "STD": "2018-04-18T18:20:00",
                                    "STA": "2018-04-18T19:40:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7840",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 29.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~7~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 39.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DPOWVYOP~OPTI~~8~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 0.0,
                                    "PromoType": "",
                                    "ProductClass": "",
                                    "JourneyFareKey": "",
                                    "IsFareAvailable": False,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": False,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7820~ ~~BCN~04/18/2018 18:55~LGW~04/18/2018 20:15~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T20:15:00",
                            "STD": "2018-04-18T18:55:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7820~ ~~BCN~04/18/2018 18:55~LGW~04/18/2018 20:15~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T18:55:00",
                                    "STA": "2018-04-18T20:15:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7820",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 0.0,
                                    "PromoType": "",
                                    "ProductClass": "",
                                    "JourneyFareKey": "",
                                    "IsFareAvailable": False,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": False,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~7828~ ~~BCN~04/18/2018 19:30~LGW~04/18/2018 20:50~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T20:50:00",
                            "STD": "2018-04-18T19:30:00",
                            "Duration": 140,
                            "IsConnection": False,
                            "ArriveNextDay": False,
                            "ConnectionTime": 0,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~7828~ ~~BCN~04/18/2018 19:30~LGW~04/18/2018 20:50~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T19:30:00",
                                    "STA": "2018-04-18T20:50:00",
                                    "Duration": 140,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "7828",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 14.99,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "0~D~~DOWVYBA~PB01~~12~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 44.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "0~DP~~DOWVYP~OPTI~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 179.99,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "0~BZ~~UBULLZ~EXCE~~1~X",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 2,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~6100~ ~~BCN~04/18/2018 07:20~FCO~04/18/2018 09:05~^VY~6224~ ~~FCO~04/18/2018 12:45~LGW~04/18/2018 14:25~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T14:25:00",
                            "STD": "2018-04-18T07:20:00",
                            "Duration": 485,
                            "IsConnection": True,
                            "ArriveNextDay": False,
                            "ConnectionTime": 220,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6100~ ~~BCN~04/18/2018 07:20~FCO~04/18/2018 09:05~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "FCO",
                                    "STD": "2018-04-18T07:20:00",
                                    "STA": "2018-04-18T09:05:00",
                                    "Duration": 105,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6100",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                },
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6224~ ~~FCO~04/18/2018 12:45~LGW~04/18/2018 14:25~",
                                    "DepartureStation": "FCO",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T12:45:00",
                                    "STA": "2018-04-18T14:25:00",
                                    "Duration": 160,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6224",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 64.98,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "2~D~~DOWVYBA~PB01~~5~X^1~D~~DOWVYBA~PB01~~14~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 98.67,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "2~DP~~DOWVYP~OPTI~~7~X^1~PP~~PPOWVYOP~OPTI~~6~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 0.0,
                                    "PromoType": "",
                                    "ProductClass": "",
                                    "JourneyFareKey": "",
                                    "IsFareAvailable": False,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": False,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~6100~ ~~BCN~04/18/2018 07:20~FCO~04/18/2018 09:05~^VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T20:05:00",
                            "STD": "2018-04-18T07:20:00",
                            "Duration": 825,
                            "IsConnection": True,
                            "ArriveNextDay": False,
                            "ConnectionTime": 560,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6100~ ~~BCN~04/18/2018 07:20~FCO~04/18/2018 09:05~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "FCO",
                                    "STD": "2018-04-18T07:20:00",
                                    "STA": "2018-04-18T09:05:00",
                                    "Duration": 105,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6100",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                },
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                                    "DepartureStation": "FCO",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T18:25:00",
                                    "STA": "2018-04-18T20:05:00",
                                    "Duration": 160,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6228",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 64.98,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "2~D~~DOWVYBA~PB01~~5~X^1~D~~DOWVYBA~PB01~~14~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 98.67,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "2~DP~~DOWVYP~OPTI~~7~X^1~PP~~PPOWVYOP~OPTI~~6~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 0.0,
                                    "PromoType": "",
                                    "ProductClass": "",
                                    "JourneyFareKey": "",
                                    "IsFareAvailable": False,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": False,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~6108~ ~~BCN~04/18/2018 09:45~FCO~04/18/2018 11:30~^VY~6224~ ~~FCO~04/18/2018 12:45~LGW~04/18/2018 14:25~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T14:25:00",
                            "STD": "2018-04-18T09:45:00",
                            "Duration": 340,
                            "IsConnection": True,
                            "ArriveNextDay": False,
                            "ConnectionTime": 75,
                            "isShortConnection": True,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6108~ ~~BCN~04/18/2018 09:45~FCO~04/18/2018 11:30~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "FCO",
                                    "STD": "2018-04-18T09:45:00",
                                    "STA": "2018-04-18T11:30:00",
                                    "Duration": 105,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6108",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                },
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6224~ ~~FCO~04/18/2018 12:45~LGW~04/18/2018 14:25~",
                                    "DepartureStation": "FCO",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T12:45:00",
                                    "STA": "2018-04-18T14:25:00",
                                    "Duration": 160,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6224",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 64.98,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "2~D~~DOWVYBA~PB01~~5~X^1~D~~DOWVYBA~PB01~~14~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 98.67,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "2~DP~~DOWVYP~OPTI~~7~X^1~PP~~PPOWVYOP~OPTI~~6~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 339.98,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "2~BZ~~UBULLZ~EXCE~~1~X^1~BZ~~BZOWVYEX~EXCE~~2~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 2,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~6108~ ~~BCN~04/18/2018 09:45~FCO~04/18/2018 11:30~^VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T20:05:00",
                            "STD": "2018-04-18T09:45:00",
                            "Duration": 680,
                            "IsConnection": True,
                            "ArriveNextDay": False,
                            "ConnectionTime": 415,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6108~ ~~BCN~04/18/2018 09:45~FCO~04/18/2018 11:30~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "FCO",
                                    "STD": "2018-04-18T09:45:00",
                                    "STA": "2018-04-18T11:30:00",
                                    "Duration": 105,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6108",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                },
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                                    "DepartureStation": "FCO",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T18:25:00",
                                    "STA": "2018-04-18T20:05:00",
                                    "Duration": 160,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6228",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 64.98,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "2~D~~DOWVYBA~PB01~~5~X^1~D~~DOWVYBA~PB01~~14~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 98.67,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "2~DP~~DOWVYP~OPTI~~7~X^1~PP~~PPOWVYOP~OPTI~~6~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 339.98,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "2~BZ~~UBULLZ~EXCE~~1~X^1~BZ~~BZOWVYEX~EXCE~~2~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 2,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        },
                        {
                            "JourneySellKey": "VY~6104~ ~~BCN~04/18/2018 11:55~FCO~04/18/2018 13:40~^VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                            "DepartureStation": "BCN",
                            "ArrivalStation": "LGW",
                            "STA": "2018-04-18T20:05:00",
                            "STD": "2018-04-18T11:55:00",
                            "Duration": 550,
                            "IsConnection": True,
                            "ArriveNextDay": False,
                            "ConnectionTime": 285,
                            "isShortConnection": False,
                            "Segments": [
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6104~ ~~BCN~04/18/2018 11:55~FCO~04/18/2018 13:40~",
                                    "DepartureStation": "BCN",
                                    "ArrivalStation": "FCO",
                                    "STD": "2018-04-18T11:55:00",
                                    "STA": "2018-04-18T13:40:00",
                                    "Duration": 105,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6104",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                },
                                {
                                    "IsInternational": True,
                                    "SegmentSellKey": "VY~6228~ ~~FCO~04/18/2018 18:25~LGW~04/18/2018 20:05~",
                                    "DepartureStation": "FCO",
                                    "ArrivalStation": "LGW",
                                    "STD": "2018-04-18T18:25:00",
                                    "STA": "2018-04-18T20:05:00",
                                    "Duration": 160,
                                    "CarrierCode": "VY",
                                    "FlightNumber": "6228",
                                    "ArriveNextDay": False,
                                    "OperatedBy": "Vueling"
                                }
                            ],
                            "JourneyFare": [
                                {
                                    "Amount": 64.98,
                                    "PromoType": "EXCLUSIVE",
                                    "ProductClass": "BA",
                                    "JourneyFareKey": "2~D~~DOWVYBA~PB01~~5~X^1~D~~DOWVYBA~PB01~~14~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 0,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 98.67,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "OP",
                                    "JourneyFareKey": "2~DP~~DOWVYP~OPTI~~7~X^1~PP~~PPOWVYOP~OPTI~~6~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 0,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 1,
                                    "CurrencyCode": "EUR"
                                },
                                {
                                    "Amount": 339.98,
                                    "PromoType": "NOT-SPECIFIED",
                                    "ProductClass": "EX",
                                    "JourneyFareKey": "2~BZ~~UBULLZ~EXCE~~1~X^1~BZ~~BZOWVYEX~EXCE~~2~",
                                    "IsFareAvailable": True,
                                    "AvailableCount": 2,
                                    "IsPromo": False,
                                    "IsPromoVYAplicable": False,
                                    "Active": True,
                                    "ColumnId": 2,
                                    "CurrencyCode": "EUR"
                                }
                            ],
                            "AtvState": None,
                            "AtvCode": None,
                            "AtvTime": 0,
                            "CheckinLostWarning": False,
                            "State": None,
                            "OperatedBy": "Vueling"
                        }
                    ]
                }
            ],
            "AtvInfo": None,
            "ShowRedressNumber": False,
            "BookingTypeAncillaries": "07"
        },
        "Signature": "",
        "Error": None,
        "Warning": None,
        "Warnings": None
    }
    return flight_list


def get_passengers():
    passengers = [
                    {
                      "name": "Daenerys",
                      "lastname": "Targaryen"
                    },
                    {
                      "name": "Tyrion",
                      "lastname": "Lannister"
                    },
                    {
                      "name": "Sansa",
                      "lastname": "Stark"
                    }
                ]
    return passengers

