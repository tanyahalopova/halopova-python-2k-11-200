import pytest

def normalize_image_url(image_url, domain):
    if image_url.startswith('//'):
        image_url = 'http:' + image_url
    elif image_url.startswith('/'):
        image_url = 'http://' + domain + image_url
    return image_url


def test_normalize_image_url_with_protocol():
    image_url = 'https://example.com/image.jpg'
    domain = 'example.com'
    assert normalize_image_url(image_url, domain) == 'https://example.com/image.jpg'

def test_normalize_image_url_without_protocol():
    image_url = '//example.com/image.jpg'
    domain = 'example.com'
    assert normalize_image_url(image_url, domain) == 'http://example.com/image.jpg'

def test_normalize_image_url_without_domain():
    image_url = '/image.jpg'
    domain = 'example.com'
    assert normalize_image_url(image_url, domain) == 'http://example.com/image.jpg'
