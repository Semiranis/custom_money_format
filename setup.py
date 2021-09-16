from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_money_format/__init__.py
from custom_money_format import __version__ as version

setup(
	name="custom_money_format",
	version=version,
	description="Changes money formatting from symbol-amount (e.g. $ 10.00) to amount-currency_code (e.g. 10.00 USD)",
	author="Levitating Frog",
	author_email="none",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
