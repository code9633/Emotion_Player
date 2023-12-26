// let's select the all required tags or elements

const wrapper = document.querySelector(".wrapper"),
musicImg = wrapper.querySelector('.img-area img'),
musicName = wrapper.querySelector(".song-details .name"),
musicArtist = wrapper.querySelector(".song-details .artist"),
mainAudio = wrapper.querySelector("#main-audio"),
playPauseBtn = wrapper.querySelector(".play-pause"),
prevBtn = wrapper.querySelector("#prev"),
nextBtn = wrapper.querySelector("#next"),
progressArea = wrapper.querySelector(".progress-area"),
progressBar = wrapper.querySelector(".progress-bar"),
repeatIcon = wrapper.querySelector("#repeat-plist"),
musicList = wrapper.querySelector(".music-list"),
showMoreBtn = wrapper.querySelector('#more-music'),
hideMusicBtn = musicList.querySelector("#close");


let musicIndex = Math.floor((Math.random() * allMusics.length) + 1);

window.addEventListener("load", ()=>{
    loadMusic(musicIndex) // calling load music function once window  is loaded
    playingNow();
})

// load music function
function loadMusic(indexNumb){
    musicName.innerText = allMusics[indexNumb-1].name;
    musicArtist.innerText = allMusics[indexNumb - 1].artist;
    musicImg.src = `images/${allMusics[indexNumb - 1 ].img}.jpg`;
    mainAudio.src = `songs/${allMusics[indexNumb - 1].src}.mp3`;
}

//play Music function
function playMusic(){
    wrapper.classList.add("paused")
    playPauseBtn.querySelector("i").className = "fa-sharp fa-solid fa-pause"
    mainAudio.play()
}

//pause music function
function pauseMusic(){
    wrapper.classList.remove("paused")
    playPauseBtn.querySelector('i').className = "fa-sharp fa-solid fa-play";
    mainAudio.pause();
}

//next music function
function nextMusic(){
    // here we'll just increment of index by i 
    musicIndex++;
    // if musicindex is greater than array length then musicIndex will be one so the first song will be play
    musicIndex > allMusics.length ? musicIndex = 1: musicIndex = musicIndex; 
    loadMusic(musicIndex)
    playMusic();
    playingNow()
}

//previous music function
function prevMusic(){
    musicIndex--;
    // if musicindex is less than 1 then musicIndex will be the last song of the array
    musicIndex < 1 ? musicIndex = allMusics.length : musicIndex = musicIndex;
    loadMusic(musicIndex)
    playMusic(); 
    playingNow()

}

//play or music button event
playPauseBtn.addEventListener('click',()=>{
    const isMusicPaused = wrapper.classList.contains("paused")
    //if isMusicPpaused is true then call pauseMusic else call play music
    isMusicPaused ? pauseMusic() : playMusic()
    playingNow()
})

//next music btn event
nextBtn.addEventListener("click", ()=>{
    nextMusic();
})

prevBtn.addEventListener("click", ()=>{
    prevMusic();
})

//update the progress bar width according to music current time
mainAudio.addEventListener("timeupdate", (e)=>{
    const currentTime = e.target.currentTime; // getting the current time
    const duration = e.target.duration; //getting the total duration of song
    let progressWidth = (currentTime / duration) *100;
    progressBar.style.width = `${progressWidth}%`;

    let musicCurrentTime = wrapper.querySelector(".current"),
        musicDuration = wrapper.querySelector(".duration");


    mainAudio.addEventListener("loadeddata" ,()=>{      
        // update song label duration
        let audioDuration = mainAudio.duration;
        let totalMin = Math.floor(audioDuration / 60);
        let totalSec = Math.floor(audioDuration % 60);
        if (totalSec < 10){ // adding 0 if sec is less than 10
            totalSec = `0${totalSec}`
            
        }
        musicDuration.innerText = `${totalMin}:${totalSec}`;

    });

        // update playing song current time

    let currentMin = Math.floor(currentTime / 60);
    let currentSec = Math.floor(currentTime % 60);
    if (currentSec < 10){ // adding 0 if sec is less than 10
        currentSec = `0${currentSec}`
            
    }
    musicCurrentTime.innerText = `${currentMin}:${currentSec}`;
        
})

