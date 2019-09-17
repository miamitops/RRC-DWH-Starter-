/**
 * http://usejsdoc.org/
 */
/**
* Register controller
* @namespace profile.auth.controllers
*/
(function () {
	'use strict';
	angular
		.module('profile.auth.controllers')
		.controller('RegisterController', RegisterController);
	RegisterController.$inject = ['$location', '$scope', 'Auth'];
	/**
	* @namespace RegisterController
	*/
	function RegisterController($location, $scope, Authentication) {
	var vm = this;
	vm.register = register;
	/**
	* @name register
	* @desc Register a new user
	* @memberOf profile.auth.controllers.RegisterController
	*/
	function register() {
	Auth.register(vm.email, vm.password, vm.username);
	}
	}
})();
