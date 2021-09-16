# Original data.py and fmt_money:
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License
#
# Changes:
# Copyright (c) 2021, Levitating Frog and Contributors
# MIT License

"""
custom_fmt_money() is modified version of fmt_money from frappe script:
frappe-bench/apps/frappe/frappe/utils/data.py

Original fmt_money returns currency symbol and amount,
custom_fmt_money returns amount and currency.

Example for both versions:

frappe.utils.data.fmt_money("10", "2", "USD")
returns: $ 10.00

custom_fmt_money("10", "2", "USD")
returns: 10.00 USD
"""

from __future__ import unicode_literals

import frappe
from frappe.utils.data import cint, get_number_format_info, flt, cstr


def custom_fmt_money(amount, precision=None, currency=None, format=None):
	# Below code is copied from frappe/utils/data.py fmt_money and modified.
	# Modified lines (in the end) are marked.

	"""
	Convert to string with commas for thousands, millions etc
	"""
	number_format = format or frappe.db.get_default("number_format") or "#,###.##"
	if precision is None:
		precision = cint(frappe.db.get_default('currency_precision')) or None

	decimal_str, comma_str, number_format_precision = get_number_format_info(number_format)

	if precision is None:
		precision = number_format_precision

	# 40,000 -> 40,000.00
	# 40,000.00000 -> 40,000.00
	# 40,000.23000 -> 40,000.23

	if isinstance(amount, str):
		amount = flt(amount, precision)

	if decimal_str:
		decimals_after = str(round(amount % 1, precision))
		parts = decimals_after.split('.')
		parts = parts[1] if len(parts) > 1 else parts[0]
		decimals = parts
		if precision > 2:
			if len(decimals) < 3:
				if currency:
					fraction  = frappe.db.get_value("Currency", currency, "fraction_units", cache=True) or 100
					precision = len(cstr(fraction)) - 1
				else:
					precision = number_format_precision
			elif len(decimals) < precision:
				precision = len(decimals)

	amount = '%.*f' % (precision, round(flt(amount), precision))

	if amount.find('.') == -1:
		decimals = ''
	else:
		decimals = amount.split('.')[1]

	parts = []
	minus = ''
	if flt(amount) < 0:
		minus = '-'

	amount = cstr(abs(flt(amount))).split('.')[0]

	if len(amount) > 3:
		parts.append(amount[-3:])
		amount = amount[:-3]

		val = number_format=="#,##,###.##" and 2 or 3

		while len(amount) > val:
			parts.append(amount[-val:])
			amount = amount[:-val]

	parts.append(amount)

	parts.reverse()

	amount = comma_str.join(parts) + ((precision and decimal_str) and (decimal_str + decimals) or "")
	if amount != '0':
		amount = minus + amount

	if currency and frappe.defaults.get_global_default("hide_currency_symbol") != "Yes":
		# ------------ modified lines ------------
		# symbol is not used anymore
		#symbol = frappe.db.get_value("Currency", currency, "symbol", cache=True) or currency
		#amount = symbol + " " + amount

		# alternative money format
		amount = amount + " " + currency
		# --------- end of modified lines ---------

	return amount

