reportBuilderApp.controller('addCtrl', function($scope, $location, reportService) {
  reportService.options().then(function(options) {
    $scope.options = options.actions.POST;
  });
  $scope.submitForm = function() {
    if ($scope.reportForm.$valid) {
      reportService.create($scope.report).then(function(result) {
        $location.path('/report/' + result.id, true);
      });
    }
  }
});
reportBuilderApp.controller('genCtrl', function($scope, $routeParams, $location, $mdSidenav, reportService) {
	  $scope.static = static;
	  $scope.ASYNC_REPORT = ASYNC_REPORT;
	  $scope.reportData = {};
	  reportService.filterFieldOptions().then(function(options) {
	    $scope.filterFieldOptions = options.actions.POST;
	  });
	  reportService.getFormats().then(function(data) {
	    $scope.formats = data;
	  });

	  $scope.reports_list_menu = function() {
	    $mdSidenav('left').open();
	  };
	  $scope.field_menu = function() {
	    $mdSidenav('right').open();
	  };
	  $scope.selectedIndex = 0;

	  $scope.fieldCanFilter = function(field) {
	    if ($scope.selectedIndex === 0) {
	      return true;
	    }
	    if ($scope.selectedIndex === 1 && field.can_filter === true) {
	      return true;
	    }
	    return false;
	  }

	  $scope.requestFullscreen = function() {
	    var
	    el = document.documentElement,
	      rfs =
	        el.requestFullScreen || el.webkitRequestFullScreen || el.mozRequestFullScreen;
	    rfs.call(el);
	  };

	  $scope.openReport = function(reportId) {
	    $scope.showFields = true;
	    $location.path('/report/generate/' + reportId, false);
	    reportService.getReport(reportId).then(function(report) {
	      $mdSidenav('left').close();
	      $scope.fields_header = report.root_model_name;
	      $scope.report = report;
	      $scope.report.lastSaved = null;
	      root_related_field = {
	        verbose_name: report.root_model_name,
	        field_name: '',
	        path: '',
	        model_id: report.root_model
	      }
	      data = {
	        "model": report.root_model,
	        "path": "",
	        "path_verbose": "",
	        "field": ""
	      }
	      $scope.related_fields = [root_related_field]
	      reportService.getRelatedFields(data).then(function(result) {
	        root_related_field.related_fields = result;
	        var help_text = 'This model is included in report builder.';
	        if (result[0].included_model == false) {
	          help_text = 'This model is not included in report builder.';
	        }
	        $scope.help_text = help_text;
	      });
	      reportService.getFields(data).then(function(result) {
	        $scope.fields = result;
	      });
	    });
	  };

	  if ($routeParams.reportId) {
	    $scope.openReport($routeParams.reportId);
	  }

	});
reportBuilderApp.controller('homeCtrl', function($scope, $routeParams, $location, $mdSidenav, reportService) {
  $scope.static = static;
  $scope.ASYNC_REPORT = ASYNC_REPORT;
  $scope.reportData = {};
  reportService.filterFieldOptions().then(function(options) {
    $scope.filterFieldOptions = options.actions.POST;
  });
  reportService.getFormats().then(function(data) {
    $scope.formats = data;
  });

  $scope.reports_list_menu = function() {
    $mdSidenav('left').open();
  };
  $scope.field_menu = function() {
    $mdSidenav('right').open();
  };
  $scope.selectedIndex = 0;

  $scope.fieldCanFilter = function(field) {
    if ($scope.selectedIndex === 0) {
      return true;
    }
    if ($scope.selectedIndex === 1 && field.can_filter === true) {
      return true;
    }
    return false;
  }

  $scope.requestFullscreen = function() {
    var
    el = document.documentElement,
      rfs =
        el.requestFullScreen || el.webkitRequestFullScreen || el.mozRequestFullScreen;
    rfs.call(el);
  };

  $scope.openReport = function(reportId) {
    $scope.showFields = true;
    $location.path('/report/' + reportId, false);
    reportService.getReport(reportId).then(function(report) {
      $mdSidenav('left').close();
      $scope.fields_header = report.root_model_name;
      $scope.report = report;
      $scope.report.lastSaved = null;
      root_related_field = {
        verbose_name: report.root_model_name,
        field_name: '',
        path: '',
        model_id: report.root_model
      }
      data = {
        "model": report.root_model,
        "path": "",
        "path_verbose": "",
        "field": ""
      }
      $scope.related_fields = [root_related_field]
      reportService.getRelatedFields(data).then(function(result) {
        root_related_field.related_fields = result;
        var help_text = 'This model is included in report builder.';
        if (result[0].included_model == false) {
          help_text = 'This model is not included in report builder.';
        }
        $scope.help_text = help_text;
      });
      reportService.getFields(data).then(function(result) {
        $scope.fields = result;
      });
    });
  };

  if ($routeParams.reportId) {
    $scope.openReport($routeParams.reportId);
  }

});

