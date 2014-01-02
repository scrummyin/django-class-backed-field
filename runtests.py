import sys
from optparse import OptionParser

app = "class_backed_field"


urlpatterns = [],
default_settings = {
    'ROOT_URLCONF': 'runtests',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.db',
        }
    },
    'INSTALLED_APPS': [
        app,
        "tests"
    ],
    "USE_TZ": True,
    "CACHES" : {
        'pitch': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
}


def runtests(*test_args):
    if not test_args:
        test_args = ["tests.test",]

    from django.conf import settings
    settings.configure(**default_settings)

    # Run the test suite, including the extra validation tests.

    from django.test.utils import get_runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=False, failfast=False)
    failures = test_runner.run_tests(test_args)
    return failures


def main(*args):
    failures = runtests(*args)
    sys.exit(failures)


if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()
    main(*args)
