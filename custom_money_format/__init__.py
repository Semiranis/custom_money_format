# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import frappe.utils.data
import custom_money_format.modified_scripts.data

__version__ = '0.0.1'

# replace frappe function and its alias with custom function
frappe.utils.fmt_money = custom_money_format.modified_scripts.data.custom_fmt_money
frappe.utils.data.fmt_money = custom_money_format.modified_scripts.data.custom_fmt_money

