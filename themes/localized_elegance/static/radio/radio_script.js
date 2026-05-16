$(document).ready(function () {
	var audioPlayer = new Audio("http://daniloquium.xyz/radio");
	var volumeControl = $("#volumeControl");
	var elapsedTimeDisplay = $("#elapsedTime");
	var currentSongDisplay = $("#currentSong");
	var nextSongDisplay = $("#nextSong");
	var playButton = $("#playButton");
	var pauseButton = $("#pauseButton");
	var muteButton = $("#muteButton");
	var unmuteButton = $("#unmuteButton");
	var listenersCountDisplay = $("#listenersCount");
	var songHistoryDisplay = $("#songHistory");

	// initial volume
	audioPlayer.volume = volumeControl.val() / 100;

	// try to trigger autoplay
	$(audioPlayer).on("canplay", function () {
		audioPlayer.play().catch(function (error) {
			console.error("Unable to start playback: ", error);
		});
		updateButtonVisibility();
	});

	volumeControl.on("input", function () {
		audioPlayer.volume = volumeControl.val() / 100;
	});

	playButton.on("click", function () {
		audioPlayer.src = "http://daniloquium.xyz/radio"; // reload the stream
		audioPlayer.play().catch(function (error) {
			console.error("Unable to start playback: ", error);
		});
		updateButtonVisibility();
	});

	pauseButton.on("click", function () {
		audioPlayer.pause();
		updateButtonVisibility();
	});

	muteButton.on("click", function () {
		audioPlayer.muted = true;
		updateButtonVisibility();
	});

	unmuteButton.on("click", function () {
		audioPlayer.muted = false;
		updateButtonVisibility();
	});

	$(audioPlayer).on("timeupdate", function () {
		var currentTime = Math.floor(audioPlayer.currentTime);
		elapsedTimeDisplay.html(formatTime(currentTime));
	});

	function formatTime(seconds) {
		var days = Math.floor(seconds / 86400);
		var hours = Math.floor((seconds % 86400) / 3600);
		var minutes = Math.floor((seconds % 3600) / 60);
		seconds = seconds % 60;
		return (days > 0 ? days + ":" : "") + (days > 0 && hours < 10 ? "0" : "") + (hours > 0 ? hours + ":" : "") + (hours > 0 && minutes < 10 ? "0" : "") + minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
	}

	function fetchSongInfo() {
		$.getJSON("http://daniloquium.xyz/now_playing.json", function (data) {
			var currentSong = data.artist + " – " + data.title + " " + data.station_name || "";
			var nextSong = data.next_song || "";
			if (currentSong !== "" && nextSong !== "") {
				currentSongDisplay.text(currentSong);
				nextSongDisplay.text(nextSong);
			}
			else {
				currentSongDisplay.html("<strong>Offline</strong>");
				nextSongDisplay.text("");
			}
		}).fail(function (error) {
			console.error("Error getting song info: ", error);
			currentSongDisplay.text("");
			nextSongDisplay.text("");
		});
		// also fetch and update the song history
		fetchSongHistory();
	}
	// fetch it every 5 seconds
	setInterval(fetchSongInfo, 5000);

	function fetchSongHistory() {
		$.getJSON("http://daniloquium.xyz/song_history.php", function (data) {
			if (data.error) {
				console.log("Error: " + data.error);
			}
			else {
				songHistoryDisplay.empty();
				$.each(data, function (index, entry) {
					var songEntry = $("<li>").addClass("song-history-entry").text(entry.artist + " – " + entry.title);
					songHistoryDisplay.append(songEntry);
				});
			}
		}).fail(function (error) {
			console.error("Error fetching data: ", error);
		});
	}
	// fetch song history every 20 seconds
	// setInterval(fetchSongHistory, 20000);

	function fetchListenersCount() {
		$.getJSON("http://daniloquium.xyz:1995/status-json.xsl", function (data) {
			var listenersCount = data.icestats.source.listeners ?? "";
			if (listenersCount !== null) {
				listenersCountDisplay.text(listenersCount);
			}
			else {
				listenersCountDisplay.text("");
			}
		}).fail(function (error) {
			console.error("Error getting listeners count: ", error);
			listenersCountDisplay.text("");
		});
	}
	// fetch listeners count every 10 seconds
	// setInterval(fetchListenersCount, 10000);

	function updateButtonVisibility() {
		if (audioPlayer.paused) {
			playButton.removeClass("hidden");
			pauseButton.addClass("hidden");
		}
		else {
			playButton.addClass("hidden");
			pauseButton.removeClass("hidden");
		}
		if (audioPlayer.muted) {
			muteButton.addClass("hidden");
			unmuteButton.removeClass("hidden");
		}
		else {
			muteButton.removeClass("hidden");
			unmuteButton.addClass("hidden");
		}
	}

	updateButtonVisibility();
	fetchSongInfo();
	fetchSongHistory();
	// fetchListenersCount();
});
