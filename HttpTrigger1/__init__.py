import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if name:
        print("req.params.get('name')")

    try:
        req_body = req.get_json()
        print("req_body is", req_body)

    except ValueError:
        print("----------------------")
        print("ValueError is", ValueError)
        print("----------------------")            
        # pass

    else:
        name = req_body.get('name')


    if name:
        return func.HttpResponse(f"Hello, executed successfully.")
    else:
        # print(name)
        return func.HttpResponse(
             f"customized response {name}",
             status_code=200
        )
    
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #         print("req_body is", req_body)

    #     except ValueError:
    #         print("----------------------")
    #         print("ValueError is", ValueError)
    #         print("----------------------")            
    #         pass

    #     else:
    #         name = req_body.get('name')

    # dict_obj = {"name": "peli9"}

    # abc = json.dumps(dict_obj)
