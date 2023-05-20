document.addEventListener('DOMContentLoaded', function() {
  var scanButton = document.getElementById('scan');
  scanButton.addEventListener('click', async function() {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const tabId = tab.id;
    chrome.scripting.executeScript(
      {
        target: { tabId },
        func: () => document.body.innerText
      },
      (result) => {
        if (result && result.length > 0) {
          const currentContent = result[0].result;
          console.log(currentContent);
          $.ajax({
	          type: "GET", // post or get
	          url: "https://dummy.restapiexample.com/api/v1/employees", 	// api url
	          // data: {currentContent:currentContent},	// sent data
	          dataType: "json", //received data 
	          success: function (data) {
	            if(data.status == "success"){
	            	console.log(currentContent)
	            	alert(currentContent)
	            	// location.reload()
	            }
	            else{
	            	alert("error")
	            }
	          },
	          error: function (statis) {
	            console.log(status);
	          },
	      	});
        } else {
          console.error("Unable to retrieve current content.");
        }
      }
    );
  });
});


$('#upload').click(uploadFile);

function uploadFile() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (file) {
    const formData = new FormData();
    formData.append('audioFile', file);

    $.ajax({
      url: 'https://dummy.restapiexample.com/api/v1/employees', // Replace with your server endpoint
      type: 'GET',
      data: formData,
      processData: false,
      contentType: false,
      success: function(response) {
        $('#output').text('File uploaded successfully.');
      },
      error: function() {
        $('#output').text('Error uploading the file.');
      }
    });
  } else {
    $('#output').text('Please select an audio file.');
  }
}
