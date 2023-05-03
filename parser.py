# Code compiled using Python 3

print("Hello There ... WELCOME BACK !!!")
import re
import json

def get_args_from_graphql_query(query: str) -> dict:
    import re
    import json

    # Now lets find the actual arguments passed into the API

    process_from_payload = query.replace(" ", "")
    # print(f"process_from_payload: {process_from_payload}")

    cleaned_raw_ard_payload = process_from_payload[process_from_payload.find("(")+1:process_from_payload.find(")")]
    # print(f"cleaned_raw_ard_payload: {cleaned_raw_ard_payload}")

    cleaned_raw_ard_payload_formated_1 = cleaned_raw_ard_payload.replace("\n", ",\"").replace(":", "\":")
    cleaned_raw_ard_payload_formated_2 = re.sub("^,|,\"$", "", cleaned_raw_ard_payload_formated_1)
    cleaned_raw_ard_payload_formated_3 = re.sub(r'([\:\{,])(\w+\")', r'\1"\2', cleaned_raw_ard_payload_formated_2)
    # print(f"cleaned_raw_ard_payload_formated_3: {cleaned_raw_ard_payload_formated_3}")

    logging.info("The arguments as JSON ....")
    logging.info("-----------------------------")
    request_id_from_payload_json = json.loads(json.dumps("{0}{1}{2}".format("{", cleaned_raw_ard_payload_formated_3, "}")))
    logging.info(request_id_from_payload_json)
    logging.info("-----------------------------")
    return json.loads(request_id_from_payload_json)



# Lets this is what you got from the graphql request body
json_data = {
    "query": "{\n  visa_graphql_api(\n    pageSize: 15\n    pageNumber: 1\n    filters: {documentType: \"visa\", status: [\"Approved\", \"Denied\"]}\n  ) {\n    records_count\n    pending_items {\n      pending_visas {\n        agent_id\n        pending_id\n        severity\n       user_message\n        event_timestamp\n        suggestions\n        document_details\n        retry_attempts\n        status\n        request_id\n        __typename\n      }\n      roster_agent {\n        roster_agent_id\n        external_name\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}

json_args = get_args_from_graphql_query(json_data['query'])
print(json_args)
