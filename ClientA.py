import pydiscover.client as pydiscover
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s - Client Discovery ] %(asctime)s - %(message)s')
log = logging.getLogger(__name__)


def main():
    try:
        response, server = pydiscover.discover(magic="fna349fn",
                                               port=50000,
                                               password="password",
                                               timeout=5)

        log.info("Discovered server: '%s - Response: \"%s\"" % (server, str(response)))
    except Exception as e:
        log.info(e)


if __name__ == '__main__':
    main()
