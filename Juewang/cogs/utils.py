
from discord.ext import commands


def get_bourgeoisie_roles(roles, lowest_role_allowed):
  """Gets the topmost roles in list of roles given.

  Args:
    roles (list): List of roles to filter.
    lowest_role_allowed (discord.Role): Lowest role inside of the proletariat class.

  Returns:
    list: List of roles above or equal to lowest_role_allowed.

  """

  bourgeoisie = list(filter(lambda x: lowest_role_allowed >= role, roles))
  return bourgeoisie


def get_proletariat_roles(roles, highest_role_allowed):
  """Gets the bottomost roles in list of roles given.

  Args:
    roles (list): List of roles to filter.
    highest_role_allowed (discord.Role): Highest role inside of the proletariat class.

  Returns:
    list: List of roles below or equal to highest_role_allowed.

  """

  proletariat = list(filter(lambda x: highest_role_allowed <= role, roles))
  return proletariat