reportBuilderApp.service('reportService', ['Restangular',
  function(Restangular) {
    var path = "report";
    var reports = Restangular.all(path);

    function getReport(reportId) {
      return Restangular.one(path, reportId).get();
    }

    function getRelatedFields(data) {
      return Restangular.all('related_fields').post(data);
    }

    function getFields(data) {
      return Restangular.all('fields').post(data);
    }

    function getFormats() {
      return Restangular.all('formats').getList();
    }

    function options() {
      return reports.options();
    }

    function filterFieldOptions() {
      return Restangular.all('filterfields').options();
    }

    function create(data) {
      return reports.post(data);
    }

    function deleteReport(reportId) {
      return Restangular.one(path, reportId).remove();
    }

    function getList() {
      return Restangular.all('reports').getList();
    }

    function getPreview(reportId) {
      return Restangular.one(path, reportId).getList('generate');
    }

    return {
      getReport: getReport,
      getRelatedFields: getRelatedFields,
      getFields: getFields,
      getFormats: getFormats,
      options: options,
      filterFieldOptions: filterFieldOptions,
      create: create,
      deleteReport: deleteReport,
      getList: getList,
      getPreview: getPreview
    };
  }
]);

reportBuilderApp.controller('LeftCtrl', function($scope, $routeParams, $mdSidenav, $location, reportService) {
  $scope.reports = reportService.getList().$object;
  $scope.reportOrder = "name";
  $scope.reverseReportOrder = false;

  $scope.currentUserFilter = function(report) {
    if ( report.user_created !== null ){
      return ( report.user_created.id == CURRENT_USER );
    } else {
      return false;
    }
  };

  $scope.notCurrentUserFilter = function(report) {
    return !( $scope.currentUserFilter(report) );
  };

  $scope.close = function() {
    $mdSidenav('left').close();
  };
  if (!$routeParams.reportId) {
    $mdSidenav('left').open();
  }
})

reportBuilderApp.controller('FieldsCtrl', function($scope, $mdSidenav, reportService, $mdDialog) {
	$scope.scrollbarConfig = {
			theme: 'dark',
			scrollInertia: 500
	};
	//Age groups 
	$scope.agegroups = [
	                    {
	                    	code:'A1',
	                    	ages:'0 to 5'
	                    },
	                    {
	                    	code:'A2',
	                    	ages:'6 to 11',
	                    },
	                    {
	                    	code:'A3',
	                    	ages:'12 to 18'
	                    },
	                    {
	                    	code:'A4',
	                    	ages:'19 t0 65'
	                    },
	                    {
	                    	code:'A5',
	                    	ages:'Above 65'
	                    }
	                    ];
	//end age groups
	
	//refugee statuses
	$scope.refugeestatuses = [
	                          {
	                        	  code:'REF',
	                        	  status:'Refugee'
	                          },
	                          {
	                        	  code:'NOC',
	                        	  status:'Not of concern'
	                          },
	                          {
	                        	  code:'RTR',
	                        	  status:'Returnee'
	                          },
	                          {
	                        	  code:'ASR',
	                        	  status:'ASR'
	                          },
	                          {
	                        	  code:'OCO',
	                        	  status:'Other of Concern'
	                          }
	                          ]
	//end refugee statuses
	
	//process statuses
	$scope.processtatuses = [
	                         {
	                        	 code:'A',
	                        	 status:'Active'
	                         },
	                         {
	                        	 code:'H',
	                        	 status:'H'
	                         },
	                         {
	                        	 code:'C',
	                        	 status:'C'
	                         },
	                         {
	                        	 code:'L',
	                        	 status:'L'
	                         }
	                         ]
	//end processstatuses
	$scope.load_fields = function(field) {
    data = {
      "model": field.model_id,
      "path": field.path,
      "path_verbose": field.path_verbose,
      "field": field.field_name
    }
    $scope.help_text = field.help_text;
    $scope.fields_header = field.verbose_name;
    reportService.getFields(data).then(function(result) {
      $scope.fields = result;
    });
    reportService.getRelatedFields(data).then(function(result) {
      field.related_fields = result;
      var help_text = 'This model is included in report builder.';
      if (result[0].included_model == false) {
        help_text = 'This model is not included in report builder.';
      }
      $scope.help_text = help_text;
    });
  }

  $scope.toggle_related_fields = function(node) {
    field = node.$nodeScope.$modelValue;
    parent_field = node.$parent.$modelValue;
    data = {
      "model": field.model_id,
      "path": parent_field.path,
      "field": field.field_name
    }
    reportService.getRelatedFields(data).then(function(result) {
      field.related_fields = result;
    });
  };
  $scope.answer = function(answer){
	  $mdDialog.hide();  
  };
  $scope.click_field = function(field) {
    $scope.help_text = '[' + field.field_type + '] ' + field.help_text;
  };
  $scope.openMenu = function($mdOpenMenu, ev) {
      originatorEv = ev;
      $mdOpenMenu(ev);
    };
  $scope.showAdvanced = function(field, ev, ind) {
	  $scope.field = field;
	  $scope.index = ind;
	  if(ind == 0){
		  //Add a display
		  //set some defaults
		 $scope.field.group = true;
		 $scope.field.total = false;
		 $scope.field.display_format = "";
		 $scope.field.sort_reverse = true;
		 var tempFile = 'dialog.add.html';
	  }else if(ind == 1){
		  
		  var tempFile = 'filter.add.html';
	  }
	  $mdDialog.show({
	      scope:$scope,
	      preserveScope: true,
	      templateUrl: '/static/report_builder/partials/' + tempFile,
	      locals:{field: $scope},
	      parent: angular.element(document.body),
	      targetEvent: ev,
	      clickOutsideToClose:true,
	    });
	 };
  $scope.add_field = function(field, index) {
    field.report = $scope.report.id;
    if (index === 0) {
      $scope.report.displayfield_set.push(angular.copy(field));
    } else if (index === 1) {
      $scope.report.filterfield_set.push(angular.copy(field));
      
    };
    console.log($scope.report.displayfield_set);
    $mdDialog.hide();
  };
});

