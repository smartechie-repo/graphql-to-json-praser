# Code compiled using Python 3

print("Hello There ... WELCOME BACK !!!")
import re
import json

# Lets this is what you got from the graphql request body
json_data = {
    "query": "{\n  my_graphql_api(\n    pageSize: 15\n    pageNumber: 1\n    filters: {documentType: \"visa\", status: [\"Processes\", \"Denied\"]}\n  ) {\n    records_count\n    pending_items {\n      pending_visas {\n        agent_id\n        pending_id\n        severity\n       user_message\n        event_timestamp\n        suggestions\n        document_details\n        retry_attempts\n        status\n        request_id\n        __typename\n      }\n      roster_agent {\n        roster_agent_id\n        external_name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}

# Now lets find the actual arguments passed into the API

process_from_payload = str(json_data['query']).replace(" ", "")
# print(f"process_from_payload: {process_from_payload}")

request_id_from_payload = process_from_payload[process_from_payload.find("(")+1:process_from_payload.find(")")]
# print(f"request_id_from_payload: {request_id_from_payload}")

request_id_from_payload_clean = request_id_from_payload.replace("\n", ",\"").replace(":", "\":")
request_id_from_payload_json_str = re.sub("^,|,\"$", "", request_id_from_payload_clean)
# print(f"request_id_from_payload_json_str: {request_id_from_payload_json_str}")

print("The arguments as JSON ....")
print("-----------------------------")
request_id_from_payload_json = json.loads(json.dumps("{0}{1}{2}".format("{", request_id_from_payload_json_str, "}")))
print(request_id_from_payload_json)
print("-----------------------------")
