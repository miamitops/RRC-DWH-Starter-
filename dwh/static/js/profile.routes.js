/**
 * http://usejsdoc.org/
 */
(function () {
	'use strict';
	angular
		.module('profile.routes')
		.config(config);
	config.$inject = ['$routeProvider'];
	/**
	* @name config
	* @desc Define valid application routes
	*/
	function config($routeProvider) {
	$routeProvider.when('/register', {
	controller: 'RegisterController',
	controllerAs: 'vm',
	templateUrl: '/static/templates/auth/register.html'
	}).otherwise('/');
	}
	})();
