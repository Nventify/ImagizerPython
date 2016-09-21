import imagizer_client
import unittest


class TestImagizerClient(unittest.TestCase):

    def test_build_url(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg"
        self.assertEqual(expected, url)

    def test_build_url_with_slash(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("/image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg"
        self.assertEqual(expected, url)

    def test_build_url_with_multiple_slashes(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("this/images/image.jpg")
        expected = "http://demo.imagizercdn.com/this/images/image.jpg"
        self.assertEqual(expected, url)

    def test_build_url_with_specified_imagizer_host(self):
        client = imagizer_client.ImagizerClient("my.image.imagizer.example.com")
        url = client.build_url("this/images/image.jpg")
        expected = "http://my.image.imagizer.example.com/this/images/image.jpg"
        self.assertEqual(expected, url)

    def test_build_url_with_specified_imagizer_host_with_https(self):
        client = imagizer_client.ImagizerClient("my.image.imagizer.example.com", True)
        url = client.build_url("this/images/image.jpg")
        expected = "https://my.image.imagizer.example.com/this/images/image.jpg"
        self.assertEqual(expected, url)

    def test_build_url_with_params(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("image.jpg", {
            "width": 200,
            "height": 300,
            "crop": "fit"
        })
        expected = "http://demo.imagizercdn.com/image.jpg?width=200&crop=fit&height=300"
        self.assertEqual(expected, url)

    def test_build_url_with_quality(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("image.jpg", {
            "quality": 60
        })
        expected = "http://demo.imagizercdn.com/image.jpg?quality=60"
        self.assertEqual(expected, url)

    def test_build_url_with_global_quality(self):
        client = imagizer_client.ImagizerClient()
        client.quality = 60
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?quality=60"
        self.assertEqual(expected, url)

    def test_build_url_with_global_quality_override(self):
        client = imagizer_client.ImagizerClient()
        client.quality = 60
        url = client.build_url("image.jpg", {
            "quality": 55
        })
        expected = "http://demo.imagizercdn.com/image.jpg?quality=55"
        self.assertEqual(expected, url)

    def test_build_url_with_dpr(self):
        client = imagizer_client.ImagizerClient()
        url = client.build_url("image.jpg", {
            "dpr": 2
        })
        expected = "http://demo.imagizercdn.com/image.jpg?dpr=2"
        self.assertEqual(expected, url)

    def test_build_url_with_global_dpr(self):
        client = imagizer_client.ImagizerClient()
        client.dpr = 2
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?dpr=2"
        self.assertEqual(expected, url)

    def test_build_url_with_global_dpr_override(self):
        client = imagizer_client.ImagizerClient()
        client.dpr = 2
        url = client.build_url("image.jpg", {
            "dpr": 3
        })
        expected = "http://demo.imagizercdn.com/image.jpg?dpr=3"
        self.assertEqual(expected, url)





    def test_build_url_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com"
        self.assertEqual(expected, url)

    def test_build_url_with_slash_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("/image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com"
        self.assertEqual(expected, url)

    def test_build_url_with_multiple_slashes_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("this/images/image.jpg")
        expected = "http://demo.imagizercdn.com/this/images/image.jpg?hostname=example.com"
        self.assertEqual(expected, url)

    def test_build_url_with_specified_imagizer_host_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient("my.image.imagizer.example.com")
        client.imageOriginHost = "example.com"
        url = client.build_url("this/images/image.jpg")
        expected = "http://my.image.imagizer.example.com/this/images/image.jpg?hostname=example.com"
        self.assertEqual(expected, url)

    def test_build_url_with_specified_imagizer_host_with_https_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient("my.image.imagizer.example.com", True)
        client.imageOriginHost = "example.com"
        url = client.build_url("this/images/image.jpg")
        expected = "https://my.image.imagizer.example.com/this/images/image.jpg?hostname=example.com"
        self.assertEqual(expected, url)

    def test_build_url_with_params_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("image.jpg", {
            "width": 200,
            "height": 300,
            "crop": "fit"
        })
        expected = "http://demo.imagizercdn.com/image.jpg?width=200&hostname=example.com&crop=fit&height=300"
        self.assertEqual(expected, url)

    def test_build_url_with_quality_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("image.jpg", {
            "quality": 60
        })
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&quality=60"
        self.assertEqual(expected, url)

    def test_build_url_with_global_quality_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        client.quality = 60
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&quality=60"
        self.assertEqual(expected, url)

    def test_build_url_with_global_quality_override_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.quality = 60
        client.imageOriginHost = "example.com"
        url = client.build_url("image.jpg", {
            "quality": 55
        })
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&quality=55"
        self.assertEqual(expected, url)

    def test_build_url_with_dpr_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        url = client.build_url("image.jpg", {
            "dpr": 2
        })
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&dpr=2"
        self.assertEqual(expected, url)

    def test_build_url_with_global_dpr_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        client.dpr = 2
        url = client.build_url("image.jpg")
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&dpr=2"
        self.assertEqual(expected, url)

    def test_build_url_with_global_dpr_override_with_origin_host_specified(self):
        client = imagizer_client.ImagizerClient()
        client.imageOriginHost = "example.com"
        client.dpr = 2
        url = client.build_url("image.jpg", {
            "dpr": 3
        })
        expected = "http://demo.imagizercdn.com/image.jpg?hostname=example.com&dpr=3"
        self.assertEqual(expected, url)