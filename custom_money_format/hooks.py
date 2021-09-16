# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "custom_money_format"
app_title = "Custom Money Format"
app_publisher = "Levitating Frog"
app_description = "Changes money formatting from symbol-amount (e.g. $ 10.00) to amount-currency_code (e.g. 10.00 USD)"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "none"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_js = "/assets/custom_money_format/js/custom_number_format.js"


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

