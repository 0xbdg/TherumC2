window.onload = function() {
    const savedCommand = localStorage.getItem('command');
    if (savedCommand) {
      document.getElementById('command').value = savedCommand;
    }
  };

function submitCommand() {

    // Simpan nilai input ke Local Storage sebelum submit

    var botId = document.getElementById('bot_id').value;
    var command = document.getElementById('command').value;
    localStorage.setItem('command', command);
    
    // Pastikan data dikodekan dengan benar
    var url = '/send_command?bot_id=' + encodeURIComponent(botId) + '&command=' + encodeURIComponent(command);

    // Redirect ke URL yang sesuai
    window.location.href = url;
}