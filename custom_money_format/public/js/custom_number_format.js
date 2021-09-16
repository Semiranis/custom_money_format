frappe.provide("frappe.public");
frappe.provide("frappe.controllers");
frappe.provide("frappe.form.formatters");

function format_currency(v, currency, decimals) {
	var format = get_number_format(currency);

	if(decimals === undefined) {
		decimals = frappe.boot.sysdefaults.currency_precision || null;
	}

	if (currency)
		return format_number(v, format, decimals) + " " + currency;
	else
		return format_number(v, format, decimals);
}

function fmt_money(v, format){
	// deprecated!
	// for backward compatibility
	return format_currency(v, format);
}

Object.assign(window, {format_currency, fmt_money});

