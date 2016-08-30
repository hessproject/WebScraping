#! python3

"""
A module for scraping Bulbapedia for pokemon stats (Currently only implemented for Gen I)
"""
import requests
import bs4


def getPokemonPageData():
    """
    :return: A BeautifulSoup object containing data from Bulbapedia
    """
    url = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_base_stats_(Generation_I)"
    r = requests.get(url, "lxml")
    soup = bs4.BeautifulSoup(r.content)
    return soup


def getPokemonIds(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon IDs
    """
    listOfIDs = []

    for element in soup.find_all("b"):
        _verifyAndAppendElement(element, listOfIDs)

    return listOfIDs


def getPokemonNames(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon names in order
    """
    listOfNames = []

    for element in soup.find_all("td", align="left"):
        _verifyAndAppendElement(element, listOfNames)

    return listOfNames


def getHPStats(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon HP base stats
    """
    listOfHPs = []

    for element in soup.find_all("td", style="background:#FF5959"):
        _verifyAndAppendElement(element,listOfHPs)

    return listOfHPs


def getAttackStats(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon Attack base stats
    """
    listOfAttacks = []

    for element in soup.find_all("td", style="background:#F5AC78"):
        _verifyAndAppendElement(element,listOfAttacks)

    return listOfAttacks


def getDefenseStats(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon Defense base stats
    """
    listOfDefenses = []

    for element in soup.find_all("td", style="background:#FAE078"):
        _verifyAndAppendElement(element,listOfDefenses)

    return listOfDefenses


def getSpeedStats(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon Speed base stats
    """
    listOfSpeeds = []

    for element in soup.find_all("td", style="background:#FA92B2"):
        _verifyAndAppendElement(element,listOfSpeeds)

    return listOfSpeeds


def getSpecialStats(soup):
    """
    :param soup: The BeautifulSoup object returned by getPageData()

    :return: A list of Pokemon Special base stats
    """
    listOfSpecials = []

    for element in soup.find_all("td", style="background:#94EFE0"):
        _verifyAndAppendElement(element,listOfSpecials)

    return listOfSpecials


def _verifyAndAppendElement(element, list):
    if element.text is not None or element.text is not "":
        list.append(element.text.strip())


def zipStats(ids, names, hps, attacks, defenses, speeds, specials):
    return list(zip(ids,names,hps,attacks,defenses,speeds,specials))


def main():
    soup = getPokemonPageData()

    ids = getPokemonIds(soup)
    names = getPokemonNames(soup)
    HPStats = getHPStats(soup)
    attackStats = getAttackStats(soup)
    defenseStats = getDefenseStats(soup)
    speedStats = getSpeedStats(soup)
    specialStats = getSpecialStats(soup)

    return zipStats(ids, names, HPStats, attackStats, defenseStats, speedStats, specialStats)

if __name__ == "__main__":
    main()