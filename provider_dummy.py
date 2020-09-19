from flask import Flask, json, abort
from flask import request

from collections import OrderedDict

# create flask application
app = Flask(__name__)

# get packet data from request to /upload/packet/data
@app.route('/api/all')
def api_all():
    # declare a dictionary for response data
    response = OrderedDict(
		{
		    "count":5,
		    "data":[
			{
			    "personal_id":1,
			    "name":"정종민",
			    "id":"alertjjm",
			    "password":"abc1234",
			    "deviceList":[
				{
				    "device_id":1,
				    "personal_id":1,
				    "mac_addr":"aa:bb:cc:dd:ee:ff",
				    "device_index":1
				},
				{
				    "device_id":2,
				    "personal_id":1,
				    "mac_addr":"bb:cc:dd:ee:aa",
				    "device_index":2
				}
			    ]
			},
			{
			    "personal_id":2,
			    "name":"서예진",
			    "id":"yejinneer",
			    "password":"aaa",
			    "deviceList":[
				{
				    "device_id":4,
				    "personal_id":2,
				    "mac_addr":"ad:df:3f:32:ff:sd",
				    "device_index":1
				}
			    ]
			},
			{
			    "personal_id":3,
			    "name":"이경하",
			    "id":"nulleekh",
			    "password":"bbb",
			    "deviceList":[
				{
				    "device_id":3,
				    "personal_id":3,
				    "mac_addr":"df:df:ee:fe:sa:aa",
				    "device_index":1
				}
			    ]
			},
			{
			    "personal_id":4,
			    "name":"진영훈",
			    "id":"hunihuni",
			    "password":"cc",
			    "deviceList":[
				
			    ]
			},
			{
			    "personal_id":5,
			    "name":"정주용",
			    "id":"juyong",
			    "password":"ccdd",
			    "deviceList":[
				
			    ]
			}
		    ]
		})

    # return response in json format
    return app.response_class(
                json.dumps(response,sort_keys=False),
                mimetype=app.config['JSONIFY_MIMETYPE'])

@app.route('/api/<personal_id>')
def api_personal(personal_id):
    # do type casting of data
    try:
        personal_id = int(personal_id)
    except Exception as e:
        print(e)
        abort(404)
    
    # declare a dictionary for response data
    if personal_id == 1:
        response = OrderedDict(
			{
			    "personal_id":1,
			    "name":"정종민",
			    "id":"alertjjm",
			    "password":"abc1234",
			    "deviceList":[
				{
				    "device_id":1,
				    "personal_id":1,
				    "mac_addr":"aa:bb:cc:dd:ee:ff",
				    "device_index":1
				},
				{
				    "device_id":2,
				    "personal_id":1,
				    "mac_addr":"bb:cc:dd:ee:aa",
				    "device_index":2
				}
			    ]
			})
    elif personal_id == 2:
        response = OrderedDict(
			{
			    "personal_id":2,
			    "name":"서예진",
			    "id":"yejinneer",
			    "password":"aaa",
			    "deviceList":[
				{
				    "device_id":4,
				    "personal_id":2,
				    "mac_addr":"ad:df:3f:32:ff:sd",
				    "device_index":1
				}
			    ]
			})
    elif personal_id == 3:
        response = OrderedDict(
			{
			    "personal_id":3,
			    "name":"이경하",
			    "id":"nulleekh",
			    "password":"bbb",
			    "deviceList":[
				{
				    "device_id":3,
				    "personal_id":3,
				    "mac_addr":"df:df:ee:fe:sa:aa",
				    "device_index":1
				}
			    ]
			})
    elif personal_id == 4:
        response = OrderedDict(
			{
			    "personal_id":4,
			    "name":"진영훈",
			    "id":"hunihuni",
			    "password":"cc",
			    "deviceList":[
				
			    ]
			})
    elif personal_id == 5:
        response = OrderedDict(
			{
			    "personal_id":5,
			    "name":"정주용",
			    "id":"juyong",
			    "password":"ccdd",
			    "deviceList":[
				
			    ]
			})
    else:
        abort(404)


    # return response in json format
    return app.response_class(
                json.dumps(response,sort_keys=False),
                mimetype=app.config['JSONIFY_MIMETYPE'])

@app.route('/api/<personal_id>/<date>')
def api_personal_date(personal_id, date):
    # do type casting of data
    try:
        personal_id = int(personal_id)
    except Exception as e:
        print(e)
        abort(404)

    # declare a dictionary for response data
    if personal_id == 1 :
        response = OrderedDict(
                    {
		        "count":2,
		        "data":[
			    {
			        "personalid":1,
			        "roomid":4,
			        "entertime":46325,
			        "exittime":75130
			    },
			    {
			        "personalid":1,
			        "roomid":4,
			        "entertime":28366,
			        "exittime":42773
			    }
		        ]
		    })
    elif 0 < personal_id and personal_id < 6:
        response = OrderedDict(
                    {
                        "count":0,
                        "data":[]
                    })
    else:
        abort(404)

    # return response in json format
    return app.response_class(
                json.dumps(response,sort_keys=False),
                mimetype=app.config['JSONIFY_MIMETYPE'])

# when this script run as main script
if __name__ == "__main__":
    # run flask application
    app.run()

