// Get all the form elements
const forms = document.getElementsByTagName('form');

// apply for each element 
Array.from(forms).forEach(form => {
	noRefresh(form);
});


function noRefresh(form){
	/* Prevent from refreshing page */
	if(form){
		form.addEventListener('submit', function(event) {
			event.preventDefault();
			const formData = new FormData(form);
			console.log(event);
			// formData[form] = data.value;
			// fetch('/', {
			// 	method: 'POST',
			// 	// body: formData,
			// 	body: event,
			// }).then(function(response) {});
		});
	} else {
		console.log(`Faield at: ${form}`);
	}
}

