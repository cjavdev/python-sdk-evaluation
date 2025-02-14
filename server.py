from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from datetime import datetime

from fern_samsara import Samsara as FernSamsara
from fern_samsara.types import (
  CreateRoutesStopRequestObjectRequestBody,
  RoutesSingleUseAddressObjectRequestBody,
  RouteSettingsRequestBody,
  RouteSettingsRequestBodyRouteCompletionCondition,
  RouteSettingsRequestBodyRouteStartingCondition
)
from stainless_samsara import Samsara as StainlessSamsara
from stainless_samsara.types.fleet.route_create_params import (
  Stop,
  StopSingleUseLocation
)
from samsara import Samsara as SpeakeasySamsara
from samsara.models.routescreaterouterequestbody import (
  CreateRoutesStopRequestObjectRequestBody as SpeakeasyCreateRoutesStopRequestObjectRequestBody
)

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fern')
def fern():
    return render_template('sdk.html', sdk='Fern')

@app.route('/stainless')
def stainless():
    return render_template('sdk.html', sdk='Stainless')

@app.route('/speakeasy')
def speakeasy():
    return render_template('sdk.html', sdk='Speakeasy')

@app.route('/fern_route', methods=['POST'])
def create_fern_route():
    route_name = request.json.get('route_name')
    client = FernSamsara(token=os.getenv("SAMSARA_API_KEY"))

    try:
        response = client.routes.create(
            name=route_name,
            stops=[
                # Example with typed params
                CreateRoutesStopRequestObjectRequestBody(
                    name="Stop 1",
                    single_use_location=RoutesSingleUseAddressObjectRequestBody(
                        latitude=37.7749,
                        longitude=-122.4194
                    ),
                    scheduled_departure_time="2025-03-01T00:01:00Z",
                ),
                {
                    "name": "Stop 2",
                    "singleUseLocation": {
                      "latitude": 37.3382,
                      "longitude": -121.8863
                    },
                    "scheduledDepartureTime": "2025-03-01T00:16:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:15:00Z"
                },
                {
                    "name": "Stop 3",
                    "singleUseLocation": {
                      "latitude": 37.4419,
                      "longitude": -122.1430
                    },
                    "scheduledDepartureTime": "2025-03-01T00:25:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:20:00Z"

                },
                {
                    "name": "Stop 4",
                    "singleUseLocation": {
                      "latitude": 37.8715,
                      "longitude": -122.2730
                    },
                    "scheduledArrivalTime": "2025-03-01T00:26:00Z",
                }
            ],
            settings=RouteSettingsRequestBody(
              route_completion_condition="arriveLastStop",
              route_starting_condition="departFirstStop"
            )
        )
        return jsonify({"success": True, "route_id": response.data.id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/stainless_route', methods=['POST'])
def create_stainless_route():
    route_name = request.json.get('route_name')
    client = StainlessSamsara(access_token=os.getenv("SAMSARA_API_KEY"))

    try:
        response = client.fleet.routes.create(
            name=route_name,
            settings={
              "routeCompletionCondition": "arriveLastStop",
              "routeStartingCondition": "departFirstStop"
            },
            stops=[
                # Example with typed params
                Stop(
                    name="Stop 1",
                    single_use_location=StopSingleUseLocation(
                      latitude=37.7749,
                      longitude=-122.4194
                    ),
                    scheduled_departure_time="2025-03-01T00:01:00Z",
                ),
                {
                    "name": "Stop 2",
                    "singleUseLocation": {
                      "latitude": 37.3382,
                      "longitude": -121.8863
                    },
                    "scheduledDepartureTime": "2025-03-01T00:15:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:14:00Z"
                },
                {
                    "name": "Stop 3",
                    "singleUseLocation": {
                      "latitude": 37.4419,
                      "longitude": -122.1430
                    },
                    "scheduledDepartureTime": "2025-03-01T00:25:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:20:00Z"
                },
                {
                    "name": "Stop 4",
                    "singleUseLocation": {
                      "latitude": 37.8715,
                      "longitude": -122.2730
                    },
                    "scheduledArrivalTime": "2025-03-01T00:35:00Z",
                }
            ]
        )
        return jsonify({"success": True, "route_id": response.data.id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/speakeasy_route', methods=['POST'])
def create_speakeasy_route():
    route_name = request.json.get('route_name')
    client = SpeakeasySamsara(access_token_header=f"Bearer {os.getenv('SAMSARA_API_KEY')}")

    try:
        response = client.routes.create_route(
            name=route_name,
            stops=[
                # Example with typed params
                SpeakeasyCreateRoutesStopRequestObjectRequestBody(
                    name="Stop 1",
                    single_use_location=StopSingleUseLocation(
                      latitude=37.7749,
                      longitude=-122.4194
                    ),
                    scheduled_departure_time="2025-03-01T00:01:00Z",
                ),
                {
                    "name": "Stop 2",
                    "singleUseLocation": {
                      "latitude": 37.3382,
                      "longitude": -121.8863
                    },
                    "scheduledDepartureTime": "2025-03-01T00:15:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:14:00Z"
                },
                {
                    "name": "Stop 3",
                    "singleUseLocation": {
                      "latitude": 37.4419,
                      "longitude": -122.1430
                    },
                    "scheduledDepartureTime": "2025-03-01T00:25:00Z",
                    "scheduledArrivalTime": "2025-03-01T00:20:00Z"
                },
                {
                    "name": "Stop 4",
                    "singleUseLocation": {
                      "latitude": 37.8715,
                      "longitude": -122.2730
                    },
                    "scheduledArrivalTime": "2025-03-01T00:35:00Z",
                }
            ]
        )
        route = response.data
        print(route.id)
        return jsonify({"success": True, "route_id": response.data.id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