// update playing song current time accroding to the progress width
progressArea.addEventListener("click", (e)=>{
    let progressWidthval = progressArea.clientWidth; //getting width of progress bar
    let clickedOffSetX = e.offsetX; //getting offset x value
    let songDuration = mainAudio.duration // gettting song duration

    mainAudio.currentTime = (clickedOffSetX / progressWidthval) * songDuration;
    playMusic();

})

//work on repeat, shuffle song according to the icon click
repeatIcon.addEventListener("click", ()=>{

    if (repeatIcon.classList.contains("fa-repeat")){

        repeatIcon.classList.remove("fa-repeat");
        repeatIcon.classList.add("fa-shuffle");
    }

    else if(repeatIcon.classList.contains('fa-shuffle'))
    {
        repeatIcon.classList.remove("fa-shuffle");
        repeatIcon.classList.add("fa-repeat");
    }  
})

// after song ended
mainAudio.addEventListener("ended", ()=>{ 

    if (repeatIcon.classList.contains("fa-repeat")){
        nextMusic();
    }   
    else if (repeatIcon.classList.contains("fa-shuffle")){
        let randomIndex = Math.floor((Math.random() * allMusics.length));
        loadMusic(randomIndex);
        playMusic();
        playingNow()
    }
})

// when clicking more-music icon show the music list
showMoreBtn.addEventListener("click", ()=>{
    musicList.classList.toggle("show");
})

hideMusicBtn.addEventListener("click", ()=>{
   showMoreBtn.click();
})
    
const ulTag = wrapper.querySelector("ul");

for (let i = 0; i < allMusics.length; i++) {

    let liTag = `<li li-index = "${i + 1}">
                    <div class="row">
                        <span>${allMusics[i].name}</span>
                        <p>${allMusics[i].artist}</p>
                    </div>
                    <span id="${allMusics[i].src}" class="audio-duration">3:40</span>
                    <audio class="${allMusics[i].src}" src="songs/${allMusics[i].src}.mp3"></audio>
                </li>`;
                
    ulTag.insertAdjacentHTML("beforeend", liTag); 
    
    let liAudioDuartionTag = ulTag.querySelector(`#${allMusics[i].src}`);
    let liAudioTag = ulTag.querySelector(`.${allMusics[i].src}`);
    liAudioTag.addEventListener("loadeddata", ()=>{
        let duration = liAudioTag.duration;
        let totalMin = Math.floor(duration / 60);
        let totalSec = Math.floor(duration % 60);
        if(totalSec < 10){ 
        totalSec = `0${totalSec}`;
        };

        liAudioDuartionTag.innerText = `${totalMin}:${totalSec}`; //passing total duation of song
        liAudioDuartionTag.setAttribute("t-duration", `${totalMin}:${totalSec}`); //adding t-duration attribute with total duration value
  });
}

// Work on play partcular song on click
 const allLiTags = ulTag.querySelectorAll("li")

 function playingNow(){

    for (let  j = 0; j < allLiTags.length ; j++){
        let audioTag = allLiTags[j].querySelector(".audio-duration")
        
        if (allLiTags[j].classList.contains("playing")){
            allLiTags[j].classList.remove("playing")
            // get that audio duration value ans pass to .audio-duration innertext
            let adDuration = audioTag.getAttribute("t-duration")
            audioTag.innerText = adDuration;
        }

        //if  there is li tag where li-index is equal to music index
        // then this music is playing now and we'll style it
        if (allLiTags[j].getAttribute("li-index") == musicIndex){
            allLiTags[j].classList.add("playing")
            audioTag.innerText = "Playing"
        }
        //adding oncllick attribute in all li tags
        allLiTags[j].setAttribute("onclick", "clicked(this)");
     }
    
 }

 function clicked(element){
    // geting li index of particular clicked li tag
    let getLiIndex = element.getAttribute("li-index")
    musicIndex = getLiIndex
    loadMusic(musicIndex)
    playMusic();
    playingNow()
 }
