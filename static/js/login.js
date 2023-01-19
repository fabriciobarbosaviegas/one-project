document.querySelector('#homeserver').addEventListener('change', () => {
    if(document.querySelector('#homeserver').value == 'other'){
        document.querySelector('#otherHomeServer').innerHTML += '<input type="text" name="newHomeServer" id="newHomeServer" placeholder="matrix.example.com" required>';
    }
    else{
        document.querySelector('#otherHomeServer').innerHTML = '';
    }
})

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