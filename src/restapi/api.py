import method


def API(func):
    # Decorator
    def api_call(*args, **kwargs):
        api_info = func(*args, **kwargs)
        if not isinstance(api_info, dict):
            raise TypeError('API infomation should be dictionary type')
        url = args[0].url + api_info['path']
        headers = api_info['headers']
        api_method = api_info['method']
        print "API '" + func.__name__ + "' was called"
        print "API info {}".format(str(api_info))
        if api_method == "Get":
            return method.get(url, headers)
        elif api_method == "Post":
            data = api_info['data'] if 'data' in api_info else None
            json = api_info['json'] if 'json' in api_info else None
            return method.post(url, headers, data, json)
        elif api_method == "Put":
            data = api_info['data'] if 'data' in api_info else None
            json = api_info['json'] if 'json' in api_info else None
            return method.put(url, headers, data, json)
        elif api_method == "Delete":
            return method.delete(url, headers)
        else:
            raise ValueError("Undefined API method '{}'".format(api_method))
    return api_call


class BaseAPIs:

    def __init__(self, url):
        self.url = url

#     @API
#     def api_1(self, a):
#         return {'path': '/v1/banners/ja_android_tabs_unlimited/banner',
#                 'headers': {'X-Device-ID': '263b6570-0d13-0def-37ff-'},
#                 'method': 'Get',
#                 'data': a}
#
#
# if __name__ == '__main__':
#     print str(BaseAPI('http://api-video').api_1(123).json())