reportBuilderApp.controller('ReportDisplayCtrl', function($scope, $mdDialog) {
  $scope.deleteField = function(elem, field) {
	if (field.field == "individualguid"){
		var tempFile = 'not_permited.html';
		$mdDialog.show({
		      scope:$scope,
		      preserveScope: true,
		      templateUrl: '/static/report_builder/partials/' + tempFile,
		      locals:{field: $scope},
		      parent: angular.element(document.body),
		      clickOutsideToClose:true,
		    });
	}else{
		 elem.remove();
	};
   
  };
});

reportBuilderApp.controller('ReportOptionsCtrl', function($scope, $location, $window, reportService) {
  $scope.deleteReport = function(reportId) {
    var url = $location.url();
    var absUrl = $location.absUrl();
    var origin = absUrl.substr(0,absUrl.indexOf(url));
    reportService.deleteReport(reportId).then(function() {
      // Getting another ID to redirect to now that our report has been deleted
      reportService.getList().then(function(list) {
        if (list[0]) {
          $window.location.href = origin + '/report/' + list[0].id;
        } else {
          $window.location.href = origin;
        }
        // $location.path('/report/' + list[0].id, true);
      });
    });
  }
});

reportBuilderApp.controller('ReportFilterCtrl', function($scope) {
  $scope.deleteField = function(field) {
    field.remove();
  };
});

reportBuilderApp.controller('ReportShowCtrl', function($scope, $window, $http, $timeout, $mdToast, reportService) {
  $scope.getPreview = function() {
    $scope.reportData.statusMessage = null;
    $scope.reportData.refresh = true;
    reportService.getPreview($scope.report.id).then(function(data) {
      columns = [];
      angular.forEach(data.meta.titles, function(value) {
        columns.push({
          'title': value
        });
      });
      $scope.reportData.items = data;
      $scope.reportData.columns = columns;
      $scope.reportData.refresh = false;
    }, function(response) {
      $scope.reportData.refresh = false;
      $scope.reportData.statusMessage = "Error with status code " + response.status;
    });
  };

  $scope.save = function() {
	  // add a field to count if it doesnt exist
	  console.log($scope.report.displayfield_set);
    angular.forEach($scope.report.displayfield_set, function(value, index) {
      value.position = index;
      if (value.sort === "") {
        value.sort = null;
      }
    });
    angular.forEach($scope.report.filterfield_set, function(value, index) {
      value.position = index;
    });
    $scope.report.save().then(function(result) {
      $scope.report.lastSaved = new Date();
      $scope.reportData.reportErrors = null;
      $mdToast.show(
        $mdToast.simple()
        .content('Report Saved!')
        .hideDelay(1000));
    }, function(response) {
      $mdToast.show(
        $mdToast.simple()
        .content('Unable to Save!')
        .hideDelay(1000));
      $scope.reportData.reportErrors = response.data;
    });
  };

  $scope.downloadReport = function(filetype) {
    base_url = BASE_URL + 'report/' + $scope.report.id
    url = base_url + '/download_file/' + filetype + '/';
    $scope.workerStatus = 'Requesting report';
    if (ASYNC_REPORT === "True") {
      $http.get(url).
      success(function(data) {
        $scope.workerStatus = 'Report Requested';
        var attempts = 0;
        var task_id = data.task_id;
        var checkPoller = function() {
          $http.get(base_url + '/check_status/' + task_id + '/').success(function(check_data) {
            if (check_data.state === "SUCCESS") {
              $scope.workerStatus = null;
              $scope.workerState = null;
              $window.location.href = check_data.link;
              $mdToast.show(
                $mdToast.simple()
                .content('Report Ready!')
                .hideDelay(4000));
            } else {
              $scope.workerStatus = 'Waiting on worker. State is ' + check_data.state;
              $scope.workerState = check_data.state;
              attempts += 1;
              if (check_data.state !== "FAILURE") {
                $timeout(checkPoller, 1000 + (500 * attempts));
              }
            }
          })
        };
        $timeout(checkPoller, 100);
      });
    } else {
      $window.location.href = url;
    }
  }
});
