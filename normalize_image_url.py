import pytest


def normalize_image_url(image_url, domain):
    if image_url.startswith('//'):
        image_url = 'http:' + image_url
    elif image_url.startswith('/'):
        image_url = 'http://' + domain + image_url
    return image_url


@pytest.mark.parametrize("image_url, domain, correct_image_url", [
    ('https://example.com/image.jpg', 'example.com', 'https://example.com/image.jpg'),
    ('//example.com/image.jpg', 'example.com', 'http://example.com/image.jpg'),
    ('/image.jpg', 'example.com', 'http://example.com/image.jpg')
])
def test_normalize_image_url_with_protocol(image_url, domain, correct_image_url):
    actual_result = normalize_image_url(image_url, domain)
    assert actual_result == correct_image_url