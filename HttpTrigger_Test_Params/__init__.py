import logging

import azure.functions as func


# this script proves the req.params is used to receive values from the url
# 1. click the url to jump to the webpage
# 2. give the name and gender at the end of url, and enter
# 3. then name and gender are retrieved from req.params

# next we need to test get and post method in the portal

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    gender = req.params.get('gender')

    res = req.params

    type_params = type(req.params)
    
    if not name:
        print("name is ", name)
        try:
            print("1")
            req_body = req.get_json()
            print(req_body)
            print("2")
        except ValueError:
            print("3")
            pass
        else:
            print("4")
            name = req_body.get('name')
            print("5")

    if name:
        lst = []
        for c in dir(req.params):
            if not c.startswith("_"):
                lst.append(c)
        return func.HttpResponse(f"Hello, {req.params.get('name')}. req.params is {req.params} and type_params is {type_params} and gender is {gender} and lst is {lst}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
