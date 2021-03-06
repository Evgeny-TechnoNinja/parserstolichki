from utils import get_document  # noqa
from bs4 import BeautifulSoup
from config import MARKUP_ANALYZER, SERVICE_URL, SERVICE_OPTIONS, REGEX, USER_NOTIFICATION, PROGRESS_BAR_SETTING  # noqa
import re
from random import sample
from tqdm import tqdm


def get_user_agents(num_ua: int):
    """Retrieves a list of user-agents.
    Receives data from a resource, makes a list of them.
    Returns the required number of user-agents.
    :param num_ua: number of user-agents
    :return: list of random user-agents
    """
    result = []
    document = get_document(SERVICE_URL['user-agent'])
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    cells = soup.find_all('td')
    for cell in tqdm(cells, desc='Receiving user-agents', bar_format=PROGRESS_BAR_SETTING):
        if re.match(REGEX['user-agent'], cell.get_text()):
            result.append(''.join(cell.get_text().split('\n')).strip())
    try:
        return sample(result, num_ua)
    except ValueError as error:
        print(USER_NOTIFICATION['attention_block'].format('User-Agent') + ' ' + str(error))
        print(USER_NOTIFICATION['attention_block'].format('User-Agent') + ' ' + USER_NOTIFICATION['attention_dialog'])
        num_ua = SERVICE_OPTIONS['number']
        return sample(result, num_ua)

