changeUserName();

document.querySelector('#homeserver').addEventListener('change', () => {
    if(document.querySelector('#homeserver').value == 'other'){
        document.querySelector('#otherHomeServer').innerHTML += '<input type="text" name="newHomeServer" id="newHomeServer" placeholder="matrix.example.com">';

        document.querySelector('#newHomeServer').addEventListener('change', () => {
            changeUserName();
        })
    }
    else{
        document.querySelector('#otherHomeServer').innerHTML = '';
        changeUserName();
    }
})

document.querySelector('#username').addEventListener('change', () => {
    changeUserName();
})

function changeUserName(){
    let homeserver = getHomeServer();
    document.querySelector('#userNameServer').innerText = homeserver;
}

function getHomeServer(){
    let homeserver;

    if (document.querySelector('#homeserver').value == 'other'){
        homeserver = document.querySelector('#newHomeServer').value;
    }
    else{
        homeserver =  document.querySelector('#homeserver').value;
    }
    
    if (homeserver.split('.').length > 2){
        homeserver = homeserver.split('.')[1]+'.'+homeserver.split('.')[2];
        return homeserver;
    }
    else{
        return homeserver;
    }

}

document.querySelector('form').addEventListener('submit', () => {
    event.preventDefault()
    document.querySelector('#username').value = `@${document.querySelector('#username').value}:${getHomeServer()}`
    document.querySelector('form').submit()
})