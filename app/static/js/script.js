const posterMasterPlay = document.getElementById("poster_master_play")
const title = document.getElementById("title")
const playIcon = document.querySelector(".bx-play-circle")

// Get the references to the song item in the "pop_song" sections
const songItems = document.querySelectorAll(".songItem")
songItems.forEach((songItem,index)=>{
    songItem.addEventListener("click",()=>{
        // get the song details fron the clicked song Item
        console.log("clicked")
        
        const coverImage = songItems.querySelector("img")
        const songName = soneItems.querySelector("h5").textContent
        const artistName = songItem.querySelector(".subtitle").textContent

        // set the Master_play section with the song details

        posterMasterPlay.src = coverImage.src
        title.innerHTML = `${songName}<br>\
                            <div class = 'subtitle'>${artistName}</div>`

        playIcon.classList.remove("bx-play-circle")
        playIcon.classList.add("bx-pause-circle")
    })
})

