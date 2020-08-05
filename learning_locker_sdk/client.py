import requests
import base64


class LearningLockerSDK(object):

    _default_headers = {
        "X-Experience-API-Version" : "1.0.3"
    }

    def __init__(self, base_url, api_path, **headers):
        self.base_url = base_url
        self.api_path = api_path
        self.headers = {**self._default_headers, **headers}

    def build_api_url(self, entity, entity_id=None):
        url_str = "{}{}/{}".format(self.base_url, self.api_path, entity)
        if entity_id is not None:
            url_str += "/" + entity_id

        return url_str
    
    def create(self, entity, **data):
        return self.do_request('post', entity, **data)
        

    def retrieve(self, entity, entity_id=None):
        return self.do_request('get', entity, entity_id=entity_id)


    def do_request(self, request_type, entity, entity_id=None, **data):
        req_url = self.build_api_url(entity, entity_id=entity_id)
        return getattr(requests, request_type)(req_url, json=data, headers=self.headers)