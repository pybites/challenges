"""
This Python script generates a JSON string as per the PCC 54 requirements. The scrupt requests and parses the
https://codechalleng.es page and collects the Challanged and Bites information.
From the list, it will randomly create a task list for 100 days and return as a JSON string.
"""
import random
import requests
from bs4 import BeautifulSoup
import json


class CurriculumGenerator:
    """Curriculum Generator Class"""
    CODE_CHALLENGE_URL = 'https://codechalleng.es'
    TASKS_COUNT = 100

    def __init__(self):
        """Constructor."""
        pass

    def _get_challenges(self):
        """Helper method to get the challenges from the Codechallenge portal and create a list of challenges"""
        url = self.CODE_CHALLENGE_URL + '/challenges'
        page = requests.get(url)
        page.raise_for_status()

        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', attrs={'id': 'filterList2'})
        anchors = table.findAll('a')

        challenges = [f"Challenge: {anchor.getText()[5:]} ({self.CODE_CHALLENGE_URL}{anchor['href']})" for anchor
                      in anchors if anchor]
        return challenges

    def _get_bites(self):
        """Helper method to get the bites from the Codechallenge portal and create a list of bites"""
        url = self.CODE_CHALLENGE_URL + '/bites'
        page = requests.get(url)
        page.raise_for_status()

        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('div', attrs={'id': 'pane-default-1'}).find('table')
        anchors = table.findAll('a', attrs={'class': 'extraIndent'})

        bites = [f"Bite: {anchor.getText().strip()} ({self.CODE_CHALLENGE_URL}{anchor['href']})" for anchor in
                 anchors if anchor]
        return bites

    def generate_task_list(self):
        """Public method to get the challenges and bites from Pybite code challenge portal and create a task for 100
        days. Each task is selected random from the pool and none are repeated.
        The result is returned as a JSON string as mandated in the PCC 55 challenge spec."""

        tasks = {'version': 0.1, 'github_repo': '',
                 'title': 'Pybites 100 days', 'tasks': list()}
        tasks_list = self._get_challenges() + self._get_bites()

        day = 1

        while day <= self.TASKS_COUNT:
            activity = random.choice(tasks_list)

            if activity not in tasks['tasks']:
                task = {
                    "day": day,
                    "activity": activity,
                    "done": False
                    }
                day += 1
                tasks['tasks'].append(task)

        return json.dumps(tasks)


if __name__ == '__main__':
    cg = CurriculumGenerator()
    print(cg.generate_task_list())
