const roomName = JSON.parse(document.getElementById('json-roomname').textContent)
const userName = JSON.parse(document.getElementById('json-username').textContent)
const chatSocket = new WebSocket(
  'ws://' + window.location.host + '/ws/' + roomName + '/'
);

function formatAMPM(date) {
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const ampm = hours >= 12 ? 'p.m.' : 'a.m.';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  const strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}

chatSocket.onmessage = function(e) {
    console.log('onmessage')

    const data = JSON.parse(e.data);

    if(data.message){
        const messageClass = data.username === userName ? 'chat-message right' : 'chat-message left';
        const now = new Date();
        const currentTime = formatAMPM(now);

        let html = '<div class="' + messageClass + '">'
            html += '<div class="message-info"><img src="https://bootdey.com/img/Content/avatar/avatar1.png" alt="User Avatar" width="40" height="40">'
            html += '<div class="message-time">' + currentTime + '</div></div>'
            html += '<div class="message-content"><div class="message-author">' + data.username + '</div>' + data.message + '</div></div>';

        document.querySelector('#chat-messages').innerHTML += html;
        scrollToBottom();
    } else{
        alert('The message was empty!');
    }
}

chatSocket.onclose = function(e) {
console.log('onclose')
}


document.querySelector('#chat-message-submit').onclick = function(e) {
    e.preventDefault();

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value.trim();

    chatSocket.send(JSON.stringify({
        'message': message,
        'room': roomName
    }));

    messageInputDom.value = '';

    return false;
}

function scrollToBottom(){
    const objDiv = document.querySelector('#chat');
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();