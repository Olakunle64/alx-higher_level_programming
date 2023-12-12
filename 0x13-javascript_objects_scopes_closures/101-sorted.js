#!/usr/bin/node

/*Write a script that imports a dictionary of occurrences by user
 * id and computes a dictionary of user ids by occurrence
 */

dict = require('./101-data').dict
big_dict = {}
for (const key in dict) {
	if (dict.hasOwnProperty(key)) {
		const value = dict[key];
		if
