let mood, audio, playbtn, nextbtn, prevbtn, mutebtn, seekslider, volumeslider, seeking = false, seekto,
    curtimetext, durtimetext, current_song, dir, playlist, ext, agent, repeat, setvolume, angry_playlist, angry_title,
    angry_poster, happy_playlist, happy_title, happy_poster, calm_playlist, calm_title, calm_poster, sad_playlist,
    sad_title, sad_poster, playlist_index;
    
    

dir = "Media/"

playlist = [];
title = [];
poster = [];

console.log(playlist)



agent = navigator.userAgent.toLowerCase()

playbtn = document.getElementById("playpausebtn");
nextbtn = document.getElementById("nextbtn");
prevbtn = document.getElementById("prevbtn");
mutebtn = document.getElementById("mutebtn");
seekslider = document.getElementById("seekslider");
volumeslider = document.getElementById("volumeslider");
curtimetext = document.getElementById("curtimetext");
durtimetext = document.getElementById("durtimetext");
current_song = document.getElementById("current_song");
repeat = document.getElementById("repeat");

audio = new Audio();
audio.loop = false;

Webcam.set({
    width: 320,
    height: 240,
    image_format: 'jpeg',
    jpeg_quality: 90
});
Webcam.attach('#imageCapture');

playbtn.addEventListener("click", playPause);
nextbtn.addEventListener("click", () => { nextSong(mood) });
prevbtn.addEventListener("click", () => { prevSong(mood) });
mutebtn.addEventListener("click", mute);
seekslider.addEventListener("mousedown", function (event) {
    seeking = true;
    seek(event);
});
seekslider.addEventListener("mousemove", function (event) {
    seek(event);
})
seekslider.addEventListener("mouseup", function () {
    seeking = false;
})
volumeslider.addEventListener("mousemove", setvolume);
audio.addEventListener("timeupdate", function () {
    seektimeupdate();
})
audio.addEventListener("ended", function () {
    switchTrack(mood);
})
repeat.addEventListener("click", loop);


function fetchMusicDetails(mood) {
    $("#playpausebtn img").attr("src", "static/images/pause.png");
 
    $("#circle-image img").attr("src", poster[playlist_index]);
    current_song.innerHTML = title[playlist_index];
    audio.src = dir + playlist[playlist_index] 

    audio.play();
}

function playPause() {
    if (audio.paused) {
        audio.play();
        $("#playpausebtn img").attr("src", "static/images/pause.png");
    } else {
        audio.pause();
        $("#playpausebtn img").attr("src", "static/images/play.png");
    }
}

function nextSong(mood) {
    playlist_index++;
 
    if (playlist_index > playlist.length - 1) {
        playlist_index = 0;
    }
    fetchMusicDetails(mood);
}

function prevSong(mood) {
    playlist_index--;
 
    if (playlist_index < 0) {
        playlist_index = playlist.length - 1;
    }
            
    fetchMusicDetails(mood);
}

function mute() {
    if (audio.muted) {
        audio.muted = false;
        $("#mutebtn img").attr("src", "static/images/speaker.png");
    } else {
        audio.muted = true;
        $("#mutebtn img").attr("src", "static/images/mute.png");
    }
}

function seek(event) {
    if (audio.duration == 0) {
        null
    } else {
        if (seeking) {
            seekslider.value = event.clientX - seekslider.offsetLeft;
            seekto = audio.duration * (seekslider.value / 100);
            audio.currentTime = seekto;
        }
    }
}

function setVolume() {
    audio.volume = volumeslider.value / 100;
}

function seektimeupdate() {
    if (audio.duration) {
        let temp = audio.currentTime * (100 / audio.duration);
        seekslider.value = temp;
        var curmins = Math.floor(audio.currentTime / 60);
        var cursecs = Math.floor(audio.currentTime - curmins * 60);
        var durmins = Math.floor(audio.duration / 60);
        var dursecs = Math.floor(audio.duration - durmins * 60);
        if (cursecs < 10) {
            cursecs = "0" + cursecs
        }
        if (curmins < 10) {
            curmins = "0" + curmins
        }
        if (dursecs < 10) {
            dursecs = "0" + dursecs
        }
        if (durmins < 10) {
            durmins = "0" + durmins
        }
        curtimetext.innerHTML = curmins + ":" + cursecs;
        durtimetext.innerHTML = durmins + ":" + dursecs;
    } else {
        curtimetext.innerHTML = "00:00";
        durtimetext.innerHTML = "00:00";
    }
}

function switchTrack(mood) {
   
    if (playlist_index == playlist.length - 1) {
        playlist_index = 0;
    } else {
        playlist_index++;
    }

    fetchMusicDetails(mood);
}

function loop() {
    if (audio.loop) {
        audio.loop = false;
        $("#repeat img").attr("src", "static/images/loop.png");
    } else {
        audio.loop = true;
        $("#repeat img").attr("src", "static/images/loop1.png");
    }
}

document.querySelector('#test').addEventListener('click', function () {
    getExpression();
});

const getExpression = () => {
    Webcam.snap(image_uri => {
        console.log(image_uri)
        fetch('/expression', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "image_uri": image_uri })
        }).then(response => {
            return response.json();
        }).then(res => {
            mood = res.mood;
            mood = mood.charAt(0).toUpperCase() + mood.slice(1);
            document.querySelector('#status').innerHTML = `Current Mood: ${mood}`;
            
            // Fetch Music details from the database based on the mood

            fetchMusicDetailsFromDatabase(mood)
            
        });
    });
}

// function to fetch music details from the database

const fetchMusicDetailsFromDatabase = (mood) =>{

    fetch(`/get_music_details?mood=${mood.toLowerCase()}`)
    .then(response => response.json())
    .then(data =>{
        console.log(data)

        // clear existing arrays
        playlist.length = 0
        title.length = 0
        poster.length = 0

        // populate arrays with new data
        
        data.forEach(song =>{
            playlist.push(song.audioFile)
            title.push(song.songName)
            poster.push(song.coverImage)
        })

        // Update UI with fetched data ( Modify as needed )
        // playlist_index = 0;
        // audio.src = dir + data[playlist_index].audioFile;
        // current_song.innerHTML = data[playlist_index].songName;
        // $("#circle-image img").attr("src", data[playlist_index].coverImage);

        //fetch and play the first song
        playlist_index = 0
        fetchMusicDetails(mood)

    })
    .catch(error => console.error("Error fetching music details: ", error))
}

setTimeout(() => { getExpression() }, 2000);


