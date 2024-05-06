document.getElementById('copy-button').addEventListener('click', function() {
    var inputText = document.getElementById('input-text').value;
    var translatedText = "Please translate this text: \n[" + inputText + "] \n into Arabic.";
    
    navigator.clipboard.writeText(translatedText).then(function() {
        document.getElementById('copy-status').innerText = 'Copied Successfully!';
    }, function(err) {
        document.getElementById('copy-status').innerText = 'Error copying text!';
    });
});