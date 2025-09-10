    async function get_messages() {
        console.log('get_messages is called')
        fetch("chats/all", { cache: "no-store" })
            .then((res) => res.json())
            .then((rows) => {
                document.getElementById('msgs').innerHTML = ""
                for (let i = 0; i < rows.messages.length; i++) {
                    let line = document.createElement('li')
                    let message = document.createElement('div')
                    let text = document.createElement('p')
                    text.innerText = rows.messages[i].writer + ':\n' + rows.messages[i].text
                    
                    message.appendChild(text)
                    document.getElementById('msgs').appendChild(message)
                }
                setTimeout('get_messages()', 1000*10);
            })
            .catch((error) => {
                alert(error)
            });
    }

    document.addEventListener('DOMContentLoaded', function () {
        get_messages()
    })