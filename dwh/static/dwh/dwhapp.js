var datawarehouse = angular.module('dataWarehose', ['ngRoute', 'restangular', 'ngMaterial', 'ui.tree', 'ngAnimate', 'ngHandsontable', 'angularPikaday']);
datawarehouse.config(function($sceProvider) {
	   $sceProvider.enabled(false);
	});

var dataWarehouseApp = angular.module('dataWarehouseApp', ['dataWarehouse']);