import pydiscover
from pydiscover.server import server_discover


def main():
    # Call server
    server_discover(answer="config.txt",
                    magic="fna349fn",
                    listen_ip="192.168.0.16",
                    port=50000,
                    password="password",
                    disable_hidden=True)


if __name__ == '__main__':
    main()

