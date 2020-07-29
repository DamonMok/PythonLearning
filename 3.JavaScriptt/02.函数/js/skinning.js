	window.onload = function(){

		var oBtnLight = document.getElementById('light');
		var oBtnDark = document.getElementById('dark');
		var oLink = document.getElementById('link');

		oBtnLight.onclick = function(){

			oLink.href = 'css/skinningLight.css'
		}

		oBtnDark.onclick = function(){

			oLink.href = 'css/skinningDark.css'
		}

	}