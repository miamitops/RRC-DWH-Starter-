/**
 * http://usejsdoc.org/
 */
(function () {
	'use strict';
	angular
		.module('profile', [
		'profile.routes',
		'profile.auth'
		]);
	angular
		.module('profile.routes', ['ngRoute']);
	angular
		.module('profile')
		.run(run);
	run.$inject = ['$http'];
	* @name run
	* @desc Update xsrf $http headers to align with Django's defaults
	*/
	function run($http) {
		$http.defaults.xsrfHeaderName = 'X‐CSRFToken';
		$http.defaults.xsrfCookieName = 'csrftoken';
	}
})();
