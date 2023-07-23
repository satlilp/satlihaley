import logging
import json
import azure.functions as func

# this script proves the req.params is used to receive values from the url
# 1. click the url to jump to the webpage
# 2. copy/paste the line below at the end of url, and press enter
#    ?name=peli&gender={"age":"18"}
# 3. then, name and gender are retrieved from req.params
# this is the result that shows on the webpage
# Hello, peli.                                     req.params is {'gender': '{"age":"18"}', 'name': 'peli'} and                                     type_params is <class 'mappingproxy'> and                                     gender is {"age":"18"} and                                     lst is ['copy', 'get', 'items', 'keys', 'values']

# next we need to test get and post method in the portal
# currently we're sure that the req.params takes values from the url, but for req.get_json,
# need to use either portal or postman to test

# obj.get_body().decode('utf-8')

# from local

def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

# from local

    gender = req.params.get('gender')

    print("--------------------")
    print(req.get_body(), "/", type(req.get_body()))
    print(req.get_body().decode("utf-8"), "/", type(req.get_body().decode("utf-8")))
    print(json.loads(req.get_body().decode("utf-8")), "/", type(json.loads(req.get_body().decode("utf-8"))))


# from local

    # comment out res and type_params since req.params is directly used in func.HttpResponse
    res = req.params
    type_params = type(req.params)
    
    if not name:
        print("name is", name)
        try:
            print("1")
            req_body = req.get_json()
            # req_body = req.get_body()
            print("req_body is", req_body)
            print("req_body type is", type(req_body))
            print('"req_body["name"] is"', req_body["name"])
            print("dir(req.get_json()) is", dir(req.get_json()))
            print("2")
        except ValueError:
            print("3")
            pass
        else:
            # from local

            print("4")
            # name = req_body.get('name')
            print("5")
# from local
# from local

    if name:
        print("6")
        # lst will give all the functions available under req.params
        lst = []
        for c in dir(req.params):
            if not c.startswith("_"):
                lst.append(c)
        # use req.params.get directly here inside the curly bracket
        return func.HttpResponse(f"Hello, {req.params.get('name')}. \
                                    req.params is {req.params} and \
                                    type_params is {type(req.params)} and \
                                    gender is {gender} and \
                                    lst is {lst}")
    # from local

    else:
        return func.HttpResponse(
             f" {req_body} No name found \
              This HTTP triggered function executed successfully. \
              Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
# from local





# from local
