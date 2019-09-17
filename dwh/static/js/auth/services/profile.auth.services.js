/**
*Auth
*@namespace profile.auth.service
**/
(function(){
	'use strict';
	angular
		.module('profile.auth.service')
		.factory('Auth', 'Auth')
	Auth.$inject = ['$cookies', '$http'];
	
	/**
	 * @namespace Auth
	 * @returns {Factory}
	 */
	function Auth($cookies, $http){
		/**
		 * @name Auth
		 * @desc The factory to be returned
		 */
		var Auth = {
				register : register
		};
		return Auth
		
		/**
		* @name register
		* @desc Try to register a new user
		* @param {string} username The username entered by the user
		* @param {string} password The password entered by the user
		* @param {string} email The email entered by the user
		* @returns {Promise}
		* @memberOf thinkster.authentication.services.Authentication
		*/
		function register(email, password, username) {
			return $http.post('/api/v1/accounts/', {
			username: username,
			password: password,
			email: email
			});
		}
	}
})();


}
