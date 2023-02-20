let contacts = document.querySelector("#sidebar-contacts").querySelectorAll("a")

for(i = 0; i < contacts.length; i++){
    contacts[i].addEventListener("click", (e) => {
        let room_id = window.location.href.split("/")
        room_id = room_id[room_id.length - 1]
        console.log(room_id)

        $.ajax({
            type: "POST",
            url: "/",
            roomid: room_id,
          });
    });
}