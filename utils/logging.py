import logging

def setup_logging():
    logging.basicConfig(
        filename='agenthive.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(console_handler)
    
    log = logging.getLogger(__name__)
    log.info("Logging setup complete")
    return log