from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        verbose_name='How old are you?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect)

    nativelang = models.StringField(
        choices = ['Yes', 'No'],
        verbose_name='Is English your native language?')

    selfrep_dataquality = models.IntegerField(
        choices = [
        [0, 'Not useful at all'],
        [1, 'Not very useful'],
        [2, 'Mostly useful'],
        [3, 'Completely useful']
        ],
        verbose_name = "Is the data you just generated of sufficient quality to be useful for scientific research? (Have you been concentrated and payed attention to the instructions) Please answer honestly.",
        widget=widgets.RadioSelect)

    income = models.IntegerField(
        choices = [
        [0, 'up to 1000'],
        [1, '1001 - 2000'],
        [2, '2001 - 3000'],
        [3, '3001 - 4000'],
        [4, '4001 - or more'],
        [99, 'Do not want to answer']
        ],
        verbose_name = 'Which category does your monthly income (after tax) fall into?')

    choice_strategie = models.LongStringField(
        verbose_name='''
        Please think back to the choice phase (when you decided between the two options). Can you describe how you made the decision which of the two options to pick?''',
    )

    instructions_clear = models.IntegerField(
        choices = [
        [0, 'Very unclear'],
        [1, 'Somewhat unclear'],
        [2, 'Not sure'],
        [3, 'Mostly clear'],
        [4, 'Absolutely clear']
        ],
        verbose_name = 'Was it clear to you what your task was in this study?')

    open_text = models.LongStringField(
        verbose_name='''
        Is there anything you would like us to know? (Optional)''',
        blank=True
    )
