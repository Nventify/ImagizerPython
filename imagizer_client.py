import urllib


class ImagizerClient:

    DEFAULT_DPR = 1.0
    DEFAULT_QUALITY = 90
    DEFAULT_IMAGIZER_HOST = "demo.imagizercdn.com"

    def __init__(self, imagizer_host=DEFAULT_IMAGIZER_HOST, use_https=False):
        self.dpr = self.DEFAULT_DPR
        self.quality = self.DEFAULT_QUALITY
        self.imagizer_host = imagizer_host
        self.use_https = use_https
        self.format = ""
        self.imageOriginHost = ""

    def build_url(self, path, params=None):
        if not params:
            params = {}

        if not path.startswith("/"):
            path = "/" + path

        params = self.add_global_params(params)
        scheme = "https" if self.use_https else "http"
        url = scheme + "://" + self.imagizer_host + path

        if len(params) > 0:
            url += "?" + urllib.urlencode(params)

        return url

    def add_global_params(self, params):

        if "dpr" not in params and self.dpr != self.DEFAULT_DPR:
            params['dpr'] = self.dpr

        if "quality" not in params and self.quality != self.DEFAULT_QUALITY:
            params['quality'] = self.quality

        if self.format:
            params['format'] = self.format

        if self.imageOriginHost:
            params['hostname'] = self.imageOriginHost

        return params
