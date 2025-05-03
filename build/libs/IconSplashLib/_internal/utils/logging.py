import logging

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # Further configuration for centralized logging systems like ELK stack, Sentry, etc.
