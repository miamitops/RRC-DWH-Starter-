/**
 * http://usejsdoc.org/
 */
(function () {
	'use strict';
	angular
		.module('profile.auth', [
		'profile.auth.controllers',
	'profile.auth.services'
	]);
	angular
	.module('profile.auth.controllers', []);
	angular
	.module('profile.auth.services', ['ngCookies']);
})();
